from abc import ABC, abstractmethod

class EmbeddingModel(ABC):

    @abstractmethod
    def generate_embedding(self, text):
        pass
