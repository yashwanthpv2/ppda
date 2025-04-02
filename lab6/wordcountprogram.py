
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words)
word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1
print(f"Total word count: {word_count}")
print("Word frequencies:", word_frequency)
