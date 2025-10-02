# AGENTCITY BAD PLATFORM - MAIN APPLICATION
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import get_bad_config
from .test_routes import router as test_router

config = get_bad_config()
app = FastAPI(
    title="AgentCity BAD Platform",
    description="Business Army Development — Cyberpunk Military Multi-Agent Ecosystem",
    version="1.0.0",
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(test_router)

@app.get("/", tags=["meta"])
async def root():
    return {
        "platform": config.PLATFORM_NAME,
        "status": "OPERATIONAL",
        "theme": config.THEME,
        "mission": "Storm corporate fortresses; conquer process inefficiencies",
        "gpu_acceleration": config.GPU_ENABLED,
    }

@app.get("/health", tags=["meta"])
async def health():
    return {"status": "ok"}

@app.get("/agents", tags=["agents"])
async def list_agents():
    return {
        "agents": [
            "AI-GENERAL-STRATEGIC-COMMAND",
            "AI-COLONEL-OPERATIONS-WARLORD",
            "AI-SERGEANT-TACTICAL-EXECUTOR",
            "AI-SPECIALIST-RECON-SCOUT",
        ]
    }

@app.post("/deploy/{agent_rank}", tags=["agents"])
async def deploy_agent(agent_rank: str, mission_brief: dict):
    return {
        "status": "DEPLOYED",
        "agent": agent_rank,
        "mission": mission_brief,
        "message": f"{agent_rank} deployed for mission: {mission_brief.get('mission_type', 'unknown')}",
        "next_steps": [
            "Agent processing mission objectives",
            "Check /agents for status updates",
            "Monitor battle logs for progress",
        ],
    }
