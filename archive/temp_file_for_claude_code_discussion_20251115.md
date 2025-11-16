## GDPR Verification

Paper: Williamson, S. M., & Prybutok, V. (2024). Balancing privacy and progress: A review of
privacy challenges, systemic oversight, and patient perceptions in AI-driven healthcare.
Applied Sciences, 14(2), 675. https://doi.org/10.3390/app14020675

### Response by my LLM

Yes, the paper discusses the GDPR in the context of healthcare AI data protection. Here are the exact quotes, page numbers, and context.

Exact Quotes and Locations:

Page 8, Section 3.3.1: "The paper navigates the complex ethical and legal frameworks essential for AI integration in healthcare. We comprehensively examine patient rights and the nuances of informed consent, along with the challenges of harmonizing advanced technologies like blockchain with the General Data Protection Regulation (GDPR)."

Page 9, Table 2: The table titled "Deeper impact of blockchain technology on privacy and decision-making in AI healthcare" includes "Regulatory Considerations" and "Additional Notes" columns with multiple specific mentions:

"Challenges in GDPR alignment"

"Facilitates audit trails"

"Aligns with GDPR personal data criteria"

"Central to GDPR compliance"

"Must adapt to evolving GDPR standards"

Page 18-19, Section 3.6: "These frameworks must harmonize with regulations such as the General Data Protection Regulation (GDPR) to ensure ethical AI usage in healthcare. The incorporation of blockchain technology in AI-driven healthcare, as explored by [29], adds another layer of complexity to these challenges. Blockchain offers opportunities for enhancing data security and patient privacy but also challenges aligning with GDPR requirements."

Page 26, Section 4.2.3: "This is fundamental in healthcare, where the precision and unchangeability of medical records are critical, ensuring that patient data remain accurate and unaltered over time... By integrating Differential Privacy into healthcare AI systems, researchers and clinicians can gain valuable insights from large datasets without risking the exposure of personal health information, thus maintaining patients’ trust and complying with stringent privacy regulations such as GDPR and HIPAA [21]."

Page 28, Section 4.3: "However, integrating blockchain technology in healthcare AI presents complex interactions with data protection laws such as the European Union’s General Data Protection Regulation (GDPR). GDPR imposes stringent requirements on personal data processing, focusing on principles such as consent, the right to access, rectification, and the right to be forgotten."

Page 31-32, Section 4.3.2: "The intricate relationship between blockchain technologies and the General Data Protection Regulation (GDPR) is fraught with complexities and tensions... The GDPR assumes the presence of identifiable data controllers for each personal data point, a notion challenged by blockchain's decentralization... Moreover, the GDPR's provisions, particularly Articles 16 and 17, assume that data can be modified or erased as needed to comply with legal requirements. However, blockchain technologies are typically designed to make data modifications purposefully onerous..."

Page 37-38, Section 5.3: "Integrating blockchain technology with the General Data Protection Regulation (GDPR) presents a multifaceted and intricate challenge. As highlighted in the study [29], the diverse nature of blockchain technologies makes a broad assessment of their compatibility with EU data protection law impractical... The GDPR assumes the presence of identifiable data controllers for each personal data point, a notion challenged by blockchain's decentralization... Moreover, the principles of data minimization and purpose limitation, central to GDPR, pose challenges when applied to blockchain technologies."

Page 40, Section 5.4: "Similar challenges arise with integrating blockchain technology into healthcare, especially concerning the General Data Protection Regulation (GDPR). Blockchain technology underscores several regulatory tensions within the GDPR framework. Its decentralized nature contradicts the GDPR's premise of identifiable data controllers..."

Context:
Yes, the GDPR is consistently discussed as a critical data protection regulation relevant to healthcare AI. The paper examines the challenges of aligning AI and related technologies (especially blockchain) with GDPR requirements, focusing on tensions regarding data controllership, the right to erasure ('right to be forgotten'), data minimization, and purpose limitation.

---

## Retrofitted Post-Hoc vs Inception Design

Papers to check:

1. Cavoukian, A., Taylor, S., & Abrams, M. E. (2010). Privacy by Design: Essential for
   organizational accountability and strong business practices. Identity in the Information
   Society, 3(2), 405–413. https://doi.org/10.1007/s12394-010-0053-z

2. Birkstedt, T., Minkkinen, M., Tandon, A., & Mäntymäki, M. (2023). AI Governance: Themes,
   knowledge gaps and future agendas. Internet Research, 33(7), 133–167.
   https://doi.org/10.1108/INTR-01-2022-0042

3. Burns, S. A., et al. (2024). [ASEAN Guide on AI Governance paper]

4. Almeida, P. G. R. C., et al. (2020). [AI regulation meta-framework paper]

These are Governance Papers which already have comprehensive details in Zotero, I paste the details as follows:

1. Cavoukian et al. (2010)
   This paper discusses the foundational principles of "Privacy by Design" (PbD) and their role in achieving organizational accountability, directly addressing how privacy governance principles can be built into systems and business processes from the outset.

**Paper:** Cavoukian et al. (2010)

**Key claim:** Privacy by Design provides a foundational framework for building privacy and accountability directly into organizational practices and technologies, enabling robust data governance.

**Framework/Principles:**

- Proactive not Reactive; Preventative not Remedial
- Privacy as the Default Setting
- Privacy Embedded into Design
- Full Functionality—Positive-Sum, not Zero-Sum
- End-to-End Security—Full Lifecycle Protection
- Visibility and Transparency
- Respect for User Privacy

**Healthcare relevance:**

The principles, especially "Privacy Embedded into Design" and "End-to-End Lifecycle Protection," provide a direct blueprint for architecting monitoring systems that collect and process sensitive health data responsibly by default.

**Quotable statements:**

- "Privacy by Design and accountability go together in much the same way that innovation and productivity go together." (p. 3)
- "To be an accountable organization a company must have rules that are based on an external measuring stick such as data protection laws..." (p. 5)
- "End-to-end lifecycle protection informs the accountable organization that it must build privacy into every process from the assessment before data is collected to the oversight when data is retired." (p. 6)

**Limitations:**

The paper does not specifically address resource-constrained environments or the technical implementation of AI and edge computing, which are central to your research context.

---

2. Birkstedt et al. (2023)

This paper is a systematic literature review that synthesizes organizational AI governance (AIG) research, directly addressing how to translate high-level ethical principles (like privacy) into practical governance mechanisms and processes, which is central to your research question.

**Paper**: Birkstedt et al. (2023)

**Key claim**: Organizational AI Governance (AIG) is a nascent but critical system of rules, practices, and processes needed to translate ethical AI principles into practice and ensure alignment with organizational strategies and values.

**Framework/Principles**:

- **Four AIG Themes:** Technology, Stakeholders & Context, Regulation, and Processes.
- **Four AIG Agendas:** Technical, Stakeholder & Contextual, Regulatory, and Process.
- **Proposed Mechanism:** Establishment of an organizational AI Oversight Unit (AOU).

**Healthcare relevance**: Provides a foundational governance framework that can be adapted to govern AI in sensitive domains like elderly safety monitoring, emphasizing processes like impact assessments and auditing to ensure ethical and responsible deployment.

**Quotable statements**:

- "AI governance is a system of rules, practices, processes and technological tools that are employed to ensure an organization’s use of AI technologies aligns with the organization’s strategies, objectives, and values..." (p. 2, adopted from Mäntymäki et al., 2022a)
- "The central knowledge gaps revealed were the limited understanding of AIG implementation, lack of attention to the AIG context, uncertain effectiveness of ethical principles and regulation, and insufficient operationalization of AIG processes." (p. 18)
- "For practitioners, we highlight training and awareness, stakeholder management and the crucial role of organizational culture, including senior management commitment." (p. 1)

**Limitations**: The review is conceptual and high-level; it does not provide specific technical implementations or address the unique constraints of resource-constrained environments, focusing instead on broad organizational governance structures.

---

3. Burns (2024)
   This paper discusses the ASEAN Guide on AI Governance and Ethics, outlining principles like privacy and accountability for AI in health security, directly relevant to privacy governance in Southeast Asian contexts like Cambodia.

**Paper**: Burns et al. (2024)

**Key claim**: The ASEAN Guide on AI Governance and Ethics establishes principles for responsible AI deployment in health security, emphasizing privacy, accountability, and sustainability.

**Framework/Principles:**

- Transparency and explainability
- Fairness and equity
- Security and safety
- Human-centric approach
- Robust data privacy and governance frameworks
- Accountability and integrity
- Robustness and reliability

**Healthcare relevance**: Provides a regional governance framework for AI in healthcare, including monitoring systems, with principles that ensure privacy and ethical use in resource-constrained environments like Cambodia.

**Quotable statements**:

- "Robust data privacy and governance frameworks are also key, especially for sensitive applications like contact tracing." (p. 3)
- "Critical LLM deployments should therefore preference low-power, on-device models." (p. 5)
- "Accountability and integrity are crucial for maintaining public trust in AI-driven health security measures." (p. 3)

**Limitations**: Does not specifically address elderly safety monitoring or detailed architectural implementations for edge-based AI systems; focuses on high-level policy and broad health security applications.

---

4. Almeida (2020)

This paper develops a comprehensive governance framework for AI regulation, synthesizing 21 existing models and emphasizing ethical principles, stakeholder roles, and processes that align with designing accountable and trustworthy AI systems.

**Paper:** Almeida et al. (2021)

**Key claim:** An effective AI governance framework must integrate ethical principles, multi-stakeholder processes, and adaptive regulation to manage risks and ensure trustworthy AI.

**Framework/Principles:**

- Integrates 21 prior AI governance models into a unified AIR framework
- Emphasizes core principles: fairness, transparency, accountability, safety, and human rights
- Proposes interactive governance with Regulatory-to-Technology (R2T) and Technology-to-Regulatory (T2R) feedback loops
- Advocates for a dedicated regulatory agency for certification, auditing, and standard-setting
- Supports "society-in-the-loop" for public participation and value alignment

**Healthcare relevance:**

- Highlights risk mitigation, data governance, and bias prevention—critical for elderly monitoring systems
- Certification and auditing processes can ensure compliance with privacy and ethical standards in health AI
- Edge-relevant principles (e.g., data locality, minimal data transfer) align with privacy-by-design in resource-constrained settings

**Quotable statements:**

- "The key challenge related to the AI regulation dilemma is demonstrating it is produced and deployed appropriately." (p. 4)
- "A trustworthy AI must be lawful, ethical, and robust." (p. 11)
- "Transparency, fairness, and accountability in cases where AI systems impact people’s rights." (p. 10)

**Limitations:**

- Does not specifically address resource-constrained or rural contexts like Cambodia
- Limited focus on edge computing or lightweight AI architectures
- Does not explore cost-benefit trade-offs of privacy-first designs in low-infrastructure settings

## Family Caregiving Norms

### Maiyapakdee et al. (2025)

Based on a thorough review of the provided paper, here is the verification:

1. Search Results:
   The paper does not contain any discussion of "strong family caregiving norms," cultural preferences for care, or comparisons between home-based and institutional care.

2. Exact Quotes and Explicit Discussion:

Relevant Quote on Living Arrangements: "Most participants (59.1%) were female, and most (96.4%) lived single-story houses." (Page 3, Table 1 and Section 3.1).

Conclusion: No other relevant quotes were found. The paper does not explicitly discuss a cultural preference for home-based care.

3. Recommendation:

Family caregiving norms are not mentioned in Factors related to home accidents among the elderly in Thailand.

You should search for other papers using terms like "elderly living arrangements Southeast Asia" or "family caregiving culture Thailand" to support this claim.

Without evidence from this paper, it is recommended to remove this specific claim if it is being attributed to this source.

### Romli et al. (2017)

Based on the provided text from the scoping review by Romli et al. (2017), here is the verification:

1. Findings:
   Yes, this paper explicitly discusses strong family caregiving norms and a cultural preference for home-based care.

2. Exact Quotes and Explicit Discussion:

Relevant Quote 1: "Older adults in ASEAN communities often live with their adult children in extended family households. The low number of falls could be due to the filial piety values associated with Asian culture, where adult children are expected to care for their parents." (Section: Discussion)

Relevant Quote 2: "Therefore, older individuals who are at risk of falls receive more supervision and assistance at home..." (Section: Discussion)

Conclusion: The paper explicitly discusses the preference for and practice of family-based, home care over institutional facilities, attributing it directly to the cultural value of "filial piety."

**NOTE**: I don't have access to the full paper, but there are comprehensive sections of the paper in https://www.sciencedirect.com/science/article/abs/pii/S0033350616304565#preview-section-snippets

---

## Technology Adoption Patterns

### Hatef et al. 2024

This paper presents a consensus-based framework specifically designed to ensure equity in digital health technologies, directly addressing governance challenges.

Paper: Hatef et al. 2024

Key claim: This paper provides an evidence- and consensus-based framework to guide stakeholders in intentionally considering and assessing equity across all phases of the digital healthcare lifecycle to prevent the exacerbation of health disparities.

Framework/Principles:

Three Core Domains: Patient and Community Characteristics; Health System Characteristics; Health Information Technology Characteristics.

Five Lifecycle Phases: Planning, Development, Acquisition, Implementation/Maintenance, and Monitoring/Improvement/Equity Assessment.

Six Guiding Principles: Include ensuring solutions ameliorate inequities, person-centeredness, inclusivity in development, and focus on impact.

Healthcare relevance: Directly applicable to elderly monitoring by framing equity challenges (e.g., digital literacy, broadband access, user-friendly design) as core considerations that must be intentionally addressed during technology development and deployment.

Quotable statements:

"The proposed Framework is designed to specify the aspects that need to be considered in a systematic and intentional approach to ensure digital healthcare solutions improve, and not exacerbate, healthcare inequities." (Page 1)

"Considerations ranging from a lack of patient digital literacy to a lack of broadband access—which is collectively often referred to as the digital divide—may impact the viability... of healthcare solutions that involve digital technologies..." (Page 2)

"Moreover, our approach acknowledged that to ensure equity intentionality for certain populations, non-digital solutions may need to stand alongside digital ones." (Page 8)

Limitations: The framework is a conceptual guide and does not provide a specific, validated assessment tool or detailed metrics for measurement. It also acknowledges that for some populations, non-digital alternatives may be necessary.

### Richardson et al. (2022)

**Paper:** Richardson et al. (2022)

**Key claim:** A comprehensive Framework for Digital Health Equity is needed to address Digital Determinants of Health (DDoH) and prevent the digitization of healthcare from widening health disparities.

**Framework/Principles:**

- Expands the NIMHD Health Disparities Framework to include a **Digital Environment** domain.
- DDoHs operate across four levels:
  - **Individual:** Digital literacy, self-efficacy, technology access, attitudes (trust).
  - **Interpersonal:** Implicit tech bias, interdependence (e.g., shared devices).
  - **Community:** Infrastructure (broadband, healthcare digital capabilities), tech norms.
  - **Societal:** Tech policy, data/design standards, algorithmic bias.

**Healthcare relevance:**

- Directly applies to digital health solutions like Remote Patient Monitoring (RPM), a key use case for elderly safety monitoring.
- Identifies **cost and access** (Individual level) and **community infrastructure** (Community level) as critical DDoHs, grounding your Proposition 2 on privacy-first architecture's co-benefits for accessibility in resource-constrained settings.

**Quotable statements:**

- "Without broadband internet access, patients cannot fully use telehealth in all its forms..." (Page 3).
- "Disparity populations are less likely to benefit from interventions focused on individual-level determinants, as barriers, including limited resources and competing priorities, are greater in these populations" (Page 4).
- "Interventions targeting 'upstream' determinants at the community and societal levels (i.e., digital infrastructure) are more likely to be effective..." (Page 4).

**Limitations:**

- The framework is general for digital health equity and does not specifically address AI-powered systems, privacy governance, or the architectural trade-offs between edge and cloud computing.

### Sylla et al. (2025)

This paper is **relevant** for establishing the foundational context of digital health challenges in LMICs like Cambodia, which directly supports the resource-constrained aspects of my research (on Elderly Incident Detection System). It provides evidence for barriers (e.g., economic, infrastructure) that justify a privacy-governance approach with cost and accessibility co-benefits.

Paper: Sylla et al. 2025

Key claim: Digital health interventions in LMICs have evolved over 25 years but face persistent barriers in equity, infrastructure, and access, requiring collaborative efforts to achieve UHC.

Framework/Principles:

\- Sustainable health information systems (e.g., HISP) for data management

\- Inclusive design involving communities and multiple stakeholders

\- Emphasis on scalability and adaptability in resource-limited settings

Healthcare relevance: Provides evidence of LMIC-specific challenges (e.g., cost, digital divide) that inform the design of accessible, cost-effective AI monitoring systems for elderly care in Cambodia.

Quotable statements:

\- "Digital health initiatives often fail to reach vulnerable populations due to structural, practical, commercial, and economic barriers" (Page 3)

\- "Limited resources, infrastructure, information, and knowledge, as well as embedded structural complexities... contribute to inequitable access to digital health services" (Page 3)

Limitations: Excludes China and India due to advanced digital health ecosystems; focuses on English/French literature, potentially missing regional studies; does not address AI-specific privacy governance or elderly care applications.

### Maiyapakdee et al. (2025)

Mentioned once above

### Romli et al. (2017)

Mentioned once above
