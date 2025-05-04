def email_slicer():
    print("Welcome to the Email Slicer!")
    email = input("Enter your email address: ").strip()

    if '@' not in email:
        print("Invalid email format. Please include '@'.")
        return

    try:
        username, domain = email.split('@')
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    except ValueError:
        print("Error: Unable to process the email address.")

if __name__ == "__main__":
    email_slicer()
