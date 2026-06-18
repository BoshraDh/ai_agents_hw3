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
- [ ] **Implement `src/main.py` and Crew orchestration** ← next pending task
  - Assemble Crew with `Process.sequential`
  - Load agents and tasks from `agents.py` / `tasks.py`
  - Add `.env` loading for API keys
  - Add Compiler agent (Step D: Markdown → LaTeX → PDF)
- [ ] Wire tasks into a sequential Crew (`Process.sequential`)
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
