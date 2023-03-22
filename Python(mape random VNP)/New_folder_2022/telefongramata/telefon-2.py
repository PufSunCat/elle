import json
import csv

contacts_list = []

def LoadContacts():    
    with open('New_folder_2022/telefongramata/contacti.json', 'r', encoding='UTF8') as file:        
        data = json.load(file)
        global contacts
        contacts = data['contacts_list']    

def PrintContacts():
    for contact in contacts:
        print(f"{contact['name']} {contact['surname']} {contact['number']} {contact['email']}")

def AddContact():
    name = input('Enter name: ')
    surname = input('Enter surname: ')
    number = input('Enter number: ')
    email = input('Enter email: ')

    contact = {
        'name': name, 
        'surname': surname, 
        'number': number,
        'email': email
    }

    contacts.append(contact)

def DeleteContact():
    name = input('Enter name: ')
    found = False

    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)        
            found = True
            break

    if found:
        print(f"{name} has been deleted.")
    else:
        print(f"{name} not found.")

def SaveContacts(format):
    if format == 'json':
        SaveContactsJson()
    elif format == 'csv':
        SaveContactsCSV()
    else:
        print('No file saved. File format not defined.')

def SaveContactsJson():
    with open('New_folder_2022/telefongramata/contacti.json', 'w', encoding='UTF8') as file:
        contacts_dict = {'contacts_list': contacts}
        json.dump(contacts_dict, file, indent=4)

def SaveContactsCSV():
    with open('New_folder_2022/telefongramata/contacti.csv', mode='w', newline='', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'surname', 'number', 'email'])
        for contact in contacts:
            writer.writerow([contact['name'], contact['surname'], contact['number'], contact['email']])

LoadContacts()
while(True):
    response = input('A-add new, D-delete,P-print, S-save as CSV, E-exit: ')
    if response == 'A':        
        AddContact()
        SaveContacts('json')             
    elif response == 'P':
        PrintContacts()
    elif response == 'D':
        DeleteContact()
        SaveContacts('json')       
    elif response == 'S':
        SaveContactsCSV()
    elif response == 'E':
        print('Bye bye!')
        break
