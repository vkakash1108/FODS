import pandas as pd
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
import nltk
nltk.download('stopwords')
def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    stop_words = set(stopwords.words('english'))
    all_comments = ' '.join(df['feedback'].astype(str).tolist())
    words = nltk.word_tokenize(all_comments.lower())
    words = [word for word in words if word.isalnum() and word not in stop_words]
    return words
def calculate_and_display_top_words(words, top_n):
    word_freq = Counter(words)
    top_words = word_freq.most_common(top_n)
    print(f"Top {top_n} words and their frequencies:")
    for word, freq in top_words:
        print(f"{word}: {freq}")
    plt.figure(figsize=(10, 6))
    plt.bar(*zip(*top_words), color='skyblue')
    plt.title(f'Top {top_n} Most Frequent Words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')
    plt.show()
def main():
    file_path = 'data.csv'  
    top_n = int(input("Enter the value of N for top words: "))
    words = load_and_preprocess_data(file_path)
    calculate_and_display_top_words(words, top_n)
if __name__ == "__main__":
    main()
