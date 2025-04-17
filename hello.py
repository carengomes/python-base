#!/usr/bin/env python3
"""Hello World Multi Línguas.

Dependendo da língua configurada no ambiente, 
o programa exibe a mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

	export LANG=pt_BR

Execução:

	python3 hello.py
	ou
	./hello.py
"""
__version__ = "0.0.1"
__author__ = "Caren Gomes"
__license__ = "Unlicense"

import os  # operation system lê variáveis de ambiente

# na linha 1 temos um shebang que indica ao linux/mac qual interpretador do python usar
# o env é mais flexível, pois determina de acordo com as variáveis do ambiente
# o windows ignora o shebang, pois ele se baseia na extensão do arquivo
# na linha 2 o que fica dentro das aspas triplas significa a documentação do seu código
# por convenção, na linha 19 podemos chamar o underline underline de: dunder, ficando -dunder version-
# essa linha não faz diferença para o programa, mas para a comunidade e alguns interpretadores pode ser legal

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
	msg = "Olá, Mundo!"
elif current_language == "it_IT":
	msg = "Ciao, Mondo!"
elif current_language == "es_SP":
	msg = "Hola, Mundo!"
elif current_language == "fr_FR":
	msg = "Bounjour, Monde!"

print(msg)
