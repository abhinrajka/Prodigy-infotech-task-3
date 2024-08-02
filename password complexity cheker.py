import re

def password_strength(password):
    # Initialize variables to track the presence of different character types
    length = len(password)
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[\W_]', password) is not None

    # Assess the strength based on criteria
    strength = 0
    if length >= 8:
        strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    # Provide feedback based on the strength score
    feedback = ""
    if strength == 5:
        feedback = "Very Strong"
    elif strength == 4:
        feedback = "Strong"
    elif strength == 3:
        feedback = "Moderate"
    elif strength == 2:
        feedback = "Weak"
    else:
        feedback = "Very Weak"

    # Suggest improvements
    suggestions = []
    if length < 8:
        suggestions.append("Increase the length to at least 8 characters.")
    if not has_upper:
        suggestions.append("Add uppercase letters.")
    if not has_lower:
        suggestions.append("Add lowercase letters.")
    if not has_digit:
        suggestions.append("Add digits.")
    if not has_special:
        suggestions.append("Add special characters.")

    return feedback, suggestions

# Example usage
password = input("Enter your password: ")
feedback, suggestions = password_strength(password)
print(f"Password Strength: {feedback}")
if suggestions:
    print("Suggestions to improve your password:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
