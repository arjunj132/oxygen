# module `main` source code
# this module is made for Oxygen purposes

def oxygeninfo():
    print("Oxygen is a programming language created for beginners to coding to learn about the basic concepts of coding to move on to more complex languages.\n\nThis is created by Arjun J.\n\n(c) Arjun J 2022. All rights reserved.")

def mainmoduleinfo():
    print("This is a module to provide easy access to very useful functions that are very useful for every Oxygen app.")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def modulo(num1, num2):
    return num1 % num2

def power(base, exponent):
    return base ** exponent

def pyprint(texttoprint):
    print(texttoprint)

def newline():
    print()

def convert(type,text):
    try:
        return type(text)
    except:
        print("Main - ERROR: Cannot convert to type \"" + type + "\" - this type is not callable")
        return text

def userinput(displaytext:str):
    return input(displaytext)
