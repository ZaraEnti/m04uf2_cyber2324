#!/usr/bin/python3

from bs4 import BeautifulSoup
file = open('characters.facx', 'r')#ponemos el modo de lectura
soup = BeautifulSoup(file, 'xml')#tipo de documento

characters = soup.find_all ("character")
file.close()#una vez sacamos la información pues lo podemos cerrar ya que esta guardada en una variable

title = "\nBienbenido/a al Faryadventures"

print(title)

for character in characters:
    print(f"{character['id']}\t{character.find('name').text}")

option = input("Quieres matar a un  personaje?(y/n)")
if option == 'y':
    num = input("\nElija a quien quiere matar: ")
    
    kill_character = soup.find('character', {'id' : num})#personaje elegido para elminar
    

    #bucle para tener nuetra nueva cadena de caracteres
    for character in characters:
        if kill_character == character:
            characters.remove(kill_character)#función remove para quitar el personaje
            print(f"Has matado: {character.find('name').text}")
else:        


    num = input("\nElija su personaje:\n")

    print("")

    character = soup.find('character', {'id' : num})#buscar a partir del id el parent

    print("El personaje elejido es:\n")
    print(f"\tNombre: {character.find('name').text}")
    print(f"\tEdad: {character.find('age').text}")
    print(f"\tGénero: {character.find('gender')['value']}")
    print(f"\tNivel: {character.find('level')['value']}")


    #Sacar el nombre a partir de la tabla intermedia
    file = open ('characters_items.facix', 'r')
    soup = BeautifulSoup(file, 'xml')
    file.close()

    charaItem = soup.find('character', {'id': num}).parent#da las etiquetas de la relación
    #print(charaItem)

    id_items = charaItem.find_all('items')#todos los items que tiene esa id relación
    #print(id_items)

    #la tabla de items
    file = open('characters.faix', 'r')
    soup = BeautifulSoup(file,'xml')
    file.close()

    #me aseguro que nos imprime todos los items que tiene este personaje
    for id_item in id_items:
        item = soup.find('item', {'id': id_item['id']})
        name_item = item.find('item').text
        print(f"\tItem: {name_item}")

