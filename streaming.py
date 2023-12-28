from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

<<<<<<< HEAD
# ストリーミング
=======
>>>>>>> f925595d1883d623db0ed234e18239077cdec332
os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

chat = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
)

messeages = [HumanMessage(content="自己紹介してください")]
result = chat(messeages)
