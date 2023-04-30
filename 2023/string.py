
upper() - converts all the characters in a string to uppercase.
lower() - converts all the characters in a string to lowercase.
capitalize() - converts the first character of a string to uppercase and the rest to lowercase.
title() - converts the first character of each word in a string to uppercase and the rest to lowercase.
strip() - removes whitespace characters (spaces, tabs, newlines) from the beginning and end of a string.
lstrip() - removes whitespace characters from the beginning of a string.
rstrip() - removes whitespace characters from the end of a string.
startswith(substring) - returns True if the string starts with the specified substring.
endswith(substring) - returns True if the string ends with the specified substring.
replace(old, new) - replaces all occurrences of old in the string with new.
split() - splits a string into a list of substrings, using whitespace as the delimiter by default.
join(iterable) - joins the elements of an iterable (e.g. a list) into a single string, using the string as the delimiter between elements.

text = "  hello world!  "
print(text.upper())  # "  HELLO WORLD!  "
print(text.strip())  # "hello world!"
print(text.startswith("hello"))  # True
print(text.replace("hello", "hi"))  # "  hi world!  "
words = text.split()  # ["hello", "world!"]
new_text = "-".join(words)  # "hello-world!"
