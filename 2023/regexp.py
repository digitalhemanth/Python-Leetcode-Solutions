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
