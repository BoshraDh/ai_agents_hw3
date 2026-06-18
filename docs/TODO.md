# TODO

## Phase 1: Setup

- [x] Create project folder structure (`/docs`, `/src`, `/output`)
- [x] Initialize git repository
- [x] Create `.gitignore`
- [x] Write `README.md`
- [x] Write initial docs (`PRD.md`, `PLAN.md`, `TODO.md`)
- [ ] Set up Python virtual environment
- [ ] Install CrewAI and dependencies (`pip install crewai`)
- [ ] Create `requirements.txt`

## Phase 2: Define Agents

- [ ] Define Research Agent (role, goal, backstory, tools)
- [ ] Define Markdown Writer Agent
- [ ] Define LaTeX Formatter Agent
- [ ] Define PDF Compiler Agent

## Phase 3: Implement Sequential Chain

- [ ] Create tasks for each agent stage
- [ ] Wire tasks into a sequential Crew (`Process.sequential`)
- [ ] Implement `src/main.py` entry point
- [ ] Test end-to-end pipeline with a short sample topic
- [ ] Run full pipeline for LangGraph vs CrewAI paper
- [ ] Review and refine output PDF
