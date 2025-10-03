from pathlib import Path
import json
from typing import List, Dict, Any

# Where to look for mercenary JSON files relative to backend app root
ROOT_CANDIDATES = [
    Path(__file__).resolve().parents[3] / "mercenaries",  # repo_root/mercenaries
    Path("/app/mercenaries"),  # alt mount
]

_cache: List[Dict[str, Any]] = []

def load_all() -> List[Dict[str, Any]]:
    global _cache
    if _cache:
        return _cache
    for root in ROOT_CANDIDATES:
        if root.exists():
            for p in sorted(root.glob("*.json")):
                try:
                    _cache.append(json.loads(p.read_text(encoding="utf-8")))
                except Exception as e:
                    # Skip bad files but do not crash
                    continue
            break
    return _cache

def get_by_id(mid: str) -> Dict[str, Any] | None:
    for m in load_all():
        if m.get("id") == mid:
            return m
    return None
