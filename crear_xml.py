#!/usr/bin/python3

from bs4 import BeautifulSoup


#tipo e documento que queremos crear
soup = BeautifulSoup(features='xml')

etiqueta =soup.new_tag('cosa', id =3)
otra_cosa= soup.new_tag('otra_cosa', value="parafrita")

otra_cosa.string= "esto es una string para la otra cosa"
etiqueta.append(otra_cosa)

print(etiqueta)
print("-----------------")
soup.append(etiqueta)
print(soup)

print(soup.prettify())
file = open('cosa', 'w')
file.write(str(soup.prettify()))
file.close()
