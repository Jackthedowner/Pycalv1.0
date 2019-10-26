print('''CREDIT:-This calculator created by github(jackthedowner))
--------------------------------------------------------------------------------
copyright(c) all Rights reserved Pycal v1.0
--------------------------------------------------------------------------------
                |////////            ========             |
                |       | |      |   |                    |
                |       | |      |   |            / \     |
                |///////| |      |   |           /   \    |
                |         /////////  |          //////\   |
                |            | |     |         /       \  |
                |            | |     |        /         \ |
                |            | |     |=======/           \|======== V1.0

                **THIS PROGRAM IS MADE BY github(jackthedowner)**

-------------------------------------------------------------------------------
''')
import math
print('''important:instruction to use this calculator''
      step-1:enter your value in a,press ENTER key
      step-2:enter your value in b,press ENTER key
      step-1:choose your operator:
            for add:you must type-add
            for subtraction: you must type-sub
            for divide:you must type-div
            for multiply:you must type-mul
            for average:you must type-avr''')

a=input("a=")
b=input("b=")
userInput=input('choose operator(e.g,add(add),multiply(mul),divide(div),subtraction(sub),average(avr)')
if userInput == "add":
    print(int(a)+int(b))
if userInput == "mul":
    print(int(a)*int(b))
if userInput == "div":
    print(int(a)/int(b))
if userInput == "sub":
    print(int(a)-int(b))
if userInput == "avr":
    print(int(a)+int(b)/2)
