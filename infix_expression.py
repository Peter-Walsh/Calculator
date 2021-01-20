import re

from infix_to_postfix import is_operator
from infix_to_postfix import convert
from evaluate_postfix import evaluate
from variable import Variable


class InfixExpression:

    def __init__(self, expression):
        self.expression = str(expression)
        self.is_valid = True
        self.clean()
        self.validate()

    def clean(self):
        self.clean_whitespace()
        self.clean_operators()
        self.clean_negatives()
        self.clean_whitespace()

    def validate(self):
        self.check_operators()
        self.check_brackets()

    def clean_whitespace(self):
        self.expression = self.expression.replace(" ", "")
        pass

    def clean_operators(self):
        addition_1 = re.compile("[+]+")
        addition_2 = re.compile("--")
        subtraction_1 = re.compile("\+-")
        subtraction_2 = re.compile("-\+")
        multiplication_1 = re.compile("\*-[A-Za-z0-9.]+")

        # convert double minus signs to addition signs first
        self.expression = re.sub(addition_2,"+", self.expression)
        # convert extra addition signs into single addition sign
        self.expression = re.sub(addition_1,"+", self.expression)
        # convert "adding negative" to just subtraction ie. > 5 +-9 >> 5 - 9
        self.expression = re.sub(subtraction_2,"-", self.expression)
        self.expression = re.sub(subtraction_1,"-", self.expression)
        pass

    def clean_negatives(self):

        i = 1
        while i < len(self.expression):
            next_item = self.expression[i]
            prev_item = self.expression[i - 1]

            if (prev_item == "*" or prev_item == "/") and (next_item == "-"):
                next_token = ""
                index = i + 1
                while index < len(self.expression) and \
                        not is_bracket(self.expression[index]) and \
                        not is_operator(self.expression[index]):

                    next_token += self.expression[index]
                    index += 1

                first_half = self.expression[0: i]
                next_token = "(0-" + next_token + ")"
                second_half = self.expression[index: len(self.expression)]
                self.expression = first_half + next_token + second_half
                i += len(next_token)
            else:
                i += 1

    def clean_more_negatives(self):
        i = 0
        while i < len(self.expression):
            next_item = self.expression[i]
            if next_item == "-":
                index = i + 1
                next_token = ""
                while index < len(self.expression) and \
                    not is_bracket(self.expression[index]) and \
                    not is_operator(self.expression[index]):

                    next_token += self.expression[index]
                    index += 1

                first_half = self.expression[0:i]
                next_token = "+(0-" + next_token + ")"
                second_half = self.expression[index: len(self.expression)]
                self.expression = first_half + next_token + second_half
                i += len(next_token)
            else:
                i += 1



    def check_operators(self):
        invalid_operator_pattern = re.compile("[*/][*/]+")
        if invalid_operator_pattern.search(self.expression) is not None:
            self.is_valid = False

    def check_brackets(self):
        bracket_stack = []

        for char in self.expression:
            if char == "(":
                bracket_stack.append(char)
            elif char == ")" and len(bracket_stack) != 0:
                bracket_stack.pop()
            elif char == ")":
                self.is_valid = False
                break

        if len(bracket_stack) != 0:
            self.is_valid = False


def is_bracket(string):
    return string == "(" or string == ")"


if __name__ == "__main__":
    var = Variable("x", "2")

    expression = "8 + 24 - (6 - 8)"
    infix_exp = InfixExpression(expression)
    expression = convert(infix_exp.expression)
    print(expression)
    print(evaluate(expression))