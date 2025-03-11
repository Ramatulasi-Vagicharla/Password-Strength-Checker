import math
import string
import random

# Common weak passwords list
COMMON_PASSWORDS = {"123456", "password", "qwerty", "abc123", "letmein", "monkey", "football"}

# Character categories for analysis
CHAR_CATEGORIES = {
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "digits": string.digits,
    "special": string.punctuation,
}

# Function to calculate entropy (strength measure)
def calculate_entropy(password):
    pool_size = 0
    for key, chars in CHAR_CATEGORIES.items():
        if any(c in chars for c in password):
            pool_size += len(chars)
    
    entropy = len(password) * math.log2(pool_size) if pool_size else 0
    return round(entropy, 2)

# Function to check password strength
def check_password_strength(password):
    strength = {
        "length": len(password) >= 12,
        "lowercase": any(c in string.ascii_lowercase for c in password),
        "uppercase": any(c in string.ascii_uppercase for c in password),
        "digits": any(c in string.digits for c in password),
        "special": any(c in string.punctuation for c in password),
        "common": password not in COMMON_PASSWORDS
    }
    
    score = sum(strength.values())
    entropy = calculate_entropy(password)

    if score == 6 and entropy >= 60:
        rating = "Very Strong 🔥"
    elif score >= 4:
        rating = "Strong 💪"
    elif score >= 3:
        rating = "Moderate ⚠️"
    else:
        rating = "Weak ❌"

    return {"rating": rating, "entropy": entropy, "breakdown": strength}

# Function to suggest a strong password
def generate_strong_password(length=12):
    if length < 12:
        length = 12

    categories = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    password = [random.choice(cat) for cat in categories]  # Ensure at least one from each category
    password += random.choices(string.ascii_letters + string.digits + string.punctuation, k=length - 4)
    random.shuffle(password)

    return "".join(password)

# User Input and Output
if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    result = check_password_strength(user_password)

    print("\n🔍 Password Strength Analysis:")
    print(f"🔹 Strength Rating: {result['rating']}")
    print(f"🔹 Entropy Score: {result['entropy']} bits")
    print(f"🔹 Breakdown: {result['breakdown']}")

    if result['rating'] in ["Weak ❌", "Moderate ⚠️"]:
        print("\n🔐 Suggested Strong Password:", generate_strong_password())
