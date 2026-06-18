import os
import sys
from pathlib import Path

# Ensure src/ is on the path so agents/tasks import correctly
# regardless of the working directory the script is launched from.
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Also fix CWD to the project root so relative output_file paths
# in tasks.py resolve to <project>/output/ correctly.
os.chdir(Path(__file__).resolve().parent.parent)

from dotenv import load_dotenv
from crewai import Crew, Process

from tasks import create_tasks

load_dotenv()

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


def build_crew() -> Crew:
    research_task, writing_task, review_task = create_tasks()

    agents = [
        research_task.agent,
        writing_task.agent,
        review_task.agent,
    ]

    return Crew(
        agents=agents,
        tasks=[research_task, writing_task, review_task],
        process=Process.sequential,
        verbose=True,
    )


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "No LLM API key found. Set OPENAI_API_KEY or ANTHROPIC_API_KEY in your .env file."
        )

    print("=" * 60)
    print("Academic Paper CrewAI Pipeline")
    print("Topic: LangGraph vs CrewAI")
    print("=" * 60)

    crew = build_crew()

    print("\n[Step 1/3] Researcher Agent — gathering data...")
    print("[Step 2/3] Writer Agent    — drafting the paper...")
    print("[Step 3/3] Reviewer Agent  — validating the draft...")
    print("\nKicking off the pipeline (Process.sequential)...\n")

    result = crew.kickoff()

    summary_path = OUTPUT_DIR / "crew_result.md"
    summary_path.write_text(str(result), encoding="utf-8")

    print("\n" + "=" * 60)
    print("Pipeline complete.")
    print(f"  Research notes : output/research_notes.md")
    print(f"  Paper draft    : output/paper.md")
    print(f"  Bibliography   : output/references.bib")
    print(f"  Crew summary   : output/crew_result.md")
    print("=" * 60)


if __name__ == "__main__":
    main()
