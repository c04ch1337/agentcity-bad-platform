# AgentCity BAD Platform — Simplified CPU Build (Reviewed & Corrected)

A **cyberpunk‑military** multi‑agent playground for Business Army Development (BAD).  
This is a CPU‑only, minimal, working scaffold suitable for local dev and demos.

## Services
- **backend** — FastAPI API (health, test endpoints, deploy stub)
- **frontend-agent** — Streamlit Agent Console (talks to backend)
- **sales-site** — Static site (nginx) for packages/marketing

## Quickstart
```bash
cp .env.example .env
docker compose up --build
# Backend:        http://localhost:8000/docs
# Agent Console:  http://localhost:8501
# Sales Site:     http://localhost:8080
```
