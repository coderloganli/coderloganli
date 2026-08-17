<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg" />
  <img src="assets/header-dark.svg" width="900" alt="Full-Stack AI Engineer — LLM / Agent Applications" />
</picture>

<img src="https://img.shields.io/badge/Open%20to-New%20Grad%20SWE%20%2F%20Applied%20AI-16a34a?style=for-the-badge" alt="Open to work" />
<img src="https://img.shields.io/badge/Boston-US%20relocation%20OK-1e40af?style=for-the-badge" alt="Location" />

</div>

```
   ██╗      ██╗          logan@github
   ██║      ██║          ─────────────────────────────────────────────────────
   ██║      ██║          Education : M.S. CS @ Northeastern · B.S. @ Peking Univ
   ██║      ██║          Status    : open to New Grad SWE / Applied AI  █
   ███████╗ ███████╗
   ╚══════╝ ╚══════╝     Languages : Python · TypeScript · Rust · Java · Go · Swift · SQL
                         AI / LLM  : RAG · LangChain · LLM Evaluation · Function Calling
                         Frameworks: FastAPI · React · Spring · PostgreSQL · Redis · LiveKit
                         Cloud     : AWS Bedrock · Lambda · S3 · DynamoDB · Step Functions
                         DevOps    : Docker · GitHub Actions · OpenTelemetry · pytest · k6
```

## 💼 Experience

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/timeline-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/timeline-light.svg" />
  <img src="assets/timeline-dark.svg" width="900" alt="Career timeline — Jan–May 2026: Northeastern CESAR Lab, Machine Learning Research Assistant; built a three-stage pipeline (RTMPose, MotionBERT, HaMeR) that labels co-speech gestures in place of hand annotation, running 97 controlled experiments to choose each stage, and the winning 3D pose representation doubled segmentation F1. Jan–Aug 2025: Amazon, Software Engineer Intern; built an AI agent on LangChain and Bedrock that autonomously generates and debugs build configurations from requirement docs and CDK packages using task orchestration, context engineering, and a knowledge base (RAG), cutting configuration time by 50% and adopted as the team's standard tool; and designed the cost-estimation step in Amazon's internal robot-simulation platform (React, Spring, DynamoDB), back-tested against historical runs and held within 20% error. Sep 2023: Northeastern University, M.S. in Computer Science — the career pivot. 2015–2023: 7 years in product roles in fintech and enterprise SaaS." />
</picture>

---

## 🚀 Projects

```console
$ ls -1 ~/projects

sonari/        # real-time voice AI companion · Rust + iOS · 0.95 s median turn
dev-harness/   # guardrails for Claude Code · 11-tool MCP server · 61 tests
gochat-scale/  # Go chat server capacity study · k6 · 7,500 req/s at 224 ms p95
```

<table>
<tr>
<td width="50%" valign="top">

### 🎙 [sonari](https://github.com/coderloganli/sonari)
**Real-Time Voice AI Companion**

- Built and shipped it as an iOS app on a Rust backend deployed to AWS, and piloted it with prospective customers to purchase intent
- Cut end-to-end turn latency to a **0.95 s median and 1.2 s p95** by restructuring the real-time speech path
- Built an eval harness of 16 adversarial clips that scores word error rate and eight latency markers to catch regressions

![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Swift](https://img.shields.io/badge/Swift-FA7343?style=flat-square&logo=swift&logoColor=white)
![LiveKit](https://img.shields.io/badge/LiveKit%20%2F%20WebRTC-1e40af?style=flat-square&logo=webrtc&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=FF9900)

</td>
<td width="50%" valign="top">

### 🛡 [dev-harness](https://github.com/coderloganli/dev-harness)
**Guardrails for Claude Code**

Built a plugin that enforces three independent controls on a project:

- **Docs-as-code** — project documentation is curated, not drifting
- **A ten-stage workflow** the agent may request but cannot advance
- **An isolated per-task workspace**

Implemented as an **11-tool MCP server with 61 tests across Linux and Windows**.

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![MCP](https://img.shields.io/badge/MCP_Server-6d28d9?style=flat-square)

</td>
</tr>
<tr>
<td colspan="2" valign="top">

### 📡 [gochat-scale](https://github.com/coderloganli/gochat-scale)
**Scaling an Open-Source Go Chat Server**

- Built a k6 step-ramp load-testing model that measures only each step's steady-state window
- Used it to place a forked Go chat server's capacity ceiling at **1,500 virtual users sustaining 7,500 requests per second at 224 ms p95**

![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![k6](https://img.shields.io/badge/k6-7D64FF?style=flat-square&logo=k6&logoColor=white)

</td>
</tr>
</table>

---

<div align="center">

```console
$ echo "Building something in voice AI, agents, or developer tooling?"
$ mail coder_logan_li@outlook.com
```

<a href="mailto:coder_logan_li@outlook.com"><img src="https://img.shields.io/badge/coder__logan__li%40outlook.com-0ea5e9?style=for-the-badge&logo=maildotru&logoColor=white" alt="Email" /></a>

</div>
