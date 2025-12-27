while True:
    password = input("\nEnter password (or type exit): ")

    if password.lower() == "exit":
        print("Program ended")
        break

    has_upper = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True

    if len(password) < 8:
        print("Password too short")
    elif not has_upper:
        print("Add at least one uppercase letter")
    elif not has_digit:
        print("Add at least one number")
    else:
        print("Strong password ✅")
