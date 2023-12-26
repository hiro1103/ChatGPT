import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

message = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="こんにちは、私はジョンと言います！"),
    AIMessage(content="こんにちは、ジョンさん！どのようにお手伝いできますか？"),
    HumanMessage(content="私の名前がわかりますか？"),
]

result = chat(message)
print(result.content)
