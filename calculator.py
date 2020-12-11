# create calculator using python

import re


print('Our Magical Calculator')
print('Type Quit to exit')
print('Select Mathematical Equation')
print('Press 1 to ')


previous = 0
run = True


def performMath():
    global run
    global previous
    equation = ""

    # if previous == 0:
    #     equation = "Enter equation"
    # else:
    #     equation = input(str(previous))

    equation = input('Enter Equation: ')

    if equation == 'Quit':
        run = False
        print('Good Bye')
    else:
        equation = re.sub('[a-zA-Z]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

        print('Result is', previous)


while run:
    performMath()
