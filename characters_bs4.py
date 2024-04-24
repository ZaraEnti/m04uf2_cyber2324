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

encontrado = False
while not encontrado:
    id=input ("Intrioduce número: ")
    file = open('characters.facx', 'r')
    soup = BeautifulSoup(file, 'xml')
    file.close()
    character = soup.find('character', {'id':id})
    if not character:
        print("Error")
    else:
        encontrado = True


print("Personaje escojido es:")
print(f"\tNombre: {character.find('name').text}")
print("Personaje escojid")
print("Personaje escojido es :")
print("Personaje escojido es :")

#mostrar los items del personaje eleejido. Buscar el character
with open ('chara_items.facix', 'r') as file:
    soup = BeautifulSoup(file, 'xml')


charaItems = soup.find_all('charaItems')

for charaItem in charaItems:
    id_items = charaItem.find('items', {'id', id})

print(id_items)
                 
             
