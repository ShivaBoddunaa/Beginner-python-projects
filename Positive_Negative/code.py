while True:
    user_input = input("Enter a number (or type 'exit' to stop): ")

    if user_input.lower() == "exit":
        print("Program stopped.")
        break

    try:
        num = int(user_input)

        if num > 0:
            print(num, "is Positive\n")
        elif num < 0:
            print(num, "is Negative\n")
        else:
            print("The number is Zero\n")

    except ValueError:
        print("Please enter a valid number.\n")
