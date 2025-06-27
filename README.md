## 🧠 What is LiteLLM?

**LiteLLM** is a powerful Python library that allows developers to connect with multiple Large Language Models (LLMs) like:

- 🔹 OpenAI (GPT-4, GPT-3.5)
- 🔹 Google Gemini
- 🔹 Anthropic Claude
- 🔹 Mistral, Groq, Perplexity, and more

It provides a **single, unified interface** to call these models using the same function — no need to learn different SDKs or APIs.

With LiteLLM, building AI apps becomes **faster, easier, and cleaner**.

### ✅ Example Usage

```python
from litellm import completion

response = completion(
  model="openai/gpt-4o",
  messages=[{"role": "user", "content": "Hello!"}],
  api_key="your_api_key"
)

print(response.choices[0].message["content"])
