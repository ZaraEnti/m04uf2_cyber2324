#!/usr/bin/python3
from bs4 import BeautifulSoup
file = open ('characters.faix','r')
soup = BeautifulSoup(file, 'xml')
file.close()

title= "Bienbenid@s a Faryadventures"
print(title)
print("="*len(title),"\n")

#Busqueda de cantidad de items

#Los items que nos interesan solo los que tienen items por lo tanto hay algo que los diferencia sin nevcesidad de dividir el número
items = soup.find_all("item", {'id': TRUE})

for item in items:
    id = item['id']
   
    objeto = item.find('item').text
    food = item.find('type').text
    raro = item.find('rarity')['value']
    
    print(f"\t[id]\t\tObjeto: {objeto}\tTipo: {food}\tRareza: {raro}") 
