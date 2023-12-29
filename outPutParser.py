from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os


# PydanticOutputParserを使ったPythonオブジェクトの取得
class Recipe(BaseModel):
    ingredients: list[str] = Field(description="ingredients of the dish")
    steps: list[str] = Field(description="steps to make the dish")


parser = PydanticOutputParser(pydantic_object=Recipe)
format_instructions = parser.get_format_instructions()
print(format_instructions)

template = """料理のレシピを考えてください。

{format_instructions}

料理名: {dish}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["dish"],
    partial_variables={"format_instructions": format_instructions},
)
formatters_prompt = prompt.format(dish="カレー")
print(formatters_prompt)
os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"
chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
messages = [HumanMessage(content=formatters_prompt)]
output = chat(messages)
print(output.content)

recipe = parser.parse(output.content)
print(recipe)
