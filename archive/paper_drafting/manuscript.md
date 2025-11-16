## Introduction

This file mimics a manuscript of a researcher, writing for a 15-year-old child to understand the project. Strictly follow the prompts below to create the manuscript:

```plaintext
ok so basically write this like how i actually text and talk irl. dont make it perfect cuz nobody writes perfect when their just typing stuff out. sometimes i forget punctuation and sometimes i use it wrong but who cares lol. make sure you:

- mess up your/you're and their/there sometimes but not everytime cuz that would be obvious
- use filler words like "like" and "basically" and "kinda" way too much
- randomly capitalize stuff for EMPHASIS or when your excited about something
- forget apostrophes in contractions sometimes (dont, wont, cant)
- use run on sentences cuz thats how teenagers actually think like one thought just flows into another thought and we dont really stop to put periods
- throw in some "tbh" and "ngl" and "lowkey/highkey" but dont overdo it
- sometimes just trail off with... or use multiple question marks???
- spell things wrong occasionally but the way autocorrect would miss them (teh, adn, etc)
- reference stuff without explaining it fully cuz you assume everyone knows what your talking about
- change topics suddenly without good transitions
- use informal logic like "this is dumb because its literally so stupid"
```

## My Informal Research Manuscript

<!-- Add the menu script below this line. -->

### 1. Introduction

ok so basically the whole world is getting old right like theres gonna be SO many elderly people everywhere and this is kinda a big problem because old people fall and hurt themselves ALL THE TIME. like literally falls are the number one cause of injury deaths for elderly people which is honestly really scary when you think about it.

in cambodia specifically were gonna have like 1.8 million elderly people by 2030 which is pretty soon tbh. and the thing is these middle income families they want to take care of their grandparents but its really hard when everyone has to work and stuff so they need some kind of monitoring system.

but heres where it gets complicated... all the existing fall detection systems have MAJOR problems with privacy and cost. like the cloud based ones they literally send video of your grandma to some company's servers which is super creepy if you think about it?? like imagine some random people could potentially see footage of elderly people in there homes doing private stuff. thats basically a huge privacy concern that nobody really talks about enough.

and even worse these cloud systems cost like $640 EVERY YEAR for the subscription which is insane. middle income families in cambodia cant afford that kind of recurring payment burden when their making like $870-1622 per month. like do the math... thats almost a whole months salary just for one year of monitoring.

also the whole AI governance situation is kinda a mess right now. like everyone talks about AI ethics and governance frameworks but its all super fragmented and nobody really shows how to actually IMPLEMENT these governance principles in real systems especially in developing countries where theres not a lot of resources.

so basically the research gap is this: existing elderly monitoring solutions they either do privacy OR affordability OR good performance but like never all three together. and nobody really demonstrates how you can use privacy governance principles to actually DRIVE your architectural design decisions from the very beginning instead of just adding privacy stuff later as an afterthought.

what we wanna do is show that edge computing can be used for privacy governance in healthcare AI for places like cambodia that dont have tons of money.

our research objectives are basically:

1. demonstrate how privacy governance can drive the architectural design from day one
2. validate that this privacy preserving edge architecture actually WORKS with NIR cameras (the cheap security cameras that work at night)
3. prove that the edge based approach is way more cost effective for middle income cambodian households

like if we can show that privacy first design actually SAVES money while also being better for privacy then thats a huge deal for policymakers and developers right???

### 2. Literature Review

ok so lemme break down what other people have done and why its not quite enough...

#### 2.1 elderly safety monitoring tech

so theres like a bunch of different approaches people have tried:

**wearable devices** - these are things like fall detection watches or pendants. the problem is old people forget to wear them or they dont charge them or whatever. like my grandma would definitely lose hers lol. compliance is just really bad with wearables.

**cloud based camera systems** - these ones they record video and send it to the cloud for processing. privacy concerns are MASSIVE here because your literally sending footage of peoples homes to third party servers. and also you need subscriptions which we already talked about being expensive.

**depth sensors** - like those 3D cameras that can see how far away things are. these are better for privacy than RGB cameras but their super expensive and kinda overkill for what we need??

**ambient sensors** - like motion sensors and door sensors and stuff. these are ok for privacy but they cant really tell you WHAT happened just that something happened somewhere which isnt that useful for detecting specific incidents.

so basically everyone prioritizes either privacy (depth cameras, federated learning) or affordability (cloud systems) or performance (fancy RGB-D sensors) but never all three as integrated design goals.

#### 2.2 privacy preserving AI stuff

theres a few different technical approaches people use for privacy:

**federated learning** - this is where you train models on different peoples data without sending the raw data anywhere. but it still requires cloud infrastructure to coordinate everything which costs money and has its own privacy risks.

**differential privacy** - you add noise to the data to protect individual privacy. but this makes your model less accurate which is bad for safety critical applications like fall detection where missing an incident could literally kill someone.

**edge computing** - processing data on local devices instead of the cloud. this gives you data locality benefits because the data never leaves the house. this is what were doing basically.

**privacy by design** - this is more of a philosophy where you build privacy into the architecture from the start. people talk about it alot but not many actually show HOW to do it in practice.

#### 2.3 technology governance frameworks

so theres all these AI ethics guidelines about transparency and accountability and fairness and explainability. and theres data protection regulations like GDPR in europe that say you have to keep data in certain places and get consent and stuff.

healthcare has its own privacy standards like HIPAA in the US. and theres all this stuff about accessibility and digital inclusion making sure technology doesnt just work for rich people.

but like heres the thing... all these governance frameworks remain nascent and fragmented. like nobody really connects them together or shows how to actually implement them in resource constrained contexts like cambodia. its all very theoretical and not practical enough.

the key gap is that governance principles are usually retrofitted post hoc instead of driving the technical decisions from inception. like people build the system first and THEN try to make it comply with regulations which is backwards.

#### 2.4 regional context for southeast asia

so for cambodia and southeast asia specifically theres some epidemiological evidence about fall incidents. like in thailand 37.7% of elderly home accidents are falls which is really high.

culturally theres strong family caregiving norms so people want to take care of elderly relatives at home not in facilities. but that means you need monitoring solutions that work in homes.

economically theres major constraints on affordability. technology adoption patterns show that people will use tech if its affordable and actually solves their problems.

the thing is most research uses western datasets and western contexts so we dont really know if the same solutions work in southeast asia. thats why we need context specific design for developing countries.

### 3. Methodology

ok so now lemme explain what we actually DID...

#### 3.1 privacy governance architecture

basically we designed this system where privacy governance principles actually DRIVE the technical architecture. like we didnt just build a system and then add privacy we designed it privacy first from day one.

**3.1.1 privacy governance principles**

we have three main mechanisms that enforce privacy by design:

1. **pose only storage** - the system only keeps 17 body keypoints in COCO format. we exclude all the face landmarks so theres no way to do facial recognition. like the raw video frames never get saved to storage ever.

2. **immediate frame disposal** - video frames get processed in real time and then deleted immediately after keypoint extraction. so theres zero video retention which means no re identification risk because theres nothing to re identify from.

3. **edge first processing** - ALL computation happens on the local device which is an NVIDIA Jetson Orin Nano with 8GB ram. zero cloud transmission means no network exposure and no data sovereignty concerns because the data literally never leaves your house.

this is architectural enforcement not just operational promises. like we make it IMPOSSIBLE to violate privacy through the design itself not through policies that people could ignore.

**3.1.2 hardware design for cost effectiveness**

we picked hardware specifically to target middle income cambodian households:

- **cameras**: RGB cameras with 850nm IR night vision. the specific model is Hikvision DS-2CD1343G2-IUF which costs $63 per camera. we use 4 cameras in 90 degree spacing to get 360 degree coverage.

- **edge processor**: NVIDIA Jetson Orin Nano 8GB costs $250. this does all the AI processing locally.

- **total system cost**: $672 one time payment with zero recurring fees. this is WAY cheaper than cloud alternatives over time.

the whole point is cost optimization while maintaining privacy and performance. accessibility governance through smart hardware choices basically.

**3.1.3 software pipeline**

our processing pipeline has a few steps:

1. **person detection**: YOLOv8n (the nano version which is super lightweight) identifies where the person is in the frame with a bounding box

2. **pose estimation**: MediaPipe extracts 33 skeletal landmarks from the image. but we only use 17 body keypoints and exclude face landmarks for privacy.

3. **processing modes**: we tested two versions - baseline which is just MediaPipe on the full frame, and integrated which is YOLO first to find the person then MediaPipe on just that region of interest.

#### 3.2 NIR camera compatibility validation

so the big question is does MediaPipe even WORK on infrared footage??? because most AI models are trained on regular RGB images not IR.

**3.2.1 validation dataset**

we tested MediaPipe on 20 commercial 850nm NIR security camera videos:

- **source**: professional CCTV demo footage that you can find online (publicly available)
- **diversity**: indoor and outdoor environments, different camera manufacturers like Hikvision and EZviz, dome cameras and turret cameras and bullet cameras, various lighting conditions
- **resolution**: 1080p and 4K videos
- **purpose**: validate pose estimation performance on 850nm NIR wavelength which is what our target cameras use

the whole point is to test on REAL commercial hardware not expensive research equipment. like we need to know if cheap $63 security cameras actually work for this.

**3.2.2 validation procedure**

we tested two pipelines on the same 20 videos:

1. **baseline**: just run MediaPipe pose estimation on the full frame
2. **integrated**: use YOLOv8n to detect the person first, crop to that ROI, then run MediaPipe on just the cropped region

for metrics we collected:

- keypoint detection rate (how many of the 33 landmarks did it detect)
- confidence scores (how sure is the model)
- false negative rate (frames where theres a person but pose detection failed)
- processing speed in FPS

**3.2.3 validation scope**

IMPORTANT: this validation tests NIR camera compatibility NOT fall detection accuracy. like were just confirming that pose estimation works on IR footage from affordable security cameras. were not testing if it can actually detect falls accurately thats a different thing that needs benchmark datasets.

#### 3.3 cost effectiveness analysis

**3.3.1 comparative cost model**

we compared our edge system to a cloud based alternative called Kami Fall Detect Camera over 3 years:

- **edge system**: $672 one time (hardware only) plus zero recurring fees forever
- **cloud system**: $99 for hardware plus mandatory subscription of $45 per month times 36 months

the question is like when does the edge system pay for itself basically.

**3.3.2 market accessibility analysis**

we used cambodia socio economic survey data to figure out who can actually afford this:

- **income brackets**: CSES has quintile data that divides people into five groups by income
- **target segment**: middle income urban households which is the 4th and 5th quintile making $870-1622 per month
- **market reach calculation**: we figured out what percentage of monthly income the system costs and then estimated how many elderly people are in households that can afford it

this tells us like how many people can we actually REACH with this system which is important for accessibility governance.

#### 3.4 evaluation metrics

for NIR camera compatibility:

- keypoint detection rate (33 landmarks per frame)
- pose detection confidence scores
- false negative rate (person present but pose failed)
- processing speed (FPS)

for cost effectiveness:

- total 3 year cost (edge vs cloud)
- breakeven point (how many months until savings exceed initial cost)
- market reach (percentage of elderly population)
- affordability threshold (cost vs monthly income)

#### 3.5 study scope and limitations

ok so lets be really clear about what we DID validate and what we DIDNT:

**what we validated:**

- NIR camera compatibility: yes MediaPipe works on 850nm IR footage (91.3% keypoint detection on 20 commercial videos)
- cost effectiveness: yes edge is way cheaper than cloud ($672 vs $1719 over 3 years which is 61% savings)
- privacy architecture: yes the design eliminates facial data (only 17 body keypoints stored, frames deleted immediately)

**what we did NOT validate:**

- fall detection accuracy: this needs benchmark datasets like MCF and LE2I and UP-Fall which we didnt test yet
- real world deployment: we havent actually installed this in elderly peoples homes yet
- user acceptance: we didnt do longitudinal studies with actual users thats future work

**why these limitations:**
this is a design study showing how privacy governance principles can inform architectural decisions. we validate technical feasibility of the privacy first approach but not the complete fall detection system. like were proving the foundation works before building the whole thing.

### 4. Results

ok so what did we actually FIND???

#### 4.1 NIR camera compatibility

we ran MediaPipe on 20 commercial 850nm NIR security camera videos from different manufacturers and environments and heres what happened:

- **keypoint detection rate**: 91.3% which means it detected 30.1 out of 33 landmarks on average. thats actually pretty good tbh.

- **average confidence**: 0.868 on a scale of 0 to 1. so the model is like 87% sure about its predictions which is solid.

- **false negative rate**: 12.3% which means in 12.3% of frames that had a person in them the pose detection completely failed. this is kinda high but not terrible for safety critical applications.

- **processing speed**: 20.53 FPS with the integrated YOLO plus MediaPipe pipeline. this is above the 15 FPS threshold for real time so were good.

now the interesting thing is we compared baseline (just MediaPipe) versus integrated (YOLO then MediaPipe):

the integrated approach got 5.7% higher keypoint detection and 22.2% better pose coverage which is great. BUT it was 2.3 times slower (20.53 FPS vs 47.37 FPS for baseline).

we chose the integrated pipeline anyway because for safety critical applications accuracy matters more than speed when both are still real time. like if you miss a fall detection someone could literally die so we prioritize accuracy over speed when both meet the minimum requirements.

the keypoint detection rate actually varied alot across videos from 73.8% to 98.9% depending on the camera type and environment. indoor videos with good IR illumination did way better than outdoor videos with ambient light interference. different manufacturers also had different performance which is kinda interesting.

#### 4.2 cost effectiveness analysis

ok so we compared costs over 3 years:

**edge based system costs:**

- $252 for cameras (4 cameras at $63 each)
- $250 for NVIDIA Jetson Orin Nano 8GB
- $170 for accessories (power supplies, cables, storage)
- **total: $672 one time payment**
- **recurring fees: $0**

**cloud based alternative costs (Kami Fall Detect Camera):**

- $99 for hardware
- $45 per month subscription
- $45 × 36 months = $1620 in subscription fees
- **total: $1719 over 3 years**

**cost savings:**

- edge system saves $1047 over 3 years
- thats a 61% cost reduction which is MASSIVE
- breakeven point is month 1 of year 2 (month 13) so you start saving money after just over a year

**market accessibility:**
we used cambodia socio economic survey data and found that middle income urban households (4th and 5th quintile) make $870-1622 per month.

for these households the edge system costs about 41-77% of one months income which is affordable as a one time investment. but the cloud system would cost 5.2% of monthly income EVERY MONTH FOREVER which adds up to 187% of a months income over 3 years. thats insane.

estimated market reach: 12-18% of elderly population which is 216,000 to 324,000 individuals by 2030.

the zero subscription model is key here because it eliminates ongoing payment burden. like paying $672 once is way more accessible than paying $45 every single month especially for middle income families that have variable income.

compared to cloud alternatives that reach less than 5% of elderly population (because of recurring costs), our system expands accessibility by 2-3x.

### 5. Discussion

ok so what does all this actually MEAN???

#### 5.1 governance implications

**privacy governance through edge architecture:**

so here's the big thing... we demonstrated how privacy governance principles can actually DRIVE architectural design decisions instead of being added later.

the edge based processing eliminates cloud transmission requirements completely. this enforces data locality through system constraints not through operational promises. like its not that we PROMISE not to send data to the cloud its that the system CANT send data to the cloud because theres no cloud component at all.

we achieve facial anonymity by design not by policy. pose only storage makes facial recognition literally impossible not just prohibited. like even if someone wanted to identify people from the data they CANT because the face information just doesnt exist.

our validation results (91.3% keypoint detection on 850nm NIR footage) confirm that this privacy first design works without compromising performance. so you dont have to sacrifice privacy for functionality which is what people usually assume.

**accessibility governance through cost optimization:**

the cool thing is edge architecture has economic co benefits beyond just privacy. eliminating cloud infrastructure reduces total cost by 61% ($672 vs $1719 over 3 years) which expands market accessibility way beyond cloud dependent alternatives.

the zero subscription model removes recurring payment barriers. for middle income cambodian households (4th-5th quintile making $870-1622 per month) a one time $672 payment is achievable but $45 every month forever is not sustainable.

estimated reach is 216,000-324,000 elderly individuals (12-18% of population by 2030) compared to under 5% for cloud alternatives. so privacy governance directly enables accessibility governance which is pretty neat.

**context specific design for developing countries:**

our system design incorporates regional epidemiological evidence. we prioritized three incident types based on thai elderly fall data (37.7% prevalence) and chinese long term care studies.

hardware selection (850nm NIR cameras, edge processor) addresses cambodias middle income market constraints while maintaining technical performance. this demonstrates how governance driven design can work for resource constrained contexts not just wealthy countries.

#### 5.2 technical validation contributions

**NIR camera compatibility for privacy preserving monitoring:**

we validated MediaPipe pose estimation on 850nm NIR footage (91.3% keypoint detection across 20 diverse commercial CCTV videos). this confirms you can do 24/7 elderly monitoring without facial recognition technology.

before this study there wasnt really empirical validation of pose estimation on NIR wavelengths used in affordable security cameras. like people assumed it would work but nobody tested it systematically.

the range of 73.8%-98.9% across videos shows that camera selection and environment setup really matter. you cant just buy any random IR camera and expect it to work perfectly.

**pipeline trade off analysis for safety critical systems:**

comparing baseline versus integrated YOLO+MediaPipe revealed this accuracy speed trade off: integrated gets 5.7% higher detection and 22.2% better coverage but its 2.3 times slower.

for safety critical applications where missing a fall detection has fatal consequences we should prioritize accuracy over speed when both still meet real time requirements. this is different from like video games where you want maximum FPS.

both configurations exceed 15 FPS real time threshold (20.53 FPS and 47.37 FPS) so we can afford to choose the more accurate one. this kind of trade off analysis is important for healthcare AI design decisions.

#### 5.3 limitations

ok so lets be honest about what we DIDNT do...

**validation scope:**
this study only validates NIR camera compatibility and cost effectiveness. we did NOT validate fall detection accuracy. that requires testing on benchmark fall datasets like MCF, LE2I, UP Fall which we havent done yet.

like we proved that pose estimation works on IR cameras and that its cheaper than cloud but we didnt prove that the actual incident classification is accurate. thats a separate thing.

**testing environment:**
we tested MediaPipe on commercial CCTV footage not actual elderly subjects. elderly people move differently than the people in commercial security camera demos. their movement patterns, body proportions, gait characteristics might be different.

this means our 91.3% detection rate might not hold up when deployed with real elderly users. we need to test on age appropriate actors or actual elderly volunteers.

**hardware deployment:**
processing speed (20.53 FPS) was measured on standard hardware not on the target edge device (Jetson Orin Nano 8GB). we THINK it will work on the Jetson but we havent actually deployed it yet to verify.

real world deployment performance needs hardware validation before we can promise 20.53 FPS on the Jetson.

**market accessibility:**
our edge system ($672) targets middle income urban households (4th-5th quintile). what about low income elderly and rural elderly populations??? they cant afford $672 upfront even if theres no subscription.

they would need subsidies or alternative deployment models to achieve accessibility. our solution doesnt help the poorest people which is a real limitation.

#### 5.4 future directions

so what should we do next???

**benchmark dataset validation:**
test fall detection accuracy on MCF, LE2I, UP Fall datasets. these are standard benchmarks everyone uses so we can compare our approach to other methods.

**custom dataset collection:**
create a CamTech dataset with 180 videos (60 per incident type across 3 lighting conditions: daylight, low light, IR). use age appropriate actors to address western dataset bias. most existing datasets use young people not elderly.

**hardware validation:**
actually deploy the full pipeline on Jetson Orin Nano and verify we can hit 20.53 FPS. right now this is just an assumption based on specs.

**expanded detection:**
add more incident types based on local epidemiological data. right now we only detect 3 types of falls but there could be other incidents worth monitoring.

**policy framework development:**
develop governance guidelines for healthcare AI in developing countries. take what we learned and generalize it into recommendations for policymakers.

### 6. Conclusion

ok so lets wrap this up...

#### 6.1 key findings

this study demonstrates privacy governance driven architectural design through our cambodia elderly monitoring case study:

**technical feasibility:** edge based pose estimation achieves 91.3% keypoint detection on 850nm NIR footage which validates 24/7 privacy preserving monitoring capability. it actually WORKS on cheap IR security cameras.

**cost effectiveness:** edge architecture reduces 3 year total cost by 61% ($672 vs $1719 cloud alternative) which expands market reach to 216,000-324,000 elderly in middle income cambodian households. thats 2-3x more people than cloud systems can reach.

**design trade offs:** safety critical priority guides pipeline selection. we chose integrated approach despite being 2.3x slower because it has 5.7% better accuracy and 22.2% better pose coverage. when someones life is at stake accuracy beats speed.

**governance driven design:** privacy governance principles informed architectural decisions from inception (edge processing, pose only storage, immediate frame disposal) rather than being retrofitted post deployment. this is the key contribution tbh.

#### 6.2 implications for practice

**for healthcare AI developers:**

NIR camera compatibility needs empirical validation before deployment. you cant just assume it works. pose estimation performance varies by camera type and environment (we saw 73.8%-98.9% range).

integrated pipeline achieves 20.53 FPS on standard hardware which suggests edge deployment is feasible but Jetson Orin Nano validation is still necessary before making promises.

test your stuff on the actual hardware you plan to use not just whatever computer you have in your lab.

**for policymakers:**

privacy by design architecture can yield economic co benefits (cost reduction) beyond privacy protection alone. so privacy regulations dont have to hurt affordability they can actually help it if you design systems right from the start.

zero subscription models expand healthcare technology accessibility in middle income markets compared to recurring fee alternatives. maybe policymakers should incentivize or require zero subscription models for essential healthcare tech???

---

**FINAL WORD COUNT:** approximately 5200 words (need to verify after polishing)
