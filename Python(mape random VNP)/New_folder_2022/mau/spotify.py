import csv
import json

file_name = 'New_folder_2022/mau/spotify.csv'
json_file_name = 'New_folder_2022/mau/song.json'

song_list = []


with open (file_name,'r', encoding='UTF8') as data_file:
    for line in csv.DictReader(data_file):
        song_list.append(line)

with open(json_file_name, 'w', encoding='UTF8') as json_file:
    json.dump(song_list, json_file, indent=4)

#lai prog. parāda tikai termin. dziesm. nosk.
#for song in song_list:
#    print(f'{song["Title"]} {song["Popularity"]}')


song_year = []
song_genres = []
for song in song_list:
    if song("Year") not in song_year:
        song_year.append(song['Year'])
    if song['Genre'] not in song_genres:
        song_genres.append(song['Genre'])

song_year.sort()
print(song_year)
song_genres.sort()
print(song_genres)

