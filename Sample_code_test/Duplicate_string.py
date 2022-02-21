duplicate = []
name = "hemanth kumar"

for i in name:
    if name.count(i) > 1:
       if i not in duplicate:
          duplicate.append(i)

print(duplicate)



