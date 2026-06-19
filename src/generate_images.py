"""
Generate the two figures required by paper.tex:
  output/images/arch_comparison.png  — LangGraph DAG vs CrewAI crew hierarchy
  output/images/performance_chart.png — radar chart across 6 dimensions
"""

import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "output" / "images"
OUT.mkdir(parents=True, exist_ok=True)

# ── colour palette ──────────────────────────────────────────────────────────
C_LG   = "#2563EB"   # LangGraph blue
C_CR   = "#DC2626"   # CrewAI red
C_EDGE = "#374151"   # dark grey edges
C_BG   = "#F9FAFB"   # near-white background
C_NODE = "#1E3A5F"   # deep navy node fill


# ════════════════════════════════════════════════════════════════════════════
# FIGURE 1 — Architecture comparison
# ════════════════════════════════════════════════════════════════════════════

def draw_arch():
    fig, (ax_lg, ax_cr) = plt.subplots(
        1, 2, figsize=(14, 7), facecolor=C_BG
    )
    fig.suptitle(
        "Architectural Overview: LangGraph vs CrewAI",
        fontsize=16, fontweight="bold", y=0.97, color=C_EDGE
    )

    # ── shared helpers ───────────────────────────────────────────────────
    def node(ax, x, y, label, color, fontsize=9, radius=0.38):
        circle = plt.Circle((x, y), radius, color=color, zorder=3)
        ax.add_patch(circle)
        ax.text(x, y, label, ha="center", va="center",
                fontsize=fontsize, fontweight="bold",
                color="white", zorder=4, wrap=True,
                multialignment="center")

    def arrow(ax, x0, y0, x1, y1, color=C_EDGE):
        ax.annotate(
            "", xy=(x1, y1), xytext=(x0, y0),
            arrowprops=dict(
                arrowstyle="-|>",
                color=color,
                lw=1.8,
                connectionstyle="arc3,rad=0.0",
            ),
            zorder=2,
        )

    def box(ax, x, y, w, h, label, color, fontsize=9):
        rect = mpatches.FancyBboxPatch(
            (x - w / 2, y - h / 2), w, h,
            boxstyle="round,pad=0.05",
            facecolor=color, edgecolor="white", linewidth=1.5, zorder=3
        )
        ax.add_patch(rect)
        ax.text(x, y, label, ha="center", va="center",
                fontsize=fontsize, fontweight="bold",
                color="white", zorder=4, multialignment="center")

    # ── LangGraph — DAG ──────────────────────────────────────────────────
    ax_lg.set_facecolor(C_BG)
    ax_lg.set_xlim(0, 6); ax_lg.set_ylim(0, 7)
    ax_lg.axis("off")
    ax_lg.set_title("LangGraph — DAG Workflow", fontsize=13,
                    fontweight="bold", color=C_LG, pad=10)

    lg_nodes = {
        "Input\nNode":       (3.0, 6.2),
        "Researcher\nAgent": (1.5, 4.8),
        "Planner\nAgent":    (3.0, 4.8),
        "Writer\nAgent":     (4.5, 4.8),
        "State\nStore":      (3.0, 3.2),
        "Reviewer\nAgent":   (1.5, 1.8),
        "Output\nNode":      (3.0, 0.6),
    }
    lg_edges = [
        ("Input\nNode",       "Researcher\nAgent"),
        ("Input\nNode",       "Planner\nAgent"),
        ("Input\nNode",       "Writer\nAgent"),
        ("Researcher\nAgent", "State\nStore"),
        ("Planner\nAgent",    "State\nStore"),
        ("Writer\nAgent",     "State\nStore"),
        ("State\nStore",      "Reviewer\nAgent"),
        ("State\nStore",      "Output\nNode"),
        ("Reviewer\nAgent",   "Output\nNode"),
    ]
    for (n0, n1) in lg_edges:
        x0, y0 = lg_nodes[n0]; x1, y1 = lg_nodes[n1]
        arrow(ax_lg, x0, y0, x1, y1, color=C_LG)
    for label, (x, y) in lg_nodes.items():
        node(ax_lg, x, y, label, color=C_LG, fontsize=8)

    ax_lg.text(3.0, -0.1,
               "Decentralised state via external store\nO(n) coordination overhead",
               ha="center", va="bottom", fontsize=8, color=C_EDGE,
               style="italic")

    # ── CrewAI — Crew Hierarchy ───────────────────────────────────────────
    ax_cr.set_facecolor(C_BG)
    ax_cr.set_xlim(0, 6); ax_cr.set_ylim(0, 7)
    ax_cr.axis("off")
    ax_cr.set_title("CrewAI — Crew Hierarchy", fontsize=13,
                    fontweight="bold", color=C_CR, pad=10)

    # Manager box at top
    box(ax_cr, 3.0, 6.0, 2.2, 0.7, "Crew Manager\n(Process Controller)", C_CR, fontsize=8)

    # Three agents in middle row
    agent_colors = ["#B91C1C", "#DC2626", "#EF4444"]
    agent_labels = ["Researcher\nAgent", "Writer\nAgent", "Reviewer\nAgent"]
    agent_positions = [(1.1, 4.2), (3.0, 4.2), (4.9, 4.2)]
    for (ax_, ay_), lbl, col in zip(agent_positions, agent_labels, agent_colors):
        box(ax_cr, ax_, ay_, 1.6, 0.75, lbl, col, fontsize=8)
        arrow(ax_cr, 3.0, 5.65, ax_, 4.575, color=C_CR)

    # Shared in-memory state
    box(ax_cr, 3.0, 2.6, 2.8, 0.7, "Shared In-Memory State\n(Centralised)", "#7F1D1D", fontsize=8)
    for ax_, ay_ in agent_positions:
        arrow(ax_cr, ax_, ay_ - 0.375, 3.0, 2.95, color="#7F1D1D")

    # Tools row
    tool_labels = ["Web\nSearch", "File\nRead/Write", "LLM\nCalls"]
    tool_positions = [(1.1, 1.2), (3.0, 1.2), (4.9, 1.2)]
    for (tx, ty), tlbl in zip(tool_positions, tool_labels):
        box(ax_cr, tx, ty, 1.4, 0.6, tlbl, "#6B7280", fontsize=7.5)
        arrow(ax_cr, 3.0, 2.25, tx, 1.5, color="#6B7280")

    ax_cr.text(3.0, 0.35,
               "Centralised state, role-based delegation\nO(n²) coordination overhead",
               ha="center", va="bottom", fontsize=8, color=C_EDGE,
               style="italic")

    plt.tight_layout(rect=[0, 0.04, 1, 0.95])
    out_path = OUT / "arch_comparison.png"
    fig.savefig(out_path, dpi=180, bbox_inches="tight", facecolor=C_BG)
    plt.close(fig)
    print(f"Saved: {out_path}")


# ════════════════════════════════════════════════════════════════════════════
# FIGURE 2 — Radar / spider chart
# ════════════════════════════════════════════════════════════════════════════

def draw_radar():
    categories = [
        "Language\nSupport",
        "Abstraction\nModel",
        "State\nManagement",
        "Tool\nSupport",
        "Scalability",
        "Community\nMaturity",
    ]
    lg_scores = [4, 5, 5, 4, 5, 3]
    cr_scores = [5, 4, 3, 4, 3, 5]

    N = len(categories)
    angles = [n / N * 2 * math.pi for n in range(N)]
    angles += angles[:1]  # close the polygon

    lg_vals = lg_scores + lg_scores[:1]
    cr_vals = cr_scores + cr_scores[:1]

    fig, ax = plt.subplots(figsize=(8, 8),
                           subplot_kw=dict(polar=True),
                           facecolor=C_BG)
    ax.set_facecolor(C_BG)

    # Grid rings
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"],
                       fontsize=8, color="#9CA3AF")

    # Draw spokes
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10.5, fontweight="bold",
                       color=C_EDGE)
    ax.tick_params(axis="x", pad=14)

    # LangGraph polygon
    ax.plot(angles, lg_vals, color=C_LG, linewidth=2.5, linestyle="solid",
            zorder=3)
    ax.fill(angles, lg_vals, color=C_LG, alpha=0.20, zorder=2)

    # CrewAI polygon
    ax.plot(angles, cr_vals, color=C_CR, linewidth=2.5, linestyle="solid",
            zorder=3)
    ax.fill(angles, cr_vals, color=C_CR, alpha=0.20, zorder=2)

    # Data-point markers
    ax.scatter(angles[:-1], lg_scores, color=C_LG, s=80, zorder=5)
    ax.scatter(angles[:-1], cr_scores, color=C_CR, s=80, zorder=5)

    # Score labels
    for angle, lg_v, cr_v in zip(angles[:-1], lg_scores, cr_scores):
        ax.text(angle, lg_v + 0.35, str(lg_v),
                ha="center", va="center", fontsize=8,
                color=C_LG, fontweight="bold")
        ax.text(angle, cr_v - 0.45, str(cr_v),
                ha="center", va="center", fontsize=8,
                color=C_CR, fontweight="bold")

    # Legend
    ax.legend(
        handles=[
            mpatches.Patch(color=C_LG, alpha=0.7, label="LangGraph"),
            mpatches.Patch(color=C_CR, alpha=0.7, label="CrewAI"),
        ],
        loc="lower center",
        bbox_to_anchor=(0.5, -0.12),
        ncol=2,
        fontsize=12,
        frameon=True,
        framealpha=0.9,
    )

    ax.set_title(
        "LangGraph vs CrewAI — Multi-Dimensional Comparison\n(Scale: 1 = Low, 5 = High)",
        fontsize=13, fontweight="bold", color=C_EDGE,
        pad=24
    )

    # Ring labels (1–5) inside
    for r in range(1, 6):
        ax.text(0, r + 0.08, str(r), ha="center", va="bottom",
                fontsize=7, color="#9CA3AF")

    out_path = OUT / "performance_chart.png"
    fig.savefig(out_path, dpi=180, bbox_inches="tight", facecolor=C_BG)
    plt.close(fig)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    draw_arch()
    draw_radar()
    print("Both images generated successfully.")
