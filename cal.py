import os
os.system('cls')
def good():
    print('''CREDIT:-This calculator created by github(jackthedowner))
    --------------------------------------------------------------------------------
    copyright(c) all Rights reserved Pycal v1.0
    --------------------------------------------------------------------------------
                    |////////            ========             |
                    |       | |      |   |                    |
                    |       | |      |   |            / \\     |
                    |///////| |      |   |           /   \\    |
                    |         /////////  |          //////\\   |
                    |            | |     |         /       \\  |
                    |            | |     |        /         \\ |
                    |            | |     |=======/           \\|======== V1.0
                    **THIS PROGRAM IS MADE BY github(jackthedowner)**
    -------------------------------------------------------------------------------
    ''')
good()
import math
for i in range(0,9999999999999999):
    print('''important:instruction to use this calculator''
          step-1:enter your value in a,press ENTER key
          step-2:enter your value in b,press ENTER key
          step-1:choose your operator:
                for add:you must type-add
                for subtraction: you must type-sub
                for divide:you must type-div
                for multiply:you must type-mul
                for average:you must type-avr
                for exit:you musr type-exit
                for about or help type-about or help''')

    a=input("a=")
    if a == "help" or a == "about":
        os.system('cls')
        good()
    elif a == "exit":
        os.system('cls')
        print('Thank You For Using The Program By github(jackthedowner)) :) :) :)\n\n')
        good()
        ff = input()
        break
    else:
        b=input("b=")
        if b == "help" or b == "about":
            os.system('cls')
            good()
        elif b == "exit":
            os.system('cls')
            print('Thank You For Using The Program By github(jackthedowner)) :) :) :)\n\n')
            good()
            ff = input()
            break
        else:
            userInput=input('choose operator(e.g,add(add),multiply(mul),divide(div),subtraction(sub),average(avr)')
            if userInput == "add":
                os.system('cls')
                print(int(a)+int(b))
            elif userInput == "mul":
                os.system('cls')
                print(int(a)*int(b))
            elif userInput == "div":
                os.system('cls')
                print(int(a)/int(b))
            elif userInput == "sub":
                os.system('cls')
                print(int(a)-int(b))
            elif userInput == "avr":
                os.system('cls')
                print(int(a)+int(b)/2)
            elif userInput == "exit":
                os.system('cls')
                print('Thank You For Using The Program By github(jackthedowner)) :) :) :)\n\n')
                good()
                ff = input()
                break
