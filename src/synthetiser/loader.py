import json
from pathlib import Path

from synthetiser.constants import ENTRETIENS_DIR


def load_entretiens(entretiens_dir: Path) -> dict:
    entretiens = [
        json.loads(file.read_text(encoding="utf-8"))
        for file in entretiens_dir.glob("*.json")
    ]
    return entretiens


print(load_entretiens(entretiens_dir=ENTRETIENS_DIR))
