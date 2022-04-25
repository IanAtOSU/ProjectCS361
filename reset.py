import math
import PySimpleGUI as gui


def rest_equation(window, nums, ops):
    equation = ""
    window['-Equation-'].update(equation)
    for i in range(0,4):
        window['-n'+str(i)+'-'].update(nums[i])
    for i in range(0,3):
        window['-o'+str(i)+'-'].update(ops[i])
    return equation
