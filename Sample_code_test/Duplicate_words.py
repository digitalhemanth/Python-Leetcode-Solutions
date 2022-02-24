sentence = input("Please enter a sentence")
words = sentence.split()
counts = {}
for word in words:
    if word in counts:
        counts[word] = word
    counts[word] += 1
print(counts)