# Analizador Lexico

Un analizador léxico es la primera etapa de un compilador, lee el código fuente y lo convierte en una secuencia de tokens.

Un token es una unidad signifactiva de lenguaje, este es un ejemplo de Mini C y maneja algunos ejemplos de tokens: <br>
`int` -> tipo `KEYWORD` <br>
`x` -> tipo `IDENTIFIER` <br>
`=` -> tipo `ASSIGN` <br>
`10` -> tipo `NUMBER` <br>

## Para correr este código

Clonar el repositorio <br>
https://github.com/JRickyAV/AnalizadorLexico


Este código esta ejecutado en python 3.11.2 y ejecutando `python3 main.py` dentro de la carpeta de repositorio ejecutará correctamente el programa.

Los casos de prueba estan almacenados en la carpeta inputs los cuales contienen ejemplos de códigos similares a C, los resultados estarán almacenados en la carpeta outputs en formato de JSON.

