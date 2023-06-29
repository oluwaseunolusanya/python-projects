"""Credit - BOOT-DEV Challenge
A calculator class is created with features below.

1. A private instance variable called result initialized to 0.
2. Methods and their respective mathematic computations where the 
   "left-hand side" of each operation is the current value of the 
   result variable. The "right-hand side" of each operation is the 
   value passed in.

    - add(self, a)
    - subtract(self, a)
    - multiply(self, a)
    - divide(self, a): If the user attempts to divide by 0, raise a 
      ValueError with "Cannot divide by zero" as the argument
    - modulo(self, a): If the user attempts to divide by 0, raise a 
      ValueError with "Cannot divide by zero" as the argument
    - power(self, a)
    - square_root(self)

3. Helper methods
    - clear(self): reset the result variable to 0
    - get_result(self): return the current value stored in the calculator's 
      private result variable.
"""

class Calculator:
    def __init__(self):
        self.__result = 0

    def add(self, a):
        self.__result += a

    def subtract(self, a):
        self.__result -= a

    def multiply(self, a):
        self.__result *= a

    def divide(self, a):
        try:
            self.__result /= a
        except ValueError as e:
            print("Cannot divide by zero")

    def modulo(self, a):
        try:
            self.__result %= a
        except ValueError as e:
            print("Cannot divide by zero")

    def power(self, a):
        self.__result **= a

    def square_root(self):
        self.__result **= 0.5

    def clear(self):
        self.__result = 0

    def get_result(self):
        return self.__result


def test(starting_num):
    calculator = Calculator()
    calculator.add(starting_num)
    print(f"Starting number: {starting_num}")
    print(f"Result: {calculator.get_result():.2f}")
    print(f"Adding 5...")
    calculator.add(5)
    print(f"Result: {calculator.get_result():.2f}")
    print(f"Modulo 7...")
    calculator.modulo(7)
    print(f"Result: {calculator.get_result():.2f}")
    print(f"Power 2...")
    calculator.power(2)
    print(f"Result: {calculator.get_result():.2f}")
    print(f"Square root...")
    calculator.square_root()
    print(f"Result: {calculator.get_result():.2f}")
    print(f"Subtracting 3...")
    calculator.subtract(3)
    print(f"Result: {calculator.get_result():.2f}")
    print(f"Multiplying by 2...")
    calculator.multiply(2)
    print(f"Result: {calculator.get_result():.2f}")
    print(f"Dividing by 6...")
    calculator.divide(6)
    print(f"Result: {calculator.get_result():.2f}")
    print(f"Clearing...")
    calculator.clear()
    print(f"Result: {calculator.get_result():.2f}")
    print("=====================================")


def main():
    test(11.0)
    test(6.0)
    test(0.0)


main()