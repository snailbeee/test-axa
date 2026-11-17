from synthetiser.constants import MODEL_PATH
from synthetiser.llm import LlamaLLM


def test_llm_synthetize_empty_conversation():
    llm = LlamaLLM(str(MODEL_PATH))

    try:
        assert llm.synthetize([]) is None
    finally:
        llm.close()
