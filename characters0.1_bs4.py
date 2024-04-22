#!/usr/bin/python3

from bs4 import BeautifulSoup
file = open('characters.facx', 'r')
soup = BeautifulSoup(file, 'xml')
characters = soup.find_all ("character")
file.close()

title = Bienbenido/a al Faryadventures

print(title)
print("="*len(title))

num = input("Elija su personaje: ")
for character in characters:
    print(f"{character['id']}\t {character.find('name').text}\t{character.find('age').text}\t{character.find('level')['value']}")

    if num == character['id']: 
        print(f"{soup.find('name').text}")
