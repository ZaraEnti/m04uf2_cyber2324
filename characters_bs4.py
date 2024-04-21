#!/usr/bin/python3

#Ejercicio haciendo lo mismo pero con otra libreria


from bs4 import BeautifulSoup

#abrir el fichero
with open("characters.facx") as file:
    soup = BeautifulSoup(file, 'xml')


#funcion len para la cantidad de personajes para
num_character = len(soup.find_all('character'))


#sacar el texto del nombre
characters = soup.find_all('character')

#for en el rango de las cantidades encontradas
for character in characters:


#acceso texto
    name = character.find('name').string
    age = character.find('age').string 
#acceso a los valores    
    gender =character.gender['value']
    level = character.level['value']

    print(f"\t{name} \t{age} \t{gender} \t{level}")
