# Simple Calculator
This is my simple calculator application. It supports several of the basic functions of a calculator and evaluates infix expressions with a wide range of operators and operands.

# Goal
The goal of this project was to familiarize myself with basic data structures and learn how to work with regular expressions and pattern matching in Python. 

# Functionality
- Evaluating infix expressions, can handle addition, subtraction, multiplication, division, exponentiation
- Assigning values to variables
- Evaluating declared variables in infix expressions
- Supports several built-in commands (see tutorial)
- Identifying invalid expressions and assignments

# What I learned
- Converting infix expressions to postfix expressions
- Evaluating postfix expressions
- Experience working with simple data structures (lists, stacks, queues)
- Regexes in Python
- Python programming language

# How to get started
To run the program, you need to have the following setup/installed:

- Python 3.7

After setting up with Python3, all you have to do to run the calculator is run the main.py file. Hopefully, the program doesn't crash when you try to run it. If it's working correctly, the console output should look something like the following:
```
>
```
Please note that ">" indicates that the program is waiting for user input. The console should appear to be blank, awaiting input from the user. For instructions on how to use the calculator, please see the tutorial below.

# Tutorial
This is going to be a brief tutorial on how to use the program and what kind of inputs and functions it can handle. Please note that the tutorial is a work in progress.

### Exiting the Program
The calculator supports two simple commands, one of which is the "\exit" command used to exit the program. 
```
>/exit
Bye!

Process finished with exit code 0
```

### Basic operators
The calculator can evaluate basic infix expressions, and supports several basic arithmetic operators. The operators and their corresponding symbols are as follows: addition ("+"), subtraction ("-"), multiplication ("*"), division ("/"), and exponentiation ("^").

### Evaluating basic expressions
The main purpose of the calculator is to be able to validate infix expressions. As such, it can handle a variety of different input expressions, with multiple operators, operands, and variables. Provided below are a few simple example input expressions. Please note that the ">" indicates user input.

```
> 2 + 2 
4
> 2 - 2 - 2
-2
> 2 -- 2
4
> 4 ++++   4 --+ 1
9
> 2 * 2
4
> 2 * 4 + 2
10
> 2 *** 2
Invalid Expression
> 2 // 2
Invalid Expression
> 4 + 2 / 2
5
>2^4
16
```

### Declaring Variables
Declaring variables in the program is fairly straighforward, all you have to do is assign a valid sequence of characters to a number value, and that's it. Some examples of invalid and valid variable assignments will be included below.
```
> x = 45
> x
45
> y = x
y
45
> y + x
90
> 3ab = 10
Invalid identifier
> ab3 = 10
Invalid identifier
> ab = ba
Unknown Variable
> ab = //343
Invalid Assignments
```
In order to use variables in expressions, they must have been declared in a prior statement, otherwise the calculator will print, "Unknonw Variable." Once a variable has been declared, it can be treated as just another number in the program. Variables 
may be assigned to other variables values. With regards to naming variables, all uppercase and lowercase letters are valid. 
Attempting to declare a variable name comprised of numerical values and other characters misc characters should produce an "Invalid identifier" error.













