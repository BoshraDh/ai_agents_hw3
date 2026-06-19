# Project Plan

## Workflow: Four-Stage Sequential Agent Pipeline

```
Step A: Researcher Agent  →  output/research_notes.md   ✅ Complete
        ↓
Step B: Writer Agent      →  output/paper.md             ✅ Complete
        output/references.bib
        ↓
Step C: Reviewer Agent    →  output/paper.md (validated) ✅ Complete
        ↓
Step D: LaTeX Conversion  →  output/paper.tex            ✅ Complete
        ↓
Step E: PDF Compilation   →  output/paper.pdf            ✅ Complete (15 pages, 514 KB)
```

---

## Step A: Researcher Agent

**Role:** Senior AI Research Analyst
**Goal:** Gather and synthesize comprehensive information on LangGraph and CrewAI.

**Output:**
- Structured research notes covering: architecture, API design, tooling, use cases, performance
- At least 5 BibTeX-ready citations
- Draft data for the comparison table and the graph
- A candidate mathematical formula (agent coordination overhead / complexity)

**Status:** ✅ Complete — `output/research_notes.md` generated and committed.

---

## Step B: Writer Agent

**Role:** Academic Technical Writer
**Goal:** Produce the full Markdown draft of the paper with all required structural elements.

**Output: `output/paper.md`**

Required sections and elements:
- Cover sheet (title, course, lecturer, semester, student name)
- Table of Contents
- Abstract
- Introduction
- Background: LangGraph
- Background: CrewAI
- Comparative Analysis (includes table)
- Performance & Complexity (includes mathematical formula)
- Architecture Diagram (image placeholder with caption)
- Comparison Chart (graph data / placeholder)
- Discussion
- Conclusion
- References (BibTeX keys)

**Also produces:** `output/references.bib`

**Status:** ✅ Complete — files generated, post-run quality fixes applied:
- Removed AI markdown wrappers
- Fixed lecturer field to "Yoram Segal"
- Corrected factual error (CrewAI language: Python, not JavaScript)
- Aligned `\cite{}` keys with `references.bib` entries
- Expanded to 5,033 words / 12 sections (15–25 page target)

---

## Step C: Reviewer Agent

**Role:** Academic Peer Reviewer
**Goal:** Validate the draft against academic standards and the PRD requirements checklist.

**Checklist:**
- [x] Cover sheet present and complete
- [x] Table of Contents present
- [x] Estimated length meets requirement (15 pages in compiled PDF)
- [x] At least one image/diagram (`arch_comparison.png`)
- [x] At least one graph/chart (`performance_chart.png`)
- [x] At least one comparison table
- [x] At least one mathematical formula
- [x] Bibliography in BibTeX format with ≥ 5 sources
- [x] Professional academic English throughout
- [x] All sections logically connected

**Status:** ✅ Complete — approved for LaTeX conversion.

---

## Step D: LaTeX Conversion

**Role:** Document Engineer
**Goal:** Convert the approved Markdown to a compilable LaTeX source file.

**Sub-steps:**
1. Convert `output/paper.md` → `output/paper.tex`
   - `article` document class, **pdflatex** engine
   - Note: engine changed from XeLaTeX to pdflatex to resolve MiKTeX 25.12
     dvipdfmx `fwrite EINVAL` crash. Hebrew text on cover page is rendered
     via ASCII transliteration; Hebrew Unicode appears in the Markdown source only.
   - Cover page with course name, lecturer, semester, author
   - Auto-generated Table of Contents (`\tableofcontents`)
   - Live `\includegraphics` (no `\fbox` placeholders)
   - Comparison table (`booktabs` + `tabularx`)
   - Math equations (`\begin{equation}`) with `\eqref{}` cross-references
   - Code listings via `fancyvrb` `CodeBlock` environment
   - Score table for radar chart data
   - Selection heuristics table
   - `natbib` bibliography (`\bibliography{references}`)

**Status:** ✅ Complete — `output/paper.tex` committed and pushed to GitHub.

**Compile instructions:**
```bash
cd output
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

---

## Step E: PDF Compilation

**Goal:** Compile `paper.tex` into a submission-ready PDF.

**Status:** ✅ Complete

- Engine: `pdflatex` (MiKTeX 25.12)
- Pages: **15**
- File size: **514 KB**
- Sequence: `pdflatex` × 1 → `bibtex` → `pdflatex` × 2
- Zero errors or warnings in final compile
- All images embedded: `arch_comparison.png`, `performance_chart.png`
- Bibliography resolved: 5 entries, `plainnat` style

---

## Execution Rules

- Each step is **strictly sequential** — next step starts only after previous output is validated.
- CrewAI `Process.sequential` enforces the agent order (Steps A–C).
- Steps D–E are performed outside the pipeline (LaTeX toolchain).
- Every file change is committed and pushed immediately with a descriptive message.

---

## Implementation Status

| Component            | File                        | Status         |
|----------------------|-----------------------------|----------------|
| Researcher Agent     | `src/agents.py`             | ✅ Complete    |
| Writer Agent         | `src/agents.py`             | ✅ Complete    |
| Reviewer Agent       | `src/agents.py`             | ✅ Complete    |
| Research Task        | `src/tasks.py`              | ✅ Complete    |
| Writing Task         | `src/tasks.py`              | ✅ Complete    |
| Review Task          | `src/tasks.py`              | ✅ Complete    |
| Crew orchestration   | `src/main.py`               | ✅ Complete    |
| Environment setup    | `requirements.txt`, `.env.example` | ✅ Complete |
| Research notes       | `output/research_notes.md`  | ✅ Complete    |
| Paper draft (MD)     | `output/paper.md`           | ✅ Complete (5,033 words, 12 sections) |
| Bibliography         | `output/references.bib`     | ✅ Complete (5 entries) |
| Crew result          | `output/crew_result.md`     | ✅ Complete    |
| LaTeX source         | `output/paper.tex`          | ✅ Complete (pdflatex) |
| Architecture image   | `output/images/arch_comparison.png` | ✅ Complete (generated by `src/generate_images.py`) |
| Performance chart    | `output/images/performance_chart.png` | ✅ Complete (generated by `src/generate_images.py`) |
| Final PDF            | `output/paper.pdf`          | ✅ Complete (**15 pages, 514 KB**) |
