<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=28&duration=2600&pause=700&color=0EA5E9&center=true&vCenter=true&width=720&height=60&lines=Full-Stack+AI+Engineer;LLM+%2F+Agent+Applications;Shipping+sub-2s+voice+agents" alt="Full-Stack AI Engineer — LLM / Agent Applications" />

<img src="https://img.shields.io/badge/Open%20to-New%20Grad%20SWE%20%2F%20Applied%20AI-16a34a?style=for-the-badge" alt="Open to work" />
<img src="https://img.shields.io/badge/Boston-US%20relocation%20OK-1e40af?style=for-the-badge" alt="Location" />

</div>

```
   ██╗      ██╗          logan@github
   ██║      ██║          ─────────────────────────────────────────────────────
   ██║      ██║          Education : M.S. CS @ Northeastern · B.S. @ Peking Univ
   ██║      ██║          Status    : open to New Grad SWE / Applied AI  █
   ███████╗ ███████╗
   ╚══════╝ ╚══════╝     Languages : Rust · Python · TypeScript · Java · Go · Swift
                         Backend   : Axum · FastAPI · Spring · PostgreSQL / pgvector
                         AI / LLM  : RAG · LLM Evaluation · Function Calling · Strands
                         Cloud     : AWS Bedrock · Lambda · DynamoDB · Docker · etcd
```

I build **LLM and agent products end-to-end** — from the Rust backend and the latency budget all the way to the app someone actually talks to.

```ts
const experience = {
  amazon: {
    title:  "Software Engineer Intern",
    when:   "Jan 2025 – Aug 2025",
    built:  "AWS Strands + Bedrock agent that autonomously generates and " +
            "debugs build configurations from requirement docs and CDK packages",
    impact: "-50% configuration time · adopted as the team's standard tool",
    also:   "Full-stack cost-estimation system (React, Spring) shipped into " +
            "Amazon's internal release workflow — async processing, " +
            "multi-level caching, DynamoDB, Lambda evaluation pipeline",
  },
  cesarLab: {
    title:  "Machine Learning Research Assistant",
    where:  "Northeastern CESAR Lab",
    when:   "Jan 2026 – May 2026",
    focus:  "LLM evaluation in Python",
  },
  priorLife: {
    title:  "Product Manager — fintech / SaaS",
    years:  7,
    note:   "I still think in users, not just tickets",
  },
} as const;
```

---

## 🚀 Projects

```console
$ ls -1 ~/projects

sonari/        # real-time voice AI agent · Rust · sub-2s turn latency
dev-harness/   # guardrails for AI coding agents · Claude Code plugin
gochat-scale/  # 8-service Go chat server · etcd discovery · k6 load model
```

<table>
<tr>
<td width="50%" valign="top">

### 🎙 [sonari](https://github.com/coderloganli/sonari)

Solo-built and shipped as an iOS/Android app on a Rust backend, with long-term memory sustaining a believable persona across sessions.

- Sub-2s end-to-end turn latency — natural-conversation speed
- In-process speech orchestration, streaming partial ASR, early first-chunk TTS, VAD endpointing
- pgvector-backed retrieval keeps the persona consistent instead of resetting every call
- Voice evals in CI catch latency and behavior regressions before production
- Piloted with prospective customers to purchase intent

![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Axum](https://img.shields.io/badge/Axum-000000?style=flat-square&logo=rust&logoColor=white)
![LiveKit](https://img.shields.io/badge/LiveKit-1e40af?style=flat-square&logo=webrtc&logoColor=white)
![pgvector](https://img.shields.io/badge/pgvector-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Swift](https://img.shields.io/badge/Swift-FA7343?style=flat-square&logo=swift&logoColor=white)

</td>
<td width="50%" valign="top">

### 🛡 [dev-harness](https://github.com/coderloganli/dev-harness)

A Claude Code plugin that governs how a project is developed — curating documentation, managing tickets and workspaces automatically, and holding the agent to an explicit development process.

- **The approval prompt is rendered by the plugin, not the model** — the agent controls *when* it asks for approval, never *what* is asked
- Enforced at the tool layer rather than in prompts: writes stay denied until a plan is approved and a failing test exists
- Every task runs in its own git worktree — the main checkout is never written to, and abandoning a task is deleting a directory
- Tests are treated as contracts: the agent cannot weaken, skip, or delete a test to turn the suite green

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Agent Guardrails](https://img.shields.io/badge/Agent_Guardrails-6d28d9?style=flat-square)

</td>
</tr>
<tr>
<td colspan="2" valign="top">

### 📡 [gochat-scale](https://github.com/coderloganli/gochat-scale)

- Containerized and horizontally scaled an open-source Go chat server into **eight independently scalable services**
- Container IPs auto-register to etcd for RPC discovery; per-service health checks drive auto-restart
- k6 step-ramp load-testing model separating ramp, warm-up, and steady-state — so measurements come from steady state rather than warm-up noise

![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![etcd](https://img.shields.io/badge/etcd-419EDA?style=flat-square&logo=etcd&logoColor=white)
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
