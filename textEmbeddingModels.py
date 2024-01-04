from langchain.embeddings.openai import OpenAIEmbeddings
import os

# textをベクトル化
os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

embeddings = OpenAIEmbeddings()

query = "AWSのS3からデータを読み込むためのDocumentLoaderはありますか？"

vector = embeddings.embed_query(query)
print(len(vector))
print(vector)
