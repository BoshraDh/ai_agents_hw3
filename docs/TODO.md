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

- [ ] Define **Researcher Agent**
  - role: "Senior AI Research Analyst"
  - goal: gather and synthesize LangGraph vs CrewAI data
  - tools: WebSearch, FileWrite
- [ ] Define **Writer Agent**
  - role: "Academic Technical Writer"
  - goal: produce full Markdown paper with all required elements
  - tools: FileWrite
- [ ] Define **Reviewer Agent**
  - role: "Academic Peer Reviewer"
  - goal: validate paper against PRD checklist
  - tools: FileRead, FileWrite
- [ ] Define **Compiler Agent**
  - role: "Document Engineer"
  - goal: convert Markdown → LaTeX → PDF
  - tools: FileRead, FileWrite, BashTool

## Phase 3: Implement Sequential Chain

- [ ] Create Task for each agent stage with clear expected_output
- [ ] Wire tasks into a sequential Crew (`Process.sequential`)
- [ ] Implement `src/main.py` entry point
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
