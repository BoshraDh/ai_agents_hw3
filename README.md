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
│   ├── main.py          # Crew orchestration entry point
│   ├── agents.py        # Agent definitions (Researcher, Writer, Reviewer)
│   └── tasks.py         # Task definitions
├── output/
│   ├── paper.md         # Markdown paper draft
│   ├── paper.tex        # LaTeX source (XeLaTeX, ready to compile)
│   ├── references.bib   # BibTeX bibliography (5 entries)
│   ├── research_notes.md # Researcher Agent output
│   └── crew_result.md   # Raw CrewAI pipeline result
├── docs/
│   ├── PRD.md           # Product requirements
│   ├── PLAN.md          # Implementation plan & status
│   └── TODO.md          # Task checklist
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
```

---

## Compiling the PDF

Requires **XeLaTeX** (included in MikTeX):

```bash
cd output
xelatex paper.tex
bibtex paper
xelatex paper.tex
xelatex paper.tex
```

> **Note:** Before compiling, place `images/arch_comparison.png` and
> `images/performance_chart.png` in the `output/` folder and replace
> the `\fbox` placeholders in `paper.tex` with `\includegraphics`.

---

## Project Status

| Phase | Status |
|---|---|
| Agent pipeline (Researcher → Writer → Reviewer) | ✅ Complete |
| `output/paper.md` — Markdown paper | ✅ Complete |
| `output/references.bib` — 5 BibTeX entries | ✅ Complete |
| `output/paper.tex` — LaTeX source | ✅ Complete |
| `output/images/` — diagram & chart assets | 🔲 Manual step |
| `output/paper.pdf` — final compiled PDF | 🔲 Pending |
