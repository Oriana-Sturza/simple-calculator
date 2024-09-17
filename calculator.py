
---

### **2. Simple Calculator**

#### **Reviewed Code (with Comments)**:
```python
def add(x, y):
    """
    Adds two numbers.
    Args:
        x (float): The first number.
        y (float): The second number.
    Returns:
        float: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """
    Subtracts the second number from the first number.
    Args:
        x (float): The first number.
        y (float): The second number.
    Returns:
        float: The difference between x and y.
    """
    return x - y

def multiply(x, y):
    """
    Multiplies two numbers.
    Args:
        x (float): The first number.
        y (float): The second number.
    Returns:
        float: The product of x and y.
    """
    return x * y

def divide(x, y):
    """
    Divides the first number by the second number.
    Args:
        x (float): The numerator.
        y (float): The denominator.
    Returns:
        float: The result of the division, or an error message if division by zero.
    """
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero."

def main():
    """
    Main function to handle user input and perform calculations.
    """
    while True:
        print("\nOptions: add, subtract, multiply, divide, quit")
        operation = input("Choose an operation: ").lower()

        if operation == "quit":
            break

        if operation in ["add", "subtract", "multiply", "divide"]:
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue

            if operation == "add":
                print(f"Result: {add(x, y)}")
            elif operation == "subtract":
                print(f"Result: {subtract(x, y)}")
            elif operation == "multiply":
                print(f"Result: {multiply(x, y)}")
            elif operation == "divide":
                print(f"Result: {divide(x, y)}")
        else:
            print("Unknown operation. Please try again.")

if __name__ == "__main__":
    main()
