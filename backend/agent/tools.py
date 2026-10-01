import ast
import operator
from datetime import datetime
from langchain_core.tools import tool

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


@tool
def calculator(expression: str):
    """Calculate a mathematical expression."""

    expression = expression.strip()
    tree = ast.parse(expression, mode="eval")

    def evaluate(node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Only numbers are allowed.")

        if isinstance(node, ast.BinOp):
            left = evaluate(node.left)
            right = evaluate(node.right)

            operation = OPERATORS.get(type(node.op))

            if operation is None:
                raise ValueError("Operator not allowed.")

            return operation(left, right)

        if isinstance(node, ast.UnaryOp):
            value = evaluate(node.operand)

            operation = OPERATORS.get(type(node.op))

            if operation is None:
                raise ValueError("Operator not allowed.")

            return operation(value)

        raise ValueError("Expression contains something that is not allowed.")

    return evaluate(tree.body)


@tool
def get_time():
    """Get the current time."""
    return datetime.now()


tools = [calculator, get_time]
