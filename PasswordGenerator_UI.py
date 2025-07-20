import PySimpleGUI as sg
import passgenfun as fun
import data
from display import hold
from checkP import check
from printfile import data_out
from securedfamilydb import fam_db_chk

# Define the layout
layout = [
    [sg.Text('Warm Greeting by Password Generator :P')],
    [sg.Text('1. Generate only a random Password')],
    [sg.Text('2. Generate - Manage and save a Password')],
    [sg.Text('3. Show Saved Accounts and Passwords')],
    [sg.Text('4. Check how strong your Password is!')],
    [sg.Text('0. STOP')],
    [sg.Text('_' * 100)],
    [sg.Text('Command@ '), sg.Input(key='-COMMAND-')],
    [sg.Button('Submit'), sg.Button('Exit')]
]

# Create the window
window = sg.Window('Password Generator', layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    cin = int(values['-COMMAND-'])

    if cin == '1':
        # Open a new window when cin is equal to '1'
        layout_new_window = [
            [sg.Text('New Window for Generating a Random Password')],
            # Add elements specific to the new window here
            # ...
            [sg.Button('Close')]
        ]

        # Create and display the new window
        window_new = sg.Window('Generate Password', layout_new_window)

        # Event loop for the new window
        while True:
            event_new, values_new = window_new.read()

            if event_new == sg.WIN_CLOSED or event_new == 'Close':
                window_new.close()
                break

    elif cin == 2:
        # Implement functionality for generating, managing, and saving a password
        pass  # Placeholder for your code

    elif cin == 3:
        # Implement functionality for showing saved accounts and passwords
        pass  # Placeholder for your code

    elif cin == 4:
        # Implement functionality for checking the strength of a password
        pass  # Placeholder for your code

    elif cin == 0:
        break

    else:
        sg.popup("No choice selected")

window.close()
