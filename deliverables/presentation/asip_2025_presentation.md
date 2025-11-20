# Privacy Governance-Driven Design of AI-Powered Elderly Safety Monitoring for Cambodia

**ASIP 2025 Conference Presentation**
December 4-5, 2025
Cambodia University of Technology and Science (CamTech)

**Presenter**: [Your Name]
**Institution**: CamTech

---

## SLIDE 1: Title Slide

### Content

# Privacy Governance-Driven Design of AI-Powered Elderly Safety Monitoring for Cambodia

**[Your Name]**
Cambodia University of Technology and Science (CamTech)

Asian Studies on Innovation and Policy (ASIP) 2025
Theme: "Governance of Emerging Intelligent Technologies"
December 4-5, 2025

### Speaker Notes

Welcome to ASIP 2025. Today I'll present our design study on privacy governance-driven AI architecture for elderly safety monitoring in Cambodia. This research demonstrates how privacy governance principles can inform architectural decisions from the outset, rather than being retrofitted after deployment. The work aligns with this conference's theme of governing emerging intelligent technologies by examining the intersection of privacy governance, edge computing, and accessibility in resource-constrained healthcare contexts.

**Transition**: Let me start by framing the challenge we're addressing.

---

## SLIDE 2: The Challenge - Elderly Safety Dilemma

### Content

## The Challenge: Elderly Safety Dilemma

**Global Aging Crisis**

- Southeast Asia: 12.2% elderly (2024) → 22.9% by 2050
- Falls: 684,000 annual deaths globally, 60% in Western Pacific/Southeast Asia
- Cambodia: 1.8M elderly by 2030

**Current Solutions Fall Short**

| Solution Type | Privacy                                     | Compliance                      | Cost                                   |
| ------------- | ------------------------------------------- | ------------------------------- | -------------------------------------- |
| Cloud Cameras | ❌ Video transmitted to third-party servers | ✓ No wearables                  | ❌ $1,719 over 3 years (subscriptions) |
| Wearables     | ✓ No cameras                                | ❌ Charging, forgetting to wear | ✓ Affordable                           |

**The Gap**: Middle-income households ($870-$1,622/month) need affordable, privacy-preserving solutions

<!-- VISUAL: Simple comparison table showing trade-offs -->

### Speaker Notes

Southeast Asia faces a rapidly aging population—from 12.2% elderly in 2024 to nearly 23% by 2050 according to WHO SEARO data. Falls are the leading cause of injury-related deaths among elderly, with 684,000 annual fatalities globally, and 60% concentrated in the Western Pacific and Southeast Asia regions. In Cambodia specifically, we're projecting 1.8 million elderly by 2030.

Current monitoring solutions force families to choose between privacy and effectiveness. Cloud-based cameras transmit video to third-party servers, creating facial recognition and re-identification risks. The Kami Fall Detect Camera, for example, requires continuous cloud connectivity and costs $1,719 over three years due to mandatory subscriptions. Wearables offer better privacy but face compliance challenges—elderly users must remember to wear devices consistently and maintain charging, which is particularly difficult at nighttime.

Our target demographic—middle-income Cambodian households earning $870 to $1,622 per month—cannot afford cloud subscriptions that represent 5.2% of monthly income, yet they need reliable safety monitoring for aging parents living at home.

**Transition**: This brings us to our research question.

---

## SLIDE 3: Research Question

### Content

## Research Question

**How can privacy governance principles inform the architectural design of AI-based elderly monitoring systems in resource-constrained contexts?**

**Research Type**: Design study with technical validation

- **NOT**: Complete fall detection system evaluation
- **IS**: Demonstration of governance-driven architecture through feasibility validation

**Three Propositions**

1. Privacy governance requirements can be translated into specific architectural decisions
2. Privacy-first design can yield co-benefits in cost-effectiveness and accessibility
3. Edge-based pose estimation provides sufficient monitoring capability while eliminating cloud privacy risks

<!-- VISUAL: Research question as main headline, propositions as supporting bullets -->

### Speaker Notes

Our research question asks how privacy governance principles can inform architectural design in resource-constrained contexts. It's important to clarify the scope: this is a design study, not a complete fall detection system evaluation. We're demonstrating how governance principles drive architectural decisions through technical feasibility validation.

We explore three propositions. First, privacy governance requirements can be translated into concrete architectural decisions—edge computing, pose-only storage, immediate frame disposal. Second, privacy-first design can yield co-benefits beyond privacy alone, particularly in cost-effectiveness and accessibility for developing countries. Third, edge-based pose estimation provides sufficient monitoring capability while eliminating cloud privacy risks.

These are propositions for conceptual exploration, not empirical hypotheses requiring statistical validation. The empirical component validates technical feasibility through NIR camera compatibility testing and cost-effectiveness analysis, which I'll present in the results section.

**Transition**: Let me show you how we translate privacy governance principles into architecture.

---

## SLIDE 4: Privacy Governance Architecture

### Content

## Privacy Governance Architecture

**Three Design Principles → Architectural Mechanisms**

**1. Edge-First Processing**

- 100% on-device computation (NVIDIA Jetson Orin Nano 8GB)
- Zero cloud transmission, zero network exposure
- Data sovereignty: data never leaves household

**2. Pose-Only Storage**

- Extract 17 body keypoints (COCO format)
- Face landmarks explicitly excluded
- Architecturally impossible to reconstruct facial features

**3. Immediate Frame Disposal**

- Raw video frames processed in real-time
- Deleted immediately after keypoint extraction
- No video retention = no re-identification risk

**Key Message**: Privacy by design, not by policy

<!-- VISUAL: System architecture diagram showing camera → edge processor → pose storage, with "no cloud" crossed out -->

### Speaker Notes

Privacy governance drives our architecture through three mechanisms. First, edge-first processing: all computation occurs on a local NVIDIA Jetson Orin Nano device with 100% on-device processing. Zero cloud transmission eliminates network exposure and ensures data sovereignty—sensitive health data never leaves the household.

Second, pose-only storage: we extract only 17 body keypoints in COCO format from each frame, explicitly excluding face landmarks. This makes facial recognition architecturally impossible, not merely prohibited by policy. You cannot reconstruct facial features from skeletal pose data alone—the information simply doesn't exist in our stored data.

Third, immediate frame disposal: raw video frames are processed in real-time and deleted immediately after keypoint extraction. We retain no video footage, eliminating re-identification risks entirely.

This reflects Cavoukian's Privacy by Design framework—embedding privacy into architecture from inception. The difference is we're implementing this proactively during design, not retrofitting privacy controls after deployment. The architecture enforces privacy through technical constraints, not operational promises.

**Transition**: Let me briefly outline the technical implementation.

---

## SLIDE 5: Technical Approach Overview

### Content

## Technical Approach Overview

**Hardware Configuration**

- **Cameras**: 4× RGB with 850nm IR night vision (Hikvision DS-2CD1343G2-IUF)
  - 90° spacing for 360° coverage
  - 24/7 monitoring capability (IR for complete darkness)
- **Edge Processor**: NVIDIA Jetson Orin Nano 8GB
- **Total System Cost**: $672 (one-time, zero recurring fees)

**Software Pipeline**

1. **Person Detection**: YOLOv8n (Nano - lightweight) identifies bounding box
2. **Pose Estimation**: MediaPipe extracts 33 skeletal landmarks → 17 body keypoints stored
3. **Privacy Layer**: Face landmarks excluded, frames immediately deleted

**Three Incident Types** (evidence-based prioritization)

- Falls while standing/walking (37.7% of Thai elderly home accidents)
- Falls from bed/chair (median 1.32 per facility in Chinese long-term care)
- Abnormal sit-to-stand transitions (99.42% detection accuracy as pre-fall risk indicator)

<!-- VISUAL: Simple pipeline diagram: Camera → YOLOv8n → MediaPipe → Pose Storage -->

### Speaker Notes

Our technical implementation uses four RGB cameras with 850nm infrared night vision, positioned at 90-degree spacing for 360-degree coverage. The Hikvision cameras provide 24/7 monitoring capability, including complete darkness through IR mode. Processing occurs on an NVIDIA Jetson Orin Nano edge device. Total system cost is $672—a one-time investment with zero recurring fees.

The software pipeline integrates YOLOv8n for lightweight person detection, MediaPipe for pose estimation extracting 33 skeletal landmarks, and our privacy layer that retains only 17 body keypoints while excluding face landmarks and immediately deleting frames.

We prioritize three incident types based on regional epidemiological evidence: falls while standing or walking account for 37.7% of Thai elderly home accidents according to Maiyapakdee et al. Falls from bed or chair show a median of 1.32 incidents per facility in Chinese long-term care settings from Li and Shi's research. Abnormal sit-to-stand transitions serve as pre-fall risk indicators with 99.42% detection accuracy in the literature.

This is a high-level overview—I'm happy to discuss technical details during Q&A.

**Transition**: Now, what exactly did we validate in this study?

---

## SLIDE 6: Validation Scope - What We Actually Tested

### Content

## Validation Scope: What We Actually Tested

### ✅ What We VALIDATED

1. **NIR Camera Compatibility**: Can MediaPipe detect poses on 850nm IR footage?
   - 20 commercial CCTV videos, diverse manufacturers and environments
2. **Cost-Effectiveness**: Is edge architecture cheaper than cloud alternatives?
   - 3-year total cost comparison
3. **Privacy Architecture**: Does design eliminate facial data collection?
   - Architectural analysis of pose-only storage

### ❌ What We DID NOT Validate

1. **Fall Detection Accuracy**: Requires benchmark datasets (MCF, LE2I, UP-Fall) - future work
2. **Real-World Deployment**: Hardware installation in actual elderly homes - not done yet
3. **User Acceptance**: Longitudinal studies with elderly and caregivers - planned research phase

**Why These Limitations**: Design study demonstrating governance-driven architecture, not complete system validation

<!-- VISUAL: Two columns with checkmarks and X marks for clarity -->

### Speaker Notes

Academic rigor requires clarity about validation scope. We validated three components: first, NIR camera compatibility—testing whether MediaPipe pose estimation works on 850nm infrared footage from affordable security cameras. We analyzed 20 commercial CCTV videos from diverse manufacturers and environments. Second, cost-effectiveness—comparing our edge-based system's three-year total cost against cloud alternatives. Third, privacy architecture—analyzing whether our design eliminates facial data collection through pose-only storage.

Critically, we did NOT validate fall detection accuracy, which requires testing on benchmark datasets like MCF, LE2I, and UP-Fall. We have not conducted real-world deployment in actual elderly homes or longitudinal user acceptance studies with elderly participants and caregivers.

These limitations are intentional. This is a design study demonstrating how privacy governance principles inform architectural decisions through feasibility validation, not a complete fall detection system evaluation. The goal is to show that privacy-first edge architecture is technically and economically viable, establishing the foundation for future empirical work on detection accuracy and user acceptance.

**Transition**: With that scope clarified, let me present our validation results.

---

## SLIDE 7: Results - NIR Camera Compatibility

### Content

## Results: NIR Camera Compatibility

**MediaPipe Pose Estimation on 850nm IR Footage**

### Validation Dataset

- **20 commercial CCTV videos** (publicly available demo footage)
- **Diversity**: Indoor/outdoor, Hikvision/EZviz/dome/turret/bullet cameras
- **Resolutions**: 1080p and 4K
- **Purpose**: Validate performance on target camera wavelength (850nm NIR)

### Performance Metrics (Integrated Pipeline)

| Metric                  | Result                              |
| ----------------------- | ----------------------------------- |
| Keypoint Detection Rate | **91.3%** (30.1 of 33 landmarks)    |
| Average Confidence      | 0.868                               |
| False Negative Rate     | 12.3% (person present, pose failed) |
| Processing Speed        | 20.53 FPS                           |

**Key Finding**: Confirms 24/7 monitoring feasibility without facial recognition technology

<!-- VISUAL: Table with metrics, possibly a sample frame showing keypoint detection on IR footage -->

### Speaker Notes

We validated MediaPipe pose estimation on 20 commercial 850nm infrared security camera videos, sourced from publicly available CCTV demo footage. The dataset included diverse environments—indoor and outdoor scenes—and multiple camera manufacturers including Hikvision, EZviz, dome, turret, and bullet camera types, at both 1080p and 4K resolutions. This diversity ensures our validation reflects real-world deployment scenarios across different hardware and lighting conditions.

Our integrated pipeline combining YOLOv8n person detection with MediaPipe pose estimation achieved 91.3% keypoint detection rate, detecting an average of 30.1 out of 33 landmarks per frame. Average confidence scored 0.868, indicating high-quality pose estimates. False negative rate—frames where a person is present but pose detection fails—was 12.3%. Processing speed reached 20.53 frames per second on standard hardware.

The critical finding is that MediaPipe, trained on visible spectrum RGB images, successfully generalizes to 850nm near-infrared wavelengths. This validates the technical feasibility of 24/7 elderly monitoring without requiring facial recognition technology—we can detect body pose in complete darkness while maintaining privacy by design. Limited prior research has empirically validated pose estimation performance on NIR wavelengths used in affordable security cameras for elderly monitoring applications.

**Transition**: Now let me show you the cost-effectiveness analysis.

---

## SLIDE 8: Results - Cost-Effectiveness Analysis

### Content

## Results: Cost-Effectiveness Analysis

### 3-Year Total Cost Comparison

| Component           | Edge-Based System                        | Cloud Alternative (Kami)         |
| ------------------- | ---------------------------------------- | -------------------------------- |
| Hardware            | $672 (4× cameras + Jetson + accessories) | $99                              |
| Subscription        | $0                                       | $45/month × 36 = $1,620          |
| **Total (3 years)** | **$672**                                 | **$1,719**                       |
| **Savings**         | —                                        | **61% reduction** ($1,047 saved) |
| **Breakeven**       | —                                        | **Month 13 (Year 2)**            |

### Market Accessibility Impact

**Target Market**: Middle-income urban Cambodian households

- 4th-5th income quintile: $870-$1,622/month
- **Estimated Reach**: 12-18% of elderly population
- **Potential Users by 2030**: 252,000-378,000 individuals

**Key Advantage**: Zero-subscription model eliminates ongoing payment burden

<!-- VISUAL: Bar chart comparing 3-year costs; pie chart showing market reach percentage -->

### Speaker Notes

Our cost-effectiveness analysis compares the edge-based system against a cloud-based elderly fall detection alternative—the Kami Fall Detect Camera, which represents current market offerings. The edge system costs $672 as a one-time investment: $252 for four cameras, $250 for the Jetson Orin Nano processor, and $170 for accessories including storage, UPS, cables, and mounting hardware. Zero recurring fees.

The cloud alternative costs $99 for hardware but requires a mandatory subscription of $45 per month. Over three years, this totals $1,719—$99 hardware plus $1,620 in subscription fees. Our edge architecture achieves 61% cost reduction, saving $1,047 over three years. The breakeven point occurs at month 13 of year two.

Market accessibility analysis shows the edge-based system targets middle-income urban Cambodian households in the fourth and fifth income quintiles, earning $870 to $1,622 per month according to Cambodia's Socio-Economic Survey data. We estimate reaching 12 to 18% of the elderly population—252,000 to 378,000 individuals by 2030.

The zero-subscription model is critical here. For middle-income households, eliminating ongoing payment burden expands affordability compared to recurring-fee alternatives where subscription costs represent 5.2% of monthly income indefinitely.

**Transition**: Let me explain a key design trade-off we encountered.

---

## SLIDE 9: Design Trade-offs - Safety-Critical Priority

### Content

## Design Trade-offs: Safety-Critical Priority

**Pipeline Comparison: Baseline vs Integrated**

Tested two approaches on same 20 NIR videos:

- **Baseline**: MediaPipe on full frame
- **Integrated**: YOLOv8n person detection → ROI crop → MediaPipe on ROI

### Performance Trade-off

| Metric             | Baseline  | Integrated | Difference         |
| ------------------ | --------- | ---------- | ------------------ |
| Keypoint Detection | 86.1%     | 91.3%      | **+5.7%** ✓        |
| Pose Coverage      | 79.5%     | 96.9%      | **+22.2%** ✓       |
| Processing Speed   | 47.37 FPS | 20.53 FPS  | **2.3× slower** ❌ |

### Decision: Integrated Pipeline Selected

**Rationale**: Prioritize accuracy for safety-critical application

- Missing fall detection has fatal consequences
- Both configurations exceed real-time requirements (20.53 FPS vs 15 FPS target)
- 5.7% accuracy gain + 22.2% better coverage justified 2.3× slower speed

<!-- VISUAL: Comparison table with color coding for trade-offs -->

### Speaker Notes

We compared two pipeline architectures on the same 20 infrared videos. The baseline approach applies MediaPipe pose estimation directly to full frames. The integrated approach adds YOLOv8n person detection first, crops the region of interest, then applies MediaPipe to the cropped ROI.

The integrated pipeline achieved 5.7% higher keypoint detection—91.3% versus 86.1%—and 22.2% better pose coverage at 96.9% versus 79.5%. However, it was 2.3 times slower, processing 20.53 frames per second compared to the baseline's 47.37 FPS.

We selected the integrated pipeline despite the speed penalty based on safety-critical priority. In elderly monitoring, missing a fall detection can have fatal consequences—false negatives are far more dangerous than lower processing speed. Critically, both configurations exceed real-time requirements. Our target is 15 frames per second for real-time monitoring; even the slower integrated pipeline delivers 20.53 FPS.

This decision reflects a governance perspective on AI design: technical performance metrics must be evaluated against application context and consequences. Speed optimization is valuable, but not at the cost of accuracy in safety-critical healthcare applications where lives are at stake.

**Transition**: These technical results lead to broader governance implications.

---

## SLIDE 10: Governance Implications ⭐

### Content

## Governance Implications

### 1. Privacy Governance Through Edge Architecture

**Edge processing eliminates cloud risks by design, not by policy**

- Data sovereignty: 100% on-device, data never leaves household
- Facial anonymity: Architecturally impossible (pose-only storage, no facial data exists)
- Validation: 91.3% NIR detection confirms privacy-first design maintains technical performance

### 2. Accessibility Governance Through Cost Optimization

**Privacy-first design yields economic co-benefits**

- Edge architecture eliminates cloud infrastructure → 61% cost reduction ($672 vs $1,719)
- Zero-subscription model expands market reach: 252,000-378,000 Cambodian elderly (12-18%)
- Privacy governance enables accessibility governance

### 3. Context-Specific Design for Developing Countries

**Regional evidence informs governance-driven architecture**

- Incident priorities based on Thai (37.7% falls) and Chinese long-term care data
- Hardware selection addresses Cambodia's middle-income market constraints
- Scalable model for similar resource-constrained contexts

<!-- VISUAL: Three pillars diagram showing interconnected governance dimensions -->

### Speaker Notes

This slide presents the core governance contributions of our research.

First, privacy governance through edge architecture. Edge-based processing eliminates cloud transmission risks through system constraints, not operational promises. Data sovereignty is enforced architecturally—data physically cannot leave the household. Facial anonymity is guaranteed because pose-only storage makes facial recognition impossible, not merely prohibited. Our validation results—91.3% keypoint detection on infrared footage—demonstrate that privacy-first design maintains technical performance without compromise.

Second, accessibility governance through cost optimization. This is where privacy governance yields unexpected co-benefits. By eliminating cloud infrastructure requirements for privacy reasons, we achieve 61% cost reduction compared to cloud alternatives. The edge architecture costs $672 versus $1,719 for cloud-based systems over three years. The zero-subscription model expands market reach to 252,000 to 378,000 Cambodian elderly in middle-income households—12 to 18% of the elderly population. Privacy governance enables accessibility governance.

Third, context-specific design for developing countries. Our architectural decisions incorporate regional epidemiological evidence—incident type prioritization based on Thai elderly fall data showing 37.7% prevalence and Chinese long-term care studies. Hardware selection addresses Cambodia's middle-income market constraints while maintaining technical requirements. This demonstrates a governance-driven design approach scalable to similar resource-constrained contexts.

**Transition**: Let me ground this in the Cambodia case study.

---

## SLIDE 11: Regional Impact - Cambodia Case Study

### Content

## Regional Impact: Cambodia Case Study

### Evidence-Based Incident Selection

**Why these three incident types?**

- Falls while standing/walking: **37.7%** of Thai elderly home accidents (Maiyapakdee et al., 2025)
- Falls from bed/chair: Median **1.32 per facility** in Chinese nursing homes (Li & Shi, 2022)
- Abnormal sit-to-stand: **99.42%** detection accuracy as pre-fall indicator (literature)

**Not arbitrary**: Prioritized based on regional epidemiological data, not Western datasets

### Middle-Income Market Targeting

**Cambodia Socio-Economic Survey Data** (National Institute of Statistics, 2019)

- **Target**: 4th-5th quintile ($870-$1,622/month household income)
- **Rationale**: Cloud subscription ($45/month) = 5.2% of monthly income indefinitely
- **Edge alternative**: $672 one-time = 0.5-0.8 months income, zero recurring fees

### Scalability for Developing Countries

Similar constraints in Southeast Asia, South Asia, Sub-Saharan Africa:

- Aging populations + middle-income market growth
- Privacy concerns + limited data protection enforcement
- Cost sensitivity + bandwidth limitations

<!-- VISUAL: Map highlighting Southeast Asia region; income distribution chart -->

### Speaker Notes

The Cambodia case study demonstrates context-specific design for developing countries. Our incident type selection is evidence-based, not arbitrary. Falls while standing or walking account for 37.7% of Thai elderly home accidents according to Maiyapakdee et al.'s 2025 research. Falls from bed or chair show a median of 1.32 incidents per facility in Chinese nursing homes per Li and Shi's 2022 study. Abnormal sit-to-stand transitions achieve 99.42% detection accuracy as pre-fall risk indicators in the literature.

We deliberately prioritize regional epidemiological data over Western datasets. Southeast Asian elderly populations have different fall patterns, living arrangements, and care norms compared to North American or European contexts. Strong family caregiving rooted in filial piety values creates preference for home-based care over institutional facilities, as documented by Romli et al.

Middle-income market targeting addresses Cambodia's specific economic context. We target the fourth and fifth income quintiles—households earning $870 to $1,622 per month according to Cambodia's Socio-Economic Survey. Cloud subscription fees of $45 monthly represent 5.2% of monthly income indefinitely, creating ongoing financial burden. Our edge alternative costs $672 one-time—equivalent to 0.5 to 0.8 months of household income with zero recurring fees.

This model scales to similar developing country contexts facing aging populations, middle-income market growth, privacy concerns with limited enforcement, cost sensitivity, and bandwidth limitations.

**Transition**: Let me address limitations and future directions.

---

## SLIDE 12: Limitations & Future Directions

### Content

## Limitations & Future Directions

### Study Limitations (Academic Rigor)

**What we validated**: NIR compatibility, cost-effectiveness, privacy architecture
**What we did NOT validate**: Fall detection accuracy, real-world deployment, user acceptance

**Specific Limitations**:

1. **Testing environment**: Commercial CCTV footage, not actual elderly subjects
   - Movement patterns, body proportions, gait may differ for elderly individuals
2. **Hardware deployment**: 20.53 FPS measured on standard hardware, not target Jetson Orin Nano
   - Real-world performance requires edge device validation
3. **Market accessibility**: $672 system targets middle-income urban households
   - Low-income and rural elderly require subsidies or alternative deployment models

### Future Research Directions

**Immediate Next Steps**:

- Benchmark dataset validation (MCF, LE2I, UP-Fall) for fall detection accuracy
- Jetson Orin Nano hardware deployment and performance validation
- Custom CamTech dataset collection (180 videos: 3 incident types × 3 lighting conditions)

**Long-term Research**:

- User acceptance studies with elderly participants and caregivers
- Policy framework development for healthcare AI governance in developing countries
- Expanded incident detection based on local epidemiological data

<!-- VISUAL: Timeline showing current stage and future milestones -->

### Speaker Notes

Academic rigor requires honest acknowledgment of limitations. We validated NIR camera compatibility, cost-effectiveness, and privacy architecture design—but not fall detection accuracy, real-world deployment performance, or user acceptance.

Three specific limitations merit attention. First, testing environment: we validated MediaPipe pose estimation on commercial CCTV footage, not actual elderly subjects. Movement patterns, body proportions, and gait characteristics of elderly individuals may differ from the commercial video subjects in our dataset. Second, hardware deployment: our 20.53 frames per second processing speed was measured on standard hardware, not the target NVIDIA Jetson Orin Nano edge device. Real-world deployment performance requires hardware-specific validation. Third, market accessibility: the $672 system targets middle-income urban households in the fourth and fifth income quintiles. Low-income and rural elderly populations require subsidies or alternative deployment models to achieve accessibility.

Future research directions include immediate next steps: validating fall detection accuracy on benchmark datasets like MCF, LE2I, and UP-Fall; deploying the full pipeline on Jetson Orin Nano hardware; and collecting a custom CamTech dataset with 180 videos covering three incident types across three lighting conditions.

Long-term research includes user acceptance studies with elderly participants and caregivers, policy framework development for healthcare AI governance in developing countries, and expanded incident detection based on local epidemiological data.

**Transition**: Let me conclude with key takeaways.

---

## SLIDE 13: Conclusion - Key Takeaways

### Content

## Conclusion: Key Takeaways

### Main Findings

1. **Privacy governance principles can drive architectural design from inception**

   - Edge processing + pose-only storage + immediate frame disposal
   - Privacy by design, not by policy

2. **Edge-first architecture achieves technical and economic feasibility**

   - 91.3% keypoint detection on 850nm NIR footage (24/7 monitoring capability)
   - 61% cost reduction over cloud alternatives ($672 vs $1,719)

3. **Privacy-by-design can yield economic co-benefits**

   - Edge architecture eliminates cloud costs → expands accessibility
   - Market reach: 252,000-378,000 Cambodian elderly (12-18% of population)

4. **Context-specific design for developing countries is essential**
   - Regional epidemiological evidence informs incident priorities
   - Economic constraints shape architecture decisions
   - Scalable governance model for resource-constrained contexts

### Implications

**For researchers**: Validate NIR compatibility empirically before deployment; pose estimation performance varies by camera type

**For policymakers**: Privacy-first architecture expands healthcare technology accessibility in middle-income markets

**For practitioners**: Zero-subscription models reduce ongoing cost barriers in developing countries

---

**Contact**: [Your Email]
**Paper**: Available upon acceptance

<!-- VISUAL: Clean summary layout with numbered takeaways -->

### Speaker Notes

Let me conclude with four key takeaways.

First, privacy governance principles can drive architectural design from inception, not as afterthoughts. Our edge processing combined with pose-only storage and immediate frame disposal demonstrates privacy by design, not by policy. The architecture enforces privacy through technical constraints.

Second, edge-first architecture achieves both technical and economic feasibility. We validated 91.3% keypoint detection on 850nm infrared footage, confirming 24/7 monitoring capability without facial recognition technology. We demonstrated 61% cost reduction compared to cloud alternatives—$672 versus $1,719 over three years.

Third, privacy-by-design can yield economic co-benefits beyond privacy protection alone. Edge architecture eliminates cloud infrastructure costs, which expands accessibility to 252,000 to 378,000 Cambodian elderly representing 12 to 18% of the elderly population.

Fourth, context-specific design for developing countries is essential. Regional epidemiological evidence from Thailand and China informed our incident priorities. Economic constraints in Cambodia's middle-income market shaped our hardware selection and cost optimization. This provides a scalable governance model for similar resource-constrained contexts across developing countries.

These findings have implications for multiple stakeholders. Researchers should validate NIR camera compatibility empirically before deployment, as pose estimation performance varies significantly by camera type—we observed a range from 73.8% to 98.9% across individual videos. Policymakers should recognize that privacy-first architecture can expand healthcare technology accessibility in middle-income markets through cost reduction co-benefits. Practitioners implementing elderly care systems should consider zero-subscription models to reduce ongoing cost barriers in developing countries.

Thank you for your attention. I'm happy to take questions.

---

## SLIDE 14: Questions & Discussion

### Content

# Questions & Discussion

**Thank you for your attention**

---

**Time for Q&A**

**Contact Information**:

- Email: [Your Email]
- Institution: Cambodia University of Technology and Science (CamTech)
- Research Project: [Link if applicable]

### Speaker Notes

I'm ready for questions. Based on the presentation, likely areas of interest include:

**Anticipated Questions**:

1. **Privacy**: "How do you ensure privacy with cameras?" → Privacy-by-design architecture explanation
2. **Affordability**: "Can middle-income households really afford $672?" → Context of monthly income and one-time vs subscription comparison
3. **NIR performance**: "Does this actually work in the dark?" → 91.3% keypoint detection validation on 850nm IR footage
4. **Validation scope**: "What did you actually validate in this paper?" → NIR compatibility and cost-effectiveness, NOT fall detection accuracy
5. **Scalability**: "Can this work in other developing countries?" → Similar constraints across Southeast Asia, South Asia, Sub-Saharan Africa

**Reference to Paper Sections**: If detailed questions arise, refer back to:

- Methodology (Section 3) for validation procedures
- Results (Section 4) for detailed metrics
- Discussion (Section 5) for governance implications
- Limitations (Section 5.3) for honest scope acknowledgment

I'm prepared to discuss technical details, governance frameworks, regional epidemiological evidence, cost calculations, and future research directions as questions arise.

---

**END OF PRESENTATION**
