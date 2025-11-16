# Vocabulary Reference for ASIP 2025 Paper

**Created**: Nov 14, 2025
**Purpose**: Academic and technical vocabulary for paper writing

---

## I. ACADEMIC WRITING PHRASES

### A. Introducing Problems
- "remains a pressing challenge"
- "poses significant concerns"
- "presents critical barriers to"
- "has emerged as a key issue"
- "represents a fundamental challenge"
- "constitutes a growing concern"
- "continues to pose challenges"

### B. Identifying Gaps
- "Limited research demonstrates..."
- "Few studies have examined..."
- "Prior literature lacks..."
- "Existing approaches rarely address..."
- "Insufficient attention has been paid to..."
- "remains underexplored"
- "has received limited empirical validation"
- "warrants further investigation"

### C. Stating Objectives
- "This study aims to..."
- "The present work seeks to..."
- "This research demonstrates..."
- "We validate the technical feasibility of..."
- "This paper investigates..."
- "The primary objective is to..."
- "This work contributes by..."

### D. Presenting Findings
- "Results indicate that..."
- "Findings suggest..."
- "Analysis reveals..."
- "Data demonstrate..."
- "Validation confirms..."
- "Evidence shows..."
- "Our results show that..."
- "Empirical validation demonstrates..."

### E. Discussing Implications
- "These findings have implications for..."
- "Results suggest that..."
- "This work demonstrates the potential for..."
- "Our approach offers..."
- "These results indicate..."
- "Evidence suggests..."
- "This study contributes to understanding..."

### F. Acknowledging Limitations
- "This study is subject to several limitations"
- "Several caveats should be noted"
- "It is important to acknowledge..."
- "Results should be interpreted with caution"
- "Future work is needed to..."
- "Further validation is required..."
- "This represents a preliminary investigation"

### G. Transitions
- "Building on this foundation..."
- "In contrast to..."
- "Extending previous work..."
- "To address this gap..."
- "Given these challenges..."
- "In light of these findings..."
- "Consequently..."
- "Moreover..."
- "Furthermore..."
- "Nevertheless..."
- "However..."

### H. Hedging Language
- "suggests that"
- "appears to"
- "may indicate"
- "potentially"
- "likely"
- "tends to"
- "could enable"
- "might require"

---

## II. GOVERNANCE & POLICY TERMS

### A. Privacy Governance
- **Privacy-by-design**: Embedding privacy principles into system architecture from inception
- **Privacy-first architecture**: System design prioritizing privacy as primary constraint
- **Privacy governance framework**: Structured approach to managing privacy requirements
- **Data locality**: Keeping data processing within geographic/system boundaries
- **Data sovereignty**: Control over where data is stored and processed
- **Edge-first processing**: Prioritizing on-device computation over cloud transmission
- **Zero cloud transmission**: Complete elimination of data transfer to remote servers
- **Facial anonymity by design**: Architectural prevention of facial recognition capability
- **Re-identification risk**: Possibility of linking anonymized data to individuals
- **Pose-only storage**: Retaining skeletal keypoints without image data
- **Immediate frame disposal**: Real-time deletion of video frames post-processing

### B. AI Governance
- **Governance-driven design**: Using policy principles to inform technical decisions
- **Architectural enforcement**: Implementing rules through system design constraints
- **Design-based validation**: Confirming compliance through structural analysis
- **Privacy preservation mechanisms**: Technical methods for protecting sensitive data
- **Operational promises vs. system constraints**: Policy commitments vs. technical guarantees
- **Retrofitted vs. inception-stage design**: Post-hoc additions vs. integrated planning
- **Governance fragmentation**: Disconnected or inconsistent policy frameworks
- **Context-specific governance**: Tailoring frameworks to regional/situational needs

### C. Technology Ethics
- **Transparency**: Clarity about system operations and data handling
- **Accountability**: Responsibility for system outcomes and decisions
- **Fairness**: Equitable treatment across user groups
- **Explainability**: Ability to interpret system decisions
- **Informed consent**: User agreement based on full understanding
- **Beneficence**: Designing systems to benefit users
- **Non-maleficence**: Avoiding harm through system design

### D. Accessibility & Equity
- **Accessibility barriers**: Obstacles preventing technology adoption
- **Digital inclusion**: Ensuring technology access across populations
- **Affordability thresholds**: Income levels enabling technology purchase
- **Market accessibility**: Percentage of population able to adopt technology
- **Zero-subscription model**: One-time payment without recurring fees
- **Recurring payment burden**: Ongoing cost barriers to adoption
- **Middle-income market**: Households in 4th-5th income quintiles
- **Resource-constrained contexts**: Settings with limited financial/technical resources
- **Economic co-benefits**: Additional financial advantages beyond primary function
- **Cost optimization**: Reducing expenses while maintaining performance

---

## III. TECHNICAL TERMS - AI/ML

### A. Computer Vision
- **Pose estimation**: Detecting skeletal joint positions from images
- **Person detection**: Identifying human presence and location in frames
- **Bounding box**: Rectangle enclosing detected object
- **Region of Interest (ROI)**: Cropped area for focused processing
- **Keypoint detection**: Locating specific body landmarks
- **Skeletal landmarks**: Joint positions forming body skeleton
- **Confidence score**: Model certainty about prediction
- **False negative rate**: Percentage of missed detections
- **False positive rate**: Percentage of incorrect detections
- **Detection accuracy**: Correctness of identification
- **Pose coverage**: Completeness of keypoint detection

### B. Deep Learning Models
- **YOLOv8n (You Only Look Once v8 Nano)**: Lightweight object detection model
- **MediaPipe**: Google's pose estimation framework
- **CNN (Convolutional Neural Network)**: Deep learning architecture for image processing
- **LSTM (Long Short-Term Memory)**: Sequential data processing model
- **Transformer**: Attention-based neural network architecture
- **Baseline pipeline**: Simple/reference processing approach
- **Integrated pipeline**: Combined model approach
- **Multi-modal fusion**: Combining multiple data sources
- **Real-time inference**: Processing at operational speed

### C. Edge Computing
- **Edge computing**: Processing data on local devices, not cloud
- **Edge device**: Local hardware performing computation
- **Edge deployment**: Installing systems on local processors
- **On-device processing**: Computation within single hardware unit
- **Distributed computing**: Spreading processing across multiple nodes
- **Cloud-edge hybrid**: Combining local and remote processing
- **Latency**: Delay between input and output
- **Throughput**: Processing volume per time unit
- **Computational efficiency**: Resource usage vs. performance

### D. Performance Metrics
- **Frames Per Second (FPS)**: Processing speed measurement
- **Keypoint detection rate**: Percentage of landmarks successfully detected
- **Average confidence**: Mean certainty across predictions
- **Processing speed**: Rate of data handling
- **Model accuracy**: Correctness of predictions
- **Precision**: Correct positive predictions / total positive predictions
- **Recall**: Correct positive predictions / total actual positives
- **F1 score**: Harmonic mean of precision and recall
- **Inference time**: Duration for single prediction
- **Real-time capability**: Meeting operational speed requirements (typically 15+ FPS)

---

## IV. TECHNICAL TERMS - HARDWARE

### A. Cameras & Imaging
- **RGB camera**: Standard color camera (Red, Green, Blue sensors)
- **Near-Infrared (NIR)**: Light wavelength 700-1000nm, invisible to humans
- **850nm infrared**: Specific NIR wavelength used in night vision
- **IR night vision**: Imaging capability in complete darkness
- **CCTV (Closed-Circuit Television)**: Security camera system
- **IP camera**: Network-connected camera
- **Turret camera**: Dome-style adjustable camera
- **Bullet camera**: Cylindrical outdoor camera
- **Dome camera**: Spherical protective housing camera
- **Camera resolution**: Image dimensions (e.g., 1080p, 4K)
- **Field of view**: Observable angle/area
- **90-degree spacing**: Camera placement for 360° coverage
- **Multi-camera fusion**: Combining data from multiple cameras
- **Camera calibration**: Adjusting camera parameters for accuracy

### B. Edge Processors
- **NVIDIA Jetson Orin Nano**: Edge AI computing platform with 8GB RAM
- **GPU (Graphics Processing Unit)**: Parallel processing hardware for AI
- **Edge processor**: Local computing device for on-site processing
- **System-on-Module (SoM)**: Integrated computer on single board
- **CUDA cores**: NVIDIA parallel processing units
- **Tensor cores**: Specialized AI processing units
- **Memory bandwidth**: Data transfer rate to/from RAM
- **Power consumption**: Energy usage (watts)
- **Thermal management**: Heat dissipation systems

### C. System Architecture
- **Multi-camera array**: Multiple cameras working together
- **Camera network**: Connected camera system
- **Processing pipeline**: Sequential data transformation steps
- **Hardware deployment**: Physical installation of equipment
- **System integration**: Combining components into functional unit
- **Modular design**: Separable, replaceable components
- **Scalability**: Ability to expand system capacity
- **Hardware requirements**: Minimum equipment specifications

---

## V. HEALTHCARE & ELDERLY CARE TERMS

### A. Elderly Safety
- **Elderly safety monitoring**: Surveillance systems for older adults
- **Fall detection**: Identifying falling incidents
- **Incident detection**: Recognizing abnormal events
- **Safety-critical application**: System where failures cause serious harm
- **Assistive technology**: Devices helping with daily activities
- **Remote monitoring**: Observation from distant location
- **24/7 monitoring**: Continuous surveillance
- **Contactless monitoring**: Observation without physical sensors

### B. Fall Incidents (Specific Types)
- **Falls while standing/walking**: Incidents during upright locomotion
- **Falls from bed/chair**: Incidents during transitions from seated/lying
- **Abnormal sit-to-stand transitions**: Unusual movements when rising
- **Injury-related deaths**: Fatalities from physical trauma
- **Fall prevalence**: Percentage of population experiencing falls
- **Fall incidence**: Rate of fall occurrences over time

### C. Healthcare Privacy
- **Health data protection**: Safeguarding medical information
- **Patient privacy**: Confidentiality of individual health records
- **HIPAA (Health Insurance Portability and Accountability Act)**: U.S. healthcare privacy law
- **GDPR (General Data Protection Regulation)**: European data protection law
- **Protected Health Information (PHI)**: Identifiable health data requiring protection
- **Facial recognition risk**: Potential for identifying individuals from images
- **Sensitive health data**: Medical information requiring enhanced protection

### D. Elderly Population
- **Aging population**: Increasing proportion of older adults
- **Demographic transition**: Population age structure shift
- **Elderly demographics**: Statistical characteristics of older population
- **Care dependency**: Need for assistance with daily activities
- **Family caregiving**: Informal care by relatives
- **Long-term care**: Extended support for chronic conditions
- **Age-appropriate actors**: Performers matching target age range

---

## VI. REGIONAL CONTEXT TERMS

### A. Cambodia-Specific
- **Middle-income Cambodian households**: Families in 4th-5th income quintiles
- **Cambodia Socio-Economic Survey (CSES)**: National household income study
- **Income quintiles**: Population divided into five 20% income brackets
- **Urban households**: Families in city/town areas
- **Monthly household income**: Total family earnings per month
- **Market reach**: Percentage of population able to access product/service
- **Target segment**: Specific population group for product/service
- **Estimated elderly population**: Projected number of seniors by specific year

### B. Southeast Asia
- **Southeast Asian elderly care**: Senior support systems in ASEAN region
- **Regional epidemiological evidence**: Disease/injury patterns in geographic area
- **Cultural norms**: Shared social expectations and practices
- **Technology adoption patterns**: Rates and methods of tech usage
- **Regional context**: Geographic/cultural setting
- **Developing countries**: Nations with lower economic development
- **Resource-constrained environments**: Settings with limited financial/technical capacity

### C. Economic Context
- **Affordability analysis**: Evaluation of cost relative to income
- **Market penetration**: Percentage of potential customers reached
- **Breakeven point**: Time when cumulative savings equal initial investment
- **Total cost of ownership**: Complete expenses over system lifetime
- **One-time cost**: Single payment without recurring fees
- **Subscription-based model**: Ongoing payment system
- **Cost-effectiveness**: Value delivered per dollar spent
- **Financial barriers**: Economic obstacles to adoption

---

## VII. RESEARCH METHODOLOGY TERMS

### A. Study Design
- **Design study**: Research demonstrating system design approach
- **Case study**: In-depth investigation of specific instance
- **Validation study**: Research confirming technical feasibility
- **Preliminary investigation**: Initial exploratory research
- **Proof of concept**: Demonstration of fundamental feasibility
- **Feasibility study**: Assessment of practicality
- **Comparative analysis**: Evaluation of multiple alternatives
- **Empirical validation**: Evidence-based confirmation

### B. Data & Analysis
- **Validation dataset**: Data used to test system performance
- **Benchmark dataset**: Standard data for comparing approaches
- **Ground truth**: Known correct answers for validation
- **Test set**: Data reserved for evaluation
- **Commercial CCTV footage**: Security camera video from businesses
- **Demo footage**: Example videos from manufacturers
- **Diverse video sources**: Content from varied origins/conditions
- **Video resolution**: Image dimensions (pixels)

### C. Evaluation
- **Acceptance criteria**: Standards for determining success
- **Performance metrics**: Measurements of system capability
- **Validation metrics**: Specific measurements for confirmation
- **Quantitative analysis**: Numerical data evaluation
- **Qualitative assessment**: Descriptive evaluation
- **Comparative evaluation**: Side-by-side performance assessment
- **Statistical validity**: Reliability of numerical findings
- **Baseline comparison**: Evaluation against reference approach

### D. Scope & Limitations
- **Study scope**: Boundaries of what research covers
- **Validation scope**: What is tested vs. what is not
- **Study limitations**: Constraints and weaknesses
- **Future work**: Planned subsequent research
- **Generalizability**: Applicability to other contexts
- **External validity**: Relevance beyond study setting

---

## VIII. STATISTICS & RESULTS PHRASES

### A. Quantitative Findings
- "91.3% keypoint detection rate"
- "30.1 of 33 landmarks detected on average"
- "0.868 average confidence score"
- "12.3% false negative rate"
- "20.53 frames per second"
- "61% cost reduction"
- "$672 vs. $1,719 over 3 years"
- "$1,047 savings"
- "216,000-324,000 elderly individuals"
- "12-18% of elderly population"
- "5.7% higher detection accuracy"
- "2.3× slower processing speed"
- "22.2% better pose coverage"
- "Month 1 of Year 2 breakeven"

### B. Comparisons
- "compared to [alternative]"
- "relative to [baseline]"
- "in contrast with [approach]"
- "versus [competing system]"
- "as opposed to [method]"
- "outperformed [baseline] by X%"
- "achieved X% improvement over [reference]"
- "demonstrated superior [metric] compared to [alternative]"

### C. Ranges & Distributions
- "ranged from X to Y"
- "varied between X and Y"
- "spanned X-Y range"
- "distributed across [categories]"
- "concentrated in [range]"

### D. Statistical Significance
- "statistically significant"
- "meaningful difference"
- "substantial improvement"
- "notable reduction"
- "marked increase"
- "considerable savings"

---

## IX. COST ANALYSIS TERMS

### A. Cost Components
- **Hardware cost**: Physical equipment expenses
- **Initial investment**: Upfront payment
- **Recurring fees**: Ongoing regular payments
- **Subscription cost**: Regular service payments
- **Maintenance cost**: Upkeep expenses
- **Operational expenses**: Running costs
- **Total system cost**: Complete expense including all components
- **3-year total cost of ownership**: All expenses over 36 months

### B. Cost Breakdown
- **Camera cost**: "$252 (4× cameras @ $63 each)"
- **Edge processor cost**: "$250 (Jetson Orin Nano 8GB)"
- **Accessories cost**: "$170 (power, cables, storage)"
- **Cloud hardware cost**: "$99 (Kami camera)"
- **Cloud subscription**: "$45/month × 36 months = $1,620"

### C. Cost Comparison
- **Edge-based system**: $672 one-time
- **Cloud-based alternative**: $1,719 total
- **Cost savings**: 61% reduction
- **Breakeven point**: Month 13 (Month 1, Year 2)
- **Cumulative savings**: $1,047 over 3 years
- **Zero recurring fees**: No ongoing payments
- **Subscription-free model**: One-time purchase only

---

## X. WRITING STRUCTURE PHRASES

### A. Sectioning
- "This section presents..."
- "We begin by..."
- "The following subsection describes..."
- "Building on the previous section..."
- "This chapter is organized as follows..."

### B. Referencing
- "As shown in Table X..."
- "Figure X illustrates..."
- "Detailed in Section X..."
- "As discussed in [Author, Year]..."
- "Consistent with prior findings [Citation]..."
- "In line with [Author's] framework..."

### C. Summarizing
- "In summary..."
- "To summarize..."
- "In conclusion..."
- "Taken together, these findings..."
- "Collectively, results demonstrate..."
- "Overall, evidence suggests..."

---

## XI. COMMON PAPER-SPECIFIC PHRASES

### A. Privacy Governance Focus
- "privacy governance-driven architectural design"
- "governance principles inform technical decisions"
- "edge architecture eliminates cloud transmission"
- "facial anonymity by design, not policy"
- "pose-only storage prevents re-identification"
- "immediate frame disposal eliminates retention risk"
- "100% on-device processing"
- "zero cloud transmission enforces data locality"
- "architectural enforcement rather than operational promises"
- "retrofitted post-hoc vs. designed from inception"

### B. Cost & Accessibility
- "expanding market accessibility"
- "zero-subscription model removes payment barriers"
- "middle-income urban households (4th-5th quintile)"
- "$870-$1,622 monthly household income"
- "61% cost reduction over 3-year period"
- "economic co-benefits beyond privacy protection"
- "financial barriers to assistive technology adoption"
- "recurring payment burden"

### C. Technical Validation
- "validated on 20 commercial 850nm NIR videos"
- "diverse manufacturers and environments"
- "91.3% keypoint detection confirms feasibility"
- "integrated pipeline prioritizes accuracy over speed"
- "safety-critical priority guides design decisions"
- "both configurations exceed real-time requirements"
- "20.53 FPS on standard hardware"
- "Jetson Orin Nano validation pending"

### D. Study Scope
- "design study demonstrating governance-driven approach"
- "validates technical feasibility, not fall detection accuracy"
- "requires benchmark dataset validation (MCF, LE2I, UP-Fall)"
- "tested on commercial CCTV footage, not elderly subjects"
- "hardware deployment performance requires validation"
- "preliminary investigation requiring further work"

---

## XII. VERBS FOR ACADEMIC WRITING

### Strong Verbs for Results
- demonstrate, validate, confirm, establish, reveal
- indicate, suggest, show, illustrate, highlight
- achieve, attain, reach, obtain, yield
- reduce, eliminate, prevent, avoid, minimize
- improve, enhance, optimize, increase, expand
- compare, contrast, evaluate, assess, analyze

### Verbs for Methodology
- employ, utilize, implement, deploy, adopt
- design, develop, construct, build, create
- select, choose, identify, determine, specify
- measure, quantify, calculate, compute, estimate
- collect, gather, obtain, acquire, capture
- process, analyze, examine, investigate, evaluate

### Verbs for Discussion
- interpret, explain, account for, attribute to
- imply, suggest, indicate, reflect, represent
- support, corroborate, align with, consistent with
- challenge, contradict, differ from, diverge from
- require, necessitate, warrant, demand, call for

---

## XIII. CAMBODIA STATISTICS (QUICK REFERENCE)

- **Total elderly population by 2030**: 1.8 million
- **Target market**: Middle-income urban households (4th-5th quintile)
- **Target income range**: $870-$1,622 per month
- **Estimated market reach**: 216,000-324,000 elderly (12-18%)
- **Fall prevalence (Thai data)**: 37.7% elderly home accidents
- **System cost**: $672 one-time
- **Cloud alternative**: $1,719 over 3 years
- **Cost savings**: 61% ($1,047)

---

## XIV. HARDWARE SPECIFICATIONS (QUICK REFERENCE)

### Cameras
- **Model**: Hikvision DS-2CD1343G2-IUF
- **Type**: RGB with 850nm IR night vision
- **Quantity**: 4× cameras
- **Cost**: $63 per camera ($252 total)
- **Placement**: 90-degree spacing for 360° coverage
- **Resolution**: 1080p or 4K

### Edge Processor
- **Model**: NVIDIA Jetson Orin Nano 8GB
- **Cost**: $250
- **Purpose**: On-device AI inference

### Accessories
- **Components**: Power supplies, ethernet cables, microSD storage
- **Cost**: $170

### Total System Cost
- **One-time investment**: $672
- **Recurring fees**: $0

---

## XV. CONFERENCE-SPECIFIC ALIGNMENT

### ASIP 2025 Theme
- "Governance of Emerging Intelligent Technologies"

### Primary Sub-themes
1. **AI & Technology Applications**: Healthcare AI with governance principles embedded in design
2. **AI & Technology Ethics**: Privacy-preserving AI through edge computing

### Secondary Sub-themes
3. **AI & Technology Governance**: Privacy governance framework for healthcare AI

### Key Conference Keywords
- technology governance
- intelligent systems
- AI ethics
- policy implications
- innovation
- digital transformation
- healthcare applications
- privacy governance
- accessibility
- developing countries

---

**Last Updated**: Nov 14, 2025
**Usage**: Reference this file while writing to maintain consistent terminology and academic tone
