# Q&A Preparation Guide - ASIP 2025 Presentation

**Purpose**: Comprehensive preparation for audience questions during 10-minute Q&A session

**Strategy**: Organized by topic area with detailed answers, supporting evidence, and paper section references

---

## Topic Area 1: Privacy and Data Protection

### Q1: How do you ensure privacy with cameras in elderly homes?

**Short Answer** (30 seconds):
Our system ensures privacy through architecture, not policy. We extract only skeletal pose data—17 body keypoints—and immediately discard the raw video frame. The system never stores or transmits facial images. It's architecturally impossible to reconstruct faces from pose data alone because that information simply doesn't exist in our stored data.

**Detailed Answer** (1 minute):
Three architectural mechanisms enforce privacy by design. First, pose-only storage: we extract 17 body keypoints in COCO format and explicitly exclude face landmarks. Second, immediate frame disposal: raw video frames are processed in real-time and deleted immediately after keypoint extraction—we retain no video footage. Third, edge-first processing: all computation occurs on the local Jetson Orin Nano device with 100% on-device processing and zero cloud transmission.

This reflects Cavoukian's Privacy by Design framework—embedding privacy into architecture from inception. The difference from commercial systems is we implement this proactively during design, not retrofitting privacy controls after deployment. Cloud-based alternatives like Kami Fall Detect Camera transmit video to third-party servers for processing, creating facial recognition and re-identification risks we eliminate architecturally.

**Supporting Evidence**:
- 100% on-device processing (designed for edge deployment)
- Pose-only storage with immediate frame disposal
- Zero facial recognition capability by design
- No cloud subscription or data transmission

**Paper Reference**: Section 3.1 (Privacy Governance Architecture), Section 5.1 (Discussion - Governance Implications)

---

### Q2: Can families still identify their elderly relative from pose data?

**Short Answer** (20 seconds):
No. Skeletal pose data shows body joint positions, not facial features, clothing, or identifying characteristics. The pose keypoints look identical regardless of whether it's your grandmother or mine—you see a stick figure representation of body position, not personal identity.

**Detailed Answer** (45 seconds):
The 17 body keypoints represent joint positions: shoulders, elbows, wrists, hips, knees, ankles, etc. This data cannot reconstruct facial features, skin tone, clothing, hair, or any visual characteristics that enable identification. Re-identification would require linking pose patterns to known individuals, which is technically infeasible in private home settings without comparison databases. Unlike commercial cameras storing video footage where you can clearly see faces, our system stores only numerical coordinates of body joints.

**Supporting Evidence**:
- COCO format: 17 body keypoints (no face landmarks)
- Cannot reconstruct facial features from pose data alone
- No visual characteristics stored (clothing, hair, skin tone)

**Paper Reference**: Section 3.1.1 (Privacy Governance Principles)

---

### Q3: What about data breaches or hacking? Could someone access the pose data remotely?

**Short Answer** (30 seconds):
Edge-first architecture minimizes breach risk because data never leaves the household. No cloud transmission means no network exposure. An attacker would need physical access to the Jetson device in the elderly person's home. Even if they gained access, the stored pose data contains no facial features or identifying information.

**Detailed Answer** (1 minute):
Network security benefits from edge processing. Cloud-based systems transmit data over the internet to third-party servers, creating multiple attack vectors—network interception, server breaches, credential theft. Our edge architecture eliminates network transmission entirely. All processing and storage occur locally on the Jetson Orin Nano device.

Physical security requires protecting the edge device itself. In deployment, we recommend standard security measures: device encryption, secure boot, regular firmware updates, physical device locks. The risk profile differs significantly—cloud breaches can expose thousands of users simultaneously, while edge deployment requires individual physical access per household.

Importantly, even in a breach scenario, the stored data contains only pose keypoints with no facial features. An attacker gains skeletal joint positions, not video footage enabling identification or re-identification.

**Supporting Evidence**:
- Zero cloud transmission = no network exposure
- Physical device security requires household access
- Pose-only storage limits breach impact
- Data sovereignty: data never leaves household

**Paper Reference**: Section 3.1.1 (Privacy Governance Principles), Section 5.1 (Discussion - Privacy Governance)

---

## Topic Area 2: Cost and Affordability

### Q4: Can middle-income households really afford $672 upfront cost?

**Short Answer** (30 seconds):
Yes, for our target demographic. Cambodian households earning $870-$1,622 per month (4th-5th income quintiles) can allocate this one-time cost for elderly parent safety. It's equivalent to 0.5-0.8 months of household income. More importantly, it's 61% cheaper than cloud alternatives costing $1,719 over three years with ongoing subscriptions.

**Detailed Answer** (1 minute):
Middle-income Cambodian households in the fourth and fifth income quintiles earn $870 to $1,622 monthly according to Cambodia's 2019 Socio-Economic Survey. The $672 system cost represents 0.5 to 0.8 months of household income as a one-time investment.

The comparison to cloud alternatives is critical. Kami Fall Detect Camera costs $99 hardware plus $45 monthly subscription—$1,719 over three years. That subscription represents 5.2% of monthly income indefinitely for middle-income households, creating ongoing financial burden. Our edge system eliminates recurring fees entirely.

From a household budgeting perspective, families allocate resources for elderly parent safety comparable to purchasing a smartphone or appliance—significant but manageable one-time expense. The zero-subscription model is actually more affordable long-term than cloud alternatives requiring perpetual payments.

We acknowledge low-income and rural elderly populations cannot afford $672. Those segments require subsidies, government programs, or alternative deployment models—that's explicitly noted in our paper's limitations section.

**Supporting Evidence**:
- Target market: $870-$1,622/month (4th-5th quintile)
- One-time cost: $672 = 0.5-0.8 months income
- Cloud alternative: $45/month = 5.2% of monthly income indefinitely
- 61% cost reduction over 3 years ($672 vs $1,719)

**Paper Reference**: Section 4.2 (Cost-Effectiveness Analysis), Section 5.1 (Accessibility Governance), Section 5.3 (Limitations)

---

### Q5: Why not use cheaper cameras or processors to reduce the $672 cost further?

**Short Answer** (30 seconds):
We optimized for the minimum viable cost while maintaining technical requirements. The Hikvision cameras at $63 each are already budget security cameras—lower-cost options sacrifice 850nm IR quality or reliability. The Jetson Orin Nano at $250 is the most affordable edge AI processor capable of real-time multi-camera inference.

**Detailed Answer** (1 minute):
Hardware selection balances cost constraints with technical requirements. The Hikvision DS-2CD1343G2-IUF cameras cost $63 per unit—these are budget commercial security cameras, not premium options. Lower-cost alternatives sacrifice 850nm IR night vision quality, reliability, or lack RTSP streaming capabilities needed for multi-camera integration.

For edge processing, the Jetson Orin Nano represents the minimum viable specification. Our integrated pipeline achieves 20.53 frames per second on standard hardware; we require similar performance on the edge device. Cheaper processors like Raspberry Pi 4 cannot handle real-time inference on YOLOv8n plus MediaPipe for four simultaneous camera streams. Higher-end Jetson models (Orin NX, AGX) cost $400-$2,000—overkill for our application.

The $170 accessories include necessary components: microSD storage, UPS for power backup during outages, Ethernet cables, camera mounts. These aren't luxuries—they're deployment requirements.

We absolutely prioritize cost reduction for accessibility. But cost optimization must maintain technical feasibility. Further cost reduction requires component-level redesign or economies of scale through mass production, which are beyond this research study's scope.

**Supporting Evidence**:
- Hikvision cameras: $63/unit (budget tier, not premium)
- Jetson Orin Nano: $250 (minimum spec for real-time multi-camera inference)
- Accessories: $170 (necessary deployment components)
- Alternative processors lack real-time performance capability

**Paper Reference**: Section 3.1.2 (Hardware Design for Cost-Effectiveness), Validation Results A4.2

---

### Q6: How does the breakeven point work? You said Month 13 of Year 2?

**Short Answer** (20 seconds):
The edge system costs $672 upfront. The cloud alternative costs $99 hardware plus $45 monthly subscription. After 12.7 months—month 1 of year 2—the cumulative cloud cost ($99 + 12.7×$45 = $672) equals our edge system cost. Beyond that point, cloud users continue paying $45/month while edge users pay nothing.

**Detailed Answer** (45 seconds):
Breakeven calculation: Edge cost is constant at $672. Cloud cost accumulates monthly: $99 + ($45 × months). Setting these equal: $672 = $99 + ($45 × M). Solving: $573 = $45M, so M = 12.7 months, which is month 1 of year 2.

After breakeven, the cost advantage compounds. At 36 months, cloud users have paid $1,719 total while edge users remain at $672. The savings grow over time—year 4 adds another $540 cloud costs, year 5 another $540, indefinitely. For long-term elderly monitoring spanning years or decades, the zero-subscription model provides substantial lifetime savings.

**Supporting Evidence**:
- Edge: $672 constant
- Cloud: $99 + ($45/month × 36 months) = $1,719
- Breakeven: Month 13 (12.7 months)
- Lifetime savings compound beyond 3 years

**Paper Reference**: Section 4.2 (Cost-Effectiveness Analysis), Validation Results A4.2

---

## Topic Area 3: Technical Performance

### Q7: Does this actually work in complete darkness? How well?

**Short Answer** (30 seconds):
Yes, validated. MediaPipe pose estimation achieves 91.3% keypoint detection on 850nm near-infrared footage from commercial security cameras. We tested 20 diverse CCTV videos including nighttime scenarios. This confirms 24/7 monitoring capability without visible light or facial recognition technology.

**Detailed Answer** (1 minute):
We validated MediaPipe pose estimation performance on 20 commercial 850nm infrared security camera videos sourced from publicly available CCTV demo footage. The dataset included nighttime scenarios with complete darkness—cameras using IR illumination only, no visible light. MediaPipe, originally trained on visible spectrum RGB images, successfully generalized to 850nm near-infrared wavelengths.

Performance metrics: 91.3% keypoint detection rate detecting 30.1 of 33 landmarks on average, 0.868 average confidence, 12.3% false negative rate. Importantly, we observed variation across individual videos—detection ranged from 73.8% to 98.9% depending on camera type, environment, and subject position. The 91.3% is the mean across all 20 videos.

This validation addresses a critical gap. Limited prior research empirically validated pose estimation on NIR wavelengths used in affordable security cameras for elderly monitoring. Most computer vision datasets use visible spectrum RGB. Our results confirm RGB-trained models can transfer to 850nm IR, enabling privacy-preserving 24/7 monitoring.

**Supporting Evidence**:
- 91.3% keypoint detection on 850nm IR footage
- 20 diverse commercial CCTV videos (multiple manufacturers, environments)
- 0.868 average confidence
- Range: 73.8%-98.9% across individual videos

**Paper Reference**: Section 4.1 (NIR Camera Compatibility), Validation Results A1.2a, A1.2c

---

### Q8: What's the false negative rate? How often does it miss detecting a person?

**Short Answer** (20 seconds):
12.3% false negative rate on our NIR validation dataset. This means in 12.3% of frames where a person is present, pose detection failed. The remaining 87.7% of frames successfully detected poses when people were visible.

**Detailed Answer** (1 minute):
False negative rate measures frames where a person is present in the camera view but the pose estimation pipeline fails to detect them. Our integrated pipeline achieved 12.3% false negative rate across 20 infrared validation videos.

Several factors contribute to false negatives: severe occlusion where body parts are blocked, extreme poses like lying flat facing away from camera, poor lighting even with IR illumination, distance from camera exceeding optimal range. These are inherent challenges in computer vision, not unique to our system.

For safety-critical fall detection, false negatives are more concerning than false positives. Missing a fall detection has fatal consequences. This is why we selected the integrated YOLO+MediaPipe pipeline despite 2.3× slower speed—it reduced false negatives by improving detection accuracy from 86.1% baseline to 91.3% integrated.

Importantly, our validation tested pose detection capability on IR footage, not fall detection accuracy. Fall detection requires validating on benchmark datasets like MCF, LE2I, UP-Fall, which is future work. The 12.3% false negative rate applies to pose detection in IR conditions, not incident classification performance.

**Supporting Evidence**:
- 12.3% false negative rate (integrated pipeline on NIR footage)
- Factors: occlusion, extreme poses, lighting, distance
- Integrated pipeline selected to minimize false negatives
- Validation scope: pose detection, NOT fall detection

**Paper Reference**: Section 4.1 (NIR Camera Compatibility), Validation Results A1.2a

---

### Q9: Why did you choose the slower integrated pipeline instead of the faster baseline?

**Short Answer** (30 seconds):
Safety-critical priority. The integrated pipeline is 2.3× slower but achieves 5.7% higher keypoint detection and 22.2% better pose coverage. Missing a fall detection can have fatal consequences, so we prioritize accuracy over speed when both configurations exceed real-time requirements—20.53 FPS versus our 15 FPS target.

**Detailed Answer** (1 minute):
We compared baseline MediaPipe against integrated YOLO+MediaPipe on the same 20 infrared videos. Baseline achieved 86.1% keypoint detection at 47.37 frames per second. Integrated achieved 91.3% detection and 96.9% pose coverage at 20.53 FPS—5.7% more accurate but 2.3 times slower.

The decision prioritizes accuracy for safety-critical applications. In elderly monitoring, false negatives—missing fall detections—can result in delayed emergency response, serious injury, or death. Speed optimization is valuable, but not at the cost of detection accuracy when lives are at stake.

Critically, both configurations exceed real-time requirements. Our target is 15 frames per second for responsive monitoring. Even the slower integrated pipeline delivers 20.53 FPS, providing 37% performance headroom above target. Going from 20.53 to 47.37 FPS doesn't improve user experience or safety outcomes—the system already responds in real-time.

This reflects a governance perspective: technical performance metrics must be evaluated against application context and consequences, not optimized in isolation.

**Supporting Evidence**:
- Integrated: 91.3% detection, 96.9% coverage, 20.53 FPS
- Baseline: 86.1% detection, 79.5% coverage, 47.37 FPS
- Target: 15 FPS (both exceed real-time requirements)
- Safety-critical priority: accuracy > speed

**Paper Reference**: Section 4.1 (NIR Camera Compatibility), Section 5.2 (Technical Validation Contributions), Validation Results A1.3

---

### Q10: Have you tested this on actual Jetson Orin Nano hardware?

**Short Answer** (15 seconds):
Not yet. Processing speed of 20.53 FPS was measured on standard hardware, not the target Jetson Orin Nano device. Hardware validation on the Jetson is planned future work and explicitly noted as a limitation in our paper.

**Detailed Answer** (45 seconds):
Our validation measured processing performance on standard computing hardware during development. The Jetson Orin Nano is the target deployment device based on specifications: 8GB RAM, 1024 CUDA cores, designed for edge AI inference. Literature benchmarks show Jetson Orin Nano handles YOLOv8n and MediaPipe individually at real-time speeds.

However, we have not validated our specific integrated pipeline on actual Jetson hardware. Real-world performance may differ due to memory bandwidth constraints, thermal throttling, multi-camera stream processing overhead. This is a limitation we explicitly acknowledge in Section 5.3 of the paper.

Future work includes deploying the full pipeline on Jetson Orin Nano, validating sustained performance across four simultaneous camera streams, and optimizing for edge-specific constraints. The 20.53 FPS result provides a performance benchmark suggesting feasibility, but hardware validation is required before production deployment.

**Supporting Evidence**:
- Current: 20.53 FPS on standard hardware
- Target: NVIDIA Jetson Orin Nano 8GB
- Limitation: Hardware deployment not yet validated
- Future work: Jetson performance validation planned

**Paper Reference**: Section 5.3 (Limitations), Section 5.4 (Future Directions), Validation Results A1.3

---

## Topic Area 4: Validation Scope and Research Design

### Q11: What exactly did you validate in this paper? It seems limited.

**Short Answer** (30 seconds):
We validated NIR camera compatibility and cost-effectiveness, not fall detection accuracy. This is a design study demonstrating how privacy governance principles inform architectural decisions through feasibility validation. Fall detection accuracy requires benchmark datasets like MCF, LE2I, UP-Fall—that's planned future work.

**Detailed Answer** (1 minute):
The research scope is intentionally focused. We validated three components: first, NIR camera compatibility—testing whether MediaPipe pose estimation works on 850nm infrared footage from affordable security cameras, achieving 91.3% keypoint detection across 20 diverse commercial CCTV videos. Second, cost-effectiveness—comparing our edge-based system's three-year total cost against cloud alternatives, demonstrating 61% reduction. Third, privacy architecture—analyzing whether pose-only storage eliminates facial data collection by design.

We explicitly did NOT validate fall detection accuracy, which requires testing on benchmark fall datasets, real-world deployment in actual elderly homes, or longitudinal user acceptance studies with elderly participants and caregivers.

This limitation is intentional, not a flaw. Our research question asks how privacy governance principles inform architectural design in resource-constrained contexts. The goal is demonstrating that privacy-first edge architecture is technically and economically viable through feasibility validation, establishing the foundation for future empirical work on detection accuracy. We're not claiming a complete validated fall detection system—we're showing the governance-driven architecture is feasible.

**Supporting Evidence**:
- Validated: NIR compatibility (91.3%), cost-effectiveness (61% savings), privacy architecture
- Not validated: Fall detection accuracy, real-world deployment, user acceptance
- Research type: Design study with technical feasibility validation
- Future work: Benchmark dataset testing, hardware validation, user studies

**Paper Reference**: Section 3.5 (Study Scope and Limitations), Section 5.3 (Limitations)

---

### Q12: Why didn't you test on benchmark fall detection datasets like MCF or LE2I?

**Short Answer** (20 seconds):
Time and scope constraints for this conference paper. Our immediate goal was validating the governance-driven architecture's feasibility—NIR compatibility and cost-effectiveness. Benchmark dataset testing for fall detection accuracy is the next research phase, explicitly planned as future work.

**Detailed Answer** (1 minute):
Benchmark dataset validation requires significant additional work: downloading MCF (192 videos), LE2I (191 videos), and UP-Fall datasets; implementing the full CNN+LSTM+Transformer incident classification module; training models; evaluating performance with cross-validation; comparing against baseline methods. This extends beyond the ASIP conference paper timeline.

Our research strategy is phased. Phase 1, completed for ASIP, validates architectural feasibility: can we achieve privacy governance through edge processing while maintaining technical capability (NIR compatibility) and economic viability (cost-effectiveness)? Phase 2, future work, validates detection accuracy: does the system accurately classify falls and incidents on benchmark datasets?

This phased approach is methodologically sound. There's no point investing months in fall detection algorithm training if the foundational architecture is technically or economically infeasible. We first establish feasibility, then build on that foundation for accuracy validation.

The ASIP conference focuses on technology governance, making the governance-driven architecture story the appropriate contribution. Full system validation suits future journal publications in healthcare informatics or AI applications.

**Supporting Evidence**:
- Benchmark datasets identified: MCF, LE2I, UP-Fall
- Future work: Fall detection accuracy validation
- Phased research strategy: feasibility first, then accuracy
- Conference focus: governance contribution, not complete system

**Paper Reference**: Section 5.4 (Future Directions), Section 3.5 (Study Scope and Limitations)

---

### Q13: How did you ensure the 20 CCTV videos represent real elderly monitoring scenarios?

**Short Answer** (25 seconds):
We didn't—and that's a limitation we acknowledge. The 20 videos are commercial CCTV demo footage, not actual elderly subjects. Movement patterns, body proportions, and gait characteristics of elderly individuals may differ from commercial video subjects. This validates NIR wavelength compatibility, not elderly-specific performance.

**Detailed Answer** (1 minute):
The validation dataset uses publicly available professional CCTV demo footage from commercial security camera manufacturers—Hikvision, EZviz, dome, turret, and bullet camera types. These videos demonstrate camera capabilities across indoor and outdoor environments, various lighting conditions, and different scenarios.

However, the subjects in these videos are not elderly individuals. Elderly people have distinct characteristics: altered gait patterns, slower movement speed, different body proportions, potential mobility aids like walkers or canes, postural changes. Our validation confirms MediaPipe can detect poses on 850nm NIR footage generally, but performance on elderly subjects specifically requires targeted validation.

This limitation is explicitly acknowledged in Section 5.3 of the paper. Future work includes collecting a custom CamTech dataset with 180 videos using age-appropriate actors simulating the three incident types across three lighting conditions. This will address elderly-specific validation.

The current validation establishes NIR wavelength compatibility as a necessary first step. Elderly-specific performance validation builds on this foundation.

**Supporting Evidence**:
- Dataset: Commercial CCTV demo footage (diverse manufacturers, environments)
- Subjects: Not elderly individuals
- Limitation: Movement patterns, body proportions, gait may differ for elderly
- Future work: Custom CamTech dataset with age-appropriate actors

**Paper Reference**: Section 3.2.1 (Validation Dataset), Section 5.3 (Limitations), Section 5.4 (Future Directions)

---

## Topic Area 5: Governance and Policy

### Q14: How does this relate to existing AI governance frameworks like GDPR or UNESCO AI Ethics?

**Short Answer** (30 seconds):
Our architecture operationalizes governance principles through design. GDPR mandates data minimization and privacy safeguards—we achieve this through pose-only storage and edge processing. UNESCO AI Ethics emphasizes transparency and human rights—we enable these through privacy-by-design eliminating surveillance risks. We translate regulatory principles into architectural implementation.

**Detailed Answer** (1 minute):
Existing governance frameworks establish principles; our research demonstrates implementation. GDPR mandates privacy safeguards for healthcare AI including data minimization, right to erasure, and data controllership. Our pose-only storage inherently minimizes data—we retain 17 body keypoints versus full video footage. Edge processing ensures data controllership remains with the household, not third-party cloud providers. Right to erasure is architecturally enforced—raw frames are immediately deleted.

UNESCO AI Ethics guidelines emphasize transparency, accountability, fairness, and human rights. Our privacy-by-design architecture enhances transparency—families know exactly what data is captured and stored (pose keypoints, not faces). Eliminating facial recognition capability protects human rights to privacy and freedom from surveillance.

The contribution here is operationalizing abstract governance principles in resource-constrained contexts. Burns (2024) identifies edge computing potential for privacy governance but doesn't quantify cost-effectiveness implications. Birkstedt et al. (2023) note implementation guidance remains limited for translating ethical principles into practice. Our work bridges that gap—showing how privacy governance principles drive specific architectural decisions with measurable technical and economic outcomes.

**Supporting Evidence**:
- GDPR compliance: data minimization, controllership, right to erasure
- UNESCO ethics: transparency, human rights, privacy protection
- Implementation focus: principles → architecture → measurable outcomes
- Cost-effectiveness quantification: 61% reduction, market reach data

**Paper Reference**: Section 2.3 (Technology Governance Frameworks), Section 5.1 (Governance Implications)

---

### Q15: Can this governance model scale to other healthcare AI applications beyond elderly monitoring?

**Short Answer** (25 seconds):
Yes, the governance-driven design approach is generalizable. Edge-first processing, data minimization through specific feature extraction, and immediate raw data disposal apply to any healthcare AI requiring privacy and cost-effectiveness: chronic disease monitoring, rehabilitation tracking, mental health applications.

**Detailed Answer** (1 minute):
The architectural principles transfer across healthcare AI domains. Edge-first processing provides data locality benefits for any sensitive health application. Data minimization through targeted feature extraction—retaining only clinically relevant information, discarding identifying characteristics—applies broadly. Immediate raw data disposal eliminates re-identification risks universally.

Specific examples: diabetes monitoring could extract blood glucose trends from continuous monitor data while discarding device identifiers. Rehabilitation tracking could capture joint range-of-motion from video while deleting facial features. Mental health applications could analyze speech patterns for depression indicators while protecting voice identity.

The economic co-benefits of edge architecture—eliminating cloud subscriptions—extend to any long-term monitoring application where recurring costs create accessibility barriers. This is particularly relevant for chronic disease management in developing countries requiring sustained multi-year monitoring.

However, technical feasibility varies by application. Real-time inference requirements, sensor modalities, computational complexity, and accuracy thresholds differ across use cases. The governance approach scales; implementation details require domain-specific adaptation.

**Supporting Evidence**:
- Generalizable principles: edge processing, data minimization, raw data disposal
- Example applications: diabetes, rehabilitation, mental health monitoring
- Economic benefits: subscription elimination for long-term monitoring
- Domain-specific adaptation required for technical implementation

**Paper Reference**: Section 5.1 (Governance Implications), Discussion of accessibility governance

---

### Q16: What policy recommendations would you make for developing countries adopting healthcare AI?

**Short Answer** (30 seconds):
Three recommendations: First, require privacy-by-design in AI procurement—mandate edge processing or equivalent data locality mechanisms. Second, evaluate total cost of ownership including subscriptions, not just upfront hardware costs. Third, encourage context-specific design using regional epidemiological data rather than uncritically adopting Western solutions.

**Detailed Answer** (1+ minutes):
First, policy should require privacy-by-design architectures in healthcare AI procurement. Government contracts and regulatory approval processes should mandate specific mechanisms: data locality through edge processing, data minimization with technical verification, transparency about data retention practices. This shifts privacy from operational compliance to architectural requirement.

Second, economic evaluation must consider total cost of ownership over the technology lifecycle. Many cloud-based systems appear affordable upfront—$99 hardware—but impose ongoing subscription burdens—$1,719 over three years. Developing country procurement policies should standardize multi-year cost analysis and prioritize zero-subscription models for long-term affordability.

Third, encourage context-specific innovation. Our system prioritizes fall incidents accounting for 37.7% of Thai elderly home accidents, not arbitrary incident types from Western datasets. Policies should incentivize using regional epidemiological evidence, targeting local income brackets, and adapting to cultural norms like home-based care preferences in Southeast Asia.

Fourth, I'd add: invest in local AI research capacity rather than solely importing foreign technologies. Our validation work—testing NIR compatibility, cost analysis—represents locally-generated evidence appropriate for Cambodia's context. Policy support for regional research institutions builds sustainable innovation ecosystems.

**Supporting Evidence**:
- Privacy-by-design procurement requirements
- Total cost of ownership analysis (multi-year subscriptions)
- Context-specific design using regional evidence
- Local research capacity investment

**Paper Reference**: Section 5.1 (Governance Implications), Section 6.2 (Implications for Practice)

---

## Topic Area 6: Regional Context and Scalability

### Q17: Why focus on Cambodia specifically? Does this work in other Southeast Asian countries?

**Short Answer** (25 seconds):
Cambodia provides the case study context for middle-income households, but the model scales across Southeast Asia and similar developing regions. Shared challenges include aging populations, privacy concerns with limited enforcement, cost sensitivity, and cultural preference for home-based elderly care.

**Detailed Answer** (1 minute):
Cambodia-specific factors inform our design: 1.8 million elderly by 2030, middle-income households earning $870-$1,622 monthly per Socio-Economic Survey data, and aging-in-place cultural norms rooted in filial piety. However, these characteristics generalize across Southeast Asia.

Thailand shares similar fall prevalence—37.7% of elderly home accidents per Maiyapakdee et al.—and cultural caregiving norms per Romli et al.'s regional study. Vietnam, Laos, Myanmar face comparable aging trends, middle-income market growth, and home-based care preferences. The governance challenges—privacy concerns with nascent data protection enforcement, cost barriers to cloud subscriptions, bandwidth limitations—extend across the region.

Beyond Southeast Asia, the model applies to South Asia (India, Bangladesh, Pakistan) and Sub-Saharan Africa contexts with similar constraints: aging populations, resource limitations, privacy governance gaps, cost sensitivity. The specific income thresholds, epidemiological priorities, and hardware availability require localization, but the architectural approach—edge processing for privacy and cost optimization—transfers.

Cambodia serves as the initial case study. Validation in other countries requires adapting income analysis, incident priorities, and infrastructure assumptions to local contexts.

**Supporting Evidence**:
- Cambodia: 1.8M elderly, $870-$1,622/month target market, home-based care norms
- Regional parallels: Thailand (falls data), Vietnam/Laos (similar constraints)
- Scalability: South Asia, Sub-Saharan Africa (aging, privacy, cost challenges)
- Localization required: income thresholds, epidemiological data, infrastructure

**Paper Reference**: Section 5.1 (Context-Specific Design), Section 2.4 (Regional Context: Southeast Asian Elderly Care)

---

### Q18: How did you select the three incident types? Why not include more?

**Short Answer** (25 seconds):
Evidence-based prioritization using regional epidemiological data. Falls while standing/walking account for 37.7% of Thai elderly home accidents. Falls from bed/chair are documented in Chinese long-term care facilities. Abnormal sit-to-stand transitions predict fall risk at 99.42% accuracy. We prioritize high-impact incidents with regional evidence.

**Detailed Answer** (1 minute):
Incident selection balances epidemiological evidence, technical feasibility, and research scope. Falls while standing or walking represent 37.7% of Thai elderly home accidents according to Maiyapakdee et al.'s 2025 research—the highest-prevalence category. Falls from bed or chair show median 1.32 incidents per facility in Chinese nursing homes per Li and Shi's 2022 study, indicating significant occurrence. Abnormal sit-to-stand transitions serve as pre-fall risk indicators, achieving 99.42% detection accuracy in literature as early warning signals.

We deliberately use regional Southeast Asian data—Thailand and China—rather than Western datasets. Southeast Asian elderly populations have different fall patterns, living arrangements, and caregiver availability compared to North American or European contexts documented by Romli et al.

More incident types—choking, cardiac events, medication errors—expand scope beyond computer vision capabilities or require additional sensors. This research focuses on vision-based contactless monitoring. Future work can expand detection based on local epidemiological priorities identified through Cambodia-specific elderly safety data collection.

The three incident types demonstrate sufficient complexity for governance-driven architecture validation while maintaining research feasibility.

**Supporting Evidence**:
- Falls standing/walking: 37.7% Thai elderly home accidents (Maiyapakdee 2025)
- Falls from bed/chair: Median 1.32 per facility China (Li & Shi 2022)
- Sit-to-stand abnormality: 99.42% detection accuracy (literature)
- Regional evidence prioritized over Western datasets

**Paper Reference**: Section 2.4 (Regional Context), Section 3.1.3 (Software Pipeline - incident types), Section 5.1 (Context-Specific Design)

---

## Topic Area 7: Practical Implementation

### Q19: When will this system be available for actual deployment in Cambodian homes?

**Short Answer** (20 seconds):
Not immediately—this is early-stage research. Before deployment, we must validate fall detection accuracy on benchmark datasets, test hardware performance on Jetson Orin Nano, conduct user acceptance studies with elderly participants, and develop installation/maintenance procedures.

**Detailed Answer** (1 minute):
Our research roadmap includes several phases before production deployment. Immediate next steps: validate fall detection accuracy on MCF, LE2I, UP-Fall benchmark datasets to establish performance baselines; deploy the integrated pipeline on actual Jetson Orin Nano hardware to confirm real-time multi-camera processing; collect custom CamTech dataset with 180 videos using age-appropriate actors for elderly-specific validation.

Following technical validation, we require user acceptance studies with elderly participants and family caregivers—semi-structured interviews, usability testing, longitudinal monitoring of acceptance over time. Privacy concerns, installation preferences, alert mechanisms, and caregiver response protocols need empirical investigation.

Practical deployment challenges include: installation procedures requiring camera positioning optimization, network configuration, caregiver training on alert responses, maintenance protocols for firmware updates, and customer support infrastructure.

Realistically, pilot deployments in 10-20 Cambodian households could occur within 12-18 months following successful benchmark validation. Commercial availability requires additional regulatory approval, manufacturing partnerships, and distribution channels—likely 2-3 years.

**Supporting Evidence**:
- Immediate: Benchmark validation, Jetson testing, custom dataset
- Mid-term: User acceptance studies, pilot deployments
- Long-term: Regulatory approval, commercial production
- Timeline estimate: Pilots 12-18 months, commercial 2-3 years

**Paper Reference**: Section 5.4 (Future Directions), Section 5.3 (Limitations - deployment not validated)

---

### Q20: How would installation work? Can families install this themselves or does it require professionals?

**Short Answer** (20 seconds):
Professional installation recommended. Camera positioning requires optimizing 360-degree coverage, mounting at appropriate heights, configuring network connectivity, and calibrating the Jetson device. Similar complexity to home security camera installation—doable for technically skilled users, but professional installation ensures optimal performance.

**Detailed Answer** (45 seconds):
Installation involves several technical steps: mounting four cameras at 90-degree spacing, typically 2.5-3 meters height for optimal coverage; running Ethernet cables to the central Jetson device for wired connectivity (preferred for reliability); configuring network settings and RTSP streaming; calibrating pose estimation parameters for each camera's field of view; testing coverage for blind spots.

Professional installers with security camera experience can complete installation in 2-3 hours. Technically proficient families could self-install following detailed guides, but camera positioning significantly impacts detection performance—poor placement creates coverage gaps.

The cost model includes installation as part of the $170 accessories/services budget. Subsidized professional installation through partnerships with local security companies or NGOs could support wider adoption.

**Supporting Evidence**:
- Technical requirements: 90-degree spacing, 2.5-3m height, network config
- Complexity: Similar to security camera installation
- Professional recommended for optimal performance
- Installation cost included in $170 accessories budget

**Paper Reference**: Section 3.1.2 (Hardware Design - camera configuration), Cost analysis A4.2

---

## General Strategy Notes

### Handling Questions Outside Scope

**If asked about topics not covered in the paper**:
- Acknowledge the question's relevance
- Explain why it's beyond current scope
- Suggest how future research could address it
- Offer related information you CAN discuss

**Example**: "That's an excellent question about [topic]. Our current study focused on [validated scope], so I don't have empirical data on [topic] yet. However, I can discuss how [related validated topic] might inform future work in that direction..."

### Redirecting to Paper

**For detailed technical questions**:
"The full methodology is detailed in Section [X] of the paper, but briefly..." [give short answer]

**For specific numbers/statistics**:
"The exact figures are in [Table/Figure X], showing..." [cite key number]

### Acknowledging Uncertainty

**When you don't know**:
"That's a great question I hadn't considered in depth. Based on [related evidence], I'd hypothesize [informed speculation], but rigorous investigation would require [specific validation approach]."

**Never fabricate data or claims not in the paper.**

---

## Time Management for 10-Minute Q&A

- **Average 3-4 questions** (2-3 minutes each including question)
- **Short answers**: 15-30 seconds (for straightforward questions)
- **Detailed answers**: 45-90 seconds (for complex questions)
- **Know when to cut yourself off**: "I could discuss this in more detail afterward if you're interested, but let me take other questions..."

---

**END OF Q&A PREPARATION GUIDE**
