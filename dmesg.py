#!/usr/bin/python3

import subprocess
import gspread
import datetime

fecha = datetime.datetime.now()

año = fecha.year
mes = fecha.strftime("%m")
dia = fecha.strftime("%d")


nombre_fecha = f"{año}-{mes}-{dia}"

gc = gspread.service_account()
sh_dmesg = gc.open("dmesg")

worksheet_list = sh_dmesg.worksheets()

print(worksheet_list)

existe = False

for word in worksheet_list:
	print(word.title)
	if word.title == nombre_fecha:
		print("existe")
		existe = True

if existe == True:
	sh_dmesg.worksheet(str(nombre_fecha)).clear()
else:
	sh_dmesg.add_worksheet(title=str(nombre_fecha), rows=100, cols=20)

dmesg = subprocess.getoutput("dmesg") 

dmesg_data = []

dmesg_lines = dmesg.splitlines()

for dmesg_line in dmesg_lines:

	dmesg_temp = dmesg_line.split("[")[1]

	dmesg_time = dmesg_temp.split("]")[0] 

	dmesg_temp = dmesg_temp.split("]")[1]

	dmesg_temp = dmesg_temp.split(":")

	dmesg_module = dmesg_temp[0]

	dmesg_info = ""

	if len (dmesg_temp) > 1:
		dmesg_info = dmesg_temp [1]
	
	dmesg_data.append([dmesg_time, dmesg_module, dmesg_info])


sh_dmesg.worksheet(str(nombre_fecha)).append_rows(dmesg_data)
print (f" Array insertada \n")

