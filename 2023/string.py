text = "  hello world!  "
print(text.upper())  # "  HELLO WORLD!  "
print(text.strip())  # "hello world!"
print(text.startswith("hello"))  # True
print(text.replace("hello", "hi"))  # "  hi world!  "
words = text.split()  # ["hello", "world!"]
new_text = "-".join(words)  # "hello-world!"
