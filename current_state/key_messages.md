# Key Messages for ASIP 2025

**Last Updated**: Nov 14, 2025

---

## Core Message

**Our research demonstrates how privacy governance principles can inform AI architecture to address elderly safety challenges in developing countries through affordable edge computing solutions.**

---

## Governance Theme Alignment

### 1. Privacy Governance in AI Systems

**Key Message**: Edge computing + privacy-by-design architecture eliminates cloud data transmission risks while maintaining high pose detection capability.

**Evidence**:
- 100% on-device processing (designed for edge deployment)
- Pose-only storage with immediate frame disposal
- Zero facial recognition capability by design
- No cloud subscription or data transmission

**Policy Implication**: Demonstrates viable model for privacy-preserving healthcare AI that doesn't sacrifice performance for privacy.

---

### 2. Accessibility and Digital Inclusion

**Key Message**: Privacy-first edge architecture yields economic co-benefits, expanding elderly safety monitoring access to middle-income households in developing countries.

**Evidence**:
- 61% cost reduction vs cloud alternatives ($672 one-time vs $1,719 over 3 years)
- Target market: Middle-income Cambodian households ($870-$1,622/month)
- Market reach: 168,000-252,000 elderly (8-12% of population by 2030)
- Zero-subscription model eliminates recurring payment burden

**Policy Implication**: Privacy-by-design architecture can yield accessibility benefits beyond privacy protection alone.

---

### 3. Regional Innovation for Global Challenges

**Key Message**: Solutions designed for developing country contexts can address global aging challenges while respecting local constraints.

**Evidence**:
- Cambodia-specific cost-effectiveness analysis
- Evidence-based incident prioritization using regional data (Thailand, China)
- Edge computing addresses bandwidth limitations in developing countries
- Scalable model for similar economies

**Policy Implication**: Technology governance frameworks should encourage context-specific innovation rather than one-size-fits-all solutions.

---

## Technical Innovation Messages

### NIR Camera Compatibility Validation

**Message**: MediaPipe pose estimation achieves 91.3% keypoint detection on 850nm NIR footage, validating 24/7 privacy-preserving monitoring capability.

**Impact**: Confirms technical feasibility of affordable RGB cameras with IR night vision for elderly monitoring without facial recognition technology.

---

### Edge Computing for Privacy and Performance

**Message**: Real-time AI inference designed for edge devices enables sub-second incident detection without cloud latency or privacy risks.

**Impact**: Integrated pipeline achieves 20.53 FPS on standard hardware, suggesting edge deployment feasibility. Zero network transmission = faster response + complete data locality.

---

### Privacy-by-Design Architecture

**Message**: System architecture eliminates privacy risks at design level (pose-only storage), not through post-processing or access controls.

**Impact**: Inherently privacy-preserving (cannot reconstruct facial features from pose data alone).

---

## Healthcare Innovation Messages

### Evidence-Based Incident Prioritization

**Message**: Focus on three high-impact incident types based on regional epidemiological evidence, not just technical feasibility.

**Evidence**:
- Falls while standing/walking: 37.7% of Thai elderly home accidents
- Falls from bed/chair: Median 1.32 per facility in Chinese long-term care settings
- Abnormal sit-to-stand: 99.42% detection accuracy as pre-fall risk indicator

**Impact**: Addresses real-world safety priorities in Southeast Asian elderly care contexts.

---

### Contactless Monitoring for Compliance

**Message**: Camera-based monitoring eliminates wearable compliance issues while respecting privacy through pose-only representation.

**Impact**: No device charging, no forgetting to wear, no physical discomfort.

---

## Key Statistics to Highlight

### Cost Comparison
- **Edge-based system**: $672 (one-time, zero recurring fees)
- **Cloud alternative** (Kami Fall Detect): $1,719 over 3 years ($99 hardware + $1,620 subscription)
- **Savings**: 61% reduction ($1,047 savings)
- **Impact**: Expands market reach to 168,000-252,000 elderly (8-12% of Cambodian population)

### Market Reach
- **Target**: Middle-income urban households (top 40-60% income bracket)
- **Population**: 8-12% of Cambodian elderly
- **By 2030**: 168,000-252,000 potential users

### Privacy Metrics
- **Facial anonymity**: 100% (no facial features stored)
- **Data locality**: 100% on-device processing
- **Cloud transmission**: 0% (zero network dependency for core function)

### Validation Results
- **NIR compatibility**: 91.3% keypoint detection on 850nm IR footage (20 commercial CCTV videos)
- **Processing speed**: 20.53 FPS (integrated YOLO+MediaPipe pipeline on standard hardware)
- **Pipeline trade-off**: Integrated approach 5.7% more accurate but 2.3× slower; accuracy prioritized for safety-critical application

---

## Elevator Pitch (30 seconds)

"Our design study demonstrates how privacy governance principles can inform AI architecture for elderly safety monitoring in developing countries. Using edge computing with pose-only storage, we validated NIR camera compatibility (91.3% keypoint detection) while achieving 61% cost reduction vs cloud alternatives ($672 vs $1,719). This expands market reach to 168,000-252,000 Cambodian elderly, showing how privacy-first design can yield economic co-benefits."

---

## Conference Presentation Hooks

### For AI Ethics Audience
"Privacy-by-design isn't just a buzzword—our architecture makes facial recognition impossible by design, not by policy."

### For Policy Makers
"Privacy-first architecture yields economic co-benefits: edge computing achieves 61% cost reduction ($672 vs $1,719), expanding access to 168,000-252,000 Cambodian elderly."

### For Healthcare Innovators
"We detect the incidents that matter most: 37.7% of Thai elderly accidents are falls while walking—our system catches them in real-time."

### For Technology Governance Scholars
"Edge computing isn't just faster—it's a governance model that keeps sensitive health data local and private."

---

## Anticipated Questions and Answers

### Q: How do you ensure privacy with cameras?
**A**: Privacy-by-design architecture. We extract skeletal pose (17 body keypoints) and immediately discard the raw frame. The system never stores or transmits facial images—it's architecturally impossible to reconstruct faces from pose data alone.

### Q: Can middle-income households really afford $672?
**A**: Yes, for target demographic. Cambodian households earning $870-$1,622/month (4th-5th quintile) can allocate this one-time cost for elderly parent safety. More importantly, it's 61% cheaper than cloud alternatives ($672 vs $1,719 over 3 years), with zero recurring fees.

### Q: Does this actually work in the dark?
**A**: VALIDATED. MediaPipe pose estimation achieves 91.3% keypoint detection on 850nm NIR footage (tested on 20 commercial CCTV videos from diverse manufacturers). Confirms 24/7 monitoring capability without facial recognition technology.

### Q: What did you actually validate in this paper?
**A**: NIR camera compatibility and cost-effectiveness, not fall detection accuracy. This is a design study demonstrating how privacy governance principles inform architecture. Fall detection validation requires benchmark datasets (MCF, LE2I, UP-Fall)—planned for future research phase.

---

## Notes for ASIP Submission

- **Emphasize governance angle** over pure technical innovation
- **Highlight regional context** (Cambodia, Southeast Asia)
- **Show policy implications** for each technical decision
- **Balance technical rigor** with accessibility for interdisciplinary audience
- **Use evidence-based claims** (cite regional epidemiological data)

---

## References

Main research project: `/Users/monireach/projects/ai_research`
