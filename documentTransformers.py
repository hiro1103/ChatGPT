from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import GitLoader


# Document transformers
def file_filter(file_path):
    return file_path.endswith(".mdx")


loader = GitLoader(
    clone_url="https://github.com/langchain-ai/langchain",
    repo_path="./langchain",
    branch="master",
    file_filter=file_filter,
)

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

raw_docs = loader.load()
print(len(raw_docs))
docs = text_splitter.split_documents(raw_docs)

print(len(docs))
