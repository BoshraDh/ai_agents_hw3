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
Step E: PDF Compilation   →  output/paper.pdf            🔲 Pending
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

---

## Step C: Reviewer Agent

**Role:** Academic Peer Reviewer
**Goal:** Validate the draft against academic standards and the PRD requirements checklist.

**Checklist:**
- [x] Cover sheet present and complete
- [x] Table of Contents present
- [x] Estimated length meets requirement
- [x] At least one image/diagram (placeholder present)
- [x] At least one graph/chart (placeholder + data table present)
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
   - `article` document class, XeLaTeX engine (for Hebrew cover page)
   - Cover page with `\texthebrew{...}`, course, lecturer, semester, author
   - Auto-generated Table of Contents (`\tableofcontents`)
   - Figure placeholders (`\fbox`) ready to swap for `\includegraphics`
   - Comparison table (`booktabs` + `tabularx`)
   - Math equations (`\begin{equation}`) with `\eqref{}` cross-references
   - Score table for radar chart data
   - `natbib` bibliography (`\bibliography{references}`)

**Status:** ✅ Complete — `output/paper.tex` committed and pushed to GitHub.

**Compile instructions:**
```
xelatex paper.tex
bibtex paper
xelatex paper.tex
xelatex paper.tex
```

---

## Step E: PDF Compilation (Pending)

**Goal:** Compile `paper.tex` into a submission-ready PDF.

**Blockers (manual steps required before compiling):**
1. Create `output/images/arch_comparison.png` — architecture diagram
2. Create `output/images/performance_chart.png` — radar/bar chart
3. Replace `\fbox` placeholders in `paper.tex` with `\includegraphics`

**Status:** 🔲 Pending — waiting on image assets.

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
| Paper draft (MD)     | `output/paper.md`           | ✅ Complete    |
| Bibliography         | `output/references.bib`     | ✅ Complete (5 entries) |
| Crew result          | `output/crew_result.md`     | ✅ Complete    |
| LaTeX source         | `output/paper.tex`          | ✅ Complete    |
| Architecture image   | `output/images/arch_comparison.png` | ✅ Complete (generated by `src/generate_images.py`) |
| Performance chart    | `output/images/performance_chart.png` | ✅ Complete (generated by `src/generate_images.py`) |
| Final PDF            | `output/paper.pdf`          | ✅ Complete (9 pages, 550 KB) |
