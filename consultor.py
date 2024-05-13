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
#worksheet = sh.get_worksheet(num_page)


#Searh world
#search_world = input(f"Introduce la palabra que quieres búscar en la hoja: {worksheet.title}")

#for find_world in worksheet_select:
 #   if find_world == search_world:
  #      print("encontrado")

accion = 2
if accion == 1:
    #Consulta
    print("consulta")
else:
    #creación arrays para poner los valores de las columnas
    time = []
    modul= []
    descrip=[]
    
    #sacamos el array de tiempo

    values_time = sh.worksheet(hoja_usr).col_values(1)
    
    values_modul = sh.worksheet(hoja_usr).col_values(2)

    values_descrip = sh.worksheet(hoja_usr).col_values(3)
    count = 0
    for value in values_time:
       #para tiempo
        time.append(value+";")
    

        count += 1
    for value in values_modul:
        #para modulo
        modul.append(value+";")

    for value in values_descrip:
        #para modulo
        descrip.append(value+";")


#para saber el size de los arryas

size = len(time)
formato_CVS=""
for num in range(size):
    #falta crear el archivo
    print(f"{time[num]}+{modul[num]}+{descrip[num]}") 
    formato_CVS="time[num]+modul[num]+descrip[num]"
