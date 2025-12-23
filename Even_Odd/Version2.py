"""
Even or Odd Checker
Check if a number is even or odd
"""

def check_even_odd(number):
    """Check if number is even or odd"""
    if number % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

def main():
    print("=" * 50)
    print("🔢  EVEN OR ODD CHECKER  🔢")
    print("=" * 50)
    
    while True:
        print("\n" + "=" * 50)
        print("📱 MENU")
        print("=" * 50)
        print("1. ✅ Check Single Number")
        print("2. 📊 Check Multiple Numbers")
        print("3. 🎲 Check Random Number")
        print("0. ❌ Exit")
        print("=" * 50)
        
        choice = input("Enter your choice (0-3): ")
        
        try:
            if choice == '1':
                number = int(input("\n🔢 Enter a number: "))
                result = check_even_odd(number)
                
                print("\n" + "=" * 50)
                print("📊 RESULT")
                print("=" * 50)
                print(f"Number: {number}")
                print(f"Result: {result} ✅")
                print("=" * 50)
                
                if result == "EVEN":
                    print(f"💡 {number} is divisible by 2")
                else:
                    print(f"💡 {number} is NOT divisible by 2")
            
            elif choice == '2':
                count = int(input("\n🔢 How many numbers to check? "))
                if count < 1:
                    print("❌ Please enter a positive number!")
                    continue
                
                print("\n" + "=" * 50)
                print("📊 RESULTS")
                print("=" * 50)
                
                even_count = 0
                odd_count = 0
                
                for i in range(count):
                    number = int(input(f"Enter number {i+1}: "))
                    result = check_even_odd(number)
                    print(f"  {number} → {result}")
                    
                    if result == "EVEN":
                        even_count += 1
                    else:
                        odd_count += 1
                
                print("=" * 50)
                print(f"📈 Summary: {even_count} Even | {odd_count} Odd")
                print("=" * 50)
            
            elif choice == '3':
                import random
                number = random.randint(1, 100)
                result = check_even_odd(number)
                
                print("\n" + "=" * 50)
                print("🎲 RANDOM NUMBER CHECK")
                print("=" * 50)
                print(f"Random Number: {number}")
                print(f"Result: {result} ✅")
                print("=" * 50)
            
            elif choice == '0':
                print("\n👋 Thank you for using Even or Odd Checker!")
                print("=" * 50)
                break
            
            else:
                print("\n❌ Invalid choice! Please select 0-3.")
        
        except ValueError:
            print("\n❌ Invalid input! Please enter a valid number.")
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")

if __name__ == '__main__':
    main()