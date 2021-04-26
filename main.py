from check_input import check_invalid_variable
from check_input import evaluate_input
from check_input import inspect_single
from check_input import commands
from infix_expression import InfixExpression
from evaluate_postfix import evaluate
from infix_to_postfix import convert

from variable import Variable

# Testing the git clone thing with my own repository
# Testing...

 
def new_func():
    pass


def main():
    while True:
        user_input = input()
        input_type = evaluate_input(user_input)
        if input_type == 'expression':
            exp = InfixExpression(user_input)
            if exp.is_valid:
                print(evaluate(convert(exp.expression)))
            else:
                print("Invalid Expression")
        elif input_type == 'assignment':
            if check_invalid_variable(user_input):
                print(check_invalid_variable(user_input))
            else:
                assignment = user_input.split('=')
                name = assignment[0].strip()
                value = assignment[1].strip()
                Variable(name, value)
        elif input_type == 'single':
            print(inspect_single(user_input))
        elif input_type == 'empty':
            continue
        elif input_type == 'command':
            if user_input in commands:
                print(commands[user_input])
                if user_input == '/exit':
                    break
            else:
                print('Unknown command')
        else:
            continue


if __name__ == '__main__':
    main()
