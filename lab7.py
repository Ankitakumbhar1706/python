print("===== TEXT ANALYZER =====")

text = input("Enter a paragraph: ")

vowels = 0
spaces = 0
characters = 0
words = 0

for ch in text:
    characters += 1

    if ch.lower() in "aeiou":
        vowels += 1

    if ch == " ":
        spaces += 1

words = len(text.split())

print("\n===== RESULT =====")

print("Characters :", characters)
print("Words      :", words)
print("Vowels     :", vowels)
print("Spaces     :", spaces)