#!/usr/bin/python3
import gspread

#API Key
gc = gspread.service_account(filename='api-test-422608-73c8ef528f53.json')
sh = gc.open ("peliculas")

array_page = []

worksheet_list = sh.worksheets()

count=1
for sheet in worksheet_list:
    array_page.append(sheet.title)

array_page = sorted(array_page, reverse=True)
page_ord = array_page[:5]

for menu in page_ord:
    print(f"{count}: {menu}")
    count+=1
    


num_page = int(input("Seleccione la página que quiere hacer la búsqueda (1-5):"))

hoja_usr = page_ord[num_page -1]

worksheet_select = sh.worksheet(hoja_usr).get_all_values()

#Selected worksheet
print(worksheet_select)
worksheet = sh.get_worksheet(num_page)


#Searh world
search_world = input(f"Introduce la palabra que quieres búscar en la hoja: {worksheet.title}")

for find_world in worksheet_select
	


