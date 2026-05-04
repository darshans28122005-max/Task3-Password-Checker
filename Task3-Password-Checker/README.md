# Password Strength Checker

This project is a simple Python program that checks the strength of a password and gives suggestions to improve it.

## Features

- Takes password input from the user
- Checks password length
- Checks for uppercase letters
- Checks for lowercase letters
- Checks for numbers
- Checks for special characters
- Gives a score and strength label: Weak, Medium, or Strong
- Shows suggestions for improving the password
- Handles empty input and very short passwords

## How It Works

The program evaluates a password using these checks:

- Length of at least 8 characters
- Extra length bonus for 12 or more characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character, such as `!@#$%^&*`

The final score is used to decide the strength:

- Weak: low score or very short password
- Medium: average score
- Strong: high score with multiple password features

## How To Run

Open a terminal in this folder and run:

```bash
python password_checker.py
```

Then enter a password when asked.

## Example Output

```text
Password: hello123

Password: hello123
Score: 3/6
Strength: Medium
Suggestions:
- Use at least 12 characters for a stronger password
- Add uppercase letters
- Add special characters
```

## Test Passwords

The program was tested with:

- `hello`
- `Hello123`
- `Hello@1234`
