print("===== CUSTOMER FEEDBACK FORMATTER =====")

name =str(input("Enter customer name: "))
feedback = str(input("Enter your feedback: "))
rating=int(input("enter the rating(1 to 5:)"))

name = name.strip()
print("name:",name)
feedback = feedback.strip()
print("feedback:",feedback)


formatted_name = name.title()
print(formatted_name)
formatted_feedback = feedback.capitalize()
print(formatted_feedback)
upper_feedback = feedback.upper()
print(upper_feedback)
lower_feedback = feedback.lower()
print(lower_feedback)


words = feedback.split()
print("Feedback Words:", words)


replaced_feedback = feedback.replace("good", "excellent")
print("Replaced Feedback:", replaced_feedback)


joined_feedback = " ".join(words)
print("Joined Feedback:", joined_feedback)

print("\n=====Professional Feedback======")

print(f"customer Name : {formatted_name}")
print(f"Feedback      :{formatted_feedback}")
print(f"rating        : {rating}/5")

print(f"\n Thank You , {formatted_name},for your valuable feedback.")
