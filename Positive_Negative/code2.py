while True:
    value = input("🔢 Enter a number (or type 🚪 exit): ")

    if value.lower() == "exit":
        print("👋 Program exited. See you!")
        break

    if not value.lstrip('-').isdigit():
        print("⚠️ Invalid input! Please enter a valid number.\n")
        continue

    num = int(value)

    if num > 0:
        print(f"✅ {num} is a POSITIVE number 😊\n")
    elif num < 0:
        print(f"❌ {num} is a NEGATIVE number 😬\n")
    else:
        print("⭕ The number is ZERO 😐\n")

