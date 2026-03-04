from abc import ABC, abstractmethod

class LLMModel(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass
