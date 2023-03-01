#1 atvert failu rakst
file = open('New_folder_2022/mau/list.csv', 'w', encoding='utf-8')
file.write("name, surname, email\n")

#2 ģenerēt sk no 1 lidz 10
#                | 1- lai nebutū 0,1,2, ... 10
#                v 2- ja 11 vietā ileikt 10, tad beigās būs 9
for i in range(1,21):
    file.write(f"Name{i}, Surname{i}, email{i}\n")

#3 aizvērt failu
file.close()