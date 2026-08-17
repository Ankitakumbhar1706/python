print("===== TEXT MODERATION FILTER =====")

feedback = input("Enter your feedback: ")

target_words = ["badword", "stupid", "hate"]

moderated_feedback = feedback

for word in target_words:
    moderated_feedback = moderated_feedback.replace(word, "****")

print("\n===== MODERATED FEEDBACK =====")
print("Original Feedback:", feedback)
print("Moderated Feedback:", moderated_feedback)