#!/usr/bin/python3

#Comunicación con http y colores para la salida
import requests
from colorama import init, Fore


#para restaurar los colores de la salida
init(autoreset=True)

#título
print(Fore.CYAN + "¡Esto es un buscador de películas!")

name = input(Fore.GREEN + "\nIntroduce una película: " + Fore.CYAN)

#iniciando la sentencia con un interrogante y le concatenamos la variable
url = "https://search.imdbot.workers.dev/?q="+name

#retornar una respuesta válida y si es válida un archivo json array
movie = requests.get(url)
data = movie.json()

#comprovación si es válida o no
if not data['description']:
    print(Fore.RED + "Error 1: No se han encontrado resultados.")
else:
    title = data['description'][0]['#TITLE']
    year = data['description'][0]['#YEAR']
    actors = data['description'][0]['#ACTORS']

    print(Fore.GREEN + "Título:" + Fore.CYAN + f"{title}")
    print(Fore.GREEN + "Año:" + Fore.CYAN + f"{year}")
    print(Fore.GREEN + "Actores:" +Fore.CYAN + f"{actors}")

