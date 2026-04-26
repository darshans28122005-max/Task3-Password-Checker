"""A simple password strength checker for beginners."""


SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"


def check_length(password):
    """Return points and suggestions based on password length."""
    if len(password) >= 12:
        return 2, []
    if len(password) >= 8:
        return 1, ["Use at least 12 characters for a stronger password"]
    if len(password) == 0:
        return 0, ["Enter a password"]
    return 0, ["Use at least 8 characters"]


def check_uppercase(password):
    """Check if the password contains at least one uppercase letter."""
    if any(character.isupper() for character in password):
        return 1, []
    return 0, ["Add uppercase letters"]


def check_lowercase(password):
    """Check if the password contains at least one lowercase letter."""
    if any(character.islower() for character in password):
        return 1, []
    return 0, ["Add lowercase letters"]


def check_digits(password):
    """Check if the password contains at least one number."""
    if any(character.isdigit() for character in password):
        return 1, []
    return 0, ["Add numbers"]


def check_special(password):
    """Check if the password contains at least one special character."""
    if any(character in SPECIAL_CHARACTERS for character in password):
        return 1, []
    return 0, ["Add special characters"]


def evaluate_password(password):
    """Evaluate a password and return its score, strength label, and suggestions."""
    checks = [
        check_length(password),
        check_uppercase(password),
        check_lowercase(password),
        check_digits(password),
        check_special(password),
    ]

    score = 0
    suggestions = []

    for points, check_suggestions in checks:
        score += points
        suggestions.extend(check_suggestions)

    # Extra handling for empty and very short passwords keeps feedback clear.
    if password == "":
        strength = "Weak"
    elif len(password) < 5:
        strength = "Weak"
    elif score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength, suggestions


def print_result(password):
    """Print the password result in a readable format."""
    score, strength, suggestions = evaluate_password(password)

    print(f"Password: {password}")
    print(f"Score: {score}/6")
    print(f"Strength: {strength}")
    print("Suggestions:")

    if suggestions:
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("- Your password is strong")

    print()


def run_tests():
    """Print results for the required sample passwords."""
    test_passwords = ["hello", "Hello123", "Hello@1234"]

    print("Password Strength Checker Test Results")
    print("--------------------------------------")

    for password in test_passwords:
        print_result(password)


def main():
    """Ask the user for a password and show its strength."""
    password = input("Password: ")
    print()
    print_result(password)


if __name__ == "__main__":
    main()
