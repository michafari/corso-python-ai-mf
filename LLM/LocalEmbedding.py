from LLM.EmbdeddingModel import EmbeddingModel


class LocalEmbedding(EmbeddingModel):

    def generate_embedding(self, text):
        return [0.9,0.1,0.8]

