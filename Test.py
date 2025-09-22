#!/home/rsm7/Python-Study/dependentes/bin/python3
""" Hello World Multi Línguas

Dependendo da lingua configurada no ambiwnrw o programa exibe a mensagem correspondente.

como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Ou informe através do CLI arguments `--lang`

Ou o usuário terá que digitar.

Execução:

    python3 hello.py
    ou
    ./hello.py

"""

__version__ = "0.1.4"
__author__ = "Rafael Silva Moura"
__license__ = "Unlicense"

import os
import sys

arguments = { "lang": None, "count": 1}

for arg in sys.argv[1:]:
    # TODO: ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()
    arguments[key] = value
   
current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    # TODO: Usar repetição
   
    if current_language is None or current_language == "C.UTF-8":
        current_language = input("Choose a language: ")

current_language = current_language[:5]

text = {"pt_BR": "Olá! Mundo!",
          "fr_FR": "Bonjour! Le Monde!",
          "it_IT": "Ciao! Mondo!",
          "en_US": "Hello World" }

print((text[current_language] + "\n")*int(arguments["count"]))

    
    
    



