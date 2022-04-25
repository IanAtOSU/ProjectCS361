import math
import PySimpleGUIQt as gui
import reset

ops = ['+', '-', '*']
nums = ['1', '3', '5', '8']

layout = [[gui.Text("Math Game!", font=("Helvetica", 35), text_color = 'red', justification = 'c', key = '-Title-')],
          [gui.Text("Start Training Your Math Skills!", font=("Helvetica", 20))],
          [gui.Button("Play", size_px = (100,50))],
          [gui.Text("Ready to Quit?", font=("Helvetica", 20))],
          [gui.Button("Exit", size_px = (100,50))]]
layout = [[gui.Column(layout, element_justification = 'c')]]

# Create the window
window = gui.Window("Math Game!", layout)

# Create an event loop
checker = 0
equation = ""
clicked = [0,0,0,0,0,0,0]
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Exit" or event == gui.WIN_CLOSED:
        break
    elif event == "Back":
        layout = [[gui.Text("Math Game!", font=("Helvetica", 35), text_color = 'red', justification = 'c', key = '-Title-')],
                  [gui.Text("Start Training Your Math Skills!", font=("Helvetica", 20))],
                  [gui.Button("Play", size_px = (100,50))],[gui.Text("Ready to Quit?", font=("Helvetica", 20))],[gui.Button("Exit", size_px = (100,50))]]
        layout = [[gui.Column(layout, element_justification = 'c')]]
        window.close()
        window = gui.Window("Math Game!", layout)
    elif event == "Play":
        layout = [[gui.Text("Math Game!!", text_color ='red', font = ("Helvetica",35), key = '-Title-')],
                  [gui.Text("Score: ", text_color ='red', font = ("Helvetica",25), key = '-Score-')],
                  [gui.Text("", text_color ='yellow', font = ("Helvetica",20), key = '-Equation-')],
                  [gui.Text("Click the buttons bellow to create your equation:", font = ("Helvetica",20), key = '-Explain-')],
                  [gui.Button(nums[0], key = '-n0-', size_px = (50,50)),gui.Button(nums[1], key = '-n1-', size_px = (50,50)),gui.Button(nums[2], key = '-n2-', size_px = (50,50)),gui.Button(nums[3], key = '-n3-', size_px = (50,50))],
                  [gui.Button(ops[0], key = '-o0-', size_px = (50,50)), gui.Button(ops[1], key = '-o1-', size_px = (50,50)), gui.Button(ops[2], key = '-o2-', size_px = (50,50))],
                  [gui.Button("Enter", key = '-Enter-', size_px = (100,50))]]
        layout = [[gui.Column([[gui.Button("Back", size_px = (50,30))]],element_justification = 'l')], [gui.Column(layout, element_justification = 'c')]]
        window.close()
        window = gui.Window("Math Game!", layout)
    elif event == '-n0-':
        if clicked[0] == 1:
            if gui.popup_ok_cancel("Are you sure you want to restart your equation?") == 'OK':
                clicked = [0,0,0,0,0,0,0]
                equation = ""
                window['-Equation-'].update(equation)
                checker = 0
                for i in range(0,4):
                    window['-n'+str(i)+'-'].update(nums[i])
                for i in range(0,3):
                    window['-o'+str(i)+'-'].update(ops[i])
        elif checker == 0:
            equation = equation + nums[0]
            window['-Equation-'].update(equation)
            checker = 1
            window['-n0-'].update('x')
            clicked[0] = 1
    elif event == '-n1-':
        if clicked[1] == 1:
            if gui.popup_ok_cancel("Are you sure you want to restart your equation?") == 'OK':
                equation = reset.rest_equation(window, nums, ops)
                clicked = [0,0,0,0,0,0,0]
                checker = 0
        elif checker == 0:
            equation = equation + nums[1]
            window['-Equation-'].update(equation)
            checker = 1
            window['-n1-'].update('x')
            clicked[1] = 1
    elif event == '-n2-':
        if clicked[2] == 1:
            if gui.popup_ok_cancel("Are you sure you want to restart your equation?") == 'OK':
                equation = reset.rest_equation(window, nums, ops)
                clicked = [0,0,0,0,0,0,0]
                checker = 0
        elif checker == 0:
            equation = equation + nums[2]
            window['-Equation-'].update(equation)
            checker = 1
            window['-n2-'].update('x')
            clicked[2] = 1
    elif event == '-n3-':
        if clicked[3] == 1:
            if gui.popup_ok_cancel("Are you sure you want to restart your equation?") == 'OK':
                equation = reset.rest_equation(window, nums, ops)
                clicked = [0,0,0,0,0,0,0]
                checker = 0
        elif checker == 0:
            equation = equation + nums[3]
            window['-Equation-'].update(equation)
            checker = 1
            window['-n3-'].update('x')
            clicked[3] = 1
    elif event == '-o0-':
        if clicked[4] == 1:
            if gui.popup_ok_cancel("Are you sure you want to restart your equation?") == 'OK':
                equation = reset.rest_equation(window, nums, ops)
                clicked = [0,0,0,0,0,0,0]
                checker = 0
        elif checker == 1:
            equation = equation + ops[0]
            window['-Equation-'].update(equation)
            checker = 0
            window['-o0-'].update('x')
            clicked[4] = 1
    elif event == '-o1-':
        if clicked[5] == 1:
            if gui.popup_ok_cancel("Are you sure you want to restart your equation?") == 'OK':
                equation = reset.rest_equation(window, nums, ops)
                clicked = [0,0,0,0,0,0,0]
                checker = 0
        elif checker == 1:
            equation = equation + ops[1]
            window['-Equation-'].update(equation)
            checker = 0
            window['-o1-'].update('x')
            clicked[5] = 1
    elif event == '-o2-':
        if clicked[6] == 1:
            if gui.popup_ok_cancel("Are you sure you want to restart your equation?") == 'OK':
                equation = reset.rest_equation(window, nums, ops)
                clicked = [0,0,0,0,0,0,0]
                checker = 0
        elif checker == 1:
            equation = equation + ops[2]
            window['-Equation-'].update(equation)
            checker = 0
            window['-o2-'].update('x')
            clicked[6] = 1
    elif event == "-Enter-":
        if equation != "":
            score = eval(equation)
            window["-Score-"].update("Score: " + str(score))
    
window.close()
