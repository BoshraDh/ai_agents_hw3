import math
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

OUT = Path(__file__).resolve().parent.parent / "output" / "images"
OUT.mkdir(parents=True, exist_ok=True)
C_LG, C_CR, C_EDGE, C_BG = "#2563EB", "#DC2626", "#374151", "#F9FAFB"


def draw_arch():
    fig, (ax_lg, ax_cr) = plt.subplots(1, 2, figsize=(14, 7), facecolor=C_BG)
    fig.suptitle("Architectural Overview: LangGraph vs CrewAI",
                 fontsize=16, fontweight="bold", y=0.97, color=C_EDGE)

    def node(ax, x, y, label, color, fontsize=9, r=0.38):
        ax.add_patch(plt.Circle((x, y), r, color=color, zorder=3))
        ax.text(x, y, label, ha="center", va="center", fontsize=fontsize,
                fontweight="bold", color="white", zorder=4,
                wrap=True, multialignment="center")

    def arrow(ax, x0, y0, x1, y1, color=C_EDGE):
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0), zorder=2,
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8,
                                   connectionstyle="arc3,rad=0.0"))

    def box(ax, x, y, w, h, label, color, fontsize=9):
        ax.add_patch(mpatches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h, boxstyle="round,pad=0.05",
            facecolor=color, edgecolor="white", linewidth=1.5, zorder=3))
        ax.text(x, y, label, ha="center", va="center", fontsize=fontsize,
                fontweight="bold", color="white", zorder=4, multialignment="center")

    for ax in (ax_lg, ax_cr):
        ax.set_facecolor(C_BG); ax.set_xlim(0, 6); ax.set_ylim(0, 7); ax.axis("off")

    ax_lg.set_title("LangGraph — DAG Workflow", fontsize=13,
                    fontweight="bold", color=C_LG, pad=10)
    lg = {"Input\nNode":(3,6.2), "Researcher\nAgent":(1.5,4.8),
          "Planner\nAgent":(3,4.8), "Writer\nAgent":(4.5,4.8),
          "State\nStore":(3,3.2), "Reviewer\nAgent":(1.5,1.8), "Output\nNode":(3,0.6)}
    for n0, n1 in [("Input\nNode","Researcher\nAgent"),("Input\nNode","Planner\nAgent"),
                   ("Input\nNode","Writer\nAgent"),("Researcher\nAgent","State\nStore"),
                   ("Planner\nAgent","State\nStore"),("Writer\nAgent","State\nStore"),
                   ("State\nStore","Reviewer\nAgent"),("State\nStore","Output\nNode"),
                   ("Reviewer\nAgent","Output\nNode")]:
        arrow(ax_lg, *lg[n0], *lg[n1], color=C_LG)
    for label, (x, y) in lg.items():
        node(ax_lg, x, y, label, C_LG, fontsize=8)
    ax_lg.text(3, -0.1, "Decentralised state via external store\nO(n) coordination overhead",
               ha="center", va="bottom", fontsize=8, color=C_EDGE, style="italic")

    ax_cr.set_title("CrewAI — Crew Hierarchy", fontsize=13,
                    fontweight="bold", color=C_CR, pad=10)
    box(ax_cr, 3, 6, 2.2, 0.7, "Crew Manager\n(Process Controller)", C_CR, fontsize=8)
    agents = [("Researcher\nAgent","#B91C1C",(1.1,4.2)),
              ("Writer\nAgent","#DC2626",(3,4.2)),
              ("Reviewer\nAgent","#EF4444",(4.9,4.2))]
    for lbl, col, (ax_, ay_) in agents:
        box(ax_cr, ax_, ay_, 1.6, 0.75, lbl, col, fontsize=8)
        arrow(ax_cr, 3, 5.65, ax_, 4.575, color=C_CR)
    box(ax_cr, 3, 2.6, 2.8, 0.7, "Shared In-Memory State\n(Centralised)", "#7F1D1D", fontsize=8)
    for _, _, (ax_, ay_) in agents:
        arrow(ax_cr, ax_, ay_ - 0.375, 3, 2.95, color="#7F1D1D")
    for lbl, (tx, ty) in [("Web\nSearch",(1.1,1.2)),("File\nRead/Write",(3,1.2)),
                           ("LLM\nCalls",(4.9,1.2))]:
        box(ax_cr, tx, ty, 1.4, 0.6, lbl, "#6B7280", fontsize=7.5)
        arrow(ax_cr, 3, 2.25, tx, 1.5, color="#6B7280")
    ax_cr.text(3, 0.35, "Centralised state, role-based delegation\nO(n²) coordination overhead",
               ha="center", va="bottom", fontsize=8, color=C_EDGE, style="italic")

    plt.tight_layout(rect=[0, 0.04, 1, 0.95])
    fig.savefig(OUT / "arch_comparison.png", dpi=180, bbox_inches="tight", facecolor=C_BG)
    plt.close(fig)
    print(f"Saved: {OUT / 'arch_comparison.png'}")


def draw_radar():
    categories = ["Language\nSupport", "Abstraction\nModel", "State\nManagement",
                  "Tool\nSupport", "Scalability", "Community\nMaturity"]
    lg_scores, cr_scores = [4, 5, 5, 4, 5, 3], [5, 4, 3, 4, 3, 5]
    N = len(categories)
    angles = [n / N * 2 * math.pi for n in range(N)] + [0]
    lg_vals, cr_vals = lg_scores + lg_scores[:1], cr_scores + cr_scores[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True), facecolor=C_BG)
    ax.set_facecolor(C_BG); ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=8, color="#9CA3AF")
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10.5, fontweight="bold", color=C_EDGE)
    ax.tick_params(axis="x", pad=14)
    for vals, color in [(lg_vals, C_LG), (cr_vals, C_CR)]:
        ax.plot(angles, vals, color=color, linewidth=2.5, zorder=3)
        ax.fill(angles, vals, color=color, alpha=0.20, zorder=2)
    ax.scatter(angles[:-1], lg_scores, color=C_LG, s=80, zorder=5)
    ax.scatter(angles[:-1], cr_scores, color=C_CR, s=80, zorder=5)
    for angle, lg_v, cr_v in zip(angles[:-1], lg_scores, cr_scores):
        ax.text(angle, lg_v + 0.35, str(lg_v), ha="center", va="center",
                fontsize=8, color=C_LG, fontweight="bold")
        ax.text(angle, cr_v - 0.45, str(cr_v), ha="center", va="center",
                fontsize=8, color=C_CR, fontweight="bold")
    ax.legend(handles=[mpatches.Patch(color=C_LG, alpha=0.7, label="LangGraph"),
                       mpatches.Patch(color=C_CR, alpha=0.7, label="CrewAI")],
              loc="lower center", bbox_to_anchor=(0.5, -0.12), ncol=2,
              fontsize=12, frameon=True, framealpha=0.9)
    ax.set_title("LangGraph vs CrewAI — Multi-Dimensional Comparison\n"
                 "(Scale: 1 = Low, 5 = High)",
                 fontsize=13, fontweight="bold", color=C_EDGE, pad=24)
    for r in range(1, 6):
        ax.text(0, r + 0.08, str(r), ha="center", va="bottom",
                fontsize=7, color="#9CA3AF")
    fig.savefig(OUT / "performance_chart.png", dpi=180, bbox_inches="tight", facecolor=C_BG)
    plt.close(fig)
    print(f"Saved: {OUT / 'performance_chart.png'}")


if __name__ == "__main__":
    draw_arch()
    draw_radar()
    print("Both images generated successfully.")
