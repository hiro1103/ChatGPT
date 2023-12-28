from langchain.prompts import PromptTemplate
import os

# プロンプトテンプレート
os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

template = """
以下の料理のレシピを考えてください。

料理名:{dish}
"""

prompt = PromptTemplate(input_variables=["dish"], template=template)

result = prompt.format(dish="カレー")
print(result)
