# Research Summary

**Last Updated**: Nov 14, 2025 (Completed NIR validation & pipeline comparison)

---

## ASIP Conference Paper Focus

**Note**: This conference submission focuses on the **governance aspect** of the AI research project, not the complete system. The paper is a design study demonstrating how privacy governance principles inform architectural decisions through a Cambodia elderly monitoring case study.

### Conference Paper Research Question

**How can privacy governance principles inform the architectural design of AI-based elderly monitoring systems in resource-constrained contexts?**

### Conference Paper Propositions

This conceptual/design paper explores three propositions (not empirical hypotheses):

**Proposition 1**: Privacy governance requirements can be translated into specific architectural decisions (edge computing, pose-only storage, immediate frame disposal)

**Proposition 2**: Privacy-first architectural choices can yield co-benefits in cost-effectiveness and accessibility for developing countries

**Proposition 3**: Edge-based processing with pose estimation provides sufficient monitoring capability while eliminating cloud privacy risks

### Hypotheses vs Propositions (Important Distinction)

**Propositions** are used in conceptual/design research - theoretical claims explored through design analysis, literature review, and cost-benefit analysis.

**Hypotheses** are used in empirical research - testable predictions requiring data collection and statistical validation (e.g., "System will achieve ≥95% detection accuracy").

Since the ASIP paper is a design study with limited empirical validation (NIR compatibility testing, cost analysis), propositions are the appropriate research structure. Future empirical work on the main AI project will test fall detection hypotheses using benchmark datasets.

---

## Project Title (Full AI Research)

Contactless AI-Powered Incident Detection System for Elderly Safety Monitoring

---

## Main Research Question (Full AI Research)

**How effectively can a contactless AI-powered system detect elderly safety incidents in real-time while maintaining user privacy and cost-effectiveness for Cambodia?**

*Note: This is the empirical research question for the complete AI project. The ASIP conference paper demonstrates governance-driven design through NIR compatibility and cost validation (see above).*

---

## Problem Statement

### Global Context
- Aging populations worldwide require safety monitoring solutions
- Falls are leading cause of injury-related deaths among elderly
- Traditional monitoring: wearables (compliance issues) or cloud cameras (privacy concerns)

### Cambodia-Specific Context
- Rapidly aging population (1.8M elderly by 2030)
- Middle-income households need affordable solutions ($870-$1,622/month income bracket)
- Privacy concerns in camera-based monitoring systems
- Limited local research on AI-powered elderly care technologies

---

## Proposed Solution

### System Architecture

**Multi-modal AI system**:
- **Cameras**: 4× RGB cameras with 850nm NIR night vision (90° spacing for 360° coverage)
- **Detection Pipeline**: YOLOv8n (person detection) → MediaPipe (pose estimation) → CNN+LSTM+Transformer (incident classification)
- **Edge Computing**: NVIDIA Jetson Orin Nano 8GB (designed for on-device processing; integrated pipeline achieves 20.53 FPS on standard hardware)
- **Privacy Design**: Pose-only storage with immediate frame disposal after keypoint extraction
- **Validated Performance**: 91.3% keypoint detection, 0.868 confidence on 850nm NIR footage

### Three Incident Types Detected

1. **Falls While Standing/Walking**
   - Sudden uncontrolled descent from standing/walking position
   - Accounts for 37.7% of Thai elderly home accidents

2. **Falls From Bed/Chair**
   - Uncontrolled descent from elevated furniture
   - Median 1.32 incidents per facility in Chinese long-term care settings

3. **Abnormal Sit-to-Stand Transitions**
   - Failed or impaired attempts to stand from seated/lying position
   - Pre-fall risk indicator (99.42% detection accuracy in literature)

---

## Technical Performance Targets

### Accuracy Metrics
- Overall accuracy: ≥95%
- Per-incident type accuracy: ≥90%
- False positive rate: <10%
- False negative rate: <5%
- Lighting conditions: Daylight, low-light, complete darkness (IR mode)

### Real-Time Performance
- Inference speed: ≥15 FPS (target 20-25 FPS)
- Latency: <100ms per frame
- Alert generation: <1 second from incident occurrence
- Power consumption: <15W

### Privacy Preservation
- Facial anonymity: 100% (no facial features stored)
- Re-identification resistance: Cannot identify individuals from pose data alone
- Data locality: 100% on-device processing (no cloud transmission)

---

## Cost-Effectiveness Analysis

### System Cost Breakdown
- **4× RGB cameras with 850nm IR**: $252 (Hikvision DS-2CD1343G2-IUF)
- **NVIDIA Jetson Orin Nano 8GB**: $250
- **Accessories** (storage, UPS, cables, mounting): $170
- **Total**: $672 (one-time cost, zero recurring fees)

### Market Comparison
- **Cloud-based alternative**: $1,719 over 3 years (Kami Fall Detect Camera: $99 + $45/month × 36 months)
- **Our system**: $672 total (61% cost savings over 3 years)
- **Breakeven point**: Month 1 of Year 2
- **Cost advantage**: Zero subscription model eliminates ongoing payment burden

### Target Market Accessibility
- **Target**: Middle-income urban Cambodian households (top 40-60% income bracket)
- **Market reach**: 12-18% of total elderly population
- **Potential users**: 252,000-378,000 individuals by 2030

---

## Research Methodology

### Quantitative Component

**Datasets**:
- **MCF Dataset**: 192 fall videos
- **LE2I Fall Detection Dataset**: 191 videos
- **UP-Fall Dataset**: Multi-modal fall detection data
- **Custom CamTech Dataset**: 180 videos (60 per incident type: 20 daylight + 20 low-light + 20 IR night vision × 4 cameras = 720 samples)

**Approach**:
- Transfer learning from benchmark datasets
- Fine-tuning on custom CamTech data
- Performance evaluation: Accuracy, precision, recall, F1-score, confusion matrix, FPS

### Qualitative Component

**Participants**:
- 5 elderly participants (age 65+, experienced fall/near-fall, currently receiving care)
- 5 caregiver participants (matched pairs)

**Method**:
- Purposive sampling (not statistical generalization)
- Semi-structured interviews: Safety concerns, technology acceptance
- Thematic analysis for deployment feasibility insights

---

## Governance Implications

### Privacy Governance
- **Edge-first design**: All processing on-device, zero cloud transmission
- **Privacy-by-design**: Pose-only storage architecture eliminates facial recognition risks
- **Transparent data handling**: Users know exactly what data is captured and stored

### Accessibility Governance
- **Affordable innovation**: 61% cost reduction vs cloud alternatives ($672 vs $1,719 over 3 years)
- **Market expansion**: 252,000-378,000 elderly in middle-income Cambodian households (12-18% of elderly population by 2030)
- **Regional context**: Evidence-based design using Thai and Chinese elderly care data

---

## Innovation Contributions

### Technical Contributions
1. **NIR camera compatibility validation**: MediaPipe pose estimation on 850nm IR footage (91.3% keypoint detection, 20 commercial CCTV videos)
2. **Privacy-preserving architecture**: Pose-only storage, immediate frame disposal, edge processing
3. **Pipeline trade-off analysis**: Integrated YOLO+MediaPipe selected despite 2.3× slower speed for safety-critical accuracy priority

### Governance Contributions
1. **Privacy governance through edge architecture**: Demonstrates how privacy principles drive design decisions
2. **Accessibility governance through cost optimization**: 61% savings expands market reach to middle-income households
3. **Context-specific design**: Evidence-based incident prioritization using regional epidemiological data

---

## Current Status

**Phase**: Research Design & Preliminary Validation (Oct-Nov 2025)

**Completed**:
- Hardware architecture finalized (Jetson Orin Nano + 4× RGB cameras with 850nm NIR)
- Three incident types defined with contextual evidence
- Cost-effectiveness analysis completed ($672 vs $1,719, 61% savings)
- Benchmark datasets identified
- **NIR validation completed**: 91.3% keypoint detection on 20 diverse 850nm NIR videos (Nov 10, 2025)
- **Pipeline comparison completed**: Integrated YOLO+MediaPipe selected despite 2.3× slower speed for accuracy priority (Nov 10, 2025)
- ASIP conference abstract submitted (Oct 28, 2025)

**In Progress**:
- ASIP conference paper writing
- Custom CamTech dataset collection planning
- Qualitative interview protocol development

**Next Steps**:
1. Complete ASIP conference paper (Section 4: Results, Section 5: Discussion)
2. Collect custom CamTech dataset (180 videos: 60 per incident type across 3 lighting conditions)
3. Conduct qualitative interviews (5 elderly + 5 caregivers)
4. Train and benchmark model on Jetson Orin Nano

---

## Key Constraints and Limitations

### System Limitations
- Camera-based only (no wearables, no physiological sensors)
- Living room/bedroom monitoring ONLY (excludes bathroom/kitchen for privacy)
- Initial phase: 3 incident types (not all biomechanical abnormalities)
- Middle-income urban market (not accessible to low-income or rural elderly without subsidies)

### Technical Assumptions Requiring Validation
- ~~MediaPipe pose estimation performance on IR night vision images~~ **VALIDATED** (Nov 10, 2025: 91.3% keypoint detection on 850nm NIR, 20 diverse videos)
- ~~YOLOv8n + MediaPipe integration improves speed~~ **DISPROVEN** (Nov 10, 2025: Integrated 2.3× slower but 5.7% more accurate; selected for safety-critical priority)
- Multi-camera fusion performance with 4× identical cameras (not tested on target hardware)
- Real-time performance on Jetson Orin Nano (benchmarked by others, not yet validated for our specific pipeline)

---

## References

**Main research project**: `/Users/monireach/projects/ai_research`

See main project for:
- [current_state/research_questions.md](../../ai_research/current_state/research_questions.md)
- [current_state/hardware_decision.md](../../ai_research/current_state/hardware_decision.md)
- [current_state/incident_types.md](../../ai_research/current_state/incident_types.md)
- [current_state/datasets.md](../../ai_research/current_state/datasets.md)
- [current_state/key_papers.md](../../ai_research/current_state/key_papers.md)
