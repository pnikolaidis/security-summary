"""Persona/voice rotation for the daily digest.

The persona for a given day is selected by `date.weekday() % len(personas)`,
so the rotation is deterministic and consistent across the pipeline.

CLI: `uv run python -m src.persona [YYYY-MM-DD]` prints today's persona as JSON.
"""
from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config" / "personas.yaml"


@dataclass(frozen=True)
class Persona:
    name: str
    voice: str
    intro_hint: str


def _load() -> list[Persona]:
    data = yaml.safe_load(CONFIG.read_text())
    return [Persona(**p) for p in data["personas"]]


def for_date(d: date) -> Persona:
    personas = _load()
    if not personas:
        raise ValueError("config/personas.yaml has no personas defined")
    return personas[d.weekday() % len(personas)]


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    d = date.fromisoformat(arg) if arg else date.today()
    print(json.dumps(asdict(for_date(d)), indent=2))
