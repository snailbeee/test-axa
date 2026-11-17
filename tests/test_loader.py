from synthetiser.constants import ENTRETIENS_DIR
from synthetiser.loader import load_entretiens


def test_load_entretiens():
    entretiens = load_entretiens(entretiens_dir=ENTRETIENS_DIR)
    assert len(entretiens) == 6
