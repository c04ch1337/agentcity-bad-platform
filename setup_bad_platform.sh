#!/usr/bin/env bash
set -euo pipefail

echo "🎯 Building AgentCity BAD Platform (Simplified, Reviewed)..."

# Optional: accept repo dir as arg
REPO_DIR="${1:-$PWD}"
cd "$REPO_DIR"

if command -v docker compose >/dev/null 2>&1; then
  docker compose down || true
else
  docker-compose down || true
fi

docker system prune -f || true

# Prepare env
[ -f ".env" ] || cp .env.example .env

# Build & run
if command -v docker compose >/dev/null 2>&1; then
  docker compose up --build
else
  docker-compose up --build
fi
