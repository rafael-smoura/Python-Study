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

language = "pt_BR"
print(language)

if language in frases:
        print(frases[language])
else:
        print(frases["en_US"])
    
    
    



