#!/usr/bin/env python3
"""
Simple Calculator
A basic calculator with standard operations
"""

import math

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Addition"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtraction"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiplication"""
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Division"""
        if b == 0:
            return "Error: Division by zero!"
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, a, b):
        """Power/Exponent"""
        result = a ** b
        self.history.append(f"{a} ^ {b} = {result}")
        return result
    
    def square_root(self, a):
        """Square Root"""
        if a < 0:
            return "Error: Cannot calculate square root of negative number!"
        result = math.sqrt(a)
        self.history.append(f"√{a} = {result}")
        return result
    
    def percentage(self, a, b):
        """Calculate percentage (a% of b)"""
        result = (a / 100) * b
        self.history.append(f"{a}% of {b} = {result}")
        return result
    
    def show_history(self):
        """Display calculation history"""
        if not self.history:
            print("\n📋 No history yet!")
            return
        
        print("\n" + "=" * 50)
        print("📋 CALCULATION HISTORY")
        print("=" * 50)
        for i, calc in enumerate(self.history, 1):
            print(f"{i}. {calc}")
        print("=" * 50)
    
    def clear_history(self):
        """Clear calculation history"""
        self.history = []
        print("\n✅ History cleared!")

def main():
    calc = Calculator()
    
    print("=" * 50)
    print("🔢  SIMPLE CALCULATOR  🔢")
    print("=" * 50)
    
    while True:
        print("\n" + "=" * 50)
        print("📱 CALCULATOR MENU")
        print("=" * 50)
        print("1. ➕ Addition")
        print("2. ➖ Subtraction")
        print("3. ✖️  Multiplication")
        print("4. ➗ Division")
        print("5. 🔢 Power (a^b)")
        print("6. √  Square Root")
        print("7. 💯 Percentage")
        print("8. 📋 View History")
        print("9. 🗑️  Clear History")
        print("0. ❌ Exit")
        print("=" * 50)
        
        choice = input("Enter your choice (0-9): ")
        
        try:
            if choice == '1':
                a = float(input("\nEnter first number: "))
                b = float(input("Enter second number: "))
                result = calc.add(a, b)
                print(f"\n✅ Result: {a} + {b} = {result}")
            
            elif choice == '2':
                a = float(input("\nEnter first number: "))
                b = float(input("Enter second number: "))
                result = calc.subtract(a, b)
                print(f"\n✅ Result: {a} - {b} = {result}")
            
            elif choice == '3':
                a = float(input("\nEnter first number: "))
                b = float(input("Enter second number: "))
                result = calc.multiply(a, b)
                print(f"\n✅ Result: {a} × {b} = {result}")
            
            elif choice == '4':
                a = float(input("\nEnter first number: "))
                b = float(input("Enter second number: "))
                result = calc.divide(a, b)
                print(f"\n✅ Result: {result}")
            
            elif choice == '5':
                a = float(input("\nEnter base number: "))
                b = float(input("Enter exponent: "))
                result = calc.power(a, b)
                print(f"\n✅ Result: {a}^{b} = {result}")
            
            elif choice == '6':
                a = float(input("\nEnter number: "))
                result = calc.square_root(a)
                print(f"\n✅ Result: √{a} = {result}")
            
            elif choice == '7':
                a = float(input("\nEnter percentage: "))
                b = float(input("Enter number: "))
                result = calc.percentage(a, b)
                print(f"\n✅ Result: {a}% of {b} = {result}")
            
            elif choice == '8':
                calc.show_history()
            
            elif choice == '9':
                calc.clear_history()
            
            elif choice == '0':
                print("\n👋 Thank you for using Simple Calculator!")
                print("=" * 50)
                break
            
            else:
                print("\n❌ Invalid choice! Please select 0-9.")
        
        except ValueError:
            print("\n❌ Invalid input! Please enter valid numbers.")
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")

if __name__ == '__main__':
    main()