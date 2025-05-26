

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
### 3️⃣ Prepare Your Chat Log

Place your `.txt` chat file in the `text/` directory. Format should follow this structure:

`User:` What is C++?
`AI:` C++ is a general-purpose programming language created by Bjarne Stroustrup.

### 4️⃣ Run the Summarizer

```bash
python chat_summarizer.py

```

### 📄 Sample Output

Summary:
- The conversation had 10 exchanges.
- The user asked mainly about Python and its uses and Machine Learning.
- Most common keywords: python, libraries, machine, learning, development





## 👨‍💻 Developed By

**Prokash Maitra**  
*Competitive Programmer | Machine Learning Enthusiast | CSE Graduate*  

- [GitHub](https://github.com/epiprokash)  
- [LinkedIn](https://www.linkedin.com/in/prokash-maitra-8387742aa/)

