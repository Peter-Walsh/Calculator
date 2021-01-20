import re
from variable import Variable

commands = {'/exit': 'Bye!', '/help': f'This program prints the sum or difference of a set of numbers'}


def clean_input(input_string):
    return [char for char in input_string.split(" ") if char != '']


def evaluate_input(input_string):
    expression = re.compile(r'\(?[+\-]?([A-Za-z0-9]+\s?[+\-]?)+\)?')
    assignment = re.compile(r'^.+=.+$')
    command = re.compile(r'/[\S]*')
    empty = re.compile(r'\s*')
    single = re.compile(r'^[A-Za-z0-9]+$')

    if re.match(single, input_string):
        return 'single'
    elif re.match(assignment, input_string):
        return 'assignment'
    elif re.match(expression, input_string):
        return 'expression'
    elif re.match(command, input_string):
        return 'command'
    elif re.match(empty, input_string):
        return 'empty'
    else:
        return 'NA'


def check_invalid_variable(input_string):
    variable = input_string.split('=')[0].strip()
    value = input_string.split('=')[1].strip()
    if not re.match(r'^[A-Za-z]+$', variable):
        return 'Invalid identifier'
    elif not re.match(r'^([A-Za-z]+|[+\-]?[\d]+)$', value) or input_string.count('=') > 1:
        return 'Invalid assignment'
    elif re.match(r'^[A-Za-z]+$', value) and value not in Variable.vrs:
        return 'Unknown variable'
    else:
        return False


def inspect_single(input_string):
    if re.match(r'^([0-9]+)$', input_string):
        return input_string
    elif re.match(r'^([A-Za-z]+)$', input_string) and input_string in Variable.vrs:
        return Variable.vrs[input_string]
    elif re.match(r'^([A-Za-z]+)$', input_string) and input_string not in Variable.vrs:
        return 'Unknown variable'
    else:
        return 'Invalid identifier'