#!/usr/bin/python3
import gspread
import subprocess
import 

#dmesg = subprocess.getoutput("dmesg")
#dmesg_data= []
#print(dmesg)

#dmesg_lines = dmesg.splitlines()
#for dmesg_line in dmesg_lines:
 #   dmesg_temp = dmesg_line.split("[")[1]
  #  dmesg_time = dmesg_temp.split("]")[0]
   # dmesg_temp= dmesg_temp.split("]")[1]
    #dmesg_temp= dmesg_temp.split(":")
    #dmesg_module = dmesg_temp[0]
    #dmesg_info =""

#if len (dmesg_temp)>1:
 #   dmesg_info =demsg_temp[1]
  #  dmesg_data.append([dmegs_time], [dmesg_module] , [dmesg_info])
#print(string)




#KeyAPi
gc = gspread.service_account(filename='api-test-422608-73c8ef528f53.json')

#Open sheet
sh = gc.open ("peliculas")

#Print values
print(sh.sheet1.get('A1'))

#Creación de una hoja de calculo nueva
#sh = gc.create("datetime")

#Share para que yo pueda desde mi correo
#sh.share('zara.zhang@enti.cat', perm_type='user', role='writer')

#Creación de nueva hoja (Solo crea si no existe)
title="Creación de una nueva hoja"
print(title)
datetime = "2024-04-10"
worksheet = sh.add_worksheet(title = datetime, rows="100", cols="10")
print("-"*len(title))

#Lista de worsheets
title="Lista de todos los worksheets"
print(title)
print(sh.worksheets())
print("-"*len(title))


#para el número especifico de la lista o puede ser nombre

#worksheet = sh.get_worksheet(0) 
#worksheet_list = sh.worksheets()


#for sheet in worksheets:
#    print(worksheets.title)


#array_worksheet = worksheet_list.split(" ")
#for worksheet in array_worksheet_list:

 #   worksheet = worksheet_list.title()

#    print(worksheet)
 #   if(worksheet == datetime):
  #      print("duplicado")
#print(worksheet)
#print(worksheet_list)



