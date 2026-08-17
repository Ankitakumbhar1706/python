email_text = input("Enter the email text: ")

at_count = 0
dot_count = 0
exclamation_count = 0

for ch in email_text:
    if ch == "@":
        at_count += 1
    elif ch == ".":
        dot_count += 1
    elif ch == "!":
        exclamation_count += 1

print("\n===== EMAIL SCANNER =====")
print("@ occurrences:", at_count)
print(". occurrences:", dot_count)
print("! occurrences:", exclamation_count)