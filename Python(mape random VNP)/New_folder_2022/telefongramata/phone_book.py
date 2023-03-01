import json

file = open('telefongramata/saved_file.json', 'r')
dictionary = json.load(file)
contacts = dictionary['contacts']
file.close()

contacts = []

while(True):
    response = input('(1) add contact (2) print contacts (3) exit: ')
    if response == '1': 
        person_name = input('Name: ')
        person_surname = input('Surname: ')
        person_phone = input('Phone: ')
        #person_email = input('Email: ')

        person_contacts = {
            'name': person_name,
            'surname': person_surname,
            'phone': person_phone
            #'email': person_email
        }

        contacts.append(person_contacts)

    elif response == '2':
        for contact in contacts:
            print("---CONTACT---")
            print(f"{contact['name']} {contact['surname']}")
            print(f"phone: {contact['phone']}")
            #print(f"email: {contact['email']}")

    elif response == '3':
        print('Save data. . .')
#kods kas saglabā datus
        dictionary = {'contacts': contacts}
        file = open('telefongramata/saved_file.json', 'w')
        json.dump(dictionary, file, indent=4)
        file.close()

        print('DAta saved.')
        print('Ok, bye!')
        exit()
    else:
        print('Please, responde with 1, 2 or 3')