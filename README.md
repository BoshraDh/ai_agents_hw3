# Multi-Agent Orchestration — Academic Paper Project

**Course:** אורקסטרקציה של סוכני AI (AI Agent Orchestration)
**Lecturer:** Yoram Segal
**Semester:** Spring 2026
**Student:** Boshra Dahamshy
**Repository:** https://github.com/BoshraDh/ai_agents_hw3

---

## Overview and Purpose

This project implements a **fully autonomous, multi-agent pipeline** using the **CrewAI** framework to produce a 15-page academic paper comparing two leading AI orchestration frameworks: **LangGraph** and **CrewAI**.

The pipeline demonstrates real-world multi-agent orchestration: three specialised agents — a Researcher, a Writer, and a Reviewer — collaborate sequentially, each receiving the previous agent's output and contributing its own, with no human intervention in the content generation process.

The final deliverable is a compiled PDF academic paper (`output/paper.pdf`) complete with architecture diagrams, radar charts, mathematical complexity analysis, comparison tables, and a BibTeX bibliography.

---

## Architecture

### Agent Pipeline (Sequential)

```
┌─────────────────────┐
│   Researcher Agent  │  Gathers data, produces structured notes + BibTeX citations
│  (Senior Analyst)   │  Output: output/research_notes.md
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│    Writer Agent     │  Converts research into a full academic paper draft
│  (Technical Writer) │  Output: output/paper.md, output/references.bib
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Reviewer Agent    │  Validates paper against PRD checklist, approves or requests fixes
│  (Peer Reviewer)    │  Output: inline feedback / approval signal in paper.md
└─────────────────────┘
         │
         ▼
  [Post-pipeline]
  LaTeX conversion + image generation + PDF compilation
  Output: output/paper.tex, output/paper.pdf
```

### Modular Code Structure

```
ai_agents_hw3/
│
├── src/                          # All executable source code
│   ├── main.py                   # Entry point: builds Crew and runs pipeline
│   ├── agents.py                 # Agent definitions (role, goal, backstory, tools)
│   ├── tasks.py                  # Task definitions (description, expected_output)
│   └── generate_images.py        # Programmatic figure generation (matplotlib)
│
├── output/                       # All pipeline and compilation outputs
│   ├── paper.md                  # Markdown draft (5,033 words, 12 sections)
│   ├── paper.tex                 # LaTeX source (pdflatex engine)
│   ├── paper.pdf                 # Final compiled PDF (15 pages, 514 KB)
│   ├── references.bib            # BibTeX bibliography (5 entries)
│   ├── research_notes.md         # Researcher Agent output
│   ├── crew_result.md            # Raw CrewAI final result
│   └── images/
│       ├── arch_comparison.png   # Dual-panel architecture diagram
│       └── performance_chart.png # Radar chart — 6-dimension comparison
│
├── docs/                         # Project planning and requirements documents
│   ├── PRD.md                    # Product Requirements Document
│   ├── PLAN.md                   # Implementation plan with step-by-step status
│   └── TODO.md                   # Task checklist (all phases)
│
├── requirements.txt              # Python dependencies
├── .env.example                  # API key template (safe to commit)
├── .gitignore                    # Excludes .env, .venv/, __pycache__/, LaTeX artifacts
└── README.md                     # This file
```

---

## Setup and Installation

### Prerequisites

- Python 3.10 or higher
- An OpenAI API key with access to `gpt-4o`
- (Optional, for PDF recompilation) MiKTeX or TeX Live with `pdflatex`

### Step 1 — Clone the repository

```bash
git clone https://github.com/BoshraDh/ai_agents_hw3.git
cd ai_agents_hw3
```

### Step 2 — Create a virtual environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Configure environment variables

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

Open `.env` in any text editor and set your key:

```
OPENAI_API_KEY=sk-...your-key-here...
```

> `.env` is listed in `.gitignore` and will never be committed to the repository.

### Step 5 — Run the agent pipeline

```bash
python src/main.py
```

The pipeline will execute three agents sequentially (Researcher → Writer → Reviewer) and write all outputs to `output/`. Expect 3–8 minutes of runtime depending on API response times.

### Step 6 — (Optional) Regenerate figures

```bash
python src/generate_images.py
```

Regenerates `output/images/arch_comparison.png` and `output/images/performance_chart.png` using matplotlib. No API key required.

### Step 7 — (Optional) Recompile the PDF

```bash
cd output
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

> The compiled `output/paper.pdf` (15 pages, 514 KB) is already committed to the repository. Recompilation is only needed if `paper.tex` is modified.

---

## Documentation

All project planning documents are located in the `docs/` folder:

| File | Purpose |
|---|---|
| [`docs/PRD.md`](docs/PRD.md) | Product Requirements Document — defines all paper elements, agent goals, deliverables, and acceptance criteria |
| [`docs/PLAN.md`](docs/PLAN.md) | Implementation Plan — five-phase workflow (Setup → Agents → Pipeline → Execution → LaTeX), with per-step status and compile instructions |
| [`docs/TODO.md`](docs/TODO.md) | Task Checklist — granular phase-by-phase checklist; all items marked complete for final submission |

---

## Output Files

| File | Description |
|---|---|
| `output/paper.pdf` | **Primary deliverable** — 15-page compiled PDF |
| `output/paper.tex` | LaTeX source (pdflatex, `article` class, `natbib`, `fancyvrb`, `booktabs`) |
| `output/paper.md` | Markdown draft produced by the Writer Agent (5,033 words) |
| `output/references.bib` | BibTeX bibliography with 5 entries |
| `output/research_notes.md` | Structured research notes produced by the Researcher Agent |
| `output/crew_result.md` | Final raw output returned by `crew.kickoff()` |
| `output/images/arch_comparison.png` | Architecture diagram: LangGraph DAG vs CrewAI hierarchy |
| `output/images/performance_chart.png` | Radar chart: 6-dimension framework comparison |

---

## Project Status

| Phase | Description | Status |
|---|---|---|
| 1 | Project setup, environment, git | ✅ Complete |
| 2 | Agent definitions (Researcher, Writer, Reviewer) | ✅ Complete |
| 3 | Sequential crew implementation (`src/main.py`) | ✅ Complete |
| 4 | Pipeline execution and output validation | ✅ Complete |
| 5 | LaTeX conversion, image generation, PDF compilation | ✅ Complete |

---

## Credits and Contribution

> **This project is a demonstration of autonomous multi-agent AI systems.**

The academic paper content — including all research notes, the full paper draft, section text, comparison tables, mathematical analysis, code examples, bibliography entries, and the peer review — was **generated entirely by autonomous AI agents** running within the CrewAI framework. The agents used `gpt-4o` as their underlying language model.

Human contributions in this project were limited to:

- Designing the agent roles, goals, and task descriptions (`src/agents.py`, `src/tasks.py`)
- Implementing the CrewAI pipeline orchestration (`src/main.py`)
- Writing the programmatic figure generation code (`src/generate_images.py`)
- Authoring the LaTeX template and compiling the final PDF (`output/paper.tex`)
- Writing all project documentation (`docs/PRD.md`, `docs/PLAN.md`, `docs/TODO.md`)

**Student:** Boshra Dahamshy
**Course:** אורקסטרקציה של סוכני AI, Spring 2026, Lecturer: Yoram Segal
