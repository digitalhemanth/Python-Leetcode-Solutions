sentence = input("Please enter a sentence")
words = sentence.split()
counts = {}
for word in words:
    if word  not in counts:
        counts[word] = 0
    counts[word] += 1
print(counts.items())