paragraph = input("Enter a paragraph: ")

paragraph = paragraph.lower()


words = paragraph.split()

count = 0

for word in words:
    if word == "python":
        count += 1

print("The word 'python' appears", count, "times.")