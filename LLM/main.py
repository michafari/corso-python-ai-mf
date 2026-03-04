from LLM.GPTModel import GPTModel
from LLM.LocalEmbedding import LocalEmbedding
from LLM.OpenAIEmbedding import OpenAIEmbedding
from LLM.PipelineAI import PipelineAI

pipeline1 = PipelineAI(GPTModel(),OpenAIEmbedding())
pipeline2 = PipelineAI(GPTModel(),LocalEmbedding())

result1 = pipeline1.execute("What is Machine Learning?")
result2 = pipeline2.execute("What is Machine Learning?")

print(result1)
print(result2)
