# i & ii. Creating and Collecting feedback

name = input("Enter your name: ")
email = input("Enter your email: ")
comment = input("Enter your feedback: ")

# iii. Normalizing feedback
name = name.strip().title()
email = email.strip().lower()
comment = comment.strip().lower()

# iv. Extracting key information
print("\n--- Extracted Information ---")
print("Name:", name)
print("Email:", email)
print("Comment:", comment)

# v. Searching for keywords
keywords = ["good", "bad", "excellent", "poor"]
print("\n--- Keyword Search ---")
for word in keywords:
    if word in comment:
        print(f"Keyword '{word}' found in feedback")

# vi. Replacing certain words
comment = comment.replace("bad", "not good")
comment = comment.replace("poor", "needs improvement")

# vii. Formatting feedback for display
formatted_feedback = f"""
----- Customer Feedback -----
Name   : {name}
Email  : {email}
Comment: {comment}
----------------------------
"""

print(formatted_feedback)

# viii. Summarizing feedback (simple summary)
words = comment.split()
summary = " ".join(words[:5])  # first 5 words as summary

print("Summary:", summary)
