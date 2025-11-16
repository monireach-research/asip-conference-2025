# Systematic Workflow to First Draft

**Last Updated**: Nov 14, 2025 (Phase 1-2 complete: Validations + Literature ready)
**Deadline**: Nov 16, 2025
**Total Estimated Time**: 55-72 hours
**Available Time**: 40-48 hours (8h/day × 5 days)

---

## PHASE 1: Validation Work (~14-19 hours)

### Quick Wins (2-3 hours) ✅ COMPLETE
- [x] A4.2: Use existing Kami Fall Detect Camera comparison (verified Oct 20, 2025)
- [x] A4.2: Create cost comparison table (Your system $672 vs Kami $1,719 over 3 years)
- [x] A1.2c: Document Oct 2025 IR footage results (93.2% detection, 0.901 confidence)

### Extended NIR Validation (6-8 hours) ✅ COMPLETE
- [x] A1.2a: Run `nir_validation_batch.py` on 20 NIR videos (~30-60 min processing)
- [x] A1.2a: Analyze summary_report.json (overall metrics vs acceptance criteria)
- [x] A1.2a: Document results in validation_results.md (pass/fail, key findings)
- [x] A1.2a: Update research_summary.md with NIR validation findings

### Pipeline Efficiency Comparison (6-8 hours) ✅ COMPLETE
- [x] A1.3: Run `pipeline_comparison.py` on same 20 NIR videos (~60-90 min processing)
- [x] A1.3: Analyze comparison_summary.json (baseline vs integrated winner)
- [x] A1.3: Review automated recommendation (use YOLOv8n integration or baseline?)
- [x] A1.3: Document speed/accuracy trade-offs in validation_results.md
- [x] A1.3: Update research_summary.md with pipeline decision rationale

---

## PHASE 2: Literature Review (~10-15 hours) ✅ COMPLETE

### Privacy & Governance Literature
- [x] Search: Privacy-by-design frameworks (Found: Cavoukian 2010)
- [x] Search: Edge computing for privacy governance (Found: Burns 2024)
- [x] Search: Healthcare AI ethics and governance (Found: Birkstedt 2023, Almeida 2020)
- [x] Search: Digital health equity and accessibility frameworks (Found: Hatef 2024, Richardson 2022, Sylla 2025)
- [x] Collect 5-7 references for privacy governance (7 governance papers identified)

### Technical Literature
- [x] Search: Elderly fall detection systems (vision-based) (31 papers from thesis research)
- [x] Search: Pose estimation for activity recognition (Covered in filtered_papers_for_thesis.md)
- [x] Search: Edge AI deployment studies (Covered in filtered_papers_for_thesis.md)
- [x] Collect 5-7 references for technical background (11 core papers available)

### Regional Context Literature
- [x] Search: Elderly care in Southeast Asia/Cambodia (Papers #48, #49, #36, #43)
- [x] Search: Healthcare technology adoption in developing countries (Sylla 2025)
- [x] Search: Affordability barriers in assistive technologies (Richardson 2022, Hatef 2024)
- [x] Collect 3-5 references for regional context (9 papers available)

### Organization
- [x] Create reference database (38 papers total: 31 technical + 7 governance)
- [x] Extract key quotes and findings for 4 remaining governance papers (Cavoukian, Burns, Birkstedt, Almeida - completed Nov 11)
- [x] Extract key quotes for 3 accessibility papers (Hatef, Richardson, Sylla - completed Nov 11)

---

## PHASE 3: Paper Writing (~25-30 hours)

### Section 1: Introduction (4 hours)
- [ ] Write problem context (aging population, Cambodia healthcare)
- [ ] Write privacy governance challenges in healthcare AI
- [ ] Write research gap and objectives
- [ ] Write paper structure overview

### Section 2: Literature Review (7-8 hours)
- [ ] Write elderly safety monitoring technologies subsection
- [ ] Write privacy-preserving AI approaches subsection
- [ ] Write technology governance frameworks subsection
- [ ] Write regional context subsection (Southeast Asia)
- [ ] Integrate 15-20 citations throughout

### Section 3: Methodology (4 hours)
- [ ] Write system architecture description
- [ ] Write privacy governance mechanisms (edge, pose-only, frame disposal)
- [ ] Write incident detection approach
- [ ] Write validation methodology (datasets, metrics)
- [ ] Create system architecture diagram

### Section 4: Results (4 hours)
- [ ] Write 4.1: Privacy Preservation (pose-only design, cite MediaPipe literature)
- [ ] Write 4.2: Technical Feasibility (A1.2c initial + A1.2a extended NIR validation, A1.3 pipeline comparison)
- [ ] Write 4.3: Cost-Effectiveness (A4.2: $672 vs $1,719, 61% savings)
- [ ] Write 4.4: Robustness (optional - cite cross-dataset literature if time permits)
- [ ] Create results tables and figures

### Section 5: Discussion (4 hours)
- [ ] Write governance implications (privacy-driven design)
- [ ] Write technical contributions (integration efficiency)
- [ ] Write accessibility implications (cost reduction)
- [ ] Write limitations (preliminary validation, no hardware deployment, Western datasets)
- [ ] Write future work (Jetson validation, CamTech dataset, user study)

### Section 6: Conclusion (2 hours)
- [ ] Summarize governance-driven design contribution
- [ ] Summarize key findings from validations
- [ ] Restate need for future empirical validation
- [ ] Closing statement on governance-driven AI design

---

## PHASE 4: Integration & Polish (~6-8 hours)

### Integration
- [ ] Combine all sections into single document
- [ ] Check flow between sections
- [ ] Ensure consistent terminology throughout
- [ ] Verify all citations are included

### Figures & Tables
- [ ] Create system architecture diagram
- [ ] Create privacy governance framework diagram (optional)
- [ ] Create cost comparison table
- [ ] Create validation results tables
- [ ] Number and caption all figures/tables

### References & Formatting
- [ ] Format all references in APA 6th style
- [ ] Check in-text citations match reference list
- [ ] Format paper according to ASIP template
- [ ] Check page limits (15-20 pages)

### Final Polish
- [ ] Proofread entire paper (grammar, spelling)
- [ ] Check technical accuracy
- [ ] Verify all claims are supported
- [ ] Generate final PDF

---

## PHASE 5: Submission

- [ ] Send to Dr. Siengheng for review
- [ ] Send to Dr. May for review
- [ ] Incorporate supervisor feedback
- [ ] Submit final version to ASIP 2025

---

## Notes

**Strategy**: Complete validations first (Phase 1), then do literature review (Phase 2) in parallel with early writing (Phase 3). This allows you to write Introduction/Methodology while waiting for validation results.

**Priority Validations Selected** (4 of 29):
1. **A1.2c**: Initial NIR validation - Feasibility proof (2 videos, Oct 31) ✅ COMPLETE
2. **A4.2**: Cloud cost comparison - Accessibility claim ($672 vs $1,719, 61% savings) ✅ COMPLETE
3. **A1.2a**: Extended NIR validation - Statistical validity (20 diverse 850nm NIR sources)
4. **A1.3**: Pipeline efficiency comparison - Baseline vs Integrated trade-off analysis

**Buffer Strategy**:
- If validation takes longer: Skip A1.2a, cite literature instead
- If writing is slow: Use AI writing assistance for first drafts
- Emergency compression: Combine phases if needed
