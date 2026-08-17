"""Generate the README's SVG assets (header + career timeline), light and dark."""

from html import escape
from pathlib import Path

W = 900
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

THEMES = {
    "dark": {
        "text": "#e6edf3",
        "muted": "#8b949e",
        "faint": "#6e7681",
        "accent": "#58a6ff",
        "rail": "#30363d",
        "pivot": "#3fb950",
    },
    "light": {
        "text": "#1f2328",
        "muted": "#59636e",
        "faint": "#818b98",
        "accent": "#0969da",
        "rail": "#d1d9e0",
        "pivot": "#1a7f37",
    },
}


# --------------------------------------------------------------------------- header

HEADLINE = "Full-Stack AI Engineer"
SUBLINE = "LLM / Agent Applications"


def build_header(c):
    mid = W // 2
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="112" \
viewBox="0 0 {W} 112" font-family="{FONT}" role="img" \
aria-label="{escape(HEADLINE)} — {escape(SUBLINE)}">
<text x="{mid}" y="46" text-anchor="middle" font-size="34" font-weight="800" \
letter-spacing="-0.5" fill="{c['accent']}">{escape(HEADLINE)}</text>
<line x1="{mid - 60}" y1="66" x2="{mid + 60}" y2="66" stroke="{c['rail']}" stroke-width="2"/>
<text x="{mid}" y="92" text-anchor="middle" font-size="15" font-weight="500" \
letter-spacing="0.6" fill="{c['muted']}">{escape(SUBLINE)}</text>
</svg>
"""


# ------------------------------------------------------------------------- timeline

RAIL_X = 70
DOT_R = 6.5
TEXT_X = 104

ENTRIES = [
    {
        "date": "JAN – MAY 2026",
        "org": "Northeastern CESAR Lab",
        "role": "Machine Learning Research Assistant · Boston, USA",
        "lines": [
            "Built a three-stage pipeline (RTMPose, MotionBERT, HaMeR) that labels co-speech gestures",
            "in place of hand annotation, running 97 controlled experiments to choose each stage; the",
            "winning 3D pose representation doubled segmentation F1.",
        ],
        "pivot": False,
    },
    {
        "date": "JAN – AUG 2025",
        "org": "Amazon",
        "role": "Software Engineer Intern · Boston, USA",
        "lines": [
            "Built an AI agent on LangChain and Bedrock that autonomously generates and debugs build",
            "configurations from requirement docs and CDK packages, using task orchestration, context",
            "engineering, and a knowledge base (RAG); cut configuration time by 50% and was adopted",
            "as the team's standard tool.",
            "",
            "Designed and built the cost-estimation step in Amazon's internal robot-simulation platform",
            "(React, Spring, DynamoDB), which every engineer passes through before running or releasing",
            "a simulation; back-tested the estimator against historical runs and held its error within 20%.",
        ],
        "pivot": False,
    },
    {
        "date": "SEP 2023",
        "org": "Northeastern University",
        "role": "M.S. in Computer Science · Boston, USA",
        "lines": [],
        "pivot": True,
    },
    {
        "date": "2015 – 2023",
        "org": "Fintech & Enterprise SaaS",
        "role": "Product roles · 7 years",
        "lines": ["Prior to graduate study."],
        "pivot": False,
    },
]


def build_timeline(c):
    body, dots, y = [], [], 26

    for e in ENTRIES:
        dots.append((y + 8, e["pivot"]))
        colour = c["pivot"] if e["pivot"] else c["accent"]

        body.append(
            f'<text x="{TEXT_X}" y="{y + 12}" font-size="11.5" font-weight="600" '
            f'letter-spacing="1.2" fill="{colour}">{escape(e["date"])}</text>'
        )
        if e["pivot"]:
            body.append(
                f'<text x="{TEXT_X + 118}" y="{y + 12}" font-size="11.5" font-weight="600" '
                f'letter-spacing="0.6" fill="{c["pivot"]}">◆ CAREER PIVOT</text>'
            )
        body.append(
            f'<text x="{TEXT_X}" y="{y + 38}" font-size="18.5" font-weight="700" '
            f'fill="{c["text"]}">{escape(e["org"])}</text>'
        )
        body.append(
            f'<text x="{TEXT_X}" y="{y + 59}" font-size="13.5" '
            f'fill="{c["muted"]}">{escape(e["role"])}</text>'
        )

        ly = y + 84
        for line in e["lines"]:
            if line:
                body.append(
                    f'<text x="{TEXT_X}" y="{ly}" font-size="13.5" '
                    f'fill="{c["faint"]}">{escape(line)}</text>'
                )
            ly += 20
        y = ly + 18

    height = y - 4
    head = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" '
        f'viewBox="0 0 {W} {height}" font-family="{FONT}" role="img" '
        f'aria-label="Career timeline of Logan Li">',
        f'<line x1="{RAIL_X}" y1="{dots[0][0]}" x2="{RAIL_X}" y2="{dots[-1][0]}" '
        f'stroke="{c["rail"]}" stroke-width="2"/>',
    ]
    for dot_y, pivot in dots:
        colour = c["pivot"] if pivot else c["accent"]
        head.append(
            f'<circle cx="{RAIL_X}" cy="{dot_y}" r="{DOT_R}" fill="none" '
            f'stroke="{colour}" stroke-width="2.5"/>'
        )

    return "\n".join(head + body + ["</svg>"]) + "\n"


# ----------------------------------------------------------------------------- main

target = Path(__file__).parent / "assets"
target.mkdir(exist_ok=True)

for name, colours in THEMES.items():
    for stem, builder in (("header", build_header), ("timeline", build_timeline)):
        path = target / f"{stem}-{name}.svg"
        path.write_text(builder(colours), encoding="utf-8")
        print(f"wrote {path}")
