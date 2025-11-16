"""
NIR Night Vision Validation for MediaPipe + YOLOv8n
Flexible batch processor for validating pose estimation on IR security camera footage

Usage:
  python nir_validation_batch.py
  python nir_validation_batch.py --input /path/to/videos --output /path/to/results

Note: If you see cv2 linter warnings (e.g., "Module 'cv2' has no 'VideoCapture' member"),
these are false positives. OpenCV dynamically loads C++ bindings that linters can't detect.
The code will run correctly with opencv-python installed.
"""

import argparse
import json
from pathlib import Path
import cv2
import mediapipe as mp
from ultralytics import YOLO


def process_video(video_path, yolo_model, mp_pose):
    """Process single video and return metrics"""
    print(f"\nProcessing: {video_path.name}")

    cap = cv2.VideoCapture(str(video_path))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    metrics = {
        "video_name": video_path.name,
        "total_frames": total_frames,
        "fps": fps,
        "frames_with_person": 0,
        "frames_with_pose": 0,
        "keypoint_counts": [],
        "confidence_scores": [],
        "false_negatives": 0,  # YOLO detected person but no pose
    }

    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # YOLOv8n person detection
        results = yolo_model(frame, verbose=False)
        persons = [box for box in results[0].boxes if box.cls == 0]  # class 0 = person

        if len(persons) > 0:
            metrics["frames_with_person"] += 1

            # Get largest bounding box
            largest_box = max(
                persons, key=lambda x: (x.xywh[0][2] * x.xywh[0][3]).item()
            )
            xywh = largest_box.xywh[0].cpu().numpy()
            x, y, w, h = xywh

            # Crop ROI for MediaPipe
            x1, y1 = int(x - w / 2), int(y - h / 2)
            x2, y2 = int(x + w / 2), int(y + h / 2)
            x1, y1 = max(0, x1), max(0, y1)
            x2, y2 = min(frame.shape[1], x2), min(frame.shape[0], y2)

            if x2 > x1 and y2 > y1:
                roi = frame[y1:y2, x1:x2]

                # MediaPipe pose estimation
                rgb_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
                pose_results = mp_pose.process(rgb_roi)

                if pose_results.pose_landmarks:
                    metrics["frames_with_pose"] += 1

                    # Count visible keypoints (visibility > 0.5)
                    visible_kps = sum(
                        1
                        for lm in pose_results.pose_landmarks.landmark
                        if lm.visibility > 0.5
                    )
                    metrics["keypoint_counts"].append(visible_kps)

                    # Average confidence
                    avg_conf = (
                        sum(
                            lm.visibility for lm in pose_results.pose_landmarks.landmark
                        )
                        / 33
                    )
                    metrics["confidence_scores"].append(avg_conf)
                else:
                    metrics["false_negatives"] += 1

        # Progress indicator
        if frame_count % 30 == 0:
            print(f"  Progress: {frame_count}/{total_frames} frames", end="\r")

    cap.release()
    print(f"  Completed: {frame_count} frames processed")

    # Calculate summary statistics
    if metrics["keypoint_counts"]:
        metrics["avg_keypoints"] = sum(metrics["keypoint_counts"]) / len(
            metrics["keypoint_counts"]
        )
        metrics["avg_confidence"] = sum(metrics["confidence_scores"]) / len(
            metrics["confidence_scores"]
        )
        metrics["keypoint_detection_rate"] = (
            metrics["avg_keypoints"] / 33.0
        )  # 33 total landmarks
    else:
        metrics["avg_keypoints"] = 0
        metrics["avg_confidence"] = 0
        metrics["keypoint_detection_rate"] = 0

    if metrics["frames_with_person"] > 0:
        metrics["pose_coverage"] = (
            metrics["frames_with_pose"] / metrics["frames_with_person"]
        )
        metrics["false_negative_rate"] = (
            metrics["false_negatives"] / metrics["frames_with_person"]
        )
    else:
        metrics["pose_coverage"] = 0
        metrics["false_negative_rate"] = 0

    return metrics


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Batch validation of NIR videos for MediaPipe pose estimation"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="/Users/monireach/datasets/nir_validation",
        help="Directory containing NIR videos (default: /Users/monireach/datasets/nir_validation)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="./validation_outputs/nir_validation",
        help="Output directory for results (default: ./validation_outputs/nir_validation)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="yolov8n.pt",
        help="YOLOv8 model path (default: yolov8n.pt)",
    )

    args = parser.parse_args()

    # Setup paths
    video_dir = Path(args.input)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Verify input directory exists
    if not video_dir.exists():
        print(f"ERROR: Input directory does not exist: {video_dir}")
        return

    # Find all videos
    video_extensions = [".mp4", ".avi", ".mov", ".mkv"]
    videos = [f for f in video_dir.iterdir() if f.suffix.lower() in video_extensions]

    if not videos:
        print(f"No videos found in {video_dir}/")
        print(f"Looking for files with extensions: {', '.join(video_extensions)}")
        return

    print(f"Found {len(videos)} videos to process")
    print(f"Input: {video_dir}")
    print(f"Output: {output_dir}\n")

    # Initialize models
    print("Loading models...")
    yolo_model = YOLO(args.model)
    mp_pose = mp.solutions.pose.Pose(
        static_image_mode=False,
        model_complexity=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
    )
    print("Models loaded successfully\n")

    # Process all videos
    all_metrics = []
    for video_path in sorted(videos):
        metrics = process_video(video_path, yolo_model, mp_pose)
        all_metrics.append(metrics)

        # Save individual results
        json_path = output_dir / f"{video_path.stem}_metrics.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(metrics, f, indent=2)

    # Generate summary report
    print("\n" + "=" * 60)
    print("SUMMARY REPORT")
    print("=" * 60)

    for m in all_metrics:
        print(f"\n{m['video_name']}:")
        print(f"  Total frames: {m['total_frames']}")
        print(f"  Frames with person: {m['frames_with_person']}")
        print(f"  Frames with pose: {m['frames_with_pose']}")
        print(
            f"  Avg keypoints detected: {m['avg_keypoints']:.1f}/33 ({m['keypoint_detection_rate']*100:.1f}%)"
        )
        print(f"  Avg confidence: {m['avg_confidence']:.3f}")
        print(f"  Pose coverage: {m['pose_coverage']*100:.1f}%")
        print(f"  False negative rate: {m['false_negative_rate']*100:.1f}%")

    # Overall statistics
    print("\n" + "=" * 60)
    print("ACCEPTANCE CRITERIA EVALUATION")
    print("=" * 60)

    avg_keypoint_rate = sum(m["keypoint_detection_rate"] for m in all_metrics) / len(
        all_metrics
    )
    avg_confidence = sum(m["avg_confidence"] for m in all_metrics) / len(all_metrics)
    avg_fn_rate = sum(m["false_negative_rate"] for m in all_metrics) / len(all_metrics)

    print("\nOverall Performance:")
    print(f"  Keypoint detection rate: {avg_keypoint_rate*100:.1f}% (target: ≥90%)")
    print(f"  Average confidence: {avg_confidence:.3f} (target: ≥0.70)")
    print(f"  False negative rate: {avg_fn_rate*100:.1f}% (target: <15%)")

    # Pass/Fail decision
    criteria_met = 0
    criteria_total = 3

    if avg_keypoint_rate >= 0.90:
        print("  ✓ Keypoint detection: PASS")
        criteria_met += 1
    else:
        print("  ✗ Keypoint detection: FAIL")

    if avg_confidence >= 0.70:
        print("  ✓ Confidence score: PASS")
        criteria_met += 1
    else:
        print("  ✗ Confidence score: FAIL")

    if avg_fn_rate < 0.15:
        print("  ✓ False negative rate: PASS")
        criteria_met += 1
    else:
        print("  ✗ False negative rate: FAIL")

    print(f"\n{'='*60}")
    if criteria_met == criteria_total:
        print("RESULT: ✓ PASS - NIR validation successful")
    else:
        print(f"RESULT: ✗ PARTIAL PASS - {criteria_met}/{criteria_total} criteria met")
    print(f"{'='*60}\n")

    # Save summary
    summary = {
        "overall_keypoint_rate": avg_keypoint_rate,
        "overall_confidence": avg_confidence,
        "overall_false_negative_rate": avg_fn_rate,
        "criteria_met": criteria_met,
        "criteria_total": criteria_total,
        "pass_fail": "PASS" if criteria_met == criteria_total else "FAIL",
        "individual_videos": all_metrics,
    }

    with open(output_dir / "summary_report.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(f"Results saved to: {output_dir}/")
    print(f"  - Individual metrics: {len(videos)} JSON files")
    print(f"  - Summary report: summary_report.json\n")


if __name__ == "__main__":
    main()
