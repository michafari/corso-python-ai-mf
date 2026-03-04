###
from LLM.LLMModel import LLMModel


class GPTModel(LLMModel):

    def generate(self, prompt):
        return f"local answer for {prompt}"

