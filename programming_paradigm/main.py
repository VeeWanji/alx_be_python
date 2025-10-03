from robust_division_calculator import safe_divide

def main():
    print("Test 1: 10 / 5")
    print("Expected: The result of the division is 2.0")
    print("Actual:   ", safe_divide(10, 5))
    print()

    print("Test 2: 10 / 0")
    print("Expected: Error: Cannot divide by zero.")
    print("Actual:   ", safe_divide(10, 0))
    print()

    print("Test 3: 'ten' / 5")
    print("Expected: Error: Please enter numeric values only.")
    print("Actual:   ", safe_divide("ten", 5))
    print()

if __name__ == "__main__":
    main() 
    