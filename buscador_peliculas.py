#!/usr/bin/python3

#Comunicación con http y colores para la salida
import requests
from colorama import init, Fore


#para restaurar los colores de la salida
init(autoreset=True)

#título
title="¡Esto es un buscador de películas!"

print(Fore.CYAN + "\n"+ title)

name = input(Fore.GREEN + "\nIntroduce una película: ")

#iniciando la sentencia con un interrogante y le concatenamos la variable
url = "https://search.imdbot.workers.dev/?q=" + name

#retornar una respuesta válida y si es válida un archivo json array
movie = requests.get(url)
data = movie.json()

#comprovación si es válida o no
if not data['description']:
    print(Fore.RED + "Error 1: No se han encontrado resultados.")
else:
    #indicamos solo la información de la primera búsqueda
    title = data['description'][0]['#TITLE']
    year = data['description'][0]['#YEAR']
    actors = data['description'][0]['#ACTORS']

    print(Fore.YELLOW + "Título:" + Fore.CYAN + f"{title}")
    print(Fore.YELLOW + "Año:" + Fore.CYAN + f"{year}")
    print(Fore.YELLOW + "Actores:" +Fore.CYAN + f"{actors}\n")

import gspread

gc = gspread.service_account(filename='api_key.json')

#nombre del archivo
sh = gc.open("peliculas")

tabla_pelis = sh.sheet1 

tabla_pelis.sheet1.append_row([title, year, actors])

print("append existosa")
