from infix_to_postfix import is_operator
from infix_to_postfix import convert

from math import pow


def evaluate(postfix_expression):
    postfix_expression = str(postfix_expression).split(" ")
    operand_stack = []

    for item in postfix_expression:
        if item == "":
            continue
        elif not is_operator(item):
            operand_stack.append(float(item))
        else:
            num1 = operand_stack.pop()
            num2 = operand_stack.pop()
            operator = item
            push_to_stack(operand_stack, num1, num2, operator)

    return operand_stack[0]


def push_to_stack(stack, num1, num2, operator):
    if operator == "+":
        stack.append(num1 + num2)
    elif operator == "-":
        stack.append(num2 - num1)
    elif operator == "*":
        stack.append(num1 * num2)
    elif operator == "/":
        stack.append(num2 / num1)
    elif operator == "^":
        stack.append(pow(num2, num1))
    pass


if __name__ == "__main__":
    exp = "-8+9"
    post = convert(exp)
    print(post)
    res = evaluate(post)
    print(res)