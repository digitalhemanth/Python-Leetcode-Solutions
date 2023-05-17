import re

# Define a pattern
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# Create a string to search within
text = 'Contact us at email@example.com or support@example.com or my_com any'

# Search for matches using the pattern
matches = re.findall(pattern, text)

# Print the matches
for match in matches:
    print(match)
    
    
    
The re module in Python provides several methods for working with regular expressions. Here are some commonly used methods:

re.search(pattern, string): Searches for a match to the pattern anywhere in the string and returns a match object if found, or None otherwise.

re.match(pattern, string): Checks if the pattern matches at the beginning of the string and returns a match object if found, or None otherwise.

re.findall(pattern, string): Returns all non-overlapping matches of the pattern in the string as a list.

re.finditer(pattern, string): Returns an iterator yielding match objects for all non-overlapping matches of the pattern in the string.

re.split(pattern, string): Splits the string by the occurrences of the pattern and returns a list of substrings.
re.sub(pattern, repl, string): Searches for all occurrences of the pattern in the string and replaces them with the specified replacement string.

re.subn(pattern, repl, string): Similar to re.sub(), but also returns the number of substitutions made.

These are some of the most commonly used methods, but there are additional methods available in the re module for more specialized operations, such as re.fullmatch(), re.escape(), re.compile(), and more. You can refer to the Python documentation for re to explore the complete list of methods and their descriptions.
