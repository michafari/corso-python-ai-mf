class PipelineAI:

    def __init__(self, llm_model, embedding_model):
        self._llm_model = llm_model
        self._embedding_model = embedding_model

    def execute(self, text):
        embedding = self._embedding_model.generate_embedding(text)
        answer = self._llm_model.generate(embedding)

        return {
            "embedding": embedding,
            "answer": answer

        }

