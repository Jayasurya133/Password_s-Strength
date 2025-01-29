import re

# Function to check password strength
def check_password_strength(password):
    strength = {"length": False, "uppercase": False, "lowercase": False, "digit": False, "special_char": False}
    
    # Check password length
    if len(password) >= 8:
        strength["length"] = True
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength["uppercase"] = True
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength["lowercase"] = True
    
    # Check for digits
    if re.search(r'[0-9]', password):
        strength["digit"] = True
    
    # Check for special characters
    if re.search(r'[\W_]', password):  # [\W_] matches non-alphanumeric characters (special characters)
        strength["special_char"] = True
    
    return strength

# Function to provide feedback
def provide_feedback(strength):
    feedback = []
    
    if not strength["length"]:
        feedback.append("Password should be at least 8 characters long.")
    if not strength["uppercase"]:
        feedback.append("Password should contain at least one uppercase letter.")
    if not strength["lowercase"]:
        feedback.append("Password should contain at least one lowercase letter.")
    if not strength["digit"]:
        feedback.append("Password should contain at least one digit.")
    if not strength["special_char"]:
        feedback.append("Password should contain at least one special character (e.g., !@#$%).")
    
    return feedback

# Main function to check password and give feedback
def password_strength_checker():
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    
    # If the password meets all requirements
    if all(strength.values()):
        print("Password is strong!")
    else:
        print("Password is weak. Here's how to improve it:")
        feedback = provide_feedback(strength)
        for f in feedback:
            print(f)

# Run the checker
if __name__ == "__main__":
    password_strength_checker()
