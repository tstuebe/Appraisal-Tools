import PySimpleGUI as sg

def compWriter():
    layout = [[(sg.Text('Fill Out Form Below:', size=[40, 1]))],
              [sg.Text('Comp Name'), sg.InputText()],
              [sg.Text('Comp Address'), sg.InputText()],
              [sg.Text('Location (City)'), sg.InputText()],
              [sg.Text('Year Built'), sg.InputText()],
              [sg.Text('Number of Stories'), sg.InputText()],
              [sg.Text('% Occupied'), sg.InputText()],
              [sg.Text('Minimum Lease Term'), sg.InputText()],
              [sg.Text('Utilities Included'), sg.InputText()],
              [sg.Output(size=(70, 15))],
              [sg.Button('SEND'), sg.Button('EXIT')]]

    # window = sg.Window('Chat Window', layout, default_element_size=(30, 2))
    window = sg.Window('Comparable Comment Writer', layout)

    while True:
        event, value = window.read()
        if event == 'SEND':
            print(value[0] + " is located at " + value[1] + " and represents market rent for " + value[2] + ", California. It was built in " + value[3] + " and is " + value[4] + " stories tall. The project is currently " + value[5] + "% occupied and typical lease terms are " + value[6] + " months. Rent includes " + value[7] + ".")
        else:
            break
    window.close()
compWriter()