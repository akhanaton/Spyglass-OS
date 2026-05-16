"""
Diagram Generator

Generates visual assets for ExamPilot content in two output formats:
  - Matplotlib PNG: mathematical concept visualizations
  - Excalidraw JSON: structural flowcharts (learning paths, timelines, decision trees)

ExamPilot color palette:
  primary    : #1a1a2e
  accent     : #e94560
  background : #f8f9fa
  grid       : #e0e0e0

Asset output directory: marketing/pipelines/assets/
"""

import os
import sys
import json
import math
import argparse
from pathlib import Path
from typing import Callable, Optional, Union

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


# ---------------------------------------------------------------------------
# ExamPilot style constants
# ---------------------------------------------------------------------------

EP_PRIMARY = "#1a1a2e"
EP_ACCENT = "#e94560"
EP_BACKGROUND = "#f8f9fa"
EP_GRID = "#e0e0e0"
EP_SECONDARY = "#16213e"
EP_LIGHT_ACCENT = "#f5a7b5"

DEFAULT_ASSET_DIR = Path("marketing/pipelines/assets")


# ---------------------------------------------------------------------------
# Matplotlib diagrams
# ---------------------------------------------------------------------------

def generate_math_diagram(
    diagram_type: str,
    params: dict,
    output_path: str,
    title: str = "",
    x_label: str = "x",
    y_label: str = "y",
) -> str:
    """
    Generate a mathematical diagram as a PNG using matplotlib.

    Supported diagram_type values:
      function_plot, integration_area, normal_distribution,
      binomial_distribution, scatter_with_regression

    Returns the absolute path of the saved PNG file.
    """
    try:
        import matplotlib
        matplotlib.use("Agg")  # non-interactive backend
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError:
        print("Error: matplotlib and numpy are required for math diagrams.")
        print("Install with: pip install matplotlib numpy")
        sys.exit(1)

    fig, ax = plt.subplots(figsize=(8, 5), facecolor=EP_BACKGROUND)
    ax.set_facecolor(EP_BACKGROUND)

    # Apply style
    ax.grid(True, color=EP_GRID, linewidth=0.8, linestyle="--", alpha=0.7)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(EP_PRIMARY)
    ax.spines["bottom"].set_color(EP_PRIMARY)
    ax.tick_params(colors=EP_PRIMARY)
    ax.xaxis.label.set_color(EP_PRIMARY)
    ax.yaxis.label.set_color(EP_PRIMARY)

    if diagram_type == "function_plot":
        _plot_function(ax, params, np)
    elif diagram_type == "integration_area":
        _plot_integration_area(ax, params, np)
    elif diagram_type == "normal_distribution":
        _plot_normal_distribution(ax, params, np)
    elif diagram_type == "binomial_distribution":
        _plot_binomial_distribution(ax, params, np)
    elif diagram_type == "scatter_with_regression":
        _plot_scatter_regression(ax, params, np)
    else:
        plt.close(fig)
        raise ValueError(f"Unknown diagram_type: '{diagram_type}'. Valid: function_plot, integration_area, normal_distribution, binomial_distribution, scatter_with_regression")

    if title:
        ax.set_title(title, color=EP_PRIMARY, fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel(x_label, color=EP_PRIMARY, fontsize=11)
    ax.set_ylabel(y_label, color=EP_PRIMARY, fontsize=11)

    plt.tight_layout()

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(out), dpi=150, bbox_inches="tight", facecolor=EP_BACKGROUND)
    plt.close(fig)

    print(f"Math diagram saved: {out.resolve()}")
    return str(out.resolve())


def _plot_function(ax, params: dict, np) -> None:
    """Plot a function from points list or lambda string."""
    points = params.get("points")
    if points:
        x_vals = [p[0] for p in points]
        y_vals = [p[1] for p in points]
    else:
        x_range = params.get("x_range", [-5, 5])
        x_vals = np.linspace(x_range[0], x_range[1], 300)
        # Support simple polynomial via coefficients [a, b, c] for ax^2 + bx + c
        coefficients = params.get("coefficients")
        if coefficients:
            y_vals = np.polyval(coefficients, x_vals)
        else:
            y_vals = x_vals  # default: identity

    ax.plot(x_vals, y_vals, color=EP_ACCENT, linewidth=2.5, label=params.get("label", "f(x)"))
    ax.axhline(0, color=EP_PRIMARY, linewidth=0.8)
    ax.axvline(0, color=EP_PRIMARY, linewidth=0.8)
    if params.get("label"):
        ax.legend(facecolor=EP_BACKGROUND, edgecolor=EP_PRIMARY)


def _plot_integration_area(ax, params: dict, np) -> None:
    """Plot f(x) with shaded area under curve between a and b."""
    coefficients = params.get("coefficients", [1, 0, 0])  # default: x^2
    a = params.get("a", 0)
    b = params.get("b", 2)

    x_full = np.linspace(a - 2, b + 2, 400)
    y_full = np.polyval(coefficients, x_full)
    ax.plot(x_full, y_full, color=EP_ACCENT, linewidth=2.5, label="f(x)")

    x_shade = np.linspace(a, b, 200)
    y_shade = np.polyval(coefficients, x_shade)
    ax.fill_between(x_shade, y_shade, alpha=0.25, color=EP_ACCENT, label=f"Area [{a}, {b}]")

    ax.axvline(a, color=EP_PRIMARY, linewidth=1.2, linestyle="--", alpha=0.7)
    ax.axvline(b, color=EP_PRIMARY, linewidth=1.2, linestyle="--", alpha=0.7)
    ax.axhline(0, color=EP_PRIMARY, linewidth=0.8)
    ax.legend(facecolor=EP_BACKGROUND, edgecolor=EP_PRIMARY)


def _plot_normal_distribution(ax, params: dict, np) -> None:
    """Plot a normal distribution curve."""
    mu = params.get("mean", 0)
    sigma = params.get("std", 1)
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

    ax.plot(x, y, color=EP_ACCENT, linewidth=2.5, label=f"N({mu}, {sigma}²)")
    ax.fill_between(x, y, alpha=0.15, color=EP_ACCENT)
    ax.axvline(mu, color=EP_PRIMARY, linewidth=1.5, linestyle="--", label=f"μ = {mu}")

    # Mark ±1σ and ±2σ
    for n, alpha in [(1, 0.3), (2, 0.15)]:
        ax.axvline(mu - n * sigma, color=EP_SECONDARY, linewidth=0.8, linestyle=":", alpha=0.7)
        ax.axvline(mu + n * sigma, color=EP_SECONDARY, linewidth=0.8, linestyle=":", alpha=0.7)

    ax.legend(facecolor=EP_BACKGROUND, edgecolor=EP_PRIMARY)
    ax.set_ylabel("Probability Density")


def _plot_binomial_distribution(ax, params: dict, np) -> None:
    """Plot binomial probability distribution as a bar chart."""
    n = params.get("n", 10)
    p = params.get("p", 0.5)

    from math import comb
    k_vals = np.arange(0, n + 1)
    prob_vals = np.array([comb(n, int(k)) * (p ** k) * ((1 - p) ** (n - k)) for k in k_vals])

    ax.bar(k_vals, prob_vals, color=EP_ACCENT, alpha=0.8, edgecolor=EP_PRIMARY, linewidth=0.6,
           label=f"B({n}, {p})")
    ax.set_xticks(k_vals)
    mu = n * p
    ax.axvline(mu, color=EP_PRIMARY, linewidth=1.5, linestyle="--", label=f"E(X) = {mu:.1f}")
    ax.legend(facecolor=EP_BACKGROUND, edgecolor=EP_PRIMARY)
    ax.set_ylabel("P(X = k)")
    ax.set_xlabel("k")


def _plot_scatter_regression(ax, params: dict, np) -> None:
    """Scatter plot with linear regression line."""
    x_data = params.get("x", [1, 2, 3, 4, 5, 6, 7, 8])
    y_data = params.get("y", [2, 4, 5, 4, 5, 7, 8, 9])

    x_arr = np.array(x_data, dtype=float)
    y_arr = np.array(y_data, dtype=float)

    ax.scatter(x_arr, y_arr, color=EP_ACCENT, s=60, zorder=5, label="Data", edgecolors=EP_PRIMARY, linewidths=0.5)

    # Linear regression
    coeffs = np.polyfit(x_arr, y_arr, 1)
    x_line = np.linspace(x_arr.min(), x_arr.max(), 100)
    y_line = np.polyval(coeffs, x_line)
    ax.plot(x_line, y_line, color=EP_PRIMARY, linewidth=2, linestyle="--",
            label=f"y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}")

    ax.legend(facecolor=EP_BACKGROUND, edgecolor=EP_PRIMARY)


# ---------------------------------------------------------------------------
# Excalidraw diagrams
# ---------------------------------------------------------------------------

NODE_SHAPES = {
    "start": "ellipse",
    "end": "ellipse",
    "step": "rectangle",
    "decision": "diamond",
}

EP_EXCALIDRAW_COLORS = {
    "start": "#e94560",
    "end": "#e94560",
    "step": "#1a1a2e",
    "decision": "#16213e",
}


def generate_excalidraw(
    diagram_type: str,
    nodes: list[dict],
    edges: list[dict],
    output_path: str,
) -> str:
    """
    Generate an Excalidraw-compatible JSON file for flowchart diagrams.

    Each node: {"id": str, "label": str, "type": "start|step|decision|end"}
    Each edge: {"from": str, "to": str, "label": str}

    Returns the absolute path of the saved .excalidraw file.
    """
    elements = []
    node_positions: dict[str, tuple[int, int]] = {}

    # Layout: simple top-to-bottom vertical layout
    SPACING_Y = 130
    SPACING_X = 220
    NODE_W = 180
    NODE_H = 70
    DIAMOND_W = 200
    DIAMOND_H = 90

    # Assign positions in a simple column layout
    for i, node in enumerate(nodes):
        x = 100 + (i % 2) * SPACING_X  # alternate columns for decision branches
        y = 80 + (i // 1) * SPACING_Y  # simple vertical stack
        # Unique vertical position per node
        x = 300
        y = 80 + i * SPACING_Y
        node_positions[node["id"]] = (x, y)

    # Node elements
    node_id_map: dict[str, str] = {}
    for node in nodes:
        nid = f"node_{node['id']}"
        node_id_map[node["id"]] = nid
        ntype = node.get("type", "step")
        x, y = node_positions[node["id"]]
        color = EP_EXCALIDRAW_COLORS.get(ntype, EP_PRIMARY)

        if ntype == "diamond" or ntype == "decision":
            w, h = DIAMOND_W, DIAMOND_H
            shape_type = "diamond"
        else:
            w, h = NODE_W, NODE_H
            shape_type = "ellipse" if ntype in ("start", "end") else "rectangle"

        element = {
            "id": nid,
            "type": "rectangle" if shape_type == "rectangle" else shape_type,
            "x": x - w // 2,
            "y": y - h // 2,
            "width": w,
            "height": h,
            "angle": 0,
            "strokeColor": color,
            "backgroundColor": EP_BACKGROUND,
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "frameId": None,
            "roundness": {"type": 2} if shape_type == "rectangle" else None,
            "isDeleted": False,
            "boundElements": [],
            "updated": 1,
            "link": None,
            "locked": False,
        }
        elements.append(element)

        # Label element
        label_el = {
            "id": f"label_{nid}",
            "type": "text",
            "x": x - w // 2,
            "y": y - 14,
            "width": w,
            "height": 28,
            "angle": 0,
            "strokeColor": color,
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 1,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "frameId": None,
            "roundness": None,
            "isDeleted": False,
            "boundElements": [],
            "updated": 1,
            "link": None,
            "locked": False,
            "text": node["label"],
            "fontSize": 14,
            "fontFamily": 1,
            "textAlign": "center",
            "verticalAlign": "middle",
            "containerId": nid,
            "originalText": node["label"],
            "lineHeight": 1.25,
        }
        elements.append(label_el)

    # Edge (arrow) elements
    for i, edge in enumerate(edges):
        from_id = node_id_map.get(edge["from"])
        to_id = node_id_map.get(edge["to"])
        if not from_id or not to_id:
            continue

        from_pos = node_positions.get(edge["from"], (300, 0))
        to_pos = node_positions.get(edge["to"], (300, 130))

        arrow_el = {
            "id": f"arrow_{i}",
            "type": "arrow",
            "x": from_pos[0],
            "y": from_pos[1] + 45,  # bottom of source node
            "width": abs(to_pos[0] - from_pos[0]),
            "height": abs(to_pos[1] - from_pos[1]) - 90,
            "angle": 0,
            "strokeColor": EP_PRIMARY,
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "frameId": None,
            "roundness": {"type": 2},
            "isDeleted": False,
            "boundElements": [],
            "updated": 1,
            "link": None,
            "locked": False,
            "startBinding": {"elementId": from_id, "focus": 0, "gap": 1},
            "endBinding": {"elementId": to_id, "focus": 0, "gap": 1},
            "lastCommittedPoint": None,
            "startArrowhead": None,
            "endArrowhead": "arrow",
            "points": [[0, 0], [0, max(10, to_pos[1] - from_pos[1] - 90)]],
        }
        elements.append(arrow_el)

        # Edge label if present
        if edge.get("label"):
            mid_x = (from_pos[0] + to_pos[0]) / 2
            mid_y = (from_pos[1] + to_pos[1]) / 2
            edge_label = {
                "id": f"edge_label_{i}",
                "type": "text",
                "x": mid_x + 5,
                "y": mid_y,
                "width": 120,
                "height": 20,
                "angle": 0,
                "strokeColor": EP_SECONDARY,
                "backgroundColor": "transparent",
                "fillStyle": "solid",
                "strokeWidth": 1,
                "strokeStyle": "solid",
                "roughness": 1,
                "opacity": 100,
                "groupIds": [],
                "frameId": None,
                "roundness": None,
                "isDeleted": False,
                "boundElements": [],
                "updated": 1,
                "link": None,
                "locked": False,
                "text": edge["label"],
                "fontSize": 11,
                "fontFamily": 1,
                "textAlign": "left",
                "verticalAlign": "top",
                "containerId": None,
                "originalText": edge["label"],
                "lineHeight": 1.25,
            }
            elements.append(edge_label)

    excalidraw_doc = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://exampilot.io",
        "elements": elements,
        "appState": {
            "gridSize": None,
            "viewBackgroundColor": EP_BACKGROUND,
        },
        "files": {},
    }

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(excalidraw_doc, indent=2), encoding="utf-8")

    print(f"Excalidraw diagram saved: {out.resolve()}")
    return str(out.resolve())


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate math diagrams (matplotlib PNG) or flowcharts (Excalidraw JSON) for ExamPilot."
    )
    parser.add_argument(
        "--type", choices=["matplotlib", "excalidraw"], required=True,
        help="Output type: 'matplotlib' for math diagrams, 'excalidraw' for flowcharts",
    )
    parser.add_argument(
        "--diagram",
        default="function_plot",
        help="Diagram sub-type (e.g. integration_area, normal_distribution, learning_path)",
    )
    parser.add_argument(
        "--output", "-o",
        default=None,
        help="Output file path (default: marketing/pipelines/assets/{diagram}.png|.excalidraw)",
    )
    parser.add_argument("--title", default="", help="Chart title")
    parser.add_argument("--x-label", default="x", help="X-axis label")
    parser.add_argument("--y-label", default="y", help="Y-axis label")
    args = parser.parse_args()

    DEFAULT_ASSET_DIR.mkdir(parents=True, exist_ok=True)

    if args.type == "matplotlib":
        ext = ".png"
        output = args.output or str(DEFAULT_ASSET_DIR / f"{args.diagram}{ext}")
        # Demo params for CLI invocation
        demo_params: dict[str, dict] = {
            "function_plot": {"x_range": [-4, 4], "coefficients": [1, 0, -1], "label": "x² - 1"},
            "integration_area": {"coefficients": [1, 0, 0], "a": 0, "b": 2},
            "normal_distribution": {"mean": 0, "std": 1},
            "binomial_distribution": {"n": 12, "p": 0.4},
            "scatter_with_regression": {
                "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                "y": [2.1, 3.9, 6.2, 7.8, 9.5, 11.2, 12.8, 14.1, 16.3, 18.0],
            },
        }
        params = demo_params.get(args.diagram, {})
        generate_math_diagram(
            diagram_type=args.diagram,
            params=params,
            output_path=output,
            title=args.title or args.diagram.replace("_", " ").title(),
            x_label=args.x_label,
            y_label=args.y_label,
        )

    elif args.type == "excalidraw":
        ext = ".excalidraw"
        output = args.output or str(DEFAULT_ASSET_DIR / f"{args.diagram}{ext}")

        # Demo nodes/edges for CLI invocation
        demo_nodes = [
            {"id": "start", "label": "Start Revision", "type": "start"},
            {"id": "diagnose", "label": "Identify Weak Topics", "type": "step"},
            {"id": "decide", "label": "Ready for Mock?", "type": "decision"},
            {"id": "practice", "label": "Practice Questions", "type": "step"},
            {"id": "mock", "label": "Take Mock Exam", "type": "step"},
            {"id": "end", "label": "Exam Ready", "type": "end"},
        ]
        demo_edges = [
            {"from": "start", "to": "diagnose", "label": ""},
            {"from": "diagnose", "to": "decide", "label": ""},
            {"from": "decide", "to": "practice", "label": "No"},
            {"from": "decide", "to": "mock", "label": "Yes"},
            {"from": "practice", "to": "decide", "label": "Review"},
            {"from": "mock", "to": "end", "label": ""},
        ]
        generate_excalidraw(
            diagram_type=args.diagram,
            nodes=demo_nodes,
            edges=demo_edges,
            output_path=output,
        )


if __name__ == "__main__":
    main()
