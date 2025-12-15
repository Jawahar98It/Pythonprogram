import re

def check_username(username):
    """
    Validates a username based on common rules:
    - 3-20 characters long
    - Only alphanumeric and underscores
    - Must start with a letter
    """
    parts = username.strip().split()
    username = "".join(parts)

    if len(username) < 3 or len(username) > 20:
        return False, "Username must be 3–20 characters long"

    if not re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", username):
        return False, "Must start with a letter and contain only letters, numbers, or underscores"

    return True, "Username is valid"


if __name__ == "__main__":
    user_input = input("Enter usernames (comma-separated): ")

    test_usernames = user_input.split(",")

    for username in test_usernames:
        is_valid, message = check_username(username)
        print(f"{username.strip()}: {message}")
