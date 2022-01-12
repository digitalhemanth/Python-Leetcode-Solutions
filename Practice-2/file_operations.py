'''
Hence, in Python, a file operation takes place in the following order:
- Open a file
- Read or write (perform operation)
- Close the file
'''

#In mode, we specify whether we want to read r, write w or append a to the file.#

file = open("test.txt")    # open file in current directory
#file = open("C:/Python38/README.txt")  # specifying full path


f = open("test.txt", encoding = 'utf-8')
# perform file operations
f.close()

try:
   f = open("test.txt", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
   
'''
The best way to close a file is by using the with statement. This ensures that the file is closed when the block inside the with statement is exited.
We don't need to explicitly call the close() method. It is done internally.
'''
todos = {
         'A':'hemanth',
         'B':'Loh'
         }

import json
with open("student.json", "w") as write_file:
     json.dump(todos, write_file,indent= 4, sort_keys=True )
     
     
