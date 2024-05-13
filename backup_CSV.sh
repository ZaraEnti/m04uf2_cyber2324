#!/usr/bin/python3
import gspread

#API Key
gc = gspread.service_account(filename='api-key.json')
sh = gc.open ("dmesg")

array_page = []
worksheet_list = sh.worksheets()

count=1

#title hojas
for sheet in worksheet_list:
    array_page.append(sheet.title)

array_page = sorted(array_page, reverse=True)#ordenar las arrays de mayor a menor
page_ord = array_page[:5]#solo guarda 5 arrays

#menu
for menu in page_ord:
    print(f"{count}: {menu}")
    count+=1
    


num_page = int(input("Seleccione la página que quiere hacer la búsqueda (1-5):"))

#seleccion la casilla mediante el número
hoja_usr = page_ord[num_page -1]

#sacar TODOS los valores de la hoja
worksheet_values = sh.worksheet(hoja_usr).get_all_values()

#Selected worksheet
#print(worksheet_values)
print(type(worksheet_values))
#worksheet = sh.get_worksheet(num_page)


#Searh world
#search_world = input(f"Introduce la palabra que quieres búscar en la hoja: {worksheet.title}")

#for find_world in worksheet_select:
 #   if find_world == search_world:
  #      print("encontrado")




#  
accion = int(input("(1)Para consultar (2)Para hacer un backup: "))
if accion == 1:
    #Consulta
    print("consulta")
else:
	#Abrimos el archivo con 'a' si existe añade
	f = open("dmesg_backups.csv", 'a')

	#creación arrays para poner los valores de las columnas
	##1. array del contenido
	for value in worksheet_values:
		time_value = value[0]
		modul_value = value[1]
		descrip_value = value[2]
	
	    #escribimos en el archivo
		f.write("{time_value}"+";"+"{modul_value}"+";"+"{descrip_value}"+";")
	print("Archivo escrito")
	f.close()
