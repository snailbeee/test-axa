from llama_cpp import Llama


class LlamaLLM:
    SYSTEM = "Tu est un conseiller assurance. Tu dois synthétiser des entretiens entre agent - client."

    def __init__(self, model_path: str):
        self.llm = Llama(
            model_path=model_path, n_ctx=2048, n_gpu_layers=0, verbose=False
        )

    def synthetize(self, conversation: list[dict]) -> str | None:
        if not conversation:
            return None
        prompt = (
            f'Synthétiser la conversation suivante: \nConversation: "{conversation}"\n.'
        )
        out = self.llm.create_chat_completion(
            messages=[
                {"role": "system", "content": self.SYSTEM},
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
            max_tokens=100,
            response_format={"type": "text"},
        )
        content = out["choices"][0]["message"]["content"]
        return content

    def close(self) -> None:
        self.llm.close()
