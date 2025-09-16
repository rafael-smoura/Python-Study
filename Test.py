#!/home/rsm7/Python-Study/dependentes/bin/env python3
""" Python Shell

Esse programa tem como finalidade testar os conhecimentos adquiridos em Python
"""

__version__ = "0.0.1"
__author__ = "Rafael Silva Moura"
__license__ = "no license"


import os

current_language = "en_US"
msg = "Hello World"

language = os.getenv("LANG", "en_US").split(".")[0] # Add a default language ( English )

if language == current_language:
    print(msg)

elif language == "pt_BR":
    print("Olá! Mundo!")

elif language == "fr_FR":
    print("Bonjour! Le Monde!")

elif language == "it_IT":
    print("Ciao! Mondo!")

else:
    print(msg)




