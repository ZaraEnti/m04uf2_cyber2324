#!/usr/bin/python3

from xml.dom import minidom

facx = minidom.parse('characters.facx')

characters = facx.getElementsByTagName('character')


print(character[0].attributes['id'].value)
print(character[0].tagName)
)
