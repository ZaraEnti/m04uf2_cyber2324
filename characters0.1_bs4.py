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

