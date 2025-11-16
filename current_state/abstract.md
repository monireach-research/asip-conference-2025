# Abstract - FINAL VERSION

**Last Updated**: Nov 14, 2025 (Added post-submission corrections in Notes section)
**Status**: Version 3 submitted Oct 28, 2025 - Historical record preserved with correction annotations
**Word Count**: 204 words (single paragraph format)

---

## Title

**Privacy Governance-Driven Design of AI-Powered Elderly Safety Monitoring for Cambodia**

---

## Authors

1. **Monireach Tang** (Graduate Student)
   Cambodia University of Technology and Science (CamTech)
   monireach.tang@gmail.com

2. **His Excellency Dr. Seingheng Hul**
   General Department of Science, Technology and Innovation
   Ministry of Industry, Science, Technology and Innovation
   [Email: To be provided]

3. **Asst. Prof. Dr. May Thu** (Associate Dean of School of Graduate Studies)
   Cambodia University of Technology and Science (CamTech)
   may.thu@camtech.edu.kh

---

## Research Framework

### Research Question

**How can privacy governance principles inform the architectural design of AI-based elderly monitoring systems in resource-constrained contexts?**

### Research Propositions

**Proposition 1**: Privacy governance requirements can be translated into specific architectural decisions (edge computing, pose-only storage, immediate frame disposal)

**Proposition 2**: Privacy-first architectural choices can yield co-benefits in cost-effectiveness and accessibility for developing countries

**Proposition 3**: Edge-based processing with pose estimation provides sufficient monitoring capability while eliminating cloud privacy risks

### Note on Research Approach

This conceptual/design paper uses **propositions** (theoretical claims explored through design analysis and literature review) rather than **hypotheses** (empirical predictions requiring data collection and testing). Propositions guide the design framework development presented in this paper. Future empirical work will validate these propositions through benchmark testing and real-world deployment studies.

---

## Abstract Body (204 words, single paragraph)

Cambodia expects 14 to 20% of its population to be elderly by 2030. Alongside this significant increase, coupled with current healthcare challenges - physician shortages and geographic disparities (WHO SEARO, 2024), this developing country requires improvement in the healthcare support system, especially in access to safety monitoring. In surveillance monitoring technology, traditional cloud-based systems, not taking into account users' privacy and dignity, transmit sensitive video footage to remote servers, creating surveillance risks that administrators can easily access private activities of elderly individuals. Using design science research methodology, this paper proposes a privacy-driven architectural framework grounded in Privacy by Design principles (Cavoukian, 2010), demonstrating how privacy governance can inform technical design from the outset, thereby embedding privacy protection mechanisms into system architecture rather than retrofitting them afterward. To operationalize these principles, the proposed architecture comprises three RGB cameras with infrared night vision and an NVIDIA Jetson Orin Nano edge computing platform. Privacy protection is achieved through immediate conversion of video frames to skeletal coordinates, storing only pose data while permanently deleting original footage. To achieve this, the processing pipeline integrates YOLOv8n person detection, MediaPipe pose estimation, and a hybrid Convolutional Neural Network-Long Short-Term Memory-Transformer (CNN+LSTM+Transformer) architecture for temporal pattern analysis and incident classification. The proposed design is structured to achieve 100% on-device processing with zero cloud transmission of sensitive data. By leveraging edge computing at significantly reduced cost, this architecture demonstrates accessibility governance implications: preliminary cost analysis suggests potential system deployment at approximately $540 (one-time) compared to cloud alternatives at $1,350-$1,950 annually, potentially enabling access for an estimated 180,000 elderly in middle-income Cambodian urban households (representing the top 50% income bracket, calculated from Cambodia Socio-Economic Survey income data (CSES, 2021) and 2030 elderly population projections). This research demonstrates that privacy governance can drive technical architecture from inception rather than being incorporated later, potentially achieving privacy preservation while improving accessibility of advanced AI monitoring systems for developing country populations. This conceptual framework requires empirical validation through benchmark dataset testing and real-world deployment studies to verify detection accuracy, alert latency, and system reliability.

---

## Metadata

**Keywords**: Privacy governance, Edge computing, Elderly safety monitoring, Privacy-by-design, Developing countries, AI ethics, Healthcare AI, Accessibility governance

**Paper Type**: Technical paper (Note: May be better classified as Conceptual Paper if conference offers this option)

**Conference Sub-themes Targeted**:

- Primary: AI & Technology Applications
- Secondary: AI & Technology Ethics
- Tertiary: AI & Technology Governance

---

## Submission Details

**Deadline**: October 31, 2025
**Submission Email**: asip2025@camtech.edu.kh
**File Location**: `deliverables/abstract_submitted/asip_2025_abstract.tex`

---

## Notes

### Version 3 Changes (Oct 30, 2025)

**Supervisor Feedback Addressed**:

- Dr. Siengheng's 9 comments (c1-c9) all addressed
- Dr. May's "preliminary survey" comment addressed by repositioning as conceptual framework
- Changed from structured format to single paragraph (per Dr. Siengheng's preference)

**Key Revisions**:

1. Added Privacy by Design (Cavoukian, 2010) citation
2. Added design science research methodology statement
3. Changed language from "achieves" to "is structured to achieve" (conceptual tone)
4. Reframed hardware as "operationalizing principles" (governance implementation)
5. Expanded CNN+LSTM+Transformer to full names
6. Added CSES 2021 citation for 180,000 figure with calculation explanation
7. Reframed cost as "accessibility governance implications"
8. Final sentence emphasizes need for empirical validation

### Format Compliance

- Single paragraph format (no section labels) per supervisor preference
- Keywords and Paper type at bottom
- 204 words

### Content Strategy

- **Framing**: Conceptual/Design paper - proposed framework requiring validation
- **Governance focus**: Privacy governance drives technical architecture from inception
- **Methodology**: Design science research (clearly stated)
- **Cost-effectiveness**: Reframed as accessibility governance, not just pricing
- **Regional context**: Cambodia healthcare constraints with WHO SEARO (2024) citation
- **Research status**: Transparent about needing empirical validation

### Academic Rigor Improvements

- Specific framework citation (Cavoukian, 2010)
- Data source citation (CSES, 2021)
- Healthcare context citation (WHO SEARO, 2024)
- Transparent about derived calculations
- Clear distinction: proposed vs. validated system

### Post-Submission Updates (Nov 14, 2025)

**IMPORTANT**: The abstract above was submitted Oct 28, 2025 and is preserved as historical record. The following corrections reflect updated information discovered during paper writing (Nov 2025). A revised abstract will be included in the full paper submission.

**Hardware Correction**:

- **Submitted**: "three RGB cameras with infrared night vision"
- **Actual**: 4× RGB cameras with 850nm IR night vision (90° spacing for 360° coverage)
- **Impact**: Changed camera count from 3 to 4 for complete room coverage

**System Cost Correction**:

- **Submitted**: "$540 (one-time)"
- **Actual**: $672 total system cost ($252 cameras + $250 Jetson Orin Nano + $170 accessories)
- **Impact**: Cost increased by $132 due to 4th camera + refined component pricing

**Cloud Alternative Cost Correction**:

- **Submitted**: "$1,350-$1,950 annually"
- **Actual**: $1,719 over 3 years ($99 Kami Fall Detect Camera hardware + $1,620 subscription at $45/month × 36 months)
- **Impact**: More precise comparison shows 61% cost reduction ($672 vs $1,719 over 3-year period)

**Market Reach Correction**:

- **Submitted**: "180,000 elderly"
- **Actual**: 252,000-378,000 elderly (12-18% of Cambodian elderly population by 2030)
- **Impact**: Market reach expanded due to refined cost-effectiveness analysis

**Income Bracket Clarification**:

- **Submitted**: "top 50% income bracket"
- **Actual**: 4th-5th quintile (middle-income urban households earning $870-$1,622/month)
- **Impact**: More precise demographic targeting (12-18% of elderly population, not 50%)

**Paper Classification Refinement**:

- **Submitted**: "proposes a privacy-driven architectural framework"
- **Actual**: Design study demonstrating how privacy governance principles inform architectural decisions
- **Impact**: Clearer research positioning - not proposing general framework, but demonstrating governance-driven design approach through Cambodia case study

**Validation Completed (Post-Submission)**:

- NIR camera compatibility validated (Nov 10, 2025): MediaPipe pose estimation achieves 91.3% keypoint detection on 850nm IR footage (20 commercial CCTV videos from diverse manufacturers)
- Pipeline comparison completed: Integrated YOLO+MediaPipe achieves 20.53 FPS on standard hardware with 5.7% higher accuracy than baseline
- Cost-effectiveness analysis finalized: $672 edge system vs $1,719 cloud alternative (Kami) over 3 years

---

## Next Steps

1. ✅ Abstract Version 3 completed (addresses all supervisor feedback)
2. ✅ Get supervisor approval on revised version
3. ✅ Confirm paper type classification (Technical vs Conceptual)
4. ✅ Update Google Docs file with Version 3 text
5. ✅ Convert to PDF
6. ✅ Submit to ASIP 2025 before Oct 31 deadline

---

## Previous Versions (Archive)

### Version 1 (Oct 26, 2025)

- Title: "Privacy-First Governance in Healthcare AI: Edge Computing for Elderly Safety Monitoring in Cambodia"
- Focus: Privacy governance + accessibility governance
- Word count: 290 words
- Format: Structured sections (Purpose/Design/Findings/Originality)
- Status: Revised after identifying accessibility governance as weak argument

### Version 2 (Oct 27-28, 2025)

- Title: "Privacy Governance-Driven Design of AI-Powered Elderly Safety Monitoring for Cambodia"
- Focus: Privacy governance exclusively (cost as co-benefit)
- Word count: 238 words
- Format: Structured sections
- Status: Submitted for supervisor review, received feedback

### Version 3 (Oct 30, 2025) - CURRENT

- Title: "Privacy Governance-Driven Design of AI-Powered Elderly Safety Monitoring for Cambodia" (unchanged)
- Focus: Conceptual/design paper with privacy governance framework
- Word count: 204 words
- Format: Single paragraph (per supervisor preference)
- Key changes: Added citations (Cavoukian 2010, CSES 2021, WHO SEARO 2024), repositioned as conceptual framework, addressed all 9 supervisor comments
- Status: Ready for final supervisor approval
