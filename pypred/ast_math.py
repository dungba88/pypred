"""
This is a supplement to the ast module. It supports math operator
"""

from .ast import Node, Undefined

class MathOperator(Node):
    "Used for all the mathematical operators"

    def __init__(self, comparison, left, right):
        self.type = comparison
        self.left = left
        self.right = right
        self.func_types = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

    def name(self):
        return "%s operator at %s" % (self.type.upper(), self.position)

    def _validate(self, info):
        if self.type not in ("+", "-", "*", "/"):
            errs = info["errors"]
            errs.append("Unknown math operator %s" % self.type)
            return False
        return True

    def reverse(self):
        "Reverses the term order without changing eval"
        # Reverse the op type

    def eval(self, ctx):
        left = self.left.eval(ctx)
        right = self.right.eval(ctx)

        if left is None or isinstance(left, Undefined):
            left = 0

        if right is None or isinstance(right, Undefined):
            right = 0

        self.assert_number(left)
        self.assert_number(right)

        func = self.func_types[self.type]
        return func(left, right)

    def assert_number(self, operand):
        """assert if the operand is actually a number"""
        import numbers
        if not isinstance(operand, numbers.Number):
            type_name = type(operand).__name__
            raise ValueError(str(operand) + ' of type ' + type_name + ' is not a Number')

    def add(self, left, right):
        """add 2 operands"""
        return left + right

    def subtract(self, left, right):
        """subtract 2 operands"""
        return left - right

    def multiply(self, left, right):
        """multiply 2 operands"""
        return left * right

    def divide(self, left, right):
        """divide 2 operands"""
        return left / right

