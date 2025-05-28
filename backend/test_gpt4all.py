from gpt4all import GPT4All

model = GPT4All("ggml-gpt4all-j.bin", model_path="backend/models")
model.open()
response = model.prompt("Summarize: The stock market fell today due to inflation fears.")
print(response)
