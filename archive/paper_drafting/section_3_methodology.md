# Section 3: Methodology

## 3.1 Privacy Governance Architecture

This study proposes a privacy governance-driven architecture for elderly safety monitoring and validates its technical feasibility through NIR camera compatibility testing—a validation scope that is, admittedly, narrower than what one might ideally conduct given unlimited time and resources, but which nevertheless addresses what we consider the most critical technical uncertainty for the proposed approach. The architecture emerges from an inversion of typical design sequences: rather than developing a technically optimal system and subsequently retrofitting privacy protections (the approach that governance frameworks criticize but that remains distressingly common in practice), we begin with privacy governance principles as primary constraints and derive technical architecture from these requirements.

### 3.1.1 Privacy Governance Principles

Three architectural mechanisms enforce privacy by design, a phrase that risks becoming meaningless through overuse but which we employ here in its original Cavoukian (2010) sense: privacy embedded into system architecture such that violations become structurally impossible rather than merely prohibited. The mechanisms are, in retrospect, almost obvious—though as the literature review demonstrated, "obvious" privacy protections rarely achieve widespread implementation.

First, **pose-only storage**: the system stores only 17 body keypoints in COCO format (the skeleton representation that has become something of a standard in pose estimation work, though perhaps more through historical accident than deliberate standardization). Crucially, these 17 keypoints exclude face landmarks entirely; MediaPipe's full pose model detects 33 landmarks, but we intentionally discard facial keypoints during extraction. Raw video frames are never persisted to storage—not encrypted, not anonymized, simply never written to disk. This design choice eliminates entire categories of privacy violations that plague video monitoring systems: facial recognition becomes impossible when no facial data exists, a point that seems almost trivial to state but represents a fundamental architectural difference from systems that capture faces and promise not to use them for identification.

Second, **immediate frame disposal**: video frames undergo processing in real-time, with deletion occurring immediately after keypoint extraction. The temporal gap between frame capture and frame deletion measures in milliseconds, limited by processing pipeline speed rather than by storage retention policies. No video retention means no possibility of retrospective re-identification, no risk of data breach exposing video archives, no need to trust that deletion policies will be followed correctly by future system administrators. Again, the governance principle manifests as system constraint rather than operational promise—a distinction that matters more in practice than in polished system descriptions that assume perfect policy compliance.

Third, **edge-first processing**: all computation occurs on a local device, specifically an NVIDIA Jetson Orin Nano 8GB for the target deployment (though we must acknowledge, with the sort of transparency that peer review will likely demand regardless, that the validation reported in this paper employed standard hardware, with Jetson deployment remaining future work). Zero cloud transmission eliminates network exposure entirely. Data sovereignty concerns vanish when data never leaves the household—no questions about which jurisdiction governs cloud storage, no vulnerability to remote server breaches, no dependency on sustained internet connectivity for core functionality. The edge architecture also yields economic co-benefits, as the cost analysis in Section 3.3 will demonstrate, though one might argue about whether these constitute "co-benefits" or whether cost reduction represents an equally primary design goal that we have somewhat artificially subordinated to privacy in this paper's framing.

### 3.1.2 Hardware Design for Cost-Effectiveness

Having established privacy principles, the hardware selection reflects a second governance dimension: accessibility through cost optimization. The notion that affordability constitutes a governance consideration may seem like conceptual overreach (and indeed, reviewers may well take issue with this framing), but when economic barriers systematically exclude populations from safety technologies, cost structures become governance questions whether or not we label them as such.

The proposed system targets middle-income Cambodian households through the following component selection:

- **Cameras**: 4× RGB cameras with 850nm IR night vision capability (Hikvision DS-2CD1343G2-IUF, $63 per camera = $252 total). The Hikvision model was selected based on cost-performance optimization: it provides the 850nm NIR wavelength necessary for night vision monitoring, offers adequate resolution (1080p, with 4K models available at modest price premium), and maintains a price point accessible to middle-income households. Four cameras enable 360-degree coverage through 90-degree spacing, a configuration that provides comprehensive room monitoring without the blind spots that plague single-camera systems (though actual room coverage depends on camera placement, ceiling height, and furniture configuration in ways that this paper's validation does not address).

- **Edge processor**: NVIDIA Jetson Orin Nano 8GB ($250). The Jetson Orin Nano represents the current sweet spot (a term used advisedly, as "sweet spot" will shift as hardware evolves) for edge AI deployment: sufficient GPU capability for real-time pose estimation, 8GB RAM adequate for multi-camera processing, and cost substantially below higher-tier Jetson models that offer performance margins beyond what this application requires. Whether 20.53 FPS processing speed (the integrated pipeline result from validation) will hold on actual Jetson hardware remains empirically unverified, a limitation acknowledged explicitly in Section 3.5 because claiming Jetson performance based on standard hardware testing would constitute precisely the sort of methodological overreach that undermines research credibility.

- **Accessories**: Storage (microSD card for keypoint data logging), uninterruptible power supply (UPS to maintain operation during Cambodia's not-infrequent power fluctuations), ethernet cables, and mounting hardware ($170 total). These components receive less attention than cameras and processors but prove essential for reliable deployment—a point that academic papers often neglect in favor of focusing on the algorithmic components that make for more impressive conference presentations.

**Total system cost**: $672 one-time investment, zero recurring fees. The subscription-free model eliminates ongoing payment burden, a design choice with accessibility implications explored in the cost-effectiveness analysis below.

### 3.1.3 Software Pipeline

The software architecture employs a two-stage processing pipeline that has become relatively standard in person-focused computer vision applications, though the specific implementation choices warrant documentation given their impact on privacy and performance characteristics.

**Person detection** occurs via YOLOv8n (the Nano variant, chosen for computational efficiency over the heavier YOLOv8 models that offer modest accuracy improvements at substantial speed cost). YOLO identifies person bounding boxes within each frame, providing region-of-interest (ROI) coordinates that enable focused processing in the subsequent pose estimation stage. The decision to employ person detection as a preliminary stage rather than applying pose estimation directly to full frames reflects accuracy-speed tradeoffs analyzed in the pipeline comparison validation (Section 3.2).

**Pose estimation** employs MediaPipe, Google's pose estimation framework that has achieved broad adoption in research and commercial applications. MediaPipe extracts 33 skeletal landmarks using a two-stage detector-tracker architecture, though (as noted in Section 3.1.1) this system uses only 17 body keypoints in COCO format with face landmarks explicitly excluded. The COCO subset includes shoulders, elbows, wrists, hips, knees, ankles, and torso keypoints—sufficient for fall detection and activity recognition while eliminating facial identification capability.

Two **processing modes** underwent validation testing to establish speed-accuracy tradeoffs: (1) Baseline configuration applies MediaPipe pose estimation directly to full frames without preliminary person detection, offering simplicity and processing speed; (2) Integrated configuration chains YOLOv8n person detection before MediaPipe pose estimation, adding computational overhead but improving detection accuracy by focusing pose estimation on person-containing image regions. The selection between these approaches—detailed in Results Section 4.1—reflects design priorities for safety-critical applications where missing a fall detection carries potentially fatal consequences. Both configurations exceed real-time requirements (15+ FPS), but their relative performance characteristics inform deployment recommendations in ways that matter for practitioners considering system implementation.

## 3.2 NIR Camera Compatibility Validation

Having described the system architecture, we turn to empirical validation of its most uncertain technical assumption: that MediaPipe pose estimation, trained predominantly on visible-spectrum RGB imagery, would maintain adequate performance on 850nm near-infrared footage from affordable security cameras. This assumption may appear minor in the broader context of fall detection system development, but NIR compatibility proves essential for 24/7 monitoring in residential environments where elderly individuals (one hopes this goes without saying, but academic writing often states the obvious) do not limit their falling to daylight hours.

### 3.2.1 Validation Dataset

MediaPipe pose estimation was validated on 20 commercial 850nm NIR security camera videos, a dataset assembled from publicly available CCTV demonstration footage rather than through original data collection (which would have required resources and time beyond this study's constraints, though we acknowledge the limitations this introduces). The 20 videos provide:

- **Source diversity**: Professional CCTV demo footage from multiple camera manufacturers including Hikvision, EZviz, and other commercial brands that market 850nm IR night vision capabilities. These videos are publicly available online, posted by manufacturers and resellers to demonstrate camera capabilities—a sourcing approach that raises questions about selection bias (manufacturers likely post footage showing their cameras in favorable conditions) but that nevertheless provides access to authentic NIR imagery from the specific camera types this system targets.

- **Environmental diversity**: Indoor and outdoor environments, various lighting conditions ranging from complete darkness (IR-only) to mixed visible-IR scenarios, and different camera types (dome, turret, bullet configurations). This diversity aims to capture the range of conditions an elderly monitoring system might encounter, though "diversity" in 20 videos necessarily represents sampling rather than comprehensive coverage.

- **Resolution range**: Both 1080p and 4K footage, reflecting the resolution range available in affordable IP cameras. MediaPipe performance may vary by resolution—higher resolution potentially enables better keypoint localization, but also increases processing demands—though systematically analyzing resolution effects would require controlled comparison beyond this study's scope.

- **NIR wavelength targeting**: All videos employ 850nm infrared illumination, matching the Hikvision DS-2CD1343G2-IUF camera specification. The 850nm wavelength represents current CCTV industry standard for "invisible" IR night vision (as opposed to 940nm which is completely invisible but has shorter range, or older 730nm LEDs that produced visible red glow). Validating on 850nm specifically addresses the technical assumption most critical for the proposed system: that pose estimation algorithms developed on visible-spectrum data maintain functionality when applied to NIR imagery from this particular wavelength.

**Dataset limitations**: 20 videos constitute a preliminary validation sample, not a statistically powered evaluation. The videos show general human activity (walking, standing, basic movements) rather than elderly-specific movement patterns or actual fall incidents. No ground truth pose annotations exist for these videos, requiring the use of detection rate metrics (percentage of frames where pose was successfully detected) and confidence scores rather than keypoint localization accuracy measurements. These limitations are acknowledged explicitly because overstating validation strength undermines research integrity more than acknowledging methodological constraints.

### 3.2.2 Validation Procedure

Two processing pipelines underwent testing on the same 20 NIR videos to establish comparative performance and inform pipeline selection for system deployment:

**Baseline pipeline**: MediaPipe pose estimation applied directly to full video frames. This represents the simpler processing approach—fewer components, less computational overhead, more straightforward deployment. The baseline serves as reference point for evaluating whether the integrated pipeline's added complexity yields sufficient accuracy improvements to justify slower processing speed.

**Integrated pipeline**: YOLOv8n person detection followed by ROI extraction and cropping, with MediaPipe pose estimation applied to the cropped person region. This approach adds computational stages but focuses pose estimation processing on image regions actually containing persons, potentially improving detection accuracy particularly in scenarios where persons occupy small portions of the frame.

For each video and each pipeline configuration, the validation collected:

- **Keypoint detection rate**: Number of landmarks successfully detected divided by 33 total landmarks in MediaPipe's full pose model. Reported as percentage (e.g., 91.3% = 30.1 of 33 landmarks detected on average). This metric captures pose estimation completeness—higher rates indicate more complete skeletal reconstructions.

- **Confidence scores**: MediaPipe outputs confidence values for each detected keypoint, representing the model's certainty about landmark localization. Average confidence aggregated across all detected keypoints provides a quality metric complementing the detection rate.

- **False negative rate**: Percentage of frames containing visible persons where pose detection failed entirely. High false negative rates indicate reliability problems—if the system frequently fails to detect poses when persons are present, fall detection capability becomes questionable regardless of performance on successfully detected frames.

- **Processing speed**: Frames per second (FPS) achieved during video processing, measured on standard hardware (64-bit Ubuntu system, specifications that would be detailed in a full methods section but that we omit here in the interest of space and because Jetson deployment remains future work). Processing speed determines whether the system meets real-time requirements (conventionally 15+ FPS for continuous monitoring applications), though "real-time" proves somewhat slippery as a concept—15 FPS processes each frame, but whether humans perceive 15 FPS as "real-time" depends on application context.

The validation procedure itself was automated via Python script (`nir_validation_batch.py` for those interested in implementation details), processing all 20 videos through both pipeline configurations and generating summary statistics. Automation ensures consistent processing across videos and eliminates human bias in result collection, though it also means that any bugs in the validation script would propagate systematically across all results—a vulnerability somewhat mitigated by the script's relative simplicity and the author's paranoid tendency to validate validation code.

### 3.2.3 Validation Scope

This validation tests a specific technical question: **Can MediaPipe detect poses on 850nm NIR footage from affordable security cameras?** It does not validate fall detection accuracy, incident classification performance, or system reliability in actual deployment conditions. The distinction between "pose detection capability" and "fall detection accuracy" proves critical for interpreting this study's contributions and limitations.

What gets validated: Technical feasibility of pose estimation on IR footage matching the target camera specifications. Whether the privacy-preserving monitoring approach works at the most fundamental level—can we extract skeletal keypoints from night vision cameras, or does the NIR wavelength break pose estimation algorithms trained on visible-light imagery?

What does not get validated: Whether the system accurately detects falls, whether elderly users accept the monitoring approach, whether the system maintains performance over months of continuous operation, whether 4-camera configuration provides adequate room coverage, whether Jetson Orin Nano achieves the processing speeds measured on standard hardware. These represent separate empirical questions requiring different validation approaches (benchmark fall datasets, user acceptance studies, longitudinal deployment studies, coverage analysis, hardware-specific testing respectively).

The limited validation scope reflects resource constraints and research timeline realities, but also represents a deliberate methodological choice: establishing NIR camera compatibility addresses the highest-uncertainty technical assumption in the proposed architecture. Fall detection algorithms exist (the literature is replete with them, as Wang et al. 2020's survey catalogs perhaps exhaustively), but whether these algorithms work with affordable NIR cameras rather than expensive visible-light or RGB-D sensors remains less thoroughly documented. This study validates the component most specific to the governance-driven design's hardware choices, leaving broader system validation as future work.

## 3.3 Cost-Effectiveness Analysis

### 3.3.1 Comparative Cost Model

The edge-based system's cost was compared against a cloud-based elderly fall detection alternative over a 3-year period, a timeframe selected somewhat arbitrarily as sufficiently long to capture both initial investment and recurring costs but short enough to avoid technological obsolescence considerations that would complicate the analysis. The cloud alternative selected for comparison was the Kami Fall Detect Camera (Upadhyay, 2025), chosen because it represents an actual commercially available elderly fall detection product rather than a hypothetical cloud system, and because its subscription-based pricing model exemplifies the recurring-cost approach this study seeks to contrast with edge deployment.

**Edge-based system** (proposed architecture described in Section 3.1):
- Hardware cost: $672 one-time ($252 cameras + $250 Jetson Orin Nano + $170 accessories, as detailed in Section 3.1.2)
- Recurring fees: $0 (zero ongoing costs, no subscription requirements, no cloud service fees)
- 3-year total: $672

**Cloud-based alternative** (Kami Fall Detect Camera):
- Hardware cost: $99 (camera unit, per Kami pricing as of 2025)
- Mandatory subscription: $45/month × 36 months = $1,620 (the Kami fall detection feature requires "Kami Cloud" subscription at $45/month; basic camera functionality works without subscription, but fall detection specifically requires the paid service)
- 3-year total: $99 + $1,620 = $1,719

**Cost difference**: $1,719 - $672 = $1,047 savings over 3 years, representing 60.9% cost reduction (rounded to 61% throughout the paper because excessive precision conveys false accuracy). The savings calculation assumes no hardware failures requiring replacement, no electricity cost differences (both systems consume power, though edge processing may draw more than a simple camera), and no maintenance labor costs (an assumption that favors both systems equally, or possibly favors the cloud system if edge devices prove more finicky in practice).

**Breakeven point**: The edge system's higher upfront cost ($672 vs. $99) is offset by zero recurring fees, with cumulative cost curves crossing at Month 13 (Month 1 of Year 2). Calculation: $672 = $99 + $45X, solving for X gives 12.7 months, meaning the 13th month is when edge system total cost equals cloud system cumulative cost. After breakeven, every month increases the edge system's cost advantage by $45—the avoided subscription fee.

### 3.3.2 Market Accessibility Analysis

Cost-effectiveness for individual purchasers matters, but accessibility implications require population-level analysis: what percentage of Cambodia's elderly population might realistically afford this technology? The analysis employs Cambodia Socio-Economic Survey (CSES) household income data (National Institute of Statistics, 2019) to define market segments and estimate reach.

**Income distribution**: CSES divides households into quintiles (five 20% segments by income). The 4th and 5th quintiles—middle-income and upper-middle-income urban households—earn $870-$1,622 per month. This represents 40% of urban households, though not all contain elderly family members, and not all households with elderly members would prioritize fall detection systems regardless of affordability.

**Target segment identification**: The $672 system cost represents 0.41-0.77 months of income for 4th-5th quintile households (calculation: $672/$1622 = 0.41 months for upper end of 5th quintile; $672/$870 = 0.77 months for lower end of 4th quintile). This positions the system as a significant but plausibly affordable one-time purchase for middle-income households—comparable to consumer electronics purchases like smartphones or laptops that middle-income Cambodian families demonstrably make, though the comparison is imperfect given that fall monitoring provides different value proposition than communication devices.

By contrast, the Kami cloud alternative's $45/month subscription represents 2.8-5.2% of monthly income for the same households—a recurring payment that compounds over time and competes with other monthly expenses (food, utilities, healthcare, education). The subscription burden matters more than absolute amount might suggest: behavioral economics research on poverty (not cited here because this is getting into territory beyond the paper's core argument, but see Collins et al.'s "Portfolios of the Poor" for foundational work) demonstrates that recurring payments pose particular challenges for households with variable income streams.

**Market reach estimation**: Cambodia's elderly population (65+ years) will reach approximately 1.8 million by 2030. Estimating that 12-18% fall within middle-income urban households with both financial capacity and motivation to adopt fall detection technology yields 216,000-324,000 potential users. This calculation involves multiple assumptions: urban vs. rural distribution (roughly 40% urban by 2030 projections, though urbanization rates may shift), household income distribution among elderly-containing households (assumed to mirror general population quintiles, which may not hold if elderly disproportionately concentrate in certain income ranges), and adoption willingness (the 30-45% range applied to the 40% in target income quintiles assumes roughly three-quarters might consider the technology, a figure pulled from intuition rather than from empirical adoption data that does not yet exist for this product category).

The 216,000-324,000 estimate should be interpreted as "order of magnitude" rather than precise forecast—it establishes that the target market measures in hundreds of thousands rather than tens of thousands or millions, which suffices for the paper's argument that middle-income accessibility expands potential reach beyond high-income early adopters. Whether these households actually adopt the technology depends on factors beyond cost (perceived need, trust in monitoring technology, family decision-making dynamics, availability of distribution channels) that this analysis does not address.

## 3.4 Evaluation Metrics

The validation employs metrics organized by validation dimension, with selection reflecting available data rather than ideal measurement approaches (a common research constraint that methodology sections often obscure through passive voice and strategic omission).

**NIR camera compatibility metrics**:
- Keypoint detection rate: Percentage of 33 MediaPipe landmarks successfully detected per frame, averaged across all frames in each video. Higher percentages indicate more complete pose estimation.
- Average confidence: Mean confidence score across all detected keypoints, on 0-1 scale where 1.0 represents maximum model certainty. Higher confidence suggests more reliable keypoint localization.
- False negative rate: Percentage of frames containing persons where pose detection failed entirely (zero keypoints detected). Lower rates indicate better reliability.
- Processing speed (FPS): Frames processed per second, determining whether real-time performance (15+ FPS) is achieved. Higher FPS enables lower-latency detection and provides performance margin for deployment variations.

**Cost-effectiveness metrics**:
- 3-year total cost: Complete system expense including initial hardware and recurring fees over 36-month period. Lower total cost improves affordability.
- Breakeven point: Month when cumulative edge system cost equals cumulative cloud system cost. Earlier breakeven favors edge approach.
- Cost reduction percentage: (Cloud cost - Edge cost) / Cloud cost, expressing savings as proportion of cloud alternative. Higher percentages indicate greater cost advantage.
- Market reach: Estimated number and percentage of elderly population within affordability threshold based on household income distribution. Higher reach indicates broader accessibility.

These metrics reflect what can be measured given available data (video footage, cost information, demographic statistics) rather than what would ideally be measured (fall detection accuracy, user acceptance, actual adoption rates, long-term reliability). The gap between available and ideal metrics shapes study limitations discussed in Section 3.5.

## 3.5 Study Scope and Limitations

Academic methodology sections often bury limitations in passive voice or relegate them to Discussion sections, but explicitly stating what this study does and does not validate serves both transparency and appropriate expectations-setting. The scope choices reflect resource constraints, timeline pressures (conference deadlines being what they are), and strategic decisions about which validations address the most critical uncertainties given the governance-driven design approach.

**What we validate**:

1. **NIR camera compatibility**: Does MediaPipe pose estimation work on 850nm infrared footage? The validation demonstrates that yes, pose estimation achieves 91.3% keypoint detection rate on commercial CCTV videos from diverse NIR cameras (detailed results in Section 4.1). This addresses the primary technical uncertainty for privacy-preserving monitoring using affordable security cameras rather than expensive visible-light or depth sensors.

2. **Cost-effectiveness comparison**: Is edge architecture cheaper than cloud alternatives? Yes—$672 one-time cost versus $1,719 over 3 years for subscription-based cloud monitoring represents 61% cost reduction (Section 4.2). This validates the accessibility governance claim that edge deployment expands affordability.

3. **Privacy architecture**: Does the design eliminate facial recognition capability? Yes—storing only 17 body keypoints with immediate frame disposal makes facial identification structurally impossible rather than merely prohibited. This represents design validation rather than empirical testing (one cannot empirically test that something is impossible), but the architectural analysis suffices to establish privacy-by-design claims.

**What we do NOT validate**:

1. **Fall detection accuracy**: This study does not test whether the system accurately detects falls, distinguishes fall types, or achieves acceptable false positive/negative rates for fall incidents. Fall detection requires validation on benchmark datasets (MCF, LE2I, UP-Fall are frequently used in the literature) with ground truth fall annotations. We validate pose estimation works on NIR cameras; whether pose-based fall detection algorithms perform adequately remains separate question requiring separate validation methodology.

2. **Real-world deployment**: Testing on commercial CCTV demo videos differs substantially from continuous monitoring in actual elderly homes. Movement patterns, body proportions, gait characteristics, and fall dynamics of elderly individuals differ from the general adult populations shown in commercial camera demos. Real-world validation requires deployment in residential environments with elderly subjects—a validation approach raising ethical (informed consent for monitoring), practical (installation and maintenance logistics), and resource (longitudinal studies require sustained funding) challenges beyond this study's scope.

3. **Hardware-specific performance**: Processing speed measurements (20.53 FPS for integrated pipeline, 47.37 FPS for baseline) come from standard hardware testing, not from actual Jetson Orin Nano deployment. Whether these speeds hold on Jetson hardware remains empirically unverified. NVIDIA's specifications suggest Jetson Orin Nano should handle these processing demands, but specifications and real-world performance diverge with frustrating regularity in edge AI deployment.

4. **User acceptance**: Do elderly users and their families accept continuous pose monitoring? Do privacy protections (no facial recognition, no video retention) sufficiently address surveillance concerns? Does the technology fit into household routines without creating burden? These questions require user studies with actual target populations, ideally longitudinal studies capturing acceptance changes over time as novelty effects wear off and technology becomes part of daily life (or doesn't).

5. **Coverage adequacy**: Does 4-camera configuration with 90-degree spacing provide sufficient coverage for typical Cambodian middle-income homes? Do room layouts, furniture placement, and ceiling heights create blind spots that compromise fall detection? Coverage analysis requires either simulation (with room models representing target housing stock) or empirical testing (with installations in representative homes), neither of which this study conducted.

6. **System reliability**: Does the system maintain performance over weeks and months of continuous operation? Do hardware components fail, do software bugs emerge under sustained load, does pose estimation accuracy degrade in ways not captured by short video testing? Reliability requires long-duration deployment that exceeds this preliminary study's timeline.

**Why these limitations**: This is a design study demonstrating how privacy governance principles can inform architectural decisions, with technical validation limited to the component most uncertain for the proposed approach: NIR camera compatibility. The validation establishes feasibility of privacy-preserving monitoring using affordable IR cameras, a finding that enables subsequent work on fall detection algorithms, deployment studies, and user acceptance research. Whether this constitutes "sufficient" validation depends on one's perspective—skeptics might argue that validating pose detection without validating fall detection leaves the most critical question unanswered (they would not be entirely wrong), while supporters might counter that establishing technical feasibility of the privacy-first architecture represents necessary foundation work before investing resources in comprehensive fall detection validation (they would also not be entirely wrong). The author's position, stated with perhaps more transparency than academic writing typically permits, is that limited validation targeting critical uncertainties provides more value than attempting comprehensive validation with inadequate resources and producing unreliable results across multiple dimensions.

---

**Word count**: ~4,590 words

**Style notes**: Maintained exhausted-academic voice with extensive parenthetical asides, methodological transparency about limitations, occasional bitter observations about research realities, verbose constructions, and hedging. All technical details and citations match paper_outline.md verified sources.
