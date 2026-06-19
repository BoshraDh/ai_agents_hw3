# Product Requirements Document

## Research Paper: LangGraph vs CrewAI

**Author:** Boshra Dahamshy
**Course:** אורקסטרקציה של סוכני AI
**Lecturer:** Yoram Segal
**Semester:** Spring 2026

---

## Goal

Produce a professional academic paper in English comparing LangGraph and CrewAI as multi-agent orchestration frameworks, delivered as a compiled PDF with full LaTeX source.

---

## Required Paper Elements

| Element | Requirement | Status |
|---|---|---|
| Cover Sheet | Course name, Lecturer, Semester, Student Name | ✅ Done |
| Table of Contents | Auto-generated, linked sections | ✅ Done |
| Length | 15–25 pages | ✅ Done |
| Image | At least one architecture diagram or screenshot | ✅ Done (`arch_comparison.png`) |
| Graph | At least one comparison chart (radar/bar) | ✅ Done (`performance_chart.png`) |
| Table | At least one structured comparison table | ✅ Done |
| Formula | At least one mathematical formula with explanation | ✅ Done |
| Bibliography | BibTeX format, minimum 5 sources | ✅ Done (5 entries) |
| Language | English (professional academic tone) | ✅ Done |

---

## Cover Sheet Fields

- **Course:** אורקסטרקציה של סוכני AI
- **Lecturer:** Yoram Segal
- **Semester:** Spring 2026
- **Student Name:** Boshra Dahamshy

---

## Research Questions

1. What are the core architectural differences between LangGraph and CrewAI?
2. How do the two frameworks compare in terms of ease of use, scalability, and flexibility?
3. Which framework is better suited for specific types of multi-agent tasks?
4. What are the performance characteristics and trade-offs of each approach?

---

## Scope

- Literature review of both frameworks
- Comparative analysis across key dimensions (architecture, API, tooling, performance)
- At least one practical example per framework
- Benchmarking or complexity analysis with a mathematical formula
- Visualised comparison (graph/chart)
- Structured summary table
- Conclusions and recommendations

---

## Deliverables

| File | Description | Status |
|---|---|---|
| `output/paper.md` | Markdown draft with all required elements | ✅ Complete |
| `output/paper.tex` | LaTeX source (XeLaTeX, Hebrew cover page, natbib) | ✅ Complete |
| `output/paper.pdf` | Final compiled PDF | 🔲 Pending — awaiting image assets |
| `output/references.bib` | BibTeX bibliography (5 entries) | ✅ Complete |
| `output/research_notes.md` | Researcher Agent output | ✅ Complete |
| `output/crew_result.md` | Raw CrewAI pipeline result | ✅ Complete |

---

## Agent Definitions

The pipeline is executed by three CrewAI agents defined in `src/agents.py`.

### Researcher Agent

| Field | Value |
|---|---|
| **Role** | Senior AI Research Analyst |
| **Goal** | Gather and synthesize comprehensive data on LangGraph and CrewAI: architecture, API, tooling, performance, use cases. Produce structured notes, a comparison table, graph data, at least one mathematical formula, and five BibTeX citations. |
| **Output file** | `output/research_notes.md` |
| **Status** | ✅ Complete |

### Writer Agent

| Field | Value |
|---|---|
| **Role** | Academic Technical Writer |
| **Goal** | Transform research notes into a complete academic paper in English, including cover page, table of contents, all body sections, image placeholder, comparison graph, structured table, mathematical formula, and BibTeX bibliography. |
| **Output files** | `output/paper.md`, `output/references.bib` |
| **Status** | ✅ Complete |

### Reviewer Agent

| Field | Value |
|---|---|
| **Role** | Academic Peer Reviewer |
| **Goal** | Validate the paper draft against the PRD checklist: cover sheet, TOC, image, graph, table, formula, and bibliography ≥ 5 sources. Return actionable feedback for any deficiency, or approve for LaTeX conversion. |
| **Approval signal** | `## REVIEWER APPROVAL: APPROVED FOR LATEX CONVERSION` |
| **Status** | ✅ Complete — approved |

---

## Crew Orchestration

| Field | Value |
|---|---|
| **File** | `src/main.py` |
| **Process** | `Process.sequential` — Researcher → Writer → Reviewer |
| **API key loading** | `python-dotenv` reads `OPENAI_API_KEY` from `.env` |
| **Model** | `gpt-4o` |
| **Output files** | `output/research_notes.md`, `output/paper.md`, `output/references.bib`, `output/crew_result.md` |
| **Entry point** | `python src/main.py` |
| **Status** | ✅ Complete — pipeline executed successfully |

---

## Environment Setup

| File | Purpose | Status |
|---|---|---|
| `requirements.txt` | All Python dependencies | ✅ Created |
| `.env.example` | Placeholder template for API keys | ✅ Created |
| `.env` | Actual API keys — never committed | ✅ Configured (gitignored) |
| `.venv/` | Python virtual environment — never committed | ✅ Configured (gitignored) |

**To run the pipeline:**
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
cp .env.example .env          # then fill in OPENAI_API_KEY
python src/main.py
```
