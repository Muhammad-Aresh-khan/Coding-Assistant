# 🤖 Coding Assistant

Welcome to **Coding Assistant** – your AI-powered programming sidekick!  
Built on [LangChain](https://github.com/langchain-ai/langchain), [Groq](https://groq.com/) (LLaMA3 or Mixtral), and [Streamlit](https://streamlit.io/), this project brings the power of advanced language models directly to your coding workflow, all through a sleek, interactive web interface.

---

## ✨ What Makes Coding Assistant Awesome?

- **Ask Anything Code**: From bug fixes, code reviews, and tricky algorithms to tech explanations, get answers in real time.
- **Turbocharged LLMs**: Harness LLaMA3 or Mixtral via Groq for fast, contextually rich responses.
- **Single File Simplicity**: All the logic lives inside `app.py` – Streamlit UI plus agent brains, no tangled imports, no extra folders.
- **Built for Developers**: Focused on programming and software problems for practical, actionable advice.
- **Streamlit Magic**: Clean, responsive UI – just run and chat!

---

## 🚀 Quickstart

### 1. Clone This Repo

```bash
git clone https://github.com/Muhammad-Aresh-khan/Coding-Assistant.git
cd Coding-Assistant
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Get Your API Keys

- **Groq API Key**: [Get it here](https://console.groq.com/)
- (Optional) Other keys if you extend the app

Create a `.env` file in the root directory and add:
```
GROQ_API_KEY=your-groq-api-key
```

### 4. Run the Assistant

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🗂️ Project Structure

```
Coding-Assistant/
├── app.py            # Streamlit UI and agent logic (all-in-one)
├── requirements.txt  # Python dependencies
├── README.md         # You are here!
└── .env.example      # Example env file
```

> ⚡ No assistant directory or scattered modules. Everything happens in `app.py`!

---

## 🧠 Under the Hood

- **Python Only**: 100% Python for maximum hackability.
- **LangChain**: Chains together LLM reasoning, tools, and your questions.
- **Groq**: Super-fast inference for LLaMA3/Mixtral.
- **Streamlit**: Interactive, real-time chat interface.

---

## 💡 How to Use

1. Type your programming question in the chat box.
2. Get instant, well-reasoned answers from your AI agent.
3. Copy-paste code snippets, explanations, or troubleshoot your code instantly.

Example questions:
- How do I fix a `TypeError` in Python?
- Write a function to reverse a linked list.
- What’s the difference between async and threading?
- Generate a SQL query for joining two tables.

---

## 🤝 Contributing

Want to add features, support new models, or improve the UI?
1. Fork this repo
2. Make a new branch: `git checkout -b my-feature`
3. Commit and push your changes
4. Open a Pull Request

---

## 📄 License

MIT License.

---

## 🙏 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [Groq](https://groq.com/)
- [Streamlit](https://streamlit.io/)
- [Meta LLaMA3](https://ai.meta.com/llama/)

---

Made with 💻 and ☕ by [Muhammad-Aresh-khan](https://github.com/Muhammad-Aresh-khan)
