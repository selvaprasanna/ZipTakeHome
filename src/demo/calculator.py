"""
A simple calculator module for demonstration purposes.
This module provides basic arithmetic operations.
"""


class Calculator:
    """A calculator class that performs basic arithmetic operations."""

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtracts two numbers."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base, exponent):
        """Power of two numbers."""
        return base ** exponent
