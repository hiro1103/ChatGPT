from langchain.llms import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

llm = OpenAI(model_name="text-davinci-003", temperature=0)

result = llm("自己紹介してください。")
print(result)
