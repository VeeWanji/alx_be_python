number = int(input("Enter a number to generate its multiplication table: "))
except ValueError:
    print("Please enter a valid integer.")
    exit(1)
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}") 




