from variable import Variable


operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": 0}


def convert(infix_expression):
    postfix_expression = ""

    operator_stack = []
    start = 0
    while start != len(infix_expression):
        next_token = get_next_token(infix_expression, start)

        if next_token == "(":
            case_is_left_bracket(operator_stack)
        elif next_token == ")":
            postfix_expression += case_is_right_bracket(operator_stack)
        elif is_operator(next_token):
            postfix_expression += case_is_operator(next_token, operator_stack)
        else:
            postfix_expression += case_is_operand(next_token)

        start += len(next_token)

    postfix_expression += empty_stack(operator_stack)

    return postfix_expression


def case_is_operator(next_token, operator_stack):
    postfix_expression = ""

    if len(operator_stack) == 0 or operator_stack[-1] == "(":
        operator_stack.append(next_token)
    elif operators.get(operator_stack[-1]) < operators.get(next_token):
        operator_stack.append(next_token)
    else:
        while operators.get(operator_stack[-1]) >= operators.get(next_token):
            postfix_expression += operator_stack.pop() + " "
            if len(operator_stack) == 0:
                break
        operator_stack.append(next_token)
        return postfix_expression
    return ""


def empty_stack(operator_stack):
    postfix_expression = ""
    while len(operator_stack) != 0:
        postfix_expression += operator_stack.pop() + " "
    return postfix_expression


def case_is_right_bracket(operator_stack):
    postfix_expression = ""
    temp = operator_stack.pop()
    while temp != "(":
        postfix_expression += temp + " "
        temp = operator_stack.pop()
    return postfix_expression


def case_is_left_bracket(operator_stack):
    operator_stack.append("(")


def case_is_operand(next_token):
    if next_token in Variable.vrs:
        return str(Variable.vrs[next_token]) + " "
    else:
        return next_token + " "


def get_next_token(infix_expression, start):
    next_token = ""
    _next = infix_expression[start]

    if is_operator(_next) or _next == "(" or _next == ")":
        next_token += _next
        return next_token

    while (not is_operator(_next)) and (not _next == "(") and (not _next == ")") and (not start == len(infix_expression)):
        start += 1
        next_token += _next
        if start != len(infix_expression):
            _next = infix_expression[start]

    return next_token


def is_operator(string):
    return string in operators


if __name__ == "__main__":
    print("ehll")
