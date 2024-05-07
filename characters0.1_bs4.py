#!/usr/bin/python3

from bs4 import BeautifulSoup
file = open('characters.facx', 'r')#ponemos el modo de lectura
soup = BeautifulSoup(file, 'xml')
characters = soup.find_all ("character")
file.close()

title = "Bienbenido/a al Faryadventures"

print(title)
print("="*len(title))


for character in characters:
    print(f"{character['id']}\t{character.find('name').text}")
 
num = input("\nElija su personaje:\n")

print("")

file = open('characters.facx', 'r')
soup = BeautifulSoup(file, 'xml')
file.close()

character = soup.find('character', {'id' : num})#buscar a partir del id el parent

print("Elpersonaje elejido es:\n")
print(f"\tNombre: {character.find('name').text}")
print(f"\tEdad: {character.find('age').text}")
print(f"\tGénero: {character.find('gender')['value']}")
print(f"\tNivel: {character.find('level')['value']}")


#Sacar el nombre a partir de la tabla intermedia
file = open ('chara_items.facix', 'r')
soup = BeautifulSoup(file, 'xml')
file.close()

charaItem = soup.find('character', {'id': num}).parent
id_item = charaItem.find('items')

file = open('characters.faix', 'r')
soup = BeautifulSoup(file,'xml')
file.close()

item= soup.find('item', {'id': id_item['id']})
name_item = item.find('item').text

print(f"\tItem: {name_item}")

file = open ('chara_items.facix', 'r')
soup = BeautifulSoup(file, 'xml')
file.close()
characters_items = soup.find_all('character_item')

for character_item in characters_itmes:
    id_character = character_item.find("character")['id']

    if id_character == id:
        id_item == character_item.find
