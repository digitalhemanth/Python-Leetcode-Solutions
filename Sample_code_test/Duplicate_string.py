duplicate = []
name = "hemanth kumar"

for i in name:
    if name.count(i) > 1:
       if i not in duplicate:
          duplicate.append(i)

print(duplicate)



## initializing string
string = "tutorialspoint"
## initializing a list to append all the duplicate characters
duplicates = []
for char in string:
   ## checking whether the character have a duplicate or not
   ## str.count(char) returns the frequency of a char in the str
   if string.count(char) > 1:
   ## appending to the list if it's already not present
       if char not in duplicates:
           duplicates.append(char)
print(*duplicates)