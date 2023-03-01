import json

file = open('New_folder_2022/uzd/students.json', 'r')
date = json.load(file)
file.close()


for s in date['Students']:
    file.write(f"{s['FirstNamet']} + {s['LastName']} + {s['Grade']} + '\n'")