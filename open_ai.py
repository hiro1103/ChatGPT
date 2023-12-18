# Chat Completions API の呼び出し

import openai
openai.api_key="自分のAPIキーを指定"

response=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"You are a a helpful assistant."},
        {"role":"user","content":"Hello! I'm John."}
    ]
)

print(response)