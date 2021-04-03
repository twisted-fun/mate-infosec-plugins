# pylint: disable=import-error
from mate import add_plugins, command
import ast
import operator as op

# supported operators
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.BitXor: op.xor,
    ast.USub: op.neg,
}


def eval_expr(expr):
    """
    >>> eval_expr('2^6')
    4
    >>> eval_expr('2**6')
    64
    >>> eval_expr('1 + 2*3**(4^5) / (6 + -7)')
    -5.0
    """
    return eval_(ast.parse(expr, mode="eval").body)


def eval_(node):
    if isinstance(node, ast.Num):  # <number>
        return node.n
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)


def get_output(num):
    if num < 0:
        num = 0xFFFFFFFFFFFFFFFF + 1 + num
    results = {}
    results["Hex"] = hex(num)
    results["Decimal"] = str(num)
    results["Octal"] = oct(num)
    results["Binary"] = bin(num)
    results["String"] = (
        num.to_bytes((num.bit_length() + 7) // 8, "big") or b"\0"
    ).__repr__()[1:]
    return results


@command(option="calc")
def ida_calc(self, *args):
    """A calc inspired by IDA Pro Calculator"""
    return get_output(eval_expr("".join(args)))


add_plugins(modules=[ida_calc])
