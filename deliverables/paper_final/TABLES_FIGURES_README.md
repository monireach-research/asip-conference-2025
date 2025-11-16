# Tables & Figures for ASIP 2025 Paper

**Created**: Nov 16, 2025
**Status**: Ready for integration into asip_2025_paper.tex

---

## Files Created

### 1. `tables_and_figures.tex`
Contains all 4 tables and 2 figure placeholders ready to insert into the main paper.

### 2. `system_architecture_diagram.tex`
Contains TikZ code for professional system architecture diagram.

---

## What's Included

### Tables (4 total)

#### **Table 1: Cost Comparison (3-Year Analysis)**
- Insert location: Section 4.2 (Cost-Effectiveness Analysis Results)
- Content: Edge ($672) vs. Cloud ($1,719) over 3 years, showing 61% cost reduction
- Format: Professional APA-style table with footnotes

#### **Table 2: NIR Camera Compatibility Validation Results**
- Insert location: Section 4.1 (NIR Camera Compatibility)
- Content: Performance metrics across 20 commercial NIR videos
- Metrics: Detection rate (91.3%), confidence (0.868), false negatives (12.3%), FPS (20.53)

#### **Table 3: Pipeline Comparison**
- Insert location: Section 4.1.2 (Pipeline Comparison)
- Content: Baseline vs. Integrated pipeline performance
- Shows: Speed-accuracy trade-off (2.3× slower but 5.7% more accurate)

#### **Table 4: Market Accessibility Analysis (OPTIONAL)**
- Insert location: After Table 1 (if space permits)
- Content: Estimated market reach in Cambodia (216,000-324,000 elderly)
- Note: Can be omitted if word count/page limit is tight

### Figures (2 total)

#### **Figure 1: System Architecture Diagram**
- **Two versions provided**:
  1. `tables_and_figures.tex` - Simple text placeholder (if TikZ unavailable)
  2. `system_architecture_diagram.tex` - Professional TikZ diagram (recommended)
- Insert location: Section 3.1 (Privacy Governance Architecture)
- Shows: 4 cameras → Edge processor → Processing pipeline → Privacy mechanisms

#### **Figure 2: Privacy Governance Framework (OPTIONAL)**
- Insert location: Section 3.1 or Section 5.1 (Discussion)
- Content: Three-layer framework (Principles → Mechanisms → Outcomes)
- Note: Only include if governance framework needs visual representation

---

## Integration Instructions

### Step 1: Add TikZ Package to Preamble (for Figure 1)

Add to the preamble of `asip_2025_paper.tex` (after line 21):

```latex
% TikZ for diagrams
\usepackage{tikz}
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, fit, backgrounds}
```

### Step 2: Insert Tables into Main Paper

Open `asip_2025_paper.tex` and insert tables at the following locations:

**Table 1 (Cost Comparison)**:
- Location: After line ~320 (end of Section 4.2.1, before Section 4.2.2)
- Copy from: `tables_and_figures.tex` lines 10-32

**Table 2 (NIR Validation)**:
- Location: After line ~280 (end of Section 4.1.1, before Section 4.1.2)
- Copy from: `tables_and_figures.tex` lines 38-58

**Table 3 (Pipeline Comparison)**:
- Location: After line ~295 (end of Section 4.1.2, before Section 4.1.3)
- Copy from: `tables_and_figures.tex` lines 64-87

**Table 4 (Market Reach - OPTIONAL)**:
- Location: After Table 1 (if space permits)
- Copy from: `tables_and_figures.tex` lines 93-122

### Step 3: Insert System Architecture Diagram

**Option A: Use TikZ diagram (RECOMMENDED)**
- Location: After line ~160 (end of Section 3.1.3, before Section 3.2)
- Copy from: `system_architecture_diagram.tex` entire content

**Option B: Use text placeholder**
- Location: Same as Option A
- Copy from: `tables_and_figures.tex` lines 128-154
- Note: Replace with actual diagram created in draw.io or PowerPoint

### Step 4: (Optional) Insert Privacy Governance Framework Diagram

- Location: After line ~175 (end of Section 3.1, before Section 3.2) OR in Discussion (Section 5.1)
- Copy from: `tables_and_figures.tex` lines 160-195

---

## Compilation Notes

### Required LaTeX Packages
All packages already included in `asip_2025_paper.tex` except:
- `\usepackage{tikz}` - Add for Figure 1 (TikZ version)
- `\usetikzlibrary{...}` - Add for Figure 1 (TikZ version)

### Checkmarks in Table 2
The `\checkmark` symbol requires no additional package (standard LaTeX).

### Table Width
All tables sized to fit within standard page margins (1 inch). If tables overflow:
- Reduce font size: `\begin{table}[htbp]\small` or `\footnotesize`
- Adjust column widths in `\begin{tabular}{...}`

### Figure Placement
- `[htbp]` = LaTeX tries: here, top, bottom, page (in that order)
- If figures float too far, change to `[h!]` to force "here"

---

## Word Count Impact

**Current paper**: 5,841 words (text only)

**Estimated addition with tables/figures**:
- 3 core tables (1, 2, 3): ~300-400 words equivalent (captions + notes)
- 1 core figure (architecture): ~100-150 words equivalent
- **Total estimated**: 6,241-6,391 words
- **Still within target**: 5,000-8,000 words ✓

**If including optional items**:
- Table 4 (market reach): +100 words
- Figure 2 (governance framework): +100 words
- **Total with all items**: 6,441-6,591 words ✓

---

## Quality Checklist

Before integrating, verify:
- [ ] All numbers match validation_results.md (91.3%, 0.868, 12.3%, 20.53 FPS, $672, $1,719)
- [ ] All table captions are descriptive and standalone
- [ ] All footnotes explain abbreviations and methodology
- [ ] Figure captions explain what's shown and why it matters
- [ ] All cross-references updated (e.g., "as shown in Table 1")
- [ ] APA style maintained (table formatting, caption style)

---

## Next Steps After Integration

1. **Compile LaTeX**: Generate PDF and check table/figure rendering
2. **Verify cross-references**: Ensure all `\ref{tab:...}` and `\ref{fig:...}` work
3. **Check page breaks**: Tables/figures shouldn't split awkwardly across pages
4. **Review captions**: Make sure they're self-explanatory
5. **Update text**: Add references to tables/figures in main text (e.g., "Table 1 shows...")

---

## Decision Points

### Do we need all 4 tables?
- **Must have**: Table 1 (cost), Table 2 (NIR validation), Table 3 (pipeline)
- **Optional**: Table 4 (market reach) - data already in text, table adds visual clarity

### Do we need both figures?
- **Must have**: Figure 1 (system architecture) - helps readers understand the system
- **Optional**: Figure 2 (governance framework) - conceptual, text might suffice

### TikZ vs. external diagram tool?
- **TikZ pros**: Professional, scalable, compiles with LaTeX
- **TikZ cons**: Requires learning curve, debugging can be tricky
- **External tool**: Easier to create, requires exporting as PDF/PNG and `\includegraphics{}`

---

## Alternative: If Tables/Figures Cause Issues

If LaTeX compilation fails or formatting is problematic:

1. **Skip optional items** (Table 4, Figure 2)
2. **Use simplified tables** (remove some columns, reduce footnotes)
3. **Replace Figure 1 with text description** (architecture already described in Section 3)
4. **Submit text-only paper** - Conference accepts 5,000-8,000 words, doesn't mandate figures

**Remember**: "Done is better than perfect" - submit on time with core content rather than miss deadline for perfect formatting.

---

## Files Summary

| File | Purpose | Status |
|------|---------|--------|
| `tables_and_figures.tex` | All 4 tables + 2 figure placeholders | Ready to integrate |
| `system_architecture_diagram.tex` | TikZ system diagram | Ready to integrate |
| `TABLES_FIGURES_README.md` | This file - integration guide | Reference only |

---

**Priority**: Integration into main paper → Compile PDF → Verify rendering → Move to Priority 15 (References & Formatting Check)
