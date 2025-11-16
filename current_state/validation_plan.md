# Component Validation Plan for ASIP 2025 Paper

**Last Updated**: Nov 10, 2025
**Status**: COMPLETE - A1.2a, A1.2c, A1.3, A4.2 all validated (Nov 10, 2025)
**Positioning**: Privacy governance paper with empirical technical validation
**Approach**: Laptop-only validations (no hardware purchase)

---

## Research Question Confirmation

**Based on conference research**: Component validation studies ARE empirical contributions at AI/CS conferences (NeurIPS, CVPR, AAAI standards).

**Evidence**:
- Ablation studies provide "empirical evidence to support component inclusion"
- Integration testing requires empirical measurement
- Performance benchmarking is fundamental empirical practice
- Published IEEE papers use YOLOv8n+MediaPipe integration as empirical contribution

---

## Validation Naming System

**Format**: `Letter + Group# + Validation#`

- **Letter** (A/B/C): Category
  - **A** = Can do now (laptop-only, no hardware purchase)
  - **B** = Need hardware (Jetson Orin Nano + cameras, $370)
  - **C** = Need custom dataset (CamTech dataset collection + participants)

- **Group# (1-6)**: Validation topic area
  - **1** = Pipeline components (YOLOv8n, MediaPipe, CNN+LSTM+Transformer)
  - **2** = Generalization & robustness (cross-dataset, lighting conditions)
  - **3** = Privacy preservation (frame deletion, re-identification, zero cloud)
  - **4** = Cost-effectiveness (hardware justification, cloud comparison)
  - **5** = Performance & latency (real-time capability, multi-camera fusion)
  - **6** = Incident detection (incident type mapping, threshold sensitivity)

- **Validation# (.1, .2, .3, ...)**: Specific validation within group

**Example**: **A3.2** = Category A (laptop), Group 3 (privacy), Validation 2 (frame deletion verification)

**Total identified**: 29 validations (A: 18, B: 7, C: 4) - A3.2 removed (implementation audit), A1.2b removed (thermal IR irrelevant for 850nm NIR camera)

---

## Paper Positioning Strategy

**Main Argument**: Privacy governance principles CAN drive technical architecture from inception while maintaining technical feasibility

**Evidence Strategy**: Each governance principle → Architectural choice → Technical validation

**Paper Type**: Design/conceptual paper with preliminary empirical validation (honest about scope)

---

## Required Validations for ASIP Paper (9 of 30, 45-61 hours)

### Category 1: Privacy Governance Validations (19-26 hours)

**Goal**: Prove privacy-by-design mechanisms work technically

**Note**: A3.2 (Frame deletion verification) removed - implementation audit, not empirical validation
**Note**: A1.2b (Thermal IR) removed Nov 10, 2025 - LLVIP/OpenThermalPose2 are thermal LWIR (8,000-14,000nm heat signatures), NOT 850nm NIR used in Hikvision cameras. Different physics - MediaPipe fails on thermal without retraining.

#### A1.2a: Extended NIR Validation - Diverse Source Testing (6-8 hours) ✅ PRIORITY
**What it validates**: Full pipeline (YOLOv8n + MediaPipe) works reliably across diverse 850nm NIR sources
**Method**: Run integrated pipeline on 20 NIR videos from different cameras, environments, subjects
**Metrics**:
- Overall keypoint detection rate (target: ≥90%)
- Overall confidence scores (target: ≥0.70)
- False negative rate (YOLO detects person but pose fails, target: <15%)
- Pose coverage across diverse scenarios (indoor/outdoor, different subjects)
**Datasets**: 20 NIR night vision videos from YouTube (diverse camera brands: Hikvision, EZVIZ, etc.)
**Location**: `/Users/monireach/datasets/nir_validation/` (20 videos downloaded Nov 10, 2025)
**Script**: `nir_validation_batch.py` (flexible, command-line args for reusability)
**Rationale**: 2-video Oct 31 validation (A1.2c) proved feasibility but insufficient sample size (research standard: PoseTrack uses 50 videos for validation). 20 videos provides better statistical validity and environmental diversity while meeting conference paper timeline.
**Deliverable**: Section 4.2 (Technical Feasibility - NIR Pipeline Validation)

#### A1.2c: Initial NIR Validation - Feasibility Proof (1-2 hours) ✅ COMPLETE
**What it validates**: Night vision camera compatibility (850nm near-IR illumination)
**Method**: Validate Oct 2025 IR footage results
**Metrics**: 93.2% detection rate, 0.901 confidence (already tested)
**Dataset**: Oct 2025 custom footage (real-world 850nm IR night vision camera)
**Note**: Near-IR (850nm) vs thermal IR (9-14μm) - different modalities
**Deliverable**: Section 4.4 (Robustness)

#### A3.1: Pose-Only Storage Re-identification Resistance Test (10-12 hours)
**What it validates**: "Facial anonymity" governance claim
**Claim supported**: Skeleton data prevents individual identification
**Method**: Train classifier to identify individuals from skeleton patterns, measure re-identification accuracy
**Metrics**:
- Re-identification accuracy (skeleton-only vs video-based)
- Baseline: Random guess (1/N individuals)
**Deliverable**: Section 4.1 (Privacy Preservation)

#### A4.1: Processing Requirements → Hardware Specification Validation (3-4 hours)
**What it validates**: "Affordability" governance principle
**Claim supported**: Governance constraints don't require expensive hardware
**Method**: Measure pipeline resource consumption, compare against Jetson Orin Nano specs
**Metrics**:
- Pipeline FPS, memory, compute requirements
- Jetson Orin Nano headroom analysis
- Alternative hardware cost comparison
**Deliverable**: Section 4.3 (Cost-Effectiveness)

---

### Category 2: Technical Feasibility Validations (16-22 hours)

**Goal**: Prove governance-driven design doesn't sacrifice performance

#### A1.1: YOLOv8n Person Detection Speed Baseline (4-6 hours)
**What it validates**: Pipeline component performance
**Claim supported**: Real-time processing capability
**Method**: Run YOLOv8n on MCF/LE2I/UP-Fall datasets, test CPU vs GPU
**Metrics**:
- Detection speed (FPS) on CPU vs GPU
- Inference latency per frame (ms)
- Memory consumption (MB)
- mAP for person class
**Baseline**: YOLOv8n COCO published benchmarks
**Deliverable**: Section 4.2 (Technical Feasibility)

#### A1.3: Pipeline Efficiency Comparison - Baseline vs Integration (6-8 hours) ✅ PRIORITY
**What it validates**: Whether YOLOv8n integration improves MediaPipe performance (speed/accuracy)
**Hypothesis**: YOLOv8n person detection + ROI cropping improves MediaPipe speed and reduces false positives compared to full-frame processing
**Method**: Run BOTH pipelines on same 20 NIR videos and compare:
  - **Baseline**: MediaPipe only (full frame)
  - **Integrated**: YOLOv8n → Crop ROI → MediaPipe (on cropped region)
**Metrics**:
- Speed: Processing FPS (achieved_fps), per-frame latency (ms)
- Accuracy: Keypoint detection rate, confidence scores
- Robustness: False negative rate (pose detection failure), pose coverage
**Critical Question**: Does YOLOv8n overhead justify the ROI speedup? Or does running 2 models slow down the pipeline?
**Dataset**: Same 20 NIR videos from A1.2a (consistency in comparison)
**Script**: `pipeline_comparison.py` (automated side-by-side comparison with recommendation)
**Deliverable**: Section 4.2 (Technical Feasibility - Pipeline Optimization Analysis)

#### A5.1: End-to-End Latency Breakdown Analysis (2-3 hours)
**What it validates**: Real-time capability with privacy constraints
**Claim supported**: <1 second alert latency achievable
**Method**: Sum component latencies from A1.3, A1.4 benchmarks
**Metrics**:
- Component breakdown: YOLOv8n (X ms) + MediaPipe (Y ms) + CNN+LSTM+Transformer (Z ms)
- Total pipeline latency: X+Y+Z
- Bottleneck identification
**Baseline**: <1 second alert target
**Deliverable**: Section 4.2 (Technical Feasibility)

#### A4.2: Cloud Alternative Cost Calculation Verification (2-3 hours)
**What it validates**: Cost-effectiveness vs cloud alternatives
**Claim supported**: 61% cost savings claim
**Method**: Research cloud service pricing, calculate data transmission + storage costs
**Metrics**:
- Cloud service pricing (Kami Fall Detect Camera, AWS, Google Cloud)
- 3-year total cost: Edge ($672 one-time) vs Cloud (monthly × 36)
**Baseline**: Kami Fall Detect Camera pricing ($99 hardware + $45/month subscription)
**Deliverable**: Section 4.3 (Cost-Effectiveness)

---

## Optional Robustness Validations (10-33 hours)

### High-Value Optional (10-13 hours)

#### A2.2: Lighting Condition Robustness Analysis (6-8 hours)
**What it validates**: 24/7 monitoring capability
**Claim supported**: IR night vision compatibility (extends Oct 2025 validation to full pipeline)
**Method**: Train on daylight videos, test on low-light/IR separately
**Metrics**:
- Accuracy by lighting: daylight, low-light, IR
- Confidence score distribution by lighting
**Deliverable**: Section 4.4 (Robustness)

#### A6.1: Benchmark Dataset Incident Type Mapping (4-5 hours)
**What it validates**: Evidence-based incident selection
**Claim supported**: 3 incident types grounded in benchmark datasets
**Method**: Map MCF/LE2I/UP-Fall labels to your 3 incident types
**Metrics**:
- Percentage per incident type
- Coverage gaps identification
**Deliverable**: Section 4.4 (Robustness)

### Time-Intensive Optional (15-20 hours)

#### A1.4: CNN+LSTM+Transformer Architecture Feasibility Test (15-20 hours)
**What it validates**: Incident classification architecture works
**Claim supported**: Hybrid model feasibility for skeleton-based classification
**Method**: Design architecture, train on MCF/LE2I skeleton data, benchmark inference
**Metrics**:
- Training convergence (does it learn?)
- Inference speed (ms), memory consumption, model size
- Baseline accuracy on benchmark datasets
**Note**: Skip if time-limited; cite literature instead
**Deliverable**: Section 4.2 (Technical Feasibility)

---

## Complete List of 30 Validations Identified

### Category A: Can Do Now (19 validations, 78-115 hours)

**Group A1: Pipeline Components**
- **A1.1**: YOLOv8n Speed Baseline (4-6h) - Detection performance on benchmarks
- **A1.2a**: Extended NIR Validation (6-8h) - 20 diverse 850nm NIR videos, full pipeline ✅ PRIORITY
- ~~**A1.2b**: Thermal IR~~ - REMOVED (thermal LWIR ≠ 850nm NIR, MediaPipe fails without retraining)
- **A1.2c**: Initial NIR Validation (1-2h) - Oct 2025 feasibility proof (93.2%, 0.901) ✅ COMPLETE
- **A1.3**: Pipeline Efficiency Comparison (6-8h) - Baseline vs Integrated, speed/accuracy trade-offs ✅ PRIORITY
- **A1.4**: CNN+LSTM+Transformer Feasibility (15-20h) - Hybrid architecture training

**Group A2: Generalization & Robustness**
- **A2.1**: Cross-Dataset Generalization (4-6h) - MCF→LE2I, LE2I→MCF testing
- **A2.2**: Lighting Condition Robustness (6-8h) - Daylight/low-light/IR performance

**Group A3: Privacy Preservation**
- **A3.1**: Re-identification Resistance Test (10-12h) - Skeleton-only privacy validation
- ~~**A3.2**: Immediate Frame Deletion Verification~~ - Removed (implementation audit, not empirical)

**Group A4: Cost-Effectiveness**
- **A4.1**: Hardware Specification Validation (3-4h) - Jetson justification from requirements
- **A4.2**: Cloud Cost Verification (2-3h) - Cloud service pricing research

**Group A5: Performance & Latency**
- **A5.1**: End-to-End Latency Breakdown (2-3h) - Component latency summation
- **A5.2**: Multi-Camera Fusion Latency Simulation (6-8h) - Parallel processing test

**Group A6: Incident Detection**
- **A6.1**: Benchmark Incident Type Mapping (4-5h) - Dataset label alignment
- **A6.2**: Threshold Sensitivity Analysis (6-8h) - ROC curves, optimal thresholds

---

### Category B: Need Hardware (7 validations, 52-68 hours, $370)

**Group B1: Edge Computing**
- **B1.1**: Jetson Real-World Performance (8-10h) - Actual FPS/latency on Jetson
- **B1.2**: Zero Cloud Transmission Verification (3-4h) - Network traffic monitoring
- **B1.3**: Multi-Camera Fusion on Jetson (10-12h) - 4 cameras simultaneous processing

**Group B2: Camera Validation**
- **B2.1**: IR Night Vision Quality Assessment (4-6h) - 850nm IR image quality testing
- **B2.2**: Coverage & Blind Spot Analysis (6-8h) - 4-camera FOV mapping

**Group B3: System Integration**
- **B3.1**: End-to-End Integration Test (15-20h) - Full system camera→alert validation
- **B3.2**: Failure Mode Testing (6-8h) - Camera disconnect, power loss scenarios

---

### Category C: Need Custom Dataset (4 validations, 72-91 hours)

**Group C1: Incident Detection with CamTech Dataset**
- **C1.1**: CamTech Dataset Accuracy (40-50h) - Train/test on 150 Cambodian elderly videos
- **C1.2**: Voting Mechanism Effectiveness (6-8h) - Multi-camera vs single-camera accuracy

**Group C2: Cross-Cultural Validation**
- **C2.1**: Body Proportion Analysis (6-8h) - Cambodian vs Western dataset comparison

**Group C3: Qualitative Validation**
- **C3.1**: Technology Acceptance Interviews (20-25h) - 5 elderly + 5 caregivers

---

**Total: 30 validations (A: 19, B: 7, C: 4)**

---

## Paper Section Mapping

### Section 4: Empirical Validation Results

**4.1 Privacy Preservation** (A3.1)
- Re-identification resistance analysis (skeleton-only privacy)

**4.2 Technical Feasibility** (A1.2a, A1.2c, A1.3, [A1.1 optional], [A5.1 optional], [A1.4 optional])
- Initial NIR validation (A1.2c) - Feasibility proof (93.2% detection, 0.901 confidence, 2 videos)
- Extended NIR validation (A1.2a) - Statistical validity (20 diverse 850nm NIR sources)
- Pipeline efficiency comparison (A1.3) - Baseline vs Integrated (speed/accuracy trade-offs)
- [YOLOv8n baseline performance - A1.1]
- [End-to-end latency analysis - A5.1]
- [CNN+LSTM+Transformer training feasibility - A1.4]

**4.3 Cost-Effectiveness** (A4.1, A4.2)
- Hardware specification justification (A4.1)
- Cloud alternative cost comparison (A4.2) - Kami Fall Detect Camera ($672 vs $1,719, 61% savings over 3 years)

**4.4 Robustness Analysis** ([A2.2 optional], [A6.1 optional])
- [Lighting condition robustness - full pipeline across datasets]
- [Evidence-based incident type mapping]
- Note: Thermal IR validation (A1.2b) removed - LWIR thermal (8,000-14,000nm) not applicable to 850nm NIR cameras

---

## Execution Resources

### Available Resources

**Fall Detection Datasets (RGB, daylight)** - `/Users/monireach/datasets/`:
- MCF (192 videos, 8 IP cameras) - `mcf_multiple_camera_fall/`
- LE2I (191 videos, single RGB) - `le2i_laboratoire_electronique_informatique_et_image/`
- UP-Fall (RGB webcams, multimodal) - Location TBD

**Thermal/IR Datasets** - `/Users/monireach/datasets/thermal/`:
- **OpenThermalPose2** ✅ (thermal pose, YOLOv8 baselines, MIT license)
- **LWIRPOSE** ✅ (2,400+ thermal images, 17 keypoint annotations)
- **LLVIP** ✅ (15,488 visible-IR pairs: low-light RGB + thermal infrared)

**Custom Test Footage**:
- Oct 2025 IR footage (93.2% detection, 0.901 confidence, 850nm near-IR night vision)

**Hardware**: Laptop/desktop with GPU (no Jetson purchase needed)

**Libraries**: YOLOv8, MediaPipe, PyTorch/TensorFlow

**Dataset Status**: All required thermal/IR datasets downloaded (Nov 8, 2025)

### Required Tools
- YOLOv8 (Ultralytics)
- MediaPipe (Google)
- PyTorch or TensorFlow

---

## Key Deliverables

✅ 9-11 empirical validations supporting governance claims
✅ Privacy-by-design mechanisms validated (not just proposed)
✅ Technical feasibility demonstrated (governance doesn't compromise performance)
✅ Cost-effectiveness proven (affordability for Cambodia)
✅ Honest limitations acknowledged (preliminary validation, no hardware deployment)

---

## Limitations to Acknowledge in Paper

**Section 6: Limitations and Future Work**

1. **Preliminary validation**: Component-level testing, not full system deployment
2. **Simulated edge performance**: Laptop benchmarks, not actual Jetson Orin Nano testing
3. **Benchmark datasets**: Western datasets, not Cambodian elderly data
4. **No user study**: Technology acceptance not empirically tested
5. **No field deployment**: Lab validation only

**Future work**:
- Hardware validation on Jetson Orin Nano
- CamTech custom dataset collection (Cambodian elderly)
- Technology acceptance interviews (5 elderly + 5 caregivers)
- Field deployment pilot study

---

## References for Validation Design

**Conference standards researched**:
- NeurIPS, CVPR, AAAI reviewer guidelines
- ACM, IEEE benchmarking standards
- Published papers: "Leveraging MediaPipe and YOLO Keypoint Detection in Ensemble Approaches" (IEEE)

**Empirical vs Conceptual definitions**:
- Enago Academy, ResearchGate, Oxford Academic sources
- Integration testing standards (ScienceDirect)

**ASIP 2025 specific**:
- Conference accepts technical papers and case studies
- Abstract format requires "Findings" section (suggests empirical expected)
- Evaluation criteria: "Theoretical and/or empirical soundness"

---

**Next Steps**: Execute validations, integrate results into paper Section 4
