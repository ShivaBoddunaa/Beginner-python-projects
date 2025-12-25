while True:
    user_input = input("Enter a year (or type 'exit' to stop): ")

    if user_input.lower() == "exit":
        print("Program stopped.")
        break

    if not user_input.isdigit():
        print("Please enter a valid year.")
        continue

    year = int(user_input)

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a Leap Year\n")
    else:
        print(year, "is NOT a Leap Year\n")
