import string

text = input("Enter a line of text: ")
word_counts = {}

for word in text.lower().split():
    word = word.strip(string.punctuation)
    if word:
        word_counts[word] = word_counts.get(word, 0) + 1

if len(word_counts) == 0:
    print("No words found.")
else:
    print("\n--- WORD FREQUENCIES ---")
    for word, count in word_counts.items():
        print(f"{word}: {count}")
