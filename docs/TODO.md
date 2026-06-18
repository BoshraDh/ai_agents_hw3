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
- [x] **Set up Python environment and install dependencies**
  - Created `requirements.txt` (crewai, crewai-tools, openai, anthropic, langchain, python-dotenv, pypdf)
  - Created `.env.example` with placeholders for all required API keys
  - Copy `.env.example` → `.env` and fill in your keys before running
- [ ] **First execution and testing** ← next pending task
  - `python -m venv .venv && .venv\Scripts\activate`
  - `pip install -r requirements.txt`
  - Copy `.env.example` to `.env` and set `OPENAI_API_KEY`
  - Run `python src/main.py` and verify all output files are generated
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
