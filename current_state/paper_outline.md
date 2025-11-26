# Paper Outline

**Last Updated**: Nov 15, 2025 (11:50 PM)
**Status**: ✅ ALL CITATIONS VERIFIED - Sections 1-6 complete with rigorous fact-checking
**Citation Status**: [VERIFIED] = fact-checked with references | All claims traced to sources

**IMPORTANT - Citation vs Verification Distinction**:

- **External sources** (e.g., Cavoukian 2010, WHO 2021, Williamson 2024) → CITE in paper using APA 6th
- **Internal files** (e.g., validation_results.md, research_summary.md, hardware_decision.md) → DO NOT cite in paper
  - These are my experimental results, design decisions, and calculations
  - Report directly in Methodology/Results sections as original contributions
  - [VERIFIED] tags reference these files to prevent hallucination during writing, NOT for citation

---

## Paper Title

**Privacy Governance-Driven Design of AI-Powered Elderly Safety Monitoring for Cambodia**

(Note: Title matches submitted abstract - Oct 28, 2025)

---

## Paper Structure

### Abstract (250-300 words)

- See [abstract.md](abstract.md)

---

### 1. Introduction (2-3 pages)

#### 1.1 Problem Context

- **Global aging population trends**: Southeast Asia's elderly population projected to increase from 12.2% (2024) to 22.9% by 2050 (WHO SEARO, n.d.) [VERIFIED]
- **Elderly safety challenges**: Falls represent leading cause of injury-related deaths; 684,000 annual fatalities globally, 60% in Western Pacific/Southeast Asia (WHO, 2021) [VERIFIED]
- **Cambodia-specific context**: 1.8M elderly by 2030; middle-income households (National Institute of Statistics, 2019) [VERIFIED]
- **Family caregiving challenges**: Strong family caregiving norms rooted in filial piety values create preference for home-based elderly care over institutional facilities in Southeast Asia (Romli et al., 2017) [VERIFIED]

#### 1.2 Technology Governance Challenges

- **Privacy concerns**: Cloud-based AI systems transmit sensitive health data to third-party servers, creating facial recognition and re-identification risks (Burns, 2024; Birkstedt et al., 2023) [VERIFIED]
  - Commercial fall detection camera systems require continuous cloud connectivity for processing (Upadhyay, 2025) [VERIFIED - Kami Fall Detect Camera]
- **Accessibility barriers**: Cloud-based fall detection systems require ongoing subscriptions (~$640/year for Kami Fall Detect Camera), excluding middle-income markets in developing countries (Upadhyay, 2025) [VERIFIED]
  - For middle-income Cambodian households earning $870-$1,622/month (4th-5th quintiles), subscription represents 5.2% of monthly income (National Institute of Statistics, 2019) [VERIFIED]
  - Economic constraints limit technology adoption (Richardson et al., 2022; Sylla et al., 2025) [VERIFIED]
- **Governance fragmentation**: AI governance frameworks remain nascent and fragmented, with limited attention to implementation in resource-constrained healthcare contexts (Birkstedt et al., 2023; Burns, 2024; Sylla et al., 2025) [VERIFIED]
  - Limited practical guidance for operationalizing ethical principles (transparency, accountability, fairness) in developing countries (Almeida et al., 2020; Birkstedt et al., 2023) [VERIFIED]

#### 1.3 Research Gap

- **Fragmented design priorities**: Existing elderly monitoring solutions prioritize either privacy (federated learning, depth cameras), affordability (cloud-based systems), or performance (RGB-D sensors)—rarely addressing all three as integrated design goals (Chang & Wang, 2024; Jalaleddini et al., 2014; Vaiyapuri et al., 2021) [VERIFIED - Paper #6, #46, #21 from filtered_papers_for_thesis.md]
- **Governance timing gap**: Privacy governance principles are most effective when embedded into system design from the outset rather than applied reactively (Cavoukian et al., 2010), though implementation guidance remains limited (Birkstedt et al., 2023) [VERIFIED - Option B wording]
  - Cavoukian's Privacy by Design framework articulates philosophical principles but lacks empirical validation in healthcare AI contexts (Cavoukian et al., 2010) [VERIFIED]
  - Burns (2024) identifies edge computing potential for privacy governance but does not quantify cost-effectiveness implications for developing countries [VERIFIED - from Zotero notes]
  - Almeida et al. (2020) examine healthcare AI ethics but focus on clinical decision-making rather than continuous monitoring systems [VERIFIED - from Zotero notes]
- **Underexplored edge-privacy-cost nexus**: Edge computing potential for privacy governance remains underexplored in healthcare AI, particularly regarding economic co-benefits in resource-constrained contexts (Burns, 2024) [VERIFIED]
- **Regional research gap**: Regional studies on elderly care technology adoption in Southeast Asia focus primarily on high-income urban populations, with limited attention to middle-income market segments (Romli et al., 2017) [VERIFIED - from Zotero abstract]

#### 1.4 Research Objectives

- Demonstrate privacy governance-driven architectural design for elderly safety monitoring
- Validate technical feasibility of privacy-preserving edge architecture (NIR camera compatibility)
- Quantify cost-effectiveness of edge-based approach for middle-income households in Cambodia

---

### 2. Literature Review (3-4 pages)

#### 2.1 Elderly Safety Monitoring Technologies

- **Wearable devices**: Fall detection watches/pendants face compliance challenges—elderly users must remember to wear devices consistently, particularly difficult at nighttime, and maintain battery charging (Chaudhuri et al., 2014) [VERIFIED]
  - Only 7.1% of wearable device projects monitored elderly in actual home environments; most testing in controlled lab settings (Chaudhuri et al., 2014) [VERIFIED]
- **Cloud-based camera systems**: Transmit video to third-party servers for processing, creating privacy concerns and requiring subscriptions (Upadhyay, 2025) [VERIFIED - Kami example]
  - Acceptance challenges as cameras perceived as intrusive by elderly (Uddin et al., 2018) [VERIFIED]
- **Depth sensors**: 3D cameras (RGB-D) provide better privacy than RGB cameras by eliminating facial recognition capability (Jalaleddini et al., 2014; Wang et al., 2020) [VERIFIED]
  - Privacy-preserving alternative to RGB cameras (Jalaleddini et al., 2014) [VERIFIED - Paper #46]
  - Sensor modality tradeoffs between cost, privacy, and performance (Wang et al., 2020) [VERIFIED]
- **Ambient sensors**: Motion/PIR/door sensors detect events but face signal ambiguity—falling and Activities of Daily Living produce similar signals, limiting incident-specific detection capability (Uddin et al., 2018; Wang et al., 2020) [VERIFIED]
  - Lack of suitable outcomes to validate delivery of technological solutions for specific needs (Uddin et al., 2018) [VERIFIED]
  - Detection precision below 90% for individual sensor systems (Wang et al., 2020) [VERIFIED]

#### 2.2 Privacy-Preserving AI Approaches

- **Federated learning**: Trains models across distributed data without sharing raw data, but still requires cloud infrastructure for coordination (Yu et al., 2022) [VERIFIED - Paper #7 from filtered_papers_for_thesis.md]
  - Privacy-preserving but with cloud dependency and associated costs
- **Differential privacy**: Adds statistical noise to data to protect individual privacy while enabling analysis; can reduce model accuracy in safety-critical applications (Liu et al., 2023; Williamson & Prybutok, 2024) [VERIFIED]
  - Performance-accuracy tradeoffs particularly challenging for healthcare AI (Liu et al., 2023) [VERIFIED]
- **Edge computing**: Processes data on local devices, providing data locality benefits—data never leaves the household (Burns, 2024; Chang et al., 2021) [VERIFIED - Burns from Zotero notes; Chang Paper #41]
  - Eliminates cloud transmission and associated privacy/cost concerns (Chang et al., 2021) [VERIFIED - Paper #41]
- **Privacy-by-design principles**: Embedding privacy into architecture from inception rather than retrofitting (Cavoukian et al., 2010) [VERIFIED]
  - Seven foundational principles including "Privacy Embedded into Design" and "Proactive not Reactive" (Cavoukian et al., 2010) [VERIFIED]

#### 2.3 Technology Governance Frameworks

- **AI ethics guidelines**: Emphasize transparency, accountability, fairness, and explainability as core principles (Almeida et al., 2020; Birkstedt et al., 2023) [VERIFIED]
  - 21 AI governance models synthesized into unified framework emphasizing fairness, transparency, accountability, safety, human rights (Almeida et al., 2020) [VERIFIED]
  - Organizational AI Governance (AIG) needed to translate ethical principles into practice; implementation guidance remains limited (Birkstedt et al., 2023) [VERIFIED]
- **Data protection regulations**: GDPR mandates privacy safeguards for healthcare AI, including data controllership, right to erasure, data minimization (Williamson & Prybutok, 2024) [VERIFIED]
  - Challenges in aligning blockchain/edge technologies with GDPR requirements (Williamson & Prybutok, 2024) [VERIFIED]
  - Enforcement mechanisms limited in Southeast Asian contexts (Burns, 2024) [VERIFIED - from Zotero notes]
- **Healthcare privacy standards**: Patient consent and data governance critical for sensitive health applications [REMOVED HIPAA - no citation found]
  - Privacy and accountability principles essential for health security applications (Burns, 2024) [VERIFIED]
- **Accessibility and digital inclusion policies**: Digital health equity frameworks address barriers including cost, digital literacy, infrastructure access (Hatef et al., 2024; Richardson et al., 2022) [VERIFIED]
  - Digital Determinants of Health operate across individual, interpersonal, community, societal levels (Richardson et al., 2022) [VERIFIED]
  - Technology adoption in LMICs faces persistent economic and infrastructure barriers (Sylla et al., 2025) [VERIFIED]

#### 2.4 Regional Context: Southeast Asian Elderly Care

- **Epidemiological evidence**: Fall incidence and incident types in Southeast Asia
  - Thailand: 37.7% of elderly home accidents are falls (Maiyapakdee et al., 2025) [VERIFIED]
  - China: Falls identified as top adverse event in 272 nursing facilities; bed/chair falls explicitly documented (Li & Shi, 2022) [VERIFIED - Paper #47 from filtered_papers_for_thesis.md]
  - Southeast Asia: Fall prevalence 7.5-10% (Thailand/Singapore), 14-34% across Asia (Romli et al., 2017) [VERIFIED]
- **Cultural norms**: Strong family caregiving rooted in filial piety values; preference for home-based care over institutional facilities (Romli et al., 2017) [VERIFIED]
  - Older adults in ASEAN communities often live in extended family households with adult children providing supervision (Romli et al., 2017) [VERIFIED - direct quote from fact-check]
- **Economic constraints**: Affordability thresholds limit technology access in middle-income markets
  - Middle-income Cambodian households (4th-5th quintile): $870-$1,622/month (National Institute of Statistics, 2019) [VERIFIED]
  - Technology adoption in LMICs faces persistent economic and infrastructure barriers (Sylla et al., 2025) [VERIFIED - Option B wording]
- **Technology adoption barriers**: Cost, infrastructure limitations, digital divide create accessibility challenges (Hatef et al., 2024; Sylla et al., 2025) [VERIFIED - Option B wording]

---

### 3. Methodology (3-4 pages)

#### 3.1 Privacy Governance Architecture

This study proposes a privacy governance-driven architecture for elderly safety monitoring and validates its technical feasibility through NIR camera compatibility testing.

**3.1.1 Privacy Governance Principles**

Two architectural mechanisms enforce privacy by design:

1. **Pose-only storage**: System stores only 17 body keypoints (COCO format), excluding face landmarks. Raw video frames never persisted to storage. [VERIFIED - research_summary.md design]

2. **Immediate frame disposal**: Video frames processed in real-time; deleted immediately after keypoint extraction. No video retention eliminates re-identification risk. [VERIFIED - research_summary.md design]

3. **Edge-first processing**: All computation on local device (NVIDIA Jetson Orin Nano 8GB). Zero cloud transmission eliminates network exposure and data sovereignty concerns. [VERIFIED - research_summary.md; NOTE: Jetson is target device, validation done on standard hardware]

**3.1.2 Hardware Design for Cost-Effectiveness**

Proposed system targets middle-income Cambodian households through cost optimization:

- **Cameras**: 4× RGB cameras with 850nm IR night vision (Hikvision DS-2CD1343G2-IUF, $63/camera = $252 total) [VERIFIED - validation_results.md A4.2, hardware_decision.md]
- **Edge processor**: NVIDIA Jetson Orin Nano 8GB ($250) [VERIFIED - validation_results.md A4.2]
- **Accessories**: Storage, UPS, cables ($170) [VERIFIED - validation_results.md A4.2]
- **Total system cost**: $672 (one-time, zero recurring fees) [VERIFIED - validation_results.md A4.2]

**3.1.3 Software Pipeline**

- **Person detection**: YOLOv8n (Nano - lightweight version) identifies person bounding box [VERIFIED - research_summary.md, A1.3 pipeline_comparison]
- **Pose estimation**: MediaPipe extracts 33 skeletal landmarks; system uses 17 body keypoints (COCO format), face landmarks excluded [VERIFIED - research_summary.md]
- **Processing modes tested**: Baseline (MediaPipe only) vs Integrated (YOLO+MediaPipe) [VERIFIED - validation_results.md A1.3]

#### 3.2 NIR Camera Compatibility Validation

**3.2.1 Validation Dataset**

MediaPipe pose estimation validated on 20 commercial 850nm NIR security camera videos:

- **Source**: Professional CCTV demo footage (publicly available online) [VERIFIED - validation_results.md A1.2c]
- **Diversity**: Indoor/outdoor environments, various camera manufacturers (Hikvision, EZviz, dome/turret/bullet types), multiple lighting conditions [VERIFIED - validation_results.md A1.2c]
- **Resolution**: 1080p and 4K [VERIFIED - validation_results.md A1.2c]
- **Purpose**: Validate pose estimation performance on 850nm NIR wavelength (matching target Hikvision DS-2CD1343G2-IUF camera specification) [VERIFIED - validation_results.md A1.2c]
- **Number of videos**: 20 videos total [VERIFIED - validation_results.md A1.2a]

**3.2.2 Validation Procedure**

Two processing pipelines tested on same 20 videos:

1. **Baseline**: MediaPipe pose estimation on full frame [VERIFIED - validation_results.md A1.3]
2. **Integrated**: YOLOv8n person detection → ROI crop → MediaPipe on ROI [VERIFIED - validation_results.md A1.3]

Metrics collected per video: keypoint detection rate (landmarks detected / 33 total), confidence scores, false negative rate (frames with person but no pose detected), processing speed (FPS). [VERIFIED - validation_results.md A1.2a, A1.3]

**3.2.3 Validation Scope**

This validation tests NIR camera compatibility for privacy-preserving monitoring, NOT fall detection accuracy. Confirms technical feasibility of pose estimation on IR footage from affordable security cameras. [VERIFIED - validation_results.md, research_summary.md scope]

#### 3.3 Cost-Effectiveness Analysis

**3.3.1 Comparative Cost Model**

Edge-based system cost compared to cloud-based elderly fall detection alternative (Kami Fall Detect Camera) over 3-year period:

- **Edge system**: Hardware cost ($672 one-time) + zero recurring fees [VERIFIED - validation_results.md A4.2]
- **Cloud system**: Hardware ($99) + mandatory subscription ($45/month × 36 months = $1,620) = $1,719 total [VERIFIED - validation_results.md A4.2; Upadhyay 2025 for Kami pricing]

**3.3.2 Market Accessibility Analysis**

Target market defined by Cambodian household income data:

- **Income brackets**: Cambodia Socio-Economic Survey (CSES) quintile data [VERIFIED - National Institute of Statistics 2019]
- **Target segment**: Middle-income urban households (4th-5th quintile, $870-$1,622/month) [VERIFIED - National Institute of Statistics 2019; validation_results.md A4.2]
- **Market reach calculation**: System cost as percentage of monthly income; estimated percentage of elderly population within affordability threshold [VERIFIED - validation_results.md A4.2 calculation methodology]

#### 3.4 Evaluation Metrics

**NIR camera compatibility:** [VERIFIED - validation_results.md A1.2a, A1.3]

- Keypoint detection rate (33 landmarks detected per frame)
- Pose detection confidence scores
- False negative rate (person present but pose failed)
- Processing speed (FPS)

**Cost-effectiveness:** [VERIFIED - validation_results.md A4.2]

- Total 3-year cost (edge vs cloud)
- Breakeven point (months)
- Market reach (percentage of elderly population)
- Affordability threshold (cost vs monthly income)

#### 3.5 Study Scope and Limitations

**What we validate:**

- NIR camera compatibility: Can MediaPipe detect poses on 850nm IR footage? (Yes - 91.3% keypoint detection on 20 commercial CCTV videos) [VERIFIED - validation_results.md A1.2a]
- Cost-effectiveness: Is edge architecture cheaper than cloud? (Yes - $672 vs $1,719 over 3 years, 61% savings) [VERIFIED - validation_results.md A4.2]
- Privacy architecture: Does design eliminate facial data? (Yes - only 17 body keypoints stored, frames deleted immediately) [VERIFIED - research_summary.md design]

**What we do NOT validate:**

- Fall detection accuracy: Requires benchmark datasets (MCF, LE2I, UP-Fall) - not tested in this paper [VERIFIED - research_summary.md scope]
- Real-world deployment: Requires hardware installation in elderly homes - not done yet [VERIFIED - research_summary.md scope]
- User acceptance: Requires longitudinal studies with actual users - future work [VERIFIED - research_summary.md scope]

**Why these limitations:**
This is a design study demonstrating how privacy governance principles can inform architectural decisions. It validates technical feasibility of the privacy-first approach through NIR camera compatibility and cost-effectiveness analysis, not the complete fall detection system. [VERIFIED - research_summary.md research framing]

---

### 4. Results (3-4 pages)

#### 4.1 NIR Camera Compatibility

MediaPipe pose estimation was validated on 20 commercial 850nm NIR security camera videos from diverse manufacturers and environments (indoor/outdoor, various lighting conditions): [VERIFIED - validation_results.md A1.2a, A1.2c]

- **Keypoint detection rate**: 91.3% (30.1 of 33 landmarks detected on average) [VERIFIED - validation_results.md A1.2a integrated pipeline result]
- **Average confidence**: 0.868 [VERIFIED - validation_results.md A1.2a integrated pipeline result]
- **False negative rate**: 12.3% (frames with person present but pose detection failed) [VERIFIED - validation_results.md A1.2a integrated pipeline result]
- **Processing speed**: 20.53 FPS (integrated YOLO+MediaPipe pipeline) [VERIFIED - validation_results.md A1.3 integrated pipeline]

Pipeline comparison tested baseline MediaPipe versus integrated YOLO+MediaPipe approach on the same 20 videos. [VERIFIED - validation_results.md A1.3] Integrated approach achieved 5.7% higher keypoint detection and 22.2% better pose coverage, but was 2.3× slower (20.53 FPS vs 47.37 FPS). [VERIFIED - validation_results.md A1.3: baseline 85.6%, integrated 91.3%; baseline 63.8%, integrated 86.0%; baseline 47.37 FPS, integrated 20.53 FPS] The integrated pipeline was selected based on safety-critical priority: accuracy over speed when both exceed real-time requirements. [VERIFIED - research_summary.md decision rationale]

#### 4.2 Cost-Effectiveness Analysis

System cost was compared against a cloud-based elderly fall detection alternative (Kami Fall Detect Camera) over a 3-year period: [VERIFIED - validation_results.md A4.2]

- **Edge-based system**: $672 one-time cost ($252 cameras + $250 Jetson Orin Nano + $170 accessories) [VERIFIED - validation_results.md A4.2]
- **Cloud-based alternative**: $1,719 total ($99 hardware + $1,620 subscription at $45/month × 36 months) [VERIFIED - validation_results.md A4.2]
- **Cost savings**: 61% reduction ($1,047 savings over 3 years) [VERIFIED - validation_results.md A4.2: ($1,719-$672)/$1,719 = 60.9%]
- **Breakeven point**: Month 1 of Year 2 [VERIFIED - validation_results.md A4.2: Month 13]

Market accessibility analysis shows edge-based system targets middle-income urban Cambodian households (4th-5th quintile, $870-$1,622/month). [VERIFIED - validation_results.md A4.2; National Institute of Statistics 2019] Estimated reach: 8-12% of elderly population (168,000-252,000 individuals by 2030). [VERIFIED - validation_results.md A4.2] Zero-subscription model eliminates ongoing payment burden, expanding affordability compared to recurring-cost alternatives. [VERIFIED - validation_results.md A4.2 analysis]

---

### 5. Discussion (3-4 pages)

#### 5.1 Governance Implications

**Privacy governance through edge architecture:**
This study demonstrates how privacy governance principles drive architectural design decisions. [VERIFIED - research_summary.md research question] Edge-based processing eliminates cloud transmission requirements, enforcing data locality through system constraints rather than operational promises. [VERIFIED - research_summary.md design] The architecture achieves facial anonymity by design: pose-only storage makes facial recognition impossible, not merely prohibited. [VERIFIED - research_summary.md design: 17 body keypoints only, face landmarks excluded] Validation results (91.3% keypoint detection on 850nm NIR footage) confirm technical feasibility of privacy-first design without performance compromise. [VERIFIED - validation_results.md A1.2a]

**Accessibility governance through cost optimization:**
Edge architecture yields economic co-benefits beyond privacy. Eliminating cloud infrastructure reduces total cost by 61% ($672 vs $1,719 over 3 years), expanding market accessibility from cloud-dependent alternatives. [VERIFIED - validation_results.md A4.2] Zero-subscription model removes recurring payment barriers, targeting middle-income Cambodian households (4th-5th quintile, $870-$1,622/month). [VERIFIED - National Institute of Statistics 2019; validation_results.md A4.2] Estimated reach: 8-12% of elderly population (168,000-252,000 individuals by 2030). Edge-based architecture expands affordability beyond cloud alternatives requiring ongoing subscriptions that limit accessibility for middle-income households. [VERIFIED - validation_results.md A4.2 market reach calculation]

**Context-specific design for developing countries:**
System design incorporates regional epidemiological evidence: three incident types prioritized based on Thai elderly fall data (37.7% prevalence) and Chinese long-term care studies. [VERIFIED - Maiyapakdee 2025; Li & Shi 2022; research_summary.md incident types] Hardware selection (850nm NIR cameras, edge processor) addresses Cambodia's middle-income market constraints while maintaining technical performance requirements. [VERIFIED - validation_results.md A1.2c, A4.2] This demonstrates governance-driven design approach for resource-constrained contexts. [VERIFIED - research_summary.md research question]

#### 5.2 Technical Validation Contributions

**NIR camera compatibility for privacy-preserving monitoring:**
Validated MediaPipe pose estimation on 850nm NIR footage (91.3% keypoint detection, 20 diverse commercial CCTV videos). [VERIFIED - validation_results.md A1.2a, A1.2c] Confirms feasibility of 24/7 elderly monitoring without facial recognition technology. Limited research has empirically validated pose estimation performance on NIR wavelengths used in affordable security cameras for elderly monitoring applications. [VERIFIED - gap identified in research_summary.md; supported by Wang et al. 2020 survey showing need for validation]

**Pipeline trade-off analysis for safety-critical systems:**
Comparison of baseline versus integrated YOLO+MediaPipe revealed accuracy-speed trade-off: integrated approach achieved 5.7% higher detection and 22.2% better coverage, but 2.3× slower. [VERIFIED - validation_results.md A1.3: 91.3% vs 85.6%, 86.0% vs 63.8%, 20.53 FPS vs 47.37 FPS] Decision prioritized accuracy for safety-critical application where missing fall detection has fatal consequences. Both configurations exceed real-time requirements (20.53 FPS vs 15 FPS target). [VERIFIED - validation_results.md A1.3; 15 FPS target from research_summary.md]

#### 5.3 Limitations

- **Validation scope**: This study validates NIR camera compatibility and cost-effectiveness, not fall detection accuracy. Incident classification performance requires validation on benchmark fall datasets (MCF, LE2I, UP-Fall). [VERIFIED - research_summary.md scope]

- **Testing environment**: MediaPipe pose estimation tested on commercial CCTV footage, not actual elderly subjects. Movement patterns, body proportions, and gait characteristics of elderly individuals may differ from commercial video subjects. [VERIFIED - validation_results.md A1.2c dataset description]

- **Hardware deployment**: Processing speed (20.53 FPS) measured on standard hardware, not yet validated on target edge device (Jetson Orin Nano 8GB). Real-world deployment performance requires hardware validation. [VERIFIED - validation_results.md A1.3; research_summary.md notes Jetson is target, not tested]

- **Market accessibility**: Edge-based system ($672) targets middle-income urban households (4th-5th quintile). Low-income and rural elderly populations require subsidies or alternative deployment models to achieve accessibility. [VERIFIED - validation_results.md A4.2]

#### 5.4 Future Directions

- **Benchmark dataset validation**: Validate fall detection accuracy on MCF, LE2I, UP-Fall datasets [VERIFIED - research_summary.md future work]
- **Custom dataset collection**: Collect CamTech dataset (180 videos: 60 per incident type across 3 lighting conditions) with simulated incidents using age-appropriate actors to address Western dataset bias [VERIFIED - research_summary.md future work, dataset plan]
- **Hardware validation**: Deploy full pipeline on Jetson Orin Nano (validate 20.53 FPS target) [VERIFIED - research_summary.md future work]
- **Expanded detection**: Add more incident types based on local epidemiological data [VERIFIED - research_summary.md future work]
- **Policy framework**: Develop governance guidelines for healthcare AI in developing countries [VERIFIED - research_summary.md future work]

---

### 6. Conclusion (1-2 pages)

#### 6.1 Key Findings

This study demonstrates privacy governance-driven architectural design through a Cambodia elderly monitoring case study: [VERIFIED - research_summary.md research question]

- **Technical feasibility**: Edge-based pose estimation achieves 91.3% keypoint detection on 850nm NIR footage, validating 24/7 privacy-preserving monitoring capability [VERIFIED - validation_results.md A1.2a]
- **Cost-effectiveness**: Edge architecture reduces 3-year total cost by 61% ($672 vs $1,719 cloud alternative), expanding market reach to 168,000-252,000 elderly in middle-income Cambodian households [VERIFIED - validation_results.md A4.2]
- **Design trade-offs**: Safety-critical priority guides pipeline selection—integrated approach chosen despite 2.3× slower speed due to 5.7% accuracy gain and 22.2% better pose coverage [VERIFIED - validation_results.md A1.3; research_summary.md decision rationale]
- **Governance-driven design**: Privacy governance principles informed architectural decisions from inception (edge processing, pose-only storage, immediate frame disposal) rather than being retrofitted post-deployment [VERIFIED - research_summary.md design; Cavoukian 2010 Privacy by Design]

#### 6.2 Implications for Practice

**For healthcare AI developers:**

- NIR camera compatibility requires empirical validation before deployment; pose estimation performance varies by camera type and environment (73.8%-98.9% range observed) [VERIFIED - validation_results.md A1.2a individual video results]
- Integrated pipeline achieves 20.53 FPS on standard hardware, suggesting edge deployment feasibility though Jetson Orin Nano validation remains necessary [VERIFIED - validation_results.md A1.3; limitation noted in research_summary.md]

**For policymakers:**

- Privacy-by-design architecture can yield economic co-benefits (cost reduction) beyond privacy protection alone [VERIFIED - validation_results.md A4.2 analysis]
- Zero-subscription models expand healthcare technology accessibility in middle-income markets compared to recurring-fee alternatives [VERIFIED - validation_results.md A4.2 market reach analysis]

---

### References

- APA 6th style
- Include key papers from main research project
- Add governance/policy literature
- Regional context references (Thailand, China epidemiological data)

---

## Writing Notes

### Tone and Audience

- **Interdisciplinary**: Accessible to policy makers, healthcare innovators, AI researchers
- **Evidence-based**: Quantified claims with citations
- **Governance-focused**: Emphasize policy implications over technical details
- **Regional context**: Cambodia/Southeast Asia specificity

### Key Statistics to Highlight

- **61% cost reduction**: $672 vs $1,719 over 3 years
- **91.3% keypoint detection**: 850nm NIR validation, 20 commercial CCTV videos
- **168,000-252,000 potential users**: 8-12% of Cambodian elderly population
- **37.7% fall prevalence**: Thai elderly home accidents (Maiyapakdee et al., 2025)
- **20.53 FPS**: Integrated pipeline on standard hardware
- **100% on-device**: Zero cloud transmission, immediate frame disposal

### Governance Themes to Emphasize

1. Privacy governance through edge computing
2. Accessibility governance through cost optimization
3. Context-specific design for developing countries
4. Evidence-based incident prioritization

---

## Next Steps

- [x] Review conference paper length requirements (5000-8000 words confirmed)
- [x] Develop detailed section outlines (completed above)
- [x] Identify supporting literature for each section (38 papers ready)
- [x] **Rigorously verify all citations** (Sections 1-6 complete with [VERIFIED] tags, all claims traced to sources)
- [ ] Draft introduction and literature review
- [x] Incorporate validation results (NIR compatibility, pipeline comparison, cost analysis complete)
- [ ] Draft discussion section
- [ ] Proofread for APA 6th style compliance

---

## References

- Research summary: [research_summary.md](research_summary.md)
- Key messages: [key_messages.md](key_messages.md)
- Conference requirements: [conference_requirements.md](conference_requirements.md)
- Main research project: `/Users/monireach/projects/ai_research`
