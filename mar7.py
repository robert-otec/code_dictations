sentence = "weather is good"
words = sentence.split()

word_lengths = []
for word in words:
    word_lengths.append(len(word))

print(sentence)
print(words)
print(word_lengths)