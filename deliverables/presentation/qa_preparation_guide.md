# Q&A Preparation Guide - ASIP 2025 Presentation

**Purpose**: Comprehensive preparation for audience questions during 10-minute Q&A session

**Strategy**: Organized by topic area with detailed answers, supporting evidence, and paper section references

---

## Topic Area 1: Privacy and Data Protection

### Q1: How do you ensure privacy with cameras in elderly homes?

**Short Answer** (30 seconds):
We build privacy into the system architecture, not just promise it through policy. The cameras capture video, but we only extract 17 skeletal body keypoints—like a stick figure. Then we immediately delete the video frame. The system never stores faces. You physically can't reconstruct someone's face from skeletal coordinates—the information doesn't exist in our data.

**Detailed Answer** (1 minute):
Three design choices enforce privacy. First, pose-only storage. We extract just 17 body joint positions—shoulders, elbows, hips, knees—and deliberately exclude face landmarks. Think of it like connect-the-dots for a skeleton. That's all we keep.

Second, immediate frame disposal. The camera captures a video frame, our software processes it to get those 17 points, then the frame gets deleted. Immediately. We don't store video footage at all.

Third, edge processing. All the computing happens on a small device in the home—the Jetson Orin Nano. Nothing gets sent to the internet. Zero cloud transmission. Your elderly parent's health data physically cannot leave the house.

This is privacy by design, not privacy by policy. Cloud-based systems like Kami Fall Detect Camera send video to company servers for processing. That creates facial recognition risks. Our architecture makes facial recognition impossible, not just prohibited. The difference? We're building privacy in from day one, not adding it later as an afterthought.

**Supporting Evidence**:

- 100% on-device processing (designed for edge deployment)
- Pose-only storage with immediate frame disposal
- Zero facial recognition capability by design
- No cloud subscription or data transmission

**Paper Reference**: Section 3.1 (Privacy Governance Architecture), Section 5.1 (Discussion - Governance Implications)

---

### Q2: Can families still identify their elderly relative from pose data?

**Short Answer** (20 seconds):
No. The pose data just shows where body joints are positioned—shoulders here, elbows there, knees here. It doesn't capture faces, clothing, skin tone, or anything that makes someone recognizable. Your grandmother's pose keypoints look the same as anyone else's—just a stick figure.

**Detailed Answer** (45 seconds):
The 17 keypoints are just coordinates. Shoulder position, elbow position, hip, knee, ankle—that's it. No facial features. No clothing. No hair color. No skin tone. Nothing that lets you identify who this person is.

Could you identify someone from how they move? Technically, maybe if you had a database of known movement patterns to compare against. But in a private home? There's no comparison database. No reference points. Just one elderly person's movement data with nothing to match it to.

Compare this to regular security cameras. You look at the video and immediately see grandma's face. With our system? You see numerical coordinates of joint positions. That's fundamentally different.

**Supporting Evidence**:

- COCO format: 17 body keypoints (no face landmarks)
- Cannot reconstruct facial features from pose data alone
- No visual characteristics stored (clothing, hair, skin tone)

**Paper Reference**: Section 3.1.1 (Privacy Governance Principles)

---

### Q3: What about data breaches or hacking? Could someone access the pose data remotely?

**Short Answer** (30 seconds):
Remote hacking is much harder with our setup. Why? The data never leaves the house. No internet transmission means no network to hack into. An attacker would need physical access—they'd have to break into the elderly person's home and physically touch the device. Even then, they'd only get pose coordinates, not faces or identifying information.

**Detailed Answer** (1 minute):
Think about how cloud systems get hacked. Data travels over the internet to company servers. Attackers can intercept the network connection, breach the servers, steal login credentials. Multiple attack points.

Our edge architecture? Data never touches the internet. All processing happens locally on the device in the home. Want to hack it? You need physical access to that specific house. That's a completely different security model.

Now, physical security still matters. If someone breaks into the home, could they steal the device? Yes. That's why we recommend standard protections: device encryption, secure boot settings, firmware updates, maybe a physical lock on the device.

But here's the key difference: if a cloud company gets breached, thousands of users get exposed simultaneously. With edge devices, an attacker has to break into each home individually. And even if they succeed? They get skeletal joint coordinates, not video footage with faces.

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
Yes, for our target demographic. We're talking about families earning $870 to $1,622 per month—that's Cambodia's fourth and fifth income quintiles. $672 is about half a month to a full month of income. It's significant, yes, but it's a one-time cost. Compare that to cloud systems costing $1,719 over three years with never-ending subscription fees.

**Detailed Answer** (1 minute):
Let's break down the economics. Middle-income Cambodian households earn $870 to $1,622 monthly according to Cambodia's Socio-Economic Survey. Our $672 system is roughly half a month to a full month of household income. That's not trivial, but think about it like buying a smartphone or major appliance—significant but manageable for this income bracket.

Now compare to cloud alternatives. Kami Fall Detect Camera: $99 hardware sounds cheap, but there's a mandatory $45 monthly subscription. Over three years? $1,719 total. That subscription is 5.2% of monthly income, every single month, forever.

Which is more affordable? Our one-time $672 payment, or paying $45 every month indefinitely? For long-term elderly monitoring—we're talking years, maybe decades—the zero-subscription model wins.

Now, I'll be honest: low-income families and rural elderly can't afford $672. That's a limitation we acknowledge in the paper. Those populations need government subsidies or different deployment models.

**Supporting Evidence**:

- Target market: $870-$1,622/month (4th-5th quintile)
- One-time cost: $672 = 0.5-0.8 months income
- Cloud alternative: $45/month = 5.2% of monthly income indefinitely
- 61% cost reduction over 3 years ($672 vs $1,719)

**Paper Reference**: Section 4.2 (Cost-Effectiveness Analysis), Section 5.1 (Accessibility Governance), Section 5.3 (Limitations)

---

### Q5: Why not use cheaper cameras or processors to reduce the $672 cost further?

**Short Answer** (30 seconds):
We already optimized for minimum cost. The Hikvision cameras are $63 each—that's budget-tier security cameras. Cheaper options sacrifice infrared quality or reliability. The Jetson Orin Nano at $250 is the cheapest edge processor that can handle real-time inference on four cameras simultaneously.

**Detailed Answer** (1 minute):
Let's talk about the cameras first. $63 per camera for the Hikvision model—these aren't premium cameras. They're budget commercial security cameras. Could we go cheaper? Sure, but you sacrifice something. Either the 850nm infrared quality degrades, or reliability drops, or you lose features like RTSP streaming that we need for multi-camera integration.

The Jetson Orin Nano processor? $250. That's the cheapest option that meets our performance needs. We need 20 frames per second processing four camera streams simultaneously. A Raspberry Pi 4 can't handle that—it chokes on the computational load. Higher-end Jetsons cost $400 to $2,000—total overkill for what we need.

The $170 in accessories aren't luxuries. microSD storage for the system. UPS backup so power outages don't kill the device. Ethernet cables. Camera mounts. These are necessary deployment components.

Look, we absolutely care about cost reduction for accessibility. But we can't sacrifice technical performance. Going cheaper means the system doesn't work. Further cost reduction needs component redesign or manufacturing at scale—that's beyond our research scope.

**Supporting Evidence**:

- Hikvision cameras: $63/unit (budget tier, not premium)
- Jetson Orin Nano: $250 (minimum spec for real-time multi-camera inference)
- Accessories: $170 (necessary deployment components)
- Alternative processors lack real-time performance capability

**Paper Reference**: Section 3.1.2 (Hardware Design for Cost-Effectiveness), Validation Results A4.2

---

### Q6: How does the breakeven point work? You said Month 13 of Year 2?

**Short Answer** (20 seconds):
Simple math. Our edge system: $672 upfront, done. Cloud system: $99 hardware, then $45 every month. After 12.7 months—basically month 1 of year two—the cloud user has paid $672 total. That's breakeven. After that? Cloud users keep paying $45 monthly. Edge users pay zero.

**Detailed Answer** (45 seconds):
Let me walk through the calculation. Edge cost is fixed: $672. Cloud cost grows every month: $99 hardware plus $45 times however many months. When do they equal each other? $672 equals $99 plus 45 times M. Solve for M: that's 12.7 months.

After breakeven, the gap widens. At three years, cloud users have paid $1,719 total. Edge users? Still $672. Year four? Cloud users add another $540. Year five? Another $540. It never stops.

For elderly monitoring, we're talking years, maybe decades of use. The lifetime savings with zero subscription is massive.

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
Yes. We tested MediaPipe pose detection on 20 infrared security camera videos—real nighttime footage, complete darkness, just 850nm infrared illumination. Detection rate: 91.3%. That confirms 24/7 monitoring works without visible light and without facial recognition technology.

**Detailed Answer** (1 minute):
We collected 20 commercial security camera videos—publicly available CCTV demo footage. These included complete darkness scenarios. The cameras use only infrared illumination at 850nm wavelength, no visible light.

Here's what's interesting: MediaPipe was originally trained on regular color images in daylight. We're testing it on infrared footage in darkness. Does it work? Yes. 91.3% keypoint detection rate. Average confidence: 0.868. That means detecting about 30 out of 33 body landmarks per frame.

Now, performance varied across videos. Some cameras hit 98.9% detection. Others dropped to 73.8%. Depends on camera quality, environment, subject position. The 91.3% is the average across all 20.

Why does this matter? Very little research has actually tested whether pose detection works on the specific infrared wavelength used in affordable security cameras. We're showing it does. This enables 24/7 privacy-preserving monitoring—you get pose data in complete darkness without needing facial recognition.

**Supporting Evidence**:

- 91.3% keypoint detection on 850nm IR footage
- 20 diverse commercial CCTV videos (multiple manufacturers, environments)
- 0.868 average confidence
- Range: 73.8%-98.9% across individual videos

**Paper Reference**: Section 4.1 (NIR Camera Compatibility), Validation Results A1.2a, A1.2c

---

### Q8: What's the false negative rate? How often does it miss detecting a person?

**Short Answer** (20 seconds):
12.3% false negative rate. That means in about 1 out of 8 frames where a person is actually there, the system fails to detect their pose. The other 87.7% of frames? It successfully detects the person.

**Detailed Answer** (1 minute):
False negatives happen when someone is in the camera view but the system misses them. Our integrated pipeline: 12.3% false negative rate across 20 infrared test videos.

Why do false negatives happen? Several reasons. Severe occlusion—body parts blocked by furniture. Extreme poses like lying flat facing away from the camera. Sometimes even with infrared, lighting is poor. Or the person is too far from the camera. These are general computer vision challenges, not unique to our system.

For safety-critical applications like fall detection, false negatives are the scary ones. Missing a fall could be fatal. That's why we chose the integrated pipeline with YOLOv8n person detection first, even though it's 2.3 times slower. It improved detection from 86.1% to 91.3%—reducing false negatives was worth the speed tradeoff.

Important clarification: this 12.3% is for pose detection on infrared footage, not fall detection accuracy. We haven't validated actual fall detection yet—that requires testing on benchmark datasets, which is future work.

**Supporting Evidence**:

- 12.3% false negative rate (integrated pipeline on NIR footage)
- Factors: occlusion, extreme poses, lighting, distance
- Integrated pipeline selected to minimize false negatives
- Validation scope: pose detection, NOT fall detection

**Paper Reference**: Section 4.1 (NIR Camera Compatibility), Validation Results A1.2a

---

### Q9: Why did you choose the slower integrated pipeline instead of the faster baseline?

**Short Answer** (30 seconds):
Because accuracy matters more than speed for safety. The integrated pipeline is 2.3 times slower, yes. But it's 5.7% more accurate at detecting keypoints and 22.2% better at pose coverage. Missing a fall could be fatal. Both pipelines run faster than our 15 frames per second target anyway, so we chose the more accurate one.

**Detailed Answer** (1 minute):
We tested both. Baseline MediaPipe: 86.1% keypoint detection, super fast at 47 frames per second. Integrated with YOLO first: 91.3% detection, 96.9% pose coverage, but only 20.53 FPS. Trade-off: more accurate but 2.3 times slower.

Why pick the slower one? Because this is safety-critical. In elderly monitoring, a false negative—missing a fall—could mean delayed emergency response, serious injury, death. Speed is nice. Accuracy keeps people alive.

Here's the key point: both pipelines exceed our real-time target of 15 frames per second. The integrated pipeline at 20.53 FPS is already 37% faster than we need. Going from 20 to 47 FPS doesn't improve safety outcomes—the system already responds in real-time.

This shows a governance principle: don't optimize technical metrics in isolation. Evaluate performance against what actually matters. In healthcare applications where lives are at stake, we optimize for accuracy first.

**Supporting Evidence**:

- Integrated: 91.3% detection, 96.9% coverage, 20.53 FPS
- Baseline: 86.1% detection, 79.5% coverage, 47.37 FPS
- Target: 15 FPS (both exceed real-time requirements)
- Safety-critical priority: accuracy > speed

**Paper Reference**: Section 4.1 (NIR Camera Compatibility), Section 5.2 (Technical Validation Contributions), Validation Results A1.3

---

### Q10: Have you tested this on actual Jetson Orin Nano hardware?

**Short Answer** (15 seconds):
Not yet. That 20.53 frames per second number? Measured on standard development hardware. The Jetson Orin Nano is our target device, but we haven't deployed on it yet. It's a limitation we acknowledge in the paper.

**Detailed Answer** (45 seconds):
Here's what we know. Literature shows Jetson Orin Nano handles YOLOv8n and MediaPipe individually at real-time speeds—8 gigabytes of RAM, over a thousand CUDA cores, purpose-built for edge AI. So the specs look good.

But have we tested our specific pipeline on actual Jetson hardware? No. Real-world performance might differ. Memory bandwidth when processing four camera streams simultaneously. Thermal throttling after hours of continuous operation. These are unknowns until we deploy.

That's future work—explicitly listed in Section 5.3. The 20.53 FPS result tells us it's likely feasible, but hardware validation is required before we can confidently say "this will work in production."

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
You're right—the scope is focused. We validated three things: NIR camera compatibility with pose detection, cost-effectiveness compared to cloud systems, and privacy architecture. We did NOT validate fall detection accuracy. This is a design study showing privacy governance can drive architecture. Fall detection testing on benchmark datasets like MCF and LE2I—that's future work.

**Detailed Answer** (1 minute):
Let me be clear about what we did and didn't do. What we validated: Can MediaPipe extract poses from 850 nanometer infrared footage? Yes—91.3% keypoint detection across 20 commercial security camera videos. Is edge computing cheaper than cloud? Yes—$672 versus $1,719 over three years, 61% savings. Does pose-only storage eliminate facial data by design? Yes—no faces stored, physically can't reconstruct identity.

What we didn't validate: Fall detection accuracy on benchmark datasets. Real-world deployment in elderly homes. User acceptance studies with actual elderly participants and their families.

This limitation is intentional. Our research question asks: how do privacy governance principles inform architectural design in resource-constrained contexts? We're showing the foundation works—technically feasible, economically viable. Building on that foundation to validate detection accuracy comes next. We're not claiming a complete system. We're demonstrating the governance-driven approach is worth pursuing.

**Supporting Evidence**:

- Validated: NIR compatibility (91.3%), cost-effectiveness (61% savings), privacy architecture
- Not validated: Fall detection accuracy, real-world deployment, user acceptance
- Research type: Design study with technical feasibility validation
- Future work: Benchmark dataset testing, hardware validation, user studies

**Paper Reference**: Section 3.5 (Study Scope and Limitations), Section 5.3 (Limitations)

---

### Q12: Why didn't you test on benchmark fall detection datasets like MCF or LE2I?

**Short Answer** (20 seconds):
Time and scope. Testing on MCF, LE2I, UP-Fall datasets means downloading hundreds of videos, implementing the full classification module, training deep learning models, running cross-validation. That's months of work beyond the ASIP timeline. We focused on validating the architecture first—feasibility before accuracy.

**Detailed Answer** (1 minute):
Here's our strategy. Phase one: validate the foundation. Can we do privacy-preserving pose detection on infrared cameras? Yes. Is edge computing economically viable? Yes. That's what we completed for ASIP.

Phase two: validate detection accuracy. Train the CNN+LSTM+Transformer module on MCF—192 fall videos. Test on LE2I—191 videos. Benchmark against baseline methods. Calculate precision, recall, F1 scores. That's the next research phase.

Why split it? Because there's no point spending months optimizing fall detection algorithms if the foundational architecture doesn't work. What if NIR cameras couldn't extract poses? What if edge processing cost twice as much as cloud? We'd have wasted time on the wrong approach.

Methodologically, it's sound: establish feasibility first, then build accuracy validation on that foundation. And ASIP's focus is technology governance—the architecture story fits perfectly. Full system validation? That's for a healthcare informatics journal later.

**Supporting Evidence**:

- Benchmark datasets identified: MCF, LE2I, UP-Fall
- Future work: Fall detection accuracy validation
- Phased research strategy: feasibility first, then accuracy
- Conference focus: governance contribution, not complete system

**Paper Reference**: Section 5.4 (Future Directions), Section 3.5 (Study Scope and Limitations)

---

### Q13: How did you ensure the 20 CCTV videos represent real elderly monitoring scenarios?

**Short Answer** (25 seconds):
Honestly? We didn't. That's a limitation we acknowledge. The 20 videos are commercial security camera demo footage—Hikvision, EZviz, different camera types. Not elderly subjects. This validates that 850 nanometer infrared works with pose detection generally. Elderly-specific performance? That requires different validation.

**Detailed Answer** (1 minute):
The subjects in those videos are not elderly people. And elderly individuals have distinct characteristics—altered gait, slower movement, different body proportions. Someone using a walker. Postural changes from arthritis. Our validation tells us MediaPipe can extract poses from NIR footage. It doesn't tell us how well it performs on elderly-specific movement patterns.

We're explicit about this in Section 5.3. It's not hidden. Future work includes collecting a custom CamTech dataset—180 videos using age-appropriate actors simulating different scenarios across three lighting conditions. That will address elderly-specific validation.

Think of it as building blocks. Step one: confirm the wavelength works—850nm infrared compatible with pose detection software. Step two: test on elderly-representative subjects. We've completed step one. Step two requires filming with actual elderly participants or age-appropriate actors, which involves ethics approval, recruitment, controlled scenarios. Different research phase.

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
We're operationalizing their principles. GDPR says "minimize data and protect privacy"—we do that through pose-only storage and edge processing. UNESCO says "transparency and human rights"—we eliminate surveillance capability by design. They set the principles. We show how to implement them in affordable healthcare AI.

**Detailed Answer** (1 minute):
Think of it this way: governance frameworks tell you what to do. We show you how.

GDPR mandates three things for healthcare AI. Data minimization—we store 17 body keypoints instead of full video. Data controllership—edge processing means families own their data, not cloud companies. Right to erasure—we delete raw frames immediately, architecturally enforced.

UNESCO AI Ethics emphasizes transparency and human rights. Our system is transparent—families know exactly what's captured: skeletal poses, not faces. Human rights to privacy and freedom from surveillance—protected because we physically can't do facial recognition. The capability doesn't exist.

Here's the contribution. Burns' 2024 paper talks about edge computing for privacy but doesn't quantify costs. Birkstedt and colleagues note that translating ethical principles into practice lacks guidance. We bridge that gap—showing privacy governance principles drive specific architecture with measurable outcomes: 61% cost reduction, 91% pose detection, zero cloud transmission.

**Supporting Evidence**:

- GDPR compliance: data minimization, controllership, right to erasure
- UNESCO ethics: transparency, human rights, privacy protection
- Implementation focus: principles → architecture → measurable outcomes
- Cost-effectiveness quantification: 61% reduction, market reach data

**Paper Reference**: Section 2.3 (Technology Governance Frameworks), Section 5.1 (Governance Implications)

---

### Q15: Can this governance model scale to other healthcare AI applications beyond elderly monitoring?

**Short Answer** (25 seconds):
Yes. The principles—edge processing, data minimization, immediate raw data disposal—apply to any healthcare AI needing privacy and affordability. Diabetes monitoring, rehabilitation tracking, mental health apps. The governance approach scales. Implementation details need adaptation for each domain.

**Detailed Answer** (1 minute):
The architecture transfers. Edge-first processing works for any sensitive health data. Data minimization—extract only what's clinically necessary, discard identifying features—applies broadly. Immediate raw data disposal eliminates re-identification universally.

Concrete examples. Diabetes monitoring: extract blood glucose trends, discard device identifiers. Rehabilitation tracking: capture joint range-of-motion from video, delete faces. Mental health apps: analyze speech patterns for depression indicators, protect voice identity.

The economic benefits scale too. Eliminating cloud subscriptions matters for any long-term monitoring where recurring costs block access—chronic disease management in developing countries requiring years of sustained monitoring.

But here's the caveat: technical feasibility varies. Real-time requirements differ. Sensor types differ. Computational complexity differs. The governance approach—privacy-first, cost-conscious design—scales. How you implement it? That needs domain-specific work.

**Supporting Evidence**:

- Generalizable principles: edge processing, data minimization, raw data disposal
- Example applications: diabetes, rehabilitation, mental health monitoring
- Economic benefits: subscription elimination for long-term monitoring
- Domain-specific adaptation required for technical implementation

**Paper Reference**: Section 5.1 (Governance Implications), Discussion of accessibility governance

---

### Q16: What policy recommendations would you make for developing countries adopting healthcare AI?

**Short Answer** (30 seconds):
Three main ones. First: require privacy-by-design in AI procurement—mandate edge processing or equivalent. Second: evaluate total cost of ownership, not just upfront prices. That $99 camera becomes $1,719 over three years with subscriptions. Third: encourage context-specific design using regional data, not just importing Western solutions.

**Detailed Answer** (1+ minutes):
First: make privacy architectural, not just policy. Government procurement for healthcare AI should mandate specific mechanisms—data locality through edge processing, data minimization with technical verification, transparency about what's stored. Shift privacy from "we promise to protect your data" to "we can't access your data by design."

Second: total cost of ownership. Cloud systems look cheap upfront—$99 hardware. But that $45 monthly subscription adds up to $1,719 over three years. Developing country procurement policies should standardize multi-year cost analysis and prioritize zero-subscription models for affordability.

Third: context-specific innovation. We designed for Cambodia's economic realities—middle-income households, $870 to $1,622 monthly income. Not a generic solution copy-pasted from Western markets. Policies should incentivize using local evidence, targeting regional income brackets, adapting to cultural preferences like home-based elderly care in Southeast Asia.

I'd add a fourth: invest in local research capacity. Don't just import foreign technologies. Our NIR validation, cost analysis—that's locally-generated evidence appropriate for Cambodia. Supporting regional research institutions builds sustainable innovation ecosystems.

**Supporting Evidence**:

- Privacy-by-design procurement requirements
- Total cost of ownership analysis (multi-year subscriptions)
- Context-specific design using regional evidence
- Local research capacity investment

**Paper Reference**: Section 5.1 (Governance Implications), Section 6.2 (Implications for Practice)

---

## Topic Area 6: Regional Context and Scalability

### Q17: Why focus on Cambodia specifically? Can this work in other countries?

**Short Answer** (25 seconds):
Cambodia is our case study. 1.8 million elderly by 2030. Middle-income households earning $870 to $1,622 monthly. Home-based care cultural norms. Those specifics shaped our design. Could it work elsewhere? The approach could transfer to similar contexts—aging populations, cost sensitivity. But you'd need to adapt the specifics.

**Detailed Answer** (1 minute):
We designed for Cambodia's realities. Income data from Cambodia's Socio-Economic Survey—middle-income households earn $870 to $1,622 per month. Aging-in-place cultural norms rooted in filial piety. A $45 monthly cloud subscription? That's 5.2% of monthly income indefinitely. Not sustainable.

Can this work in other countries? The governance-driven approach—edge processing for privacy and cost—could transfer to similar contexts. But you'd need to localize it. Income thresholds differ. Infrastructure varies—internet reliability, electricity stability. Cultural norms about elderly care aren't universal.

Think of Cambodia as proof-of-concept. We're showing privacy-first architecture can work in resource-constrained settings when you design for local context. Other countries would validate using their own economic data, infrastructure realities, cultural factors. We're not saying "copy this everywhere." We're showing the methodology: how to design context-specific solutions driven by governance principles.

**Supporting Evidence**:

- Cambodia context: 1.8M elderly, $870-$1,622/month target market, home-based care norms
- Transferable approach: Edge processing, cost optimization methodology
- Localization required: Income thresholds, infrastructure assumptions, cultural factors
- Proof-of-concept for resource-constrained contexts

**Paper Reference**: Section 5.1 (Context-Specific Design), Section 2.4 (Regional Context: Southeast Asian Elderly Care)

---

## Topic Area 7: Practical Implementation

### Q19: When will this system be available for actual deployment in Cambodian homes?

**Short Answer** (20 seconds):
Not immediately. This is early-stage research. Before deployment: validate fall detection on benchmark datasets, test on actual Jetson hardware, conduct user studies with elderly participants, develop installation procedures. Pilot deployments? Maybe 12 to 18 months. Commercial? Two to three years.

**Detailed Answer** (1 minute):
Here's the roadmap. Immediate next steps: validate fall detection accuracy on MCF, LE2I, UP-Fall benchmark datasets. Deploy on actual Jetson Orin Nano hardware to confirm it handles four camera streams in real-time. Collect custom CamTech dataset—180 videos with age-appropriate actors for elderly-specific validation.

After technical validation: user acceptance studies. Interview elderly participants and family caregivers. Usability testing. Longitudinal monitoring—do families actually use this over time, or does it sit unplugged after a week? Privacy concerns, alert mechanisms, caregiver response protocols—all need empirical investigation.

Practical deployment challenges: installation procedures for camera positioning, network configuration, caregiver training, maintenance for firmware updates, customer support infrastructure.

Realistically? Pilot deployments in 10 to 20 Cambodian households—12 to 18 months after benchmark validation succeeds. Commercial availability requires regulatory approval, manufacturing partnerships, distribution channels—two to three years.

**Supporting Evidence**:

- Immediate: Benchmark validation, Jetson testing, custom dataset
- Mid-term: User acceptance studies, pilot deployments
- Long-term: Regulatory approval, commercial production
- Timeline estimate: Pilots 12-18 months, commercial 2-3 years

**Paper Reference**: Section 5.4 (Future Directions), Section 5.3 (Limitations - deployment not validated)

---

### Q20: How would installation work? Can families install this themselves or does it require professionals?

**Short Answer** (20 seconds):
Professional installation recommended. Four cameras at 90-degree spacing, 2.5 to 3 meters height, network configuration, Jetson calibration. Similar complexity to security camera installation—technically skilled users could do it, but professionals ensure optimal performance. We budget installation in that $170 accessories cost.

**Detailed Answer** (45 seconds):
Installation steps: mount four cameras at 90-degree spacing for 360-degree coverage. Height matters—typically 2.5 to 3 meters for optimal pose detection angles. Run Ethernet cables to the central Jetson device—wired preferred for reliability. Configure network settings and RTSP streaming. Calibrate pose estimation for each camera's field of view. Test for blind spots.

Professional installers with security camera experience? Two to three hours. Technically proficient families could self-install with detailed guides. But here's the thing: camera positioning significantly impacts detection performance. Poor placement creates coverage gaps that miss falls.

The $170 accessories budget includes installation. We're exploring subsidized professional installation through partnerships—local security companies or NGOs—to support wider adoption.

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

# Other Q&A

Q: In your slide, there are 4 cameras tediously placed around a small bedroom, why?

- 4 cameras are useful when the room is large or highly occluded. For simple room layouts, 1 or 2 cameras will be enough.

Q: Why is Hikvision DS-2CD1343G2-IUF chosen?

- (answer)

Q: Why is NVIDIA Jetson Orin Nano Chosen?

- (answer)
