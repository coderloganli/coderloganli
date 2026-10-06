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
        "date": "VENTURE",
        "org": "Combrabo",
        "role": "Founding Engineer",
        "lines": [
            "Built the iOS client and Rust backend: an agent memory system with short- and long-term",
            "recall, plus agent engineering that gives it a believable human personality.",
            "",
            "Built an evaluation set that scores every change to the voice path, then cut end-to-end",
            "call latency to 1.2 s; piloted with prospective customers to purchase intent.",
        ],
        "pivot": False,
    },
    {
        "date": "VENTURE",
        "org": "Kleepay",
        "role": "Founding Engineer",
        "lines": [
            "Built the entire React front end and the Rust marketing engine behind referral commission,",
            "cashback and new-user bonuses.",
            "",
            "Built the agent payment MCP end to end, so any AI agent can complete a payment on the",
            "platform's cards within an authorized scope.",
        ],
        "pivot": False,
    },
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
        "role": "Software Engineer · USA",
        "lines": [
            "Built a RAG-grounded AI agent on LangChain and Bedrock that writes and debugs the build",
            "configurations engineers used to write by hand; it cut configuration time by 50% and",
            "became the team's standard tool.",
            "",
            "Built the cost-estimation gate every engineer passes through before running a simulation",
            "on Amazon's robot-simulation platform (React, Spring, DynamoDB), holding estimate error",
            "within 20%.",
        ],
        "pivot": False,
    },
    {
        "date": "SEP 2023 – AUG 2026",
        "org": "Northeastern University",
        "role": "M.S. in Computer Science · Boston, USA",
        "lines": [],
        "pivot": False,
    },
    {
        "date": "OCT 2021 – MAR 2023",
        "org": "eSign",
        "role": "Software Engineer · China",
        "lines": [
            "Designed and developed RESTful APIs for electronic signature services using Java Spring,",
            "and designed the relational database schemas and SQL tables behind core business workflows.",
            "",
            "Developed customized e-signature workflows to client requirements, integrating third-party",
            "authentication, facial recognition and external business systems so clients could adopt",
            "electronic signatures inside their existing applications.",
        ],
        "pivot": False,
    },
    {
        "date": "DEC 2019 – OCT 2021",
        "org": "EbidChain",
        "role": "Founding Engineer · China",
        "lines": [
            "Designed and developed a consortium blockchain on Hyperledger to notarize public-resource",
            "transaction data, implementing on-chain submission, immutable record storage and",
            "blockchain-based verification.",
            "",
            "Designed and developed a suite of external RESTful APIs in Java and Spring, authored the",
            "API documentation, and supported client-side integration with external systems.",
        ],
        "pivot": False,
    },
    {
        "date": "NOV 2018 – AUG 2019",
        "org": "Wilmar",
        "role": "Senior Product Manager · China",
        "lines": [
            "Owned a transportation management system covering dispatch, route planning, freight",
            "settlement and in-transit tracking across dozens of distribution centers; dispatch",
            "turnaround fell 80% versus manual.",
        ],
        "pivot": False,
    },
    {
        "date": "SEP 2015 – APR 2018",
        "org": "A Fintech Company",
        "role": "Product Manager · China",
        "lines": [
            "Owned a consumer-lending app from 0 to 1 and built out its risk-review back office,",
            "reaching thousands of daily active users.",
        ],
        "pivot": False,
    },
    {
        "date": "SEP 2011 – AUG 2015",
        "org": "Peking University",
        "role": "B.S. in Psychology & B.S. in Economics · Beijing, China",
        "lines": [],
        "pivot": False,
    },
]


def build_timeline(c):
    body, dots, y = [], [], 26

    for e in ENTRIES:
        dots.append((y + 8, e["pivot"]))
        colour = c["pivot"] if e["pivot"] else c["accent"]

        tag = (
            f'<tspan dx="14" letter-spacing="0.6">◆ CAREER PIVOT</tspan>' if e["pivot"] else ""
        )
        body.append(
            f'<text x="{TEXT_X}" y="{y + 12}" font-size="11.5" font-weight="600" '
            f'letter-spacing="1.2" fill="{colour}">{escape(e["date"])}{tag}</text>'
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
    for stem, builder in (("header", build_header), ("timeline-v2", build_timeline)):
        path = target / f"{stem}-{name}.svg"
        path.write_text(builder(colours), encoding="utf-8")
        print(f"wrote {path}")
