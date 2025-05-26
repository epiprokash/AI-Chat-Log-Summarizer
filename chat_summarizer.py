import re
from collections import Counter
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def read_chat_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def parse_chat(lines):
    user_msgs, ai_msgs = [], []

    for line in lines:
        if line.startswith("User:"):
            user_msgs.append(line[5:].strip())
        elif line.startswith("AI:"):
            ai_msgs.append(line[3:].strip())

    return user_msgs, ai_msgs

def clean_and_tokenize(messages):
    stop_words = set(stopwords.words('english'))
    words = []
    for msg in messages:
        tokens = re.findall(r'\b\w+\b', msg.lower())
        words.extend([word for word in tokens if word not in stop_words and word not in string.punctuation])
    return words

def conversation_topic(keywords):
    topic_map = {
        'python': 'Python and its uses',
        'ai': 'Artificial Intelligence',
        'machine': 'Machine Learning',
        'learning': 'Machine Learning',
        'data': 'Data Science',
        'language': 'Programming Languages',
        'web': 'Web Development',
        'analysis': 'Data Analysis',
        'c': 'C Programming',
        'c++': 'C++ Programming',
        'oop': 'Object-Oriented Programming',
        'embedded': 'Embedded Systems',
    }

    matched_topics = {topic_map[word] for word in keywords if word in topic_map}
    if matched_topics:
        return " and ".join(matched_topics)
    else:
        return "General technical discussion"
    
def summarize(filepath):
    lines = read_chat_file(filepath)
    user_msgs, ai_msgs = parse_chat(lines)
    total_msgs = len(user_msgs) + len(ai_msgs)

    all_msgs = user_msgs + ai_msgs
    keywords = clean_and_tokenize(all_msgs)
    keyword_freq = Counter(keywords).most_common(5)
    keyword_list = [word for word, _ in keyword_freq]

    topic = conversation_topic(keyword_list)

    print("\nSummary:")
    print(f"- The conversation had {total_msgs} exchanges.")
    print(f"- The user asked mainly about {topic}.")
    print(f"- Most common keywords: {', '.join(keyword_list)}")

if __name__ == "__main__":
    summarize('text/input_chat.txt')