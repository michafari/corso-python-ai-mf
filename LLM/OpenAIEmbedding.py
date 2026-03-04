from LLM.EmbdeddingModel import EmbeddingModel


class OpenAIEmbedding(EmbeddingModel):

    def generate_embedding(self, text):
        return [1.0,0.5,0.3]

