"""simple_calculator.py

Raises:
    TypeError: if any of the inputs are not INT
    ZeroDivisionError: if the calculator tries to divide by zero

Returns:
    int: result of the calculation (addition, subtraction, multiplication, division)
"""
class SimpleCalculator:
    """ Calculator to do simple arithmetic:
        - Addition (+)
        - Subtraction (-)
        - Multiplication (*)
        - Division (/)
    """

    def add(self, x:int, y:int) -> int:
        """Adds two numbers together

        Args:
            x (int): summand 
            y (int): summand

        Returns:
            int: sum
        """
        # Verify inputs are INT
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError
        # Return sum
        return x + y
    
    def subtract(self, x:int, y:int) -> int:
        """Subtract two numbers together

        Args:
            x (int): minuend
            y (int): subtrahend

        Returns:
            int: difference
        """
        # Verify inputs are INT
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError
        # Return difference
        return x - y
    
    def multiply(self, x:int, y:int) -> int:
        """Multiply two numbers together

        Args:
            x (int): multiplier
            y (int): multiplicand

        Returns:
            int: product
        """
        # Verify inputs are INT
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError
        # Return product
        return x * y
    
    def divide(self, x:int, y:int) -> float:
        """Divides two numbers together

        Args:
            x (int): dividend/numerator
            y (int): divisor/denomincator

        Returns:
            int: quotient
        """
        # Verify inputs are INT
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError
        # Try to return quotient
        try:
            return x / y
        except ZeroDivisionError as exc:
            raise ZeroDivisionError from exc
