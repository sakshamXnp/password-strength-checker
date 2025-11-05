import re
import math

COMMON_PASSWORDS = ["password", "123456", "qwerty", "letmein", "admin", "welcome"]

def password_entropy(password):
    # Estimate entropy based on character sets used
    pool = 0
    if re.search(r"[a-z]", password): pool += 26
    if re.search(r"[A-Z]", password): pool += 26
    if re.search(r"[0-9]", password): pool += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): pool += 32

    if pool == 0:
        return 0
    entropy = math.log2(pool ** len(password))
    return round(entropy, 2)

def estimate_crack_time(entropy):
    guesses = 2 ** entropy
    guesses_per_second = 1e9  # assume 1 billion guesses/sec
    seconds = guesses / guesses_per_second

    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    else:
        return f"{seconds/31536000:.2f} years"
    
def contains_sequence(password):
    sequences = ["1234", "abcd", "qwerty"]
    for seq in sequences:
        if seq in password.lower():
            return True
    return False

def password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Too short (minimum 8 characters).")

    # Upper/lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Use both uppercase and lowercase letters.")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Add some numbers.")

    # Special chars
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
         score += 1
    else:
        feedback.append("❌ Add special characters.")

    # Common passwords
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("❌ This is a common password. Avoid it!")

    # Sequence check
    if contains_sequence(password):
        feedback.append("❌ Avoid common sequences like '1234' or 'abcd'.")

    # Repeated characters
    if re.search(r"(.)\1{2,}", password):
        feedback.append("❌ Avoid repeated characters (e.g., aaa, 111).")

    # Final evaluation
    if score >= 5:
        strength = "🔒 Very Strong"
    elif score == 4:
        strength = "💪 Strong"
    elif score == 3:
        strength = "🙂 Medium"
    else:
        strength = "⚠️ Weak"

    # Entropy and crack time
    entropy = password_entropy(password)
    crack_time = estimate_crack_time(entropy)

    return strength, feedback, entropy, crack_time

# --- Run the checker ---
if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    strength, issues, entropy, crack_time = password_strength(pwd)

    print("\nPassword Strength:", strength)
    print(f"🔑 Entropy: {entropy} bits")
    print(f"⏱️ Estimated crack time: {crack_time}")

    if issues:
        print("\nSuggestions:")
        for item in issues:
            print(" -", item)