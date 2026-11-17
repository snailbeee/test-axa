import json
from pathlib import Path

from synthetiser.constants import ENTRETIENS_DIR


def load_entretiens(entretiens_dir: Path) -> dict:
    entretiens = {}
    files = entretiens_dir.glob("*.json")
    for f in files:
        content = json.loads(f.read_text(encoding="utf-8"))
        entretien_id = content["id"]
        segments = content["segments"]
        conversation = []
        for seg in segments:
            conversation.append({"locuteur": seg["locuteur"], "texte": seg["texte"]})
        entretiens[entretien_id] = conversation
    return entretiens


print(load_entretiens(ENTRETIENS_DIR))
