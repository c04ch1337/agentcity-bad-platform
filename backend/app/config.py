# BAD MILITARY CONFIGURATION — simplified (no pydantic-settings)
import os
from typing import Dict

def env(k: str, default: str):
    return os.getenv(k, default)

class BADConfig:
    PLATFORM_NAME: str = env("PLATFORM_NAME", "AgentCity BAD")
    BUSINESS_IDENTITY: str = env("BUSINESS_IDENTITY", "Business Army Development")
    THEME: str = env("THEME", "cyberpunk-military")
    GLITCH_INTENSITY: str = env("GLITCH_INTENSITY", "medium")
    GPU_ENABLED: bool = env("GPU_ENABLED", "false").lower() == "true"
    LLM_MODEL: str = env("LLM_MODEL", "gpt-4o-mini")

    MILITARY_RANKS: Dict[str, str] = {
        "AI-GENERAL": "Strategic Command Overlord",
        "AI-COLONEL": "Operations Warlord",
        "AI-SERGEANT": "Tactical Executor",
        "AI-SPECIALIST": "Ground Operations",
    }

    CYBERPUNK_COLORS: Dict[str, str] = {
        "neon_cyan": "#00FFFF",
        "neon_magenta": "#FF00FF",
        "camo_dark": "#0A0A0A",
        "alert_red": "#FF0000",
    }

def get_bad_config() -> BADConfig:
    return BADConfig()
