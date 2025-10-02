from fastapi import APIRouter

router = APIRouter(prefix="/test", tags=["test"])

@router.get("")
async def test_root():
    return {
        "status": "SUCCESS",
        "message": "AgentCity BAD Platform is running!",
        "endpoints": ["/", "/agents", "/test", "/deploy/{agent_rank}"]
    }

@router.get("/agents")
async def test_agents():
    return {
        "agents": [
            {"rank": "AI-GENERAL-STRATEGIC-COMMAND", "role": "Strategic Command Overlord", "status": "READY"},
            {"rank": "AI-COLONEL-OPERATIONS-WARLORD", "role": "Operations Warlord", "status": "READY"},
            {"rank": "AI-SERGEANT-TACTICAL-EXECUTOR", "role": "Tactical Executor", "status": "READY"},
        ]
    }
