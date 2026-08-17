print("===== NAME SANITIZER =====")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")


first_name = first_name.strip()
last_name = last_name.strip()

first_name = first_name.title()
last_name = last_name.title()


full_name = (f"{first_name} {last_name}")

print("\n===== CLEAN NAME =====")
print(f"Full Name: {full_name}")