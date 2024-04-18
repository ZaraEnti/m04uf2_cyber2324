#!/usr/bin/python3

from xml.dom import minidom

facx = minidom.parse('characters.facx')

#elementos de la etiqueta de este oersonaje. siempre retorna un array
characters = facx.getElementsByTagName('character')

#diferencias para acceso segun las etiquetas
for character in characters:
    id = character.getAttribute('id')
    print(id)

    name = character.getElementByTagName('name')
    name_value = name [0].firstChild.valueNode
    print(name_value)



print(character[0].attributes['id'].value)
print(character[0].tagName)

#hacedido al primer hijo y despues el valor
print(name[0].firtsChild.valueNode)
