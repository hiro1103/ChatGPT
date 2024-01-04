from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import GitLoader
import os


# textをベクトル化、vector storesを準備して、ドキュメントをベクトル化
# LangChainにおいて、テキストに関連するドキュメントを得るインターフェースをRetrievers


def file_filter(file_path):
    return file_path.endswith(".mdx")


loader = GitLoader(
    clone_url="https://github.com/langchain-ai/langchain",
    repo_path="./langchain",
    branch="master",
    file_filter=file_filter,
)

raw_docs = loader.load()
print(len(raw_docs))

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

docs = text_splitter.split_documents(raw_docs)
print(len(docs))

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"
embeddings = OpenAIEmbeddings()

query = "AWSのS3からデータを読み込むためのDocumentLoaderはありますか？"

vector = embeddings.embed_query(query)
print(len(vector))
print(vector)

db = Chroma.from_documents(docs, embeddings)
retriever = db.as_retriever()
query = "AWSのS3からデータを読み込むためのDocumentLoaderはありますか？"

context_docs = retriever.get_relevant_documents(query)
print(f"len = {len(context_docs)}")

first_doc = context_docs[0]
print(f"metadata = {first_doc.metadata}")
print(first_doc.page_content)
