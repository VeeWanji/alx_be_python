def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations (add, subtract, multiply, divide)
    using a dictionary of lambda functions.
    """

    operations = {
        "add": lambda a, b: a + b,
        "subtract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b,
        "divide": lambda a, b: "Error: Division by zero" if b == 0 else a / b,
    }
    func = operations.get(operation)

    if func:
        return func(num1, num2)
    else:
        return "Error: Invalid operation"