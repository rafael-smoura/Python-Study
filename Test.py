#!/home/rsm7/Python-Study/dependentes/bin/env python3
""" Python Shell

Esse programa tem como finalidade testar os conhecimentos adquiridos em Python
"""

__version__ = "0.0.1"
__author__ = "Rafael Silva Moura"
__license__ = "no license"


import os

frases = {"pt_BR": "Olá! Mundo!",
          "fr_FR": "Bonjour! Le Monde!",
          "it_IT": "Ciao! Mondo!",
          "en_US": "Hello World" }

language = os.getenv("LANG", "en_US").split(".")[0] # Add a default language ( English )

for langue, text in frases.items():
    if language not in frases:
        print(frases["en_US"])
        break

    if langue == language:
            print(text)
    
    
    




