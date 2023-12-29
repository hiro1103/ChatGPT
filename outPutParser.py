from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate


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
