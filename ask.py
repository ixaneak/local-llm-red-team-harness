import requests
import json

url = "http://localhost:11434/api/generate"

questions = [
    "What is a system prompt in a large language model? Answer in one sentence.",
    "What is 12 times 12?",
    "Who wrote ROmeo and Juliet?",
    "What is the capital of France?",
    "Explain what prompt injection is in one sentence.",
]

results = []

for q in questions: 
    data = {"model": "llama3.2", "prompt": q, "stream": False}
    reply = requests.post(url, json=data)
    answer = reply.json()["response"]
    print("Q:", q)
    print("A:", answer)
    print("-" * 40)
    results.append({"question": q, "answer": answer})

    with open("results .json", "w") as f:
        json.dump(results, f, indent=2)