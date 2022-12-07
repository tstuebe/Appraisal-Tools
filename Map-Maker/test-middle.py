# DO NOT USE UNLESS NECESSARY

subject = '<name>Acton</name>'
end = '<placemark>'

with open('test.txt') as oldfile, open('trash/new_middle.txt', 'w') as newfile:
    file_lines = oldfile.readlines()
    for i, line in enumerate(file_lines):
        if subject in line:
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
            newfile.write("\n  " + f13.strip())
