"""Generate the career timeline SVG (light + dark) for the profile README."""

from html import escape
from pathlib import Path

W = 900
RAIL_X = 70
DOT_R = 6.5
TEXT_X = 104

ENTRIES = [
    {
        "date": "JAN – MAY 2026",
        "org": "Northeastern CESAR Lab",
        "role": "Machine Learning Research Assistant",
        "lines": ["LLM evaluation in Python"],
        "pivot": False,
    },
    {
        "date": "JAN – AUG 2025",
        "org": "Amazon",
        "role": "Software Engineer Intern",
        "lines": [
            "Built an AWS Strands + Bedrock agent that autonomously generates and debugs build",
            "configurations from requirement docs and CDK packages — cut configuration time by 50%,",
            "adopted as the team's standard tool",
            "",
            "Led a full-stack cost-estimation system (React, Spring) into Amazon's internal release",
            "workflow — async processing, multi-level caching, DynamoDB, Lambda evaluation pipeline",
        ],
        "pivot": False,
    },
    {
        "date": "SEP 2023",
        "org": "Northeastern University",
        "role": "M.S. Computer Science · Boston",
        "lines": ["Left product management to build the thing instead of speccing it"],
        "pivot": True,
    },
    {
        "date": "2015 – 2022",
        "org": "Fintech / SaaS",
        "role": "Product Manager · 7 years",
        "lines": ["I still think in users, not just tickets"],
        "pivot": False,
    },
]

THEMES = {
    "dark": {
        "text": "#e6edf3",
        "muted": "#8b949e",
        "faint": "#6e7681",
        "accent": "#58a6ff",
        "rail": "#30363d",
        "pivot": "#3fb950",
        "chip_text": "#3fb950",
    },
    "light": {
        "text": "#1f2328",
        "muted": "#59636e",
        "faint": "#818b98",
        "accent": "#0969da",
        "rail": "#d1d9e0",
        "pivot": "#1a7f37",
        "chip_text": "#1a7f37",
    },
}

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"


def build(theme_name):
    c = THEMES[theme_name]
    out = []
    y = 26
    dots = []

    for e in ENTRIES:
        dot_y = y + 8
        dots.append((dot_y, e["pivot"]))
        colour = c["pivot"] if e["pivot"] else c["accent"]

        out.append(
            f'<text x="{TEXT_X}" y="{y + 12}" font-size="11.5" font-weight="600" '
            f'letter-spacing="1.2" fill="{colour}">{escape(e["date"])}</text>'
        )
        if e["pivot"]:
            out.append(
                f'<text x="{TEXT_X + 118}" y="{y + 12}" font-size="11.5" font-weight="600" '
                f'letter-spacing="0.6" fill="{c["chip_text"]}">◆ CAREER PIVOT</text>'
            )

        out.append(
            f'<text x="{TEXT_X}" y="{y + 38}" font-size="18.5" font-weight="700" '
            f'fill="{c["text"]}">{escape(e["org"])}</text>'
        )
        out.append(
            f'<text x="{TEXT_X}" y="{y + 59}" font-size="13.5" '
            f'fill="{c["muted"]}">{escape(e["role"])}</text>'
        )

        ly = y + 84
        for line in e["lines"]:
            if line:
                out.append(
                    f'<text x="{TEXT_X}" y="{ly}" font-size="13.5" '
                    f'fill="{c["faint"]}">{escape(line)}</text>'
                )
            ly += 20
        y = ly + 18

    height = y - 4
    rail_top, rail_bottom = dots[0][0], dots[-1][0]

    head = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" '
        f'viewBox="0 0 {W} {height}" font-family="{FONT}" role="img" '
        f'aria-label="Career timeline of Logan Li">',
        f'<line x1="{RAIL_X}" y1="{rail_top}" x2="{RAIL_X}" y2="{rail_bottom}" '
        f'stroke="{c["rail"]}" stroke-width="2"/>',
    ]
    for dot_y, pivot in dots:
        colour = c["pivot"] if pivot else c["accent"]
        head.append(
            f'<circle cx="{RAIL_X}" cy="{dot_y}" r="{DOT_R}" fill="none" '
            f'stroke="{colour}" stroke-width="2.5"/>'
        )

    return "\n".join(head + out + ["</svg>"]) + "\n"


target = Path(__file__).parent / "assets"
target.mkdir(exist_ok=True)
for name in THEMES:
    path = target / f"timeline-{name}.svg"
    path.write_text(build(name), encoding="utf-8")
    print(f"wrote {path}")
