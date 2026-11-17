from synthetiser.constants import ENTRETIENS_DIR, MODEL_PATH
from synthetiser.llm import LlamaLLM
from synthetiser.loader import load_entretiens


def main():
    llm = LlamaLLM(str(MODEL_PATH))
    entretiens = load_entretiens(ENTRETIENS_DIR)
    synthesis = {}
    try:
        for entretien_id, conversation in entretiens.items():
            content = llm.synthetize(conversation)
            synthesis[entretien_id] = content
        return synthesis
    finally:
        llm.close()
    return 0


if __name__ == "__main__":
    main()
