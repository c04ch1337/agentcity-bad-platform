from fastapi import APIRouter, HTTPException
from ..mercenaries.registry import load_all, get_by_id

router = APIRouter(prefix="/mercenaries", tags=["mercenaries"])

@router.get("")
def list_mercenaries():
    return {"count": len(load_all()), "items": load_all()}

@router.get("/{mid}")
def get_mercenary(mid: str):
    m = get_by_id(mid)
    if not m:
        raise HTTPException(404, detail="Mercenary not found")
    return m

@router.post("/instantiate/{mid}")
def instantiate_mercenary(mid: str, overrides: dict | None = None):
    m = get_by_id(mid)
    if not m:
        raise HTTPException(404, detail="Mercenary not found")
    # This returns a safe, non-operational "agent config" blob
    cfg = {
        "id": m["id"],
        "name": m["name"],
        "role": m["role"],
        "sandbox_mode": True,
        "safety": "defensive_only",
        "memory": {k.strip(): None for k in m.get("memory_keys","").split(",")},
        "prompt": m["prompt_template"],
        "overrides": overrides or {},
    }
    return {"status": "CREATED", "agent_config": cfg}
