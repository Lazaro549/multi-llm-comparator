# 🚀 Multi LLM Comparator

A simple and powerful tool to **compare responses from multiple Large Language Models (LLMs)** side-by-side, helping you quickly identify the best output for your use case.

---

## 📌 Overview

Working with multiple AI models often leads to different answers for the same prompt. Each model has its own strengths—some are better at reasoning, others at coding, and others at creativity.

This project provides a unified interface to:

* Send a single prompt to multiple LLMs
* View responses side-by-side
* Analyze differences in quality, structure, and accuracy
* Choose the best answer quickly

---

## ✨ Features

* ⚡ **Multi-model querying** – Run prompts across multiple LLM providers
* 📊 **Side-by-side comparison** – Visualize outputs in parallel
* 🧠 **Better decision-making** – Identify strengths/weaknesses of each model
* 🔌 **Extensible architecture** – Easily plug in new models
* 💾 **Prompt reuse** – Test the same input across different models consistently

---

## 🧩 Use Cases

* Compare **code generation quality**
* Evaluate **prompt engineering strategies**
* Benchmark **model performance**
* Detect **hallucinations or inconsistencies**
* Choose the best model for a specific task

---

## 🏗️ Architecture

```
User Prompt
     │
     ▼
+----------------------+
|  Multi-LLM Router    |
+----------------------+
   │       │       │
   ▼       ▼       ▼
 Model A  Model B  Model C
   │       │       │
   +-------+-------+
           ▼
   Response Comparator
           ▼
   Side-by-Side Output
```

---

## ⚙️ Installation

```bash
git clone https://github.com/Lazaro549/multi-llm-comparator.git
cd multi-llm-comparator
```

Install dependencies:

```bash
npm install
# or
pip install -r requirements.txt
```

---

## ▶️ Usage

### Example

```bash
npm run start
```

or

```bash
python main.py
```

Then:

1. Enter a prompt
2. Select models
3. Compare results instantly

---

## 🔌 Supported Models (example)

* OpenAI (GPT series)
* Anthropic (Claude)
* Google (Gemini)
* Local models (via Ollama or similar)

> Easily extend this list by adding new providers.

---

## 📊 Example Output

| Model  | Response                              |
| ------ | ------------------------------------- |
| GPT    | Explanation with structured reasoning |
| Claude | More verbose and nuanced              |
| Gemini | Concise but sometimes less detailed   |

---

## 🛠️ Configuration

Set your API keys:

```bash
OPENAI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key
GOOGLE_API_KEY=your_key
```

---

## 🧪 Roadmap

* [ ] Automatic response ranking
* [ ] Scoring metrics (accuracy, style, latency)
* [ ] Cost tracking per request
* [ ] Response merging / ensemble mode
* [ ] UI improvements

---

## 💸 Donations

If you'd like to support this project:

* 🇦🇷 **ARS (Argentina)**
  Alias: `lazaro.503.alaba.mp`

* 🌎 **USD (Argentina only, local transfers)**
  Alias: `ahogada.duras.foca`

Thank you for your support ❤️

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Submit a PR

---

## 📄 License

MIT License

---

## ⭐ Support

If you find this project useful:

* Give it a ⭐ on GitHub
* Share it with others
* Open issues or suggest features
