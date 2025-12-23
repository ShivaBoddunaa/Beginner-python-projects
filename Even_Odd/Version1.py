
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
    print("=" * 40)
    print("EVEN OR ODD CHECKER")
    print("=" * 40)
    
    while True:
        print("\nMENU:")
        print("1. Check Number")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        try:
            if choice == '1':
                number = int(input("\nEnter a number: "))
                result = check_even_odd(number)
                
                print("\n" + "-" * 40)
                print(f"Number: {number}")
                print(f"Result: {result}")
                print("-" * 40)
            
            elif choice == '2':
                print("\nThank you for using Even or Odd Checker!")
                break
            
            else:
                print("\nInvalid choice! Please select 1 or 2.")
        
        except ValueError:
            print("\nInvalid input! Please enter a valid number.")

if __name__ == '__main__':
    main()