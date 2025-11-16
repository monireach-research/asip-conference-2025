"""
Pipeline Comparison: MediaPipe Baseline vs YOLOv8n+MediaPipe Integration
Tests whether YOLOv8n ROI cropping improves MediaPipe performance

Validates hypothesis: "YOLOv8n person detection + ROI cropping improves
MediaPipe pose estimation speed and accuracy compared to full-frame processing"

Usage:
  python pipeline_comparison.py
  python pipeline_comparison.py --input /path/to/videos --output /path/to/results
"""

import argparse
import json
from pathlib import Path
import time
import cv2
import mediapipe as mp
from ultralytics import YOLO


def process_video_baseline(video_path, mp_pose):
    """Process video with MediaPipe only (full frame)"""
    print(f"\n[BASELINE] Processing: {video_path.name}")

    cap = cv2.VideoCapture(str(video_path))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps_video = cap.get(cv2.CAP_PROP_FPS)

    metrics = {
        "video_name": video_path.name,
        "mode": "baseline",
        "total_frames": total_frames,
        "video_fps": fps_video,
        "frames_processed": 0,
        "frames_with_pose": 0,
        "keypoint_counts": [],
        "confidence_scores": [],
        "processing_times": [],  # Per-frame processing time
    }

    frame_count = 0
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        frame_start = time.time()

        # MediaPipe on full frame
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pose_results = mp_pose.process(rgb_frame)

        frame_time = time.time() - frame_start
        metrics["processing_times"].append(frame_time)

        if pose_results.pose_landmarks:
            metrics["frames_with_pose"] += 1

            # Count visible keypoints
            visible_kps = sum(
                1 for lm in pose_results.pose_landmarks.landmark if lm.visibility > 0.5
            )
            metrics["keypoint_counts"].append(visible_kps)

            # Average confidence
            avg_conf = (
                sum(lm.visibility for lm in pose_results.pose_landmarks.landmark) / 33
            )
            metrics["confidence_scores"].append(avg_conf)

        # Progress
        if frame_count % 30 == 0:
            print(f"  Progress: {frame_count}/{total_frames} frames", end="\r")

    total_time = time.time() - start_time
    metrics["frames_processed"] = frame_count
    metrics["total_processing_time"] = total_time
    metrics["achieved_fps"] = frame_count / total_time if total_time > 0 else 0

    cap.release()
    print(f"  Completed: {frame_count} frames in {total_time:.1f}s")

    # Calculate statistics
    if metrics["keypoint_counts"]:
        metrics["avg_keypoints"] = sum(metrics["keypoint_counts"]) / len(
            metrics["keypoint_counts"]
        )
        metrics["avg_confidence"] = sum(metrics["confidence_scores"]) / len(
            metrics["confidence_scores"]
        )
        metrics["keypoint_detection_rate"] = metrics["avg_keypoints"] / 33.0
    else:
        metrics["avg_keypoints"] = 0
        metrics["avg_confidence"] = 0
        metrics["keypoint_detection_rate"] = 0

    if metrics["frames_processed"] > 0:
        metrics["pose_coverage"] = (
            metrics["frames_with_pose"] / metrics["frames_processed"]
        )
    else:
        metrics["pose_coverage"] = 0

    metrics["avg_frame_time"] = (
        sum(metrics["processing_times"]) / len(metrics["processing_times"])
        if metrics["processing_times"]
        else 0
    )

    return metrics


def process_video_integrated(video_path, yolo_model, mp_pose):
    """Process video with YOLOv8n + MediaPipe (ROI cropping)"""
    print(f"\n[INTEGRATED] Processing: {video_path.name}")

    cap = cv2.VideoCapture(str(video_path))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps_video = cap.get(cv2.CAP_PROP_FPS)

    metrics = {
        "video_name": video_path.name,
        "mode": "integrated",
        "total_frames": total_frames,
        "video_fps": fps_video,
        "frames_processed": 0,
        "frames_with_person": 0,
        "frames_with_pose": 0,
        "keypoint_counts": [],
        "confidence_scores": [],
        "processing_times": [],
        "yolo_times": [],
        "mediapipe_times": [],
        "false_negatives": 0,
    }

    frame_count = 0
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        frame_start = time.time()

        # YOLOv8n person detection
        yolo_start = time.time()
        results = yolo_model(frame, verbose=False)
        persons = [box for box in results[0].boxes if box.cls == 0]
        yolo_time = time.time() - yolo_start
        metrics["yolo_times"].append(yolo_time)

        if len(persons) > 0:
            metrics["frames_with_person"] += 1

            # Get largest bounding box
            largest_box = max(
                persons, key=lambda x: (x.xywh[0][2] * x.xywh[0][3]).item()
            )
            xywh = largest_box.xywh[0].cpu().numpy()
            x, y, w, h = xywh

            # Crop ROI
            x1, y1 = int(x - w / 2), int(y - h / 2)
            x2, y2 = int(x + w / 2), int(y + h / 2)
            x1, y1 = max(0, x1), max(0, y1)
            x2, y2 = min(frame.shape[1], x2), min(frame.shape[0], y2)

            if x2 > x1 and y2 > y1:
                roi = frame[y1:y2, x1:x2]

                # MediaPipe on ROI
                mp_start = time.time()
                rgb_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
                pose_results = mp_pose.process(rgb_roi)
                mp_time = time.time() - mp_start
                metrics["mediapipe_times"].append(mp_time)

                if pose_results.pose_landmarks:
                    metrics["frames_with_pose"] += 1

                    # Count visible keypoints
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

        frame_time = time.time() - frame_start
        metrics["processing_times"].append(frame_time)

        # Progress
        if frame_count % 30 == 0:
            print(f"  Progress: {frame_count}/{total_frames} frames", end="\r")

    total_time = time.time() - start_time
    metrics["frames_processed"] = frame_count
    metrics["total_processing_time"] = total_time
    metrics["achieved_fps"] = frame_count / total_time if total_time > 0 else 0

    cap.release()
    print(f"  Completed: {frame_count} frames in {total_time:.1f}s")

    # Calculate statistics
    if metrics["keypoint_counts"]:
        metrics["avg_keypoints"] = sum(metrics["keypoint_counts"]) / len(
            metrics["keypoint_counts"]
        )
        metrics["avg_confidence"] = sum(metrics["confidence_scores"]) / len(
            metrics["confidence_scores"]
        )
        metrics["keypoint_detection_rate"] = metrics["avg_keypoints"] / 33.0
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

    metrics["avg_frame_time"] = (
        sum(metrics["processing_times"]) / len(metrics["processing_times"])
        if metrics["processing_times"]
        else 0
    )
    metrics["avg_yolo_time"] = (
        sum(metrics["yolo_times"]) / len(metrics["yolo_times"])
        if metrics["yolo_times"]
        else 0
    )
    metrics["avg_mediapipe_time"] = (
        sum(metrics["mediapipe_times"]) / len(metrics["mediapipe_times"])
        if metrics["mediapipe_times"]
        else 0
    )

    return metrics


def main():
    parser = argparse.ArgumentParser(
        description="Compare MediaPipe baseline vs YOLOv8n+MediaPipe integration"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="/Users/monireach/datasets/nir_validation",
        help="Directory containing NIR videos",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="./validation_outputs/pipeline_comparison",
        help="Output directory for results",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="yolov8n.pt",
        help="YOLOv8 model path",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limit number of videos to process (for quick testing)",
    )

    args = parser.parse_args()

    # Setup paths
    video_dir = Path(args.input)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    if not video_dir.exists():
        print(f"ERROR: Input directory does not exist: {video_dir}")
        return

    # Find videos
    video_extensions = [".mp4", ".avi", ".mov", ".mkv"]
    videos = sorted(
        [f for f in video_dir.iterdir() if f.suffix.lower() in video_extensions]
    )

    if args.limit:
        videos = videos[: args.limit]

    if not videos:
        print(f"No videos found in {video_dir}/")
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

    # Process all videos in BOTH modes
    baseline_results = []
    integrated_results = []

    for video_path in videos:
        # Baseline mode
        baseline_metrics = process_video_baseline(video_path, mp_pose)
        baseline_results.append(baseline_metrics)

        # Integrated mode
        integrated_metrics = process_video_integrated(video_path, yolo_model, mp_pose)
        integrated_results.append(integrated_metrics)

        # Save individual comparison
        comparison = {
            "video_name": video_path.name,
            "baseline": baseline_metrics,
            "integrated": integrated_metrics,
        }
        json_path = output_dir / f"{video_path.stem}_comparison.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(comparison, f, indent=2)

    # Generate summary comparison
    print("\n" + "=" * 80)
    print("PIPELINE COMPARISON SUMMARY")
    print("=" * 80)

    # Average metrics
    baseline_avg_fps = sum(m["achieved_fps"] for m in baseline_results) / len(
        baseline_results
    )
    integrated_avg_fps = sum(m["achieved_fps"] for m in integrated_results) / len(
        integrated_results
    )

    baseline_avg_keypoints = sum(
        m["keypoint_detection_rate"] for m in baseline_results
    ) / len(baseline_results)
    integrated_avg_keypoints = sum(
        m["keypoint_detection_rate"] for m in integrated_results
    ) / len(integrated_results)

    baseline_avg_conf = sum(m["avg_confidence"] for m in baseline_results) / len(
        baseline_results
    )
    integrated_avg_conf = sum(m["avg_confidence"] for m in integrated_results) / len(
        integrated_results
    )

    baseline_avg_pose_coverage = sum(
        m["pose_coverage"] for m in baseline_results
    ) / len(baseline_results)
    integrated_avg_pose_coverage = sum(
        m["pose_coverage"] for m in integrated_results
    ) / len(integrated_results)

    print("\n📊 PERFORMANCE COMPARISON")
    print("-" * 80)
    print(f"{'Metric':<30} {'Baseline':<20} {'Integrated':<20} {'Winner':<10}")
    print("-" * 80)

    # FPS comparison
    fps_diff = (integrated_avg_fps - baseline_avg_fps) / baseline_avg_fps * 100
    fps_winner = (
        "Integrated ✓" if integrated_avg_fps > baseline_avg_fps else "Baseline ✓"
    )
    print(
        f"{'Processing Speed (FPS)':<30} {baseline_avg_fps:<20.2f} {integrated_avg_fps:<20.2f} {fps_winner:<10}"
    )
    print(f"{'  → Speed change:':<30} {'':<20} {fps_diff:+.1f}%")

    # Keypoint detection
    kp_diff = (integrated_avg_keypoints - baseline_avg_keypoints) * 100
    kp_winner = (
        "Integrated ✓"
        if integrated_avg_keypoints > baseline_avg_keypoints
        else "Baseline ✓"
    )
    print(
        f"{'Keypoint Detection Rate':<30} {baseline_avg_keypoints*100:<20.1f}% {integrated_avg_keypoints*100:<20.1f}% {kp_winner:<10}"
    )
    print(f"{'  → Accuracy change:':<30} {'':<20} {kp_diff:+.1f}%")

    # Confidence
    conf_diff = (integrated_avg_conf - baseline_avg_conf) * 100
    conf_winner = (
        "Integrated ✓" if integrated_avg_conf > baseline_avg_conf else "Baseline ✓"
    )
    print(
        f"{'Confidence Score':<30} {baseline_avg_conf:<20.3f} {integrated_avg_conf:<20.3f} {conf_winner:<10}"
    )
    print(f"{'  → Confidence change:':<30} {'':<20} {conf_diff:+.3f}")

    # Pose coverage
    cov_diff = (integrated_avg_pose_coverage - baseline_avg_pose_coverage) * 100
    cov_winner = (
        "Integrated ✓"
        if integrated_avg_pose_coverage > baseline_avg_pose_coverage
        else "Baseline ✓"
    )
    print(
        f"{'Pose Coverage':<30} {baseline_avg_pose_coverage*100:<20.1f}% {integrated_avg_pose_coverage*100:<20.1f}% {cov_winner:<10}"
    )
    print(f"{'  → Coverage change:':<30} {'':<20} {cov_diff:+.1f}%")

    print("\n" + "=" * 80)
    print("RECOMMENDATION")
    print("=" * 80)

    # Decision logic
    speed_win = integrated_avg_fps > baseline_avg_fps
    accuracy_win = (
        integrated_avg_keypoints >= baseline_avg_keypoints * 0.95
    )  # Allow 5% degradation

    if speed_win and accuracy_win:
        print("✅ RECOMMENDATION: Use YOLOv8n + MediaPipe integration")
        print(f"   - Faster: {fps_diff:+.1f}% speed improvement")
        print(f"   - Accurate: {kp_diff:+.1f}% keypoint detection change")
        print("   - Integrated pipeline improves both speed and accuracy")
    elif speed_win and not accuracy_win:
        print("⚠️  RECOMMENDATION: Consider trade-offs")
        print(f"   - Faster: {fps_diff:+.1f}% speed improvement")
        print(f"   - BUT: {kp_diff:.1f}% accuracy degradation")
        print("   - Evaluate if speed gain justifies accuracy loss")
    elif not speed_win and accuracy_win:
        print("⚠️  RECOMMENDATION: Use baseline (MediaPipe only)")
        print(f"   - Slower: {fps_diff:.1f}% speed reduction")
        print(f"   - BUT: {kp_diff:+.1f}% accuracy improvement")
        print("   - YOLOv8n overhead not justified by accuracy gain")
    else:
        print("❌ RECOMMENDATION: Use baseline (MediaPipe only)")
        print(f"   - Slower: {fps_diff:.1f}% speed reduction")
        print(f"   - Worse: {kp_diff:.1f}% accuracy degradation")
        print("   - YOLOv8n integration provides no benefit")

    print("=" * 80 + "\n")

    # Save summary
    summary = {
        "baseline": {
            "avg_fps": baseline_avg_fps,
            "avg_keypoint_rate": baseline_avg_keypoints,
            "avg_confidence": baseline_avg_conf,
            "avg_pose_coverage": baseline_avg_pose_coverage,
        },
        "integrated": {
            "avg_fps": integrated_avg_fps,
            "avg_keypoint_rate": integrated_avg_keypoints,
            "avg_confidence": integrated_avg_conf,
            "avg_pose_coverage": integrated_avg_pose_coverage,
        },
        "comparison": {
            "fps_improvement_percent": fps_diff,
            "keypoint_rate_change_percent": kp_diff,
            "confidence_change": conf_diff,
            "pose_coverage_change_percent": cov_diff,
        },
        "recommendation": "integrated" if (speed_win and accuracy_win) else "baseline",
        "individual_videos": [
            {"baseline": b, "integrated": i}
            for b, i in zip(baseline_results, integrated_results)
        ],
    }

    with open(output_dir / "comparison_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(f"Results saved to: {output_dir}/")
    print(f"  - Individual comparisons: {len(videos)} JSON files")
    print(f"  - Summary: comparison_summary.json\n")


if __name__ == "__main__":
    main()
