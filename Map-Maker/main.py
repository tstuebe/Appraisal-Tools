import PySimpleGUI as sg

# import list
from new_list import neighborhoods as nh

# open files
beginning = ['<!-- Beginning -->']
middle = []
end = ['<!-- End -->']

# layout
layout = [  [sg.Text('Enter Desired File Name'), sg.InputText()],
            [sg.Text('Please Choose a Neighborhood'), sg.InputCombo(nh)],
            [sg.Button('Write Beginning'), sg.Button('Write Middle'), sg.Button('Write End'),sg.Button('Quit')] ]

window = sg.Window('Los Angeles Neighborhood Map Maker', layout)

while True:
    event, values = window.read()
    fileName = "map-files/" + values[0] + ".kml" # name kml
    middle = values[1]

    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    
    if event == 'Write Beginning':
        with open('neighborhoods.txt') as oldfile, open(fileName, 'w') as newfile:
            for line in oldfile:
                # write beginning
                if any(i in line for i in beginning):
                    newfile.write(line)


    if event == 'Write Middle':
        with open('neighborhoods.txt') as oldfile, open(fileName, 'a') as newfile:
            file_lines = oldfile.readlines()
            for i, line in enumerate(file_lines):
                if middle in line:
                    f1 = file_lines[i-1]
                    f2 = file_lines[i]
                    f3 = file_lines[i+1]
                    f4 = file_lines[i+2]
                    f5 = file_lines[i+3]
                    f6 = file_lines[i+4]
                    f7 = file_lines[i+5]
                    f8 = file_lines[i+6]
                    f9 = file_lines[i+7]
                    f10 = file_lines[i+8]
                    f11 = file_lines[i+9]
                    f12 = file_lines[i+10]
                    f13 = file_lines[i+11]
                    newfile.write("\n  " + f1.strip())
                    newfile.write("\n    " + f2.strip())
                    newfile.write("\n    " + f3.strip())
                    newfile.write("\n    " + f4.strip())
                    newfile.write("\n        " + f5.strip())
                    newfile.write("\n        " + f6.strip())
                    newfile.write("\n        " + f7.strip())
                    newfile.write("\n        " + f8.strip())
                    newfile.write("\n        " + f9.strip())
                    newfile.write("\n        " + f10.strip())
                    newfile.write("\n    " + f11.strip())
                    newfile.write("\n      " + f12.strip())
                    newfile.write("\n  " + f13.strip() + "\n")
    if event == 'Write End':
        with open('neighborhoods.txt') as oldfile, open(fileName, 'a') as newfile:
            for line in oldfile:
                # write end
                if any(i in line for i in end):
                    newfile.write(line)
            



window.close()