# Product Requirements Document

## Research Paper: LangGraph vs CrewAI

**Author:** Boshra Dahamshy
**Course:** אורקסטרקציה של סוכני AI
**Semester:** Spring 2026

---

## Goal

Produce a professional academic paper (15–25 pages) in English comparing LangGraph and CrewAI as multi-agent orchestration frameworks.

---

## Required Paper Elements

| Element | Requirement |
|---|---|
| Cover Sheet | Course name, Lecturer, Semester, Student Name |
| Table of Contents | Auto-generated, linked sections |
| Length | 15–25 pages |
| Image | At least one architecture diagram or screenshot |
| Graph | At least one comparison chart (e.g., performance, complexity) |
| Table | At least one structured comparison table |
| Formula | At least one mathematical formula (e.g., efficiency metric, complexity) |
| Bibliography | BibTeX format, minimum 5 sources |
| Language | English (professional academic tone) |

---

## Cover Sheet Fields

- **Course:** אורקסטרקציה של סוכני AI
- **Lecturer:** (TBD)
- **Semester:** Spring 2026
- **Student Name:** Boshra Dahamshy

---

## Research Questions

1. What are the core architectural differences between LangGraph and CrewAI?
2. How do the two frameworks compare in terms of ease of use, scalability, and flexibility?
3. Which framework is better suited for specific types of multi-agent tasks?
4. What are the performance characteristics and tradeoffs of each approach?

---

## Scope

- Literature review of both frameworks
- Comparative analysis across key dimensions (architecture, API, tooling, performance)
- At least one practical example per framework
- Benchmarking or complexity analysis with a mathematical formula
- Visualized comparison (graph/chart)
- Structured summary table
- Conclusions and recommendations

---

## Deliverables

1. `output/paper.md` — Markdown draft with all required elements
2. `output/paper.tex` — LaTeX-formatted version with proper academic structure
3. `output/paper.pdf` — Final compiled PDF
4. `output/references.bib` — BibTeX bibliography file

---

## Agent Definitions

The pipeline is executed by three CrewAI agents defined in `src/agents.py`.

### Researcher Agent

| Field | Value |
|---|---|
| **Role** | Senior AI Research Analyst |
| **Goal** | Gather and synthesize comprehensive data on LangGraph and CrewAI: architecture, API, tooling, performance, use cases. Produce structured notes, a comparison table, graph data, at least one mathematical formula, and five BibTeX citations. |
| **Backstory** | A seasoned AI researcher with deep expertise in multi-agent systems and LLM orchestration. Reviews benchmarks and documentation with precision; always backs claims with sources. |
| **Output file** | `output/research_notes.md` |

### Writer Agent

| Field | Value |
|---|---|
| **Role** | Academic Technical Writer |
| **Goal** | Transform research notes into a complete 15–25 page academic paper in English, including cover page, table of contents, all body sections, image placeholder, comparison graph, structured table, mathematical formula, and BibTeX bibliography. |
| **Backstory** | An experienced academic writer with numerous conference papers and journal articles in AI. Maintains formal tone, structures arguments rigorously, and never declares a draft complete until every required element is present. |
| **Output files** | `output/paper.md`, `output/references.bib` |

### Reviewer Agent

| Field | Value |
|---|---|
| **Role** | Academic Peer Reviewer |
| **Goal** | Validate the paper draft against the PRD checklist: cover sheet, TOC, length ≥ 15 pages, image, graph, table, formula, and bibliography ≥ 5 sources. Return actionable feedback for any deficiency, or approve for LaTeX conversion. |
| **Backstory** | A rigorous peer reviewer with experience at top-tier AI conferences. Checks both content quality and structural completeness; never approves a paper missing a required element. |
| **Approval signal** | Appends `## REVIEWER APPROVAL: APPROVED FOR LATEX CONVERSION` to `output/paper.md` |

---

## Crew Orchestration

Implemented in `src/main.py`. Assembles all agents and tasks into a single CrewAI pipeline.

| Field | Value |
|---|---|
| **File** | `src/main.py` |
| **Process** | `Process.sequential` — Researcher → Writer → Reviewer |
| **API key loading** | `python-dotenv` reads `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` from `.env` |
| **Output files** | `output/research_notes.md`, `output/paper.md`, `output/references.bib`, `output/crew_result.md` |
| **Entry point** | `python src/main.py` |
| **Status** | ✅ Implemented |
