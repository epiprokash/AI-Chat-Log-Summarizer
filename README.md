

# 🧠 AI Chat Log Summarizer

A lightweight and extensible Python-based tool to automatically **summarize AI-user chat logs**, extract **message statistics**, and identify **dominant topics** based on conversational keywords.

Designed for simplicity and effectiveness, this utility demonstrates essential **NLP techniques** in Python with real-world applicability in conversational analysis, chatbot analytics, and intelligent logging systems.

---

## 📌 Features

- 🔍 **Message Parsing**: Separates and categorizes messages from `User` and `AI`
- 📊 **Chat Statistics**: Calculates total exchanges and per-speaker message count
- 🧠 **Keyword Analysis**: Extracts most frequently used non-trivial terms (stopword removal included)
- 🗂 **Topic Inference**: Infers nature of the conversation based on contextual keywords
- 📄 **Readable Summary**: Generates structured, human-readable summaries
- 🚀 **Plug-and-play** ready for automation, enhancements, and real-world deployment

---

## 🛠 Technologies Used

- **Python 3.8+**
- [`NLTK`](https://www.nltk.org/) for stopword filtering
- `collections`, `re`, and standard libraries for efficient processing

---

## 📂 Project Structure

ai-chat-summarizer/
├── chat_summarizer.py # Main summarization script
├── text/
│ └── input_chat.txt # Sample chat log file (editable)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/epiprokash/AI-Chat-Log-Summarizer.git
cd ai-chat-summarizer
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```
