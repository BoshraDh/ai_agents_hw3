# TODO

## Phase 1: Setup

- [x] Create project folder structure (`/docs`, `/src`, `/output`)
- [x] Initialize git repository
- [x] Create `.gitignore`
- [x] Write `README.md`
- [x] Write initial docs (`PRD.md`, `PLAN.md`, `TODO.md`)
- [x] Update docs for מטלה 3 requirements
- [ ] Set up Python virtual environment (`python -m venv .venv`)
- [ ] Install CrewAI and dependencies (`pip install crewai crewai-tools`)
- [ ] Create `requirements.txt`
- [ ] Verify LaTeX toolchain is available (`pdflatex` or `xelatex`)

## Phase 2: Define Agents

- [x] Define **Researcher Agent** (`src/agents.py`)
  - role: "Senior AI Research Analyst"
  - goal: gather and synthesize LangGraph vs CrewAI data
  - tools: WebSearch, FileWrite
- [x] Define **Writer Agent** (`src/agents.py`)
  - role: "Academic Technical Writer"
  - goal: produce full Markdown paper with all required elements
  - tools: FileWrite
- [x] Define **Reviewer Agent** (`src/agents.py`)
  - role: "Academic Peer Reviewer"
  - goal: validate paper against PRD checklist
  - tools: FileRead, FileWrite
- [ ] Define **Compiler Agent** (`src/main.py` / Step D)
  - role: "Document Engineer"
  - goal: convert Markdown → LaTeX → PDF
  - tools: FileRead, FileWrite, BashTool

## Phase 3: Implement Sequential Chain

- [x] Create Task for each agent stage with clear expected_output (`src/tasks.py`)
- [x] **Implement `src/main.py` and Crew orchestration** (`src/main.py`)
  - Assembles Crew with `Process.sequential`
  - Loads agents and tasks from `agents.py` / `tasks.py`
  - Loads API keys from `.env` via `python-dotenv`
  - Writes final result to `output/crew_result.md`
- [x] Wire tasks into a sequential Crew (`Process.sequential`)
- [ ] **Set up Python environment and install dependencies** ← next pending task
  - `python -m venv .venv`
  - `pip install crewai crewai-tools python-dotenv`
  - Create `requirements.txt`
  - Configure `.env` with API key
- [ ] Test pipeline on a short sample topic
- [ ] Run full pipeline: LangGraph vs CrewAI paper
- [ ] Verify all PRD requirements met in output PDF
  - [ ] Cover sheet
  - [ ] Table of Contents
  - [ ] Image/diagram
  - [ ] Graph/chart
  - [ ] Comparison table
  - [ ] Mathematical formula
  - [ ] BibTeX bibliography (≥ 5 sources)
  - [ ] Length 15–25 pages
- [ ] Final review and submission
