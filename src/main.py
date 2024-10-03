from typing import Union


class Calculator:
    def add(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('Both arguments should be numeric')
        return x + y

    def divide(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('Both arguments should be numeric')
        if y == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return x/y

    def subtraction(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('Both arguments should be numeric')
        return x - y

    def multiplication(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('Both arguments should be numeric')
        return x*y
if __name__ == '__main__':
    b = Calculator()
