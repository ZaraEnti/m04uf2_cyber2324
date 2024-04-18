#!/usr/bin/python3

from bs4 import BeautifulSoup
with open("characters.faix") as file:
    soup = BeautifulSoup(file, 'xml')

