
class Calculator:
    def __init__(self, a, b, operation):
        self.a = float(a)
        self.b = float(b)
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            return self.a / self.b if self.b != 0 else "Cannot divide by zero"
        else:
            return "Invalid operation"

a = float(input("Enter a: "))
b = float(input("Enter b: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

calc = Calculator(a, b, operation)
print("Result:", calc.calculate())
