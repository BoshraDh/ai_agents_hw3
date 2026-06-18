# Project Plan

## Workflow: Sequential Agent Pipeline

The paper is produced through a four-stage sequential workflow, each stage handled by a dedicated CrewAI agent.

```
Research -> Markdown -> LaTeX -> PDF
```

### Stage 1: Research

- Agent collects and synthesizes information on LangGraph and CrewAI
- Output: structured research notes and citations

### Stage 2: Markdown

- Agent drafts the full academic paper in Markdown format
- Sections: Abstract, Introduction, Background, Comparison, Conclusion, References
- Output: `output/paper.md`

### Stage 3: LaTeX

- Agent converts the Markdown draft to a properly formatted LaTeX document
- Applies academic paper template (article class)
- Output: `output/paper.tex`

### Stage 4: PDF

- Agent compiles the LaTeX source to a PDF
- Output: `output/paper.pdf`

## Dependencies

Each stage depends on the successful completion of the previous stage (strict sequential chain).
