# TODO

## Phase 1: Setup

- [x] Create project folder structure (`/docs`, `/src`, `/output`)
- [x] Initialize git repository
- [x] Create `.gitignore` (excludes `.venv/`, `.env`, `__pycache__/`, `.env.example`)
- [x] Write `README.md`
- [x] Write initial docs (`PRD.md`, `PLAN.md`, `TODO.md`)
- [x] Update docs for מטלה 3 requirements
- [x] Set up Python virtual environment (`.venv/`)
- [x] Install CrewAI and dependencies (`pip install -r requirements.txt`)
- [x] Create `requirements.txt`
- [ ] Verify LaTeX toolchain is available (`xelatex` — required for Hebrew support)

## Phase 2: Define Agents

- [x] Define **Researcher Agent** (`src/agents.py`)
  - role: "Senior AI Research Analyst"
  - goal: gather and synthesize LangGraph vs CrewAI data
- [x] Define **Writer Agent** (`src/agents.py`)
  - role: "Academic Technical Writer"
  - goal: produce full Markdown paper with all required elements
- [x] Define **Reviewer Agent** (`src/agents.py`)
  - role: "Academic Peer Reviewer"
  - goal: validate paper against PRD checklist
- [ ] Define **Compiler Agent** — optional future enhancement
  - goal: automate Markdown → LaTeX → PDF conversion inside the pipeline

## Phase 3: Implement Sequential Chain

- [x] Create Task for each agent stage with clear `expected_output` (`src/tasks.py`)
- [x] Implement `src/main.py` and Crew orchestration
  - Assembles Crew with `Process.sequential`
  - Loads agents and tasks from `agents.py` / `tasks.py`
  - Loads API keys from `.env` via `python-dotenv`
  - Writes final result to `output/crew_result.md`
- [x] Wire tasks into a sequential Crew (`Process.sequential`)
- [x] Set up Python environment and install dependencies
  - `requirements.txt` created (crewai, crewai-tools, openai, anthropic, langchain, python-dotenv, pypdf)
  - `.env.example` with placeholders for all required API keys

## Phase 4: Pipeline Execution & Validation

- [x] **First execution** — `python src/main.py` — completed successfully (gpt-4o, sequential)
- [x] **Validate `output/research_notes.md`** — created by Researcher Agent ✅
- [x] **Validate `output/paper.md`** — created by Writer Agent, approved by Reviewer ✅
- [x] **Validate `output/references.bib`** — 5 BibTeX entries present ✅
- [x] **Validate `output/crew_result.md`** — final crew summary written ✅
- [x] **Post-run quality fix** — removed AI markdown wrappers, fixed lecturer name, fixed factual error (CrewAI language), aligned `\cite{}` keys with `references.bib`

## Phase 5: LaTeX Conversion

- [x] Create `output/paper.tex` — full XeLaTeX source with:
  - Cover page (Hebrew course name, Yoram Segal, Spring 2026, Boshra Dahamshy)
  - Auto-generated Table of Contents
  - All body sections with `\section{}` / `\subsection{}`
  - Comparison table (`booktabs` + `tabularx`)
  - Math equations (`\begin{equation}`) with cross-references
  - Figure placeholders for `images/arch_comparison.png` and `images/performance_chart.png`
  - Score table for radar chart data
  - `natbib` bibliography linked to `references.bib`
- [ ] **Create `output/images/arch_comparison.png`** — architecture diagram (manual step)
- [ ] **Create `output/images/performance_chart.png`** — radar/bar chart (manual step)
- [ ] Replace `\fbox` placeholders in `paper.tex` with `\includegraphics` once images exist
- [ ] Compile `paper.tex` → `paper.pdf`:
  ```
  xelatex paper.tex
  bibtex paper
  xelatex paper.tex
  xelatex paper.tex
  ```
- [ ] Verify PDF meets all PRD requirements:
  - [ ] Cover sheet (course, lecturer, semester, author)
  - [ ] Table of Contents with page numbers
  - [ ] At least one image/diagram
  - [ ] At least one graph/chart
  - [ ] Comparison table
  - [ ] Mathematical formula with cross-references
  - [ ] BibTeX bibliography (≥ 5 sources)
  - [ ] Length 15–25 pages
- [ ] Final review and GitHub submission
