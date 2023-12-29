from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain import LLMChain
from langchain.chains import SimpleSequentialChain
import os


class Recipe(BaseModel):
    ingredients: list[str] = Field(description="ingredients of the dish")
    steps: list[str] = Field(description="step to make the dish")


output_parser = PydanticOutputParser(pydantic_object=Recipe)

template = """料理のレシピを考えてください。

{format_instructions}

料理名：{dish}

"""

prompt = PromptTemplate(
    template=template,
    input_variables=["dish"],
    partial_variables={"format_instructions": output_parser.get_format_instructions()},
)

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"
chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

chain = LLMChain(prompt=prompt, llm=chat, output_parser=output_parser)

recipe = chain.run(dish="カレー")
print(type(recipe))
print(recipe)

cot_template = """以下の質問に回答してください。
質問：{question}
ステップバイステップで考えましょう。
"""

cot_prompt = PromptTemplate(input_variables=["question"], template=cot_template)
cot_chain = LLMChain(llm=chat, prompt=cot_prompt)

summarize_template = """以下の文章を結論だけ一言に要約してください。

{input}

"""

summarize_prompt = PromptTemplate(
    input_variables=["input"], template=summarize_template
)

summarize_chain = LLMChain(llm=chat, prompt=summarize_prompt)

cot_summarize_chain = SimpleSequentialChain(chains=[cot_chain, summarize_chain])

result = cot_summarize_chain(
    "私は市場に行って10個のリンゴを買いました。隣人に2つ、修理工に2つ渡しました。それから5つのリンゴを買って1つ食べました。残りは何個ですか？"
)
print(result["output"])
