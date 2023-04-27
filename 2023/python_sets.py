# In Python, a set is an unordered collection of unique elements. Sets are defined using curly braces {} or the set() function.


note = {2,2,3}

note.add(5)

kotu = {6,2,9,4,6}

# note.remove(2)

# # note.remove(66)
# note.discard(66)

# note.pop()

# note.clear()



# note = note.union(kotu)

# note = note.intersection(kotu)

# note = note.symmetric_difference(kotu)

note = note.difference(kotu)


note = note.issuperset(kotu)


print(note)
