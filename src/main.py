import operations as op

class Calculator():
    def start(self):
        while True:
            try:
                fnum = int(input("Enter first number: "))
                snum = int(input("Enter second number: "))
                operation = input("Choose operation (Add, Subtract, Multiply, Divide): ").strip().lower()
                if operation == "add":
                    result = op.add(fnum, snum)
                elif operation == "subtract":
                    result = op.subtract(fnum, snum)
                elif operation == "multiply":
                    result = op.multiply(fnum, snum)
                elif operation == "divide":
                    result = op.divide(fnum, snum)
                else:
                    print("Invalid operation.")
                    continue
                print(f"Result: {result}")
            except ValueError:
                print("Error: Please enter numeric values.")
            except ZeroDivisionError:
                print("Error: Division by zero is not possible.")

if __name__ == "__main__":
    app = Calculator()
    app.start()