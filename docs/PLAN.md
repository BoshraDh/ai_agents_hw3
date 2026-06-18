# Project Plan

## Workflow: Four-Stage Sequential Agent Pipeline

```
Step A: Researcher Agent
        ↓
Step B: Writer Agent
        ↓
Step C: Reviewer Agent
        ↓
Step D: LaTeX + PDF Compiler
```

---

## Step A: Researcher Agent

**Role:** Senior AI Research Analyst
**Goal:** Gather and synthesize comprehensive information on LangGraph and CrewAI.

**Output:**
- Structured research notes covering: architecture, API design, tooling, use cases, performance
- At least 5 BibTeX-ready citations
- Draft data for the comparison table and the graph
- A candidate mathematical formula (e.g., agent coordination overhead, complexity)

**Tools:** WebSearch, file write

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

---

## Step C: Reviewer Agent

**Role:** Academic Peer Reviewer
**Goal:** Validate the draft against academic standards and the PRD requirements checklist.

**Checklist:**
- [ ] Cover sheet present and complete
- [ ] Table of Contents present
- [ ] Length ≥ 15 pages (estimate from word count)
- [ ] At least one image/diagram
- [ ] At least one graph/chart
- [ ] At least one comparison table
- [ ] At least one mathematical formula
- [ ] Bibliography in BibTeX format with ≥ 5 sources
- [ ] Professional academic English throughout
- [ ] All sections logically connected

**Output:** Annotated feedback written back into `output/paper.md` if corrections needed, then signals approval.

---

## Step D: LaTeX + PDF Compiler

**Role:** Document Engineer
**Goal:** Convert the approved Markdown to LaTeX and compile to PDF.

**Sub-steps:**
1. Convert `output/paper.md` → `output/paper.tex`
   - Apply `article` document class
   - Include cover page (`\maketitle` with course metadata)
   - Generate Table of Contents (`\tableofcontents`)
   - Embed images (`\includegraphics`)
   - Render table (`tabular` or `booktabs`)
   - Render formula (`equation` or `align`)
   - Link bibliography (`\bibliography{references}`)
2. Compile `paper.tex` → `output/paper.pdf` (via `pdflatex` or `xelatex`)

---

## Execution Rules

- Each step is **strictly sequential** — the next step starts only after the previous step's output is validated.
- CrewAI `Process.sequential` enforces the order.
- Each agent writes its output to a file before the next agent reads it.
- The pipeline is defined in `src/main.py`.

---

## Implementation Status

| Component | File | Status |
|---|---|---|
| Researcher Agent | `src/agents.py` | ✅ Implemented |
| Writer Agent | `src/agents.py` | ✅ Implemented |
| Reviewer Agent | `src/agents.py` | ✅ Implemented |
| Research Task | `src/tasks.py` | ✅ Implemented |
| Writing Task | `src/tasks.py` | ✅ Implemented |
| Review Task | `src/tasks.py` | ✅ Implemented |
| Crew orchestration | `src/main.py` | 🔲 Pending |
| LaTeX conversion | `src/main.py` / Step D | 🔲 Pending |
| PDF compilation | Step D | 🔲 Pending |
