#!/usr/bin/python3
from bs4 import BeautifulSoup
file = open ('characters.faix','r')
soup = BeautifulSoup(file, 'xml')
file.close()

title= "Bienbenid@s a Faryadventures"
print(title)
print("="*len(title),"\n")

#Busqueda de cantidad de items
item_list = soup.find_all('item')

#para etiquetas repetidas 
cantidad = len(item_list)/2


print("La tabla de items\n")

#bucle para encontrar solamente los items con ID
id=1
while id < cantidad:
    item= soup.find('item', {'id' : id})
   
    objeto = item.find('item').text
    food = item.find('type').text
    raro = item.find('rarity')['value']
    
    #incremento de id
    id+=1
    
    print(f"\t\tObjeto: {objeto}\tTipo: {food}\tRareza: {raro}") 
