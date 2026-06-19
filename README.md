# Academic Paper — Multi-Agent Orchestration

**Course:** אורקסטרקציה של סוכני AI
**Lecturer:** Yoram Segal
**Semester:** Spring 2026
**Student:** Boshra Dahamshy

---

## Project Overview

A three-agent CrewAI pipeline that autonomously researches, writes, and peer-reviews an academic paper comparing **LangGraph** and **CrewAI** as multi-agent orchestration frameworks.

```
Researcher Agent  →  Writer Agent  →  Reviewer Agent
       ↓                  ↓                 ↓
research_notes.md     paper.md         (validates)
                    references.bib
```

---

## Repository Structure

```
ai_agents_hw3/
├── src/
│   ├── main.py              # Crew orchestration entry point
│   ├── agents.py            # Agent definitions (Researcher, Writer, Reviewer)
│   ├── tasks.py             # Task definitions
│   └── generate_images.py   # Generates arch_comparison.png & performance_chart.png
├── output/
│   ├── paper.md             # Markdown paper draft (5,033 words, 12 sections)
│   ├── paper.tex            # LaTeX source (pdflatex, ready to compile)
│   ├── paper.pdf            # Final compiled PDF (15 pages, 514 KB)
│   ├── references.bib       # BibTeX bibliography (5 entries)
│   ├── research_notes.md    # Researcher Agent output
│   ├── crew_result.md       # Raw CrewAI pipeline result
│   └── images/
│       ├── arch_comparison.png    # Architecture diagram (LangGraph DAG vs CrewAI)
│       └── performance_chart.png  # Radar chart (6-dimension comparison)
├── docs/
│   ├── PRD.md               # Product requirements
│   ├── PLAN.md              # Implementation plan & status
│   └── TODO.md              # Task checklist
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/BoshraDh/ai_agents_hw3.git
cd ai_agents_hw3

# 2. Create virtual environment and install dependencies
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt

# 3. Set up API key
copy .env.example .env
# Edit .env and set OPENAI_API_KEY=your_key_here

# 4. Run the pipeline
python src/main.py

# 5. (Optional) Regenerate figures
python src/generate_images.py
```

---

## Compiling the PDF

Requires **pdflatex** (included in MiKTeX / TeX Live):

```bash
cd output
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

> **Note:** `output/paper.pdf` is already compiled and committed (15 pages, 514 KB).
> The images in `output/images/` are also committed — no manual steps required.

---

## Project Status

| Phase | Status |
|---|---|
| Agent pipeline (Researcher → Writer → Reviewer) | ✅ Complete |
| `output/paper.md` — Markdown paper (5,033 words) | ✅ Complete |
| `output/references.bib` — 5 BibTeX entries | ✅ Complete |
| `output/images/` — diagram & chart assets | ✅ Complete (`src/generate_images.py`) |
| `output/paper.tex` — LaTeX source (pdflatex) | ✅ Complete |
| `output/paper.pdf` — final compiled PDF | ✅ Complete (**15 pages, 514 KB**) |
