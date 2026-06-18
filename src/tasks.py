from crewai import Task
from agents import create_researcher, create_writer, create_reviewer


def create_tasks():
    researcher = create_researcher()
    writer = create_writer()
    reviewer = create_reviewer()

    research_task = Task(
        description=(
            "Conduct a comprehensive comparative study of LangGraph and CrewAI. "
            "Your output must be a structured Markdown document containing:\n"
            "1. An overview of each framework's architecture and design philosophy.\n"
            "2. A comparison table covering: language, abstraction model, state management, "
            "   tool support, scalability, and community maturity.\n"
            "3. Graph data (as a Markdown table or CSV block) suitable for plotting a "
            "   bar or radar chart comparing the two frameworks across key dimensions.\n"
            "4. At least one mathematical formula that quantifies a meaningful difference "
            "   (e.g., agent coordination overhead O(n) vs O(n²), or a task latency model).\n"
            "5. At least five BibTeX-formatted citations from academic papers, official docs, "
            "   or credible technical reports.\n"
            "6. Notes on real-world use cases where each framework excels or struggles.\n"
            "Save the output to output/research_notes.md."
        ),
        expected_output=(
            "A structured Markdown file (output/research_notes.md) containing: "
            "architecture overview, comparison table, graph data block, at least one "
            "mathematical formula with explanation, five BibTeX citations, and use-case notes."
        ),
        agent=researcher,
        output_file="output/research_notes.md",
    )

    writing_task = Task(
        description=(
            "Using the research notes provided as context, write a complete academic paper "
            "(15–25 pages) in English on 'LangGraph vs CrewAI: A Comparative Study of "
            "Multi-Agent Orchestration Frameworks'. The paper must follow this structure:\n\n"
            "1. Cover Page — Title, Course: אורקסטרקציה של סוכני AI, Lecturer, "
            "   Semester: Spring 2026, Student Name: Boshra Dahamshy.\n"
            "2. Table of Contents — with section numbers and page references.\n"
            "3. Abstract — 150–200 words summarising the paper.\n"
            "4. Introduction — motivation, research questions, paper structure.\n"
            "5. Background: LangGraph — architecture, key concepts, strengths.\n"
            "6. Background: CrewAI — architecture, key concepts, strengths.\n"
            "7. Comparative Analysis — include the structured comparison table from research.\n"
            "8. Performance & Complexity — include the mathematical formula with derivation.\n"
            "9. Architecture Diagram — include an image placeholder with caption: "
            "   ![Architecture Comparison](images/arch_comparison.png).\n"
            "10. Visual Comparison — include a graph/chart placeholder with caption and "
            "    the underlying data table.\n"
            "11. Discussion — interpret findings, limitations, tradeoffs.\n"
            "12. Conclusion — summary and recommendations.\n"
            "13. References — all BibTeX keys cited in-text and listed at the end.\n\n"
            "Also produce output/references.bib with all BibTeX entries.\n"
            "Save the paper to output/paper.md."
        ),
        expected_output=(
            "A complete Markdown academic paper (output/paper.md) with all 13 required "
            "sections, a cover page, table of contents, comparison table, mathematical "
            "formula, image placeholder, graph placeholder with data, and in-text citations. "
            "A separate output/references.bib file with all BibTeX entries."
        ),
        agent=writer,
        context=[research_task],
        output_file="output/paper.md",
    )

    review_task = Task(
        description=(
            "Review the academic paper draft provided as context and validate it against "
            "the following PRD checklist. For each item, mark PASS or FAIL and explain why:\n\n"
            "[ ] Cover page present with all required fields "
            "(title, course, lecturer, semester, student name).\n"
            "[ ] Table of Contents present.\n"
            "[ ] Estimated length is 15–25 pages (check word count ≥ 4,500 words).\n"
            "[ ] At least one image placeholder with caption.\n"
            "[ ] At least one graph/chart placeholder with a data table.\n"
            "[ ] At least one structured comparison table.\n"
            "[ ] At least one mathematical formula with explanation.\n"
            "[ ] Bibliography section present with BibTeX keys cited in-text.\n"
            "[ ] output/references.bib contains at least 5 entries.\n"
            "[ ] Academic English tone throughout — no informal language.\n"
            "[ ] All sections logically connected and coherent.\n\n"
            "If any item is FAIL, provide specific, actionable corrections directly in the "
            "paper text. Once all items pass, append '## REVIEWER APPROVAL: APPROVED FOR "
            "LATEX CONVERSION' to the end of output/paper.md."
        ),
        expected_output=(
            "An annotated version of output/paper.md where all checklist items PASS "
            "and the final line reads '## REVIEWER APPROVAL: APPROVED FOR LATEX CONVERSION'."
        ),
        agent=reviewer,
        context=[research_task, writing_task],
        output_file="output/paper.md",
    )

    return research_task, writing_task, review_task
