#!/usr/bin/python3
from xml.dom import minidom

import xml.etree.ElementTree as  Et
#vinculación del archiva  la que quiere acceder los datos
faix = minidom.parse('characters.faix')

items = faix.getElementsTag

print(f"\t{items}")



#for item in items:
 #   id = item.getAttribute('id')
 #

  #  it = item.getElementsByTagName('item')
   # it_value = it[0].firstChild.valueNode
    
    #tipo = tipo.getElementisByTagName('type')
   # tipo_value = tipo[0].firstChild.valueNode

    #rarity = rarity.getElemenstByTagName('rarity')
    #rarity_value = rarity[0].getAttribute('value')
    
   # print(f"\t{it_value}\t{tipo_value}\t{rarity_value}")

