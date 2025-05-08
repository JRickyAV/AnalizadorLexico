import re
import json

def cargar_tokens(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def leer_archivo(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        return f.read()

def guardar_json(tokens, ruta_salida):
    with open(ruta_salida, 'w', encoding='utf-8') as f:
        json.dump(tokens, f, indent=2, ensure_ascii=False)   

def lexer(input_code, token_specs):
    tokens = []
    position = 0
    line_number = 1

    while position < len(input_code):
        match = None
        for token_type, pattern in token_specs:
            regex = re.compile(pattern)
            match = regex.match(input_code, position)
            if match:
                value = match.group(0)
                if token_type == 'WHITESPACE':
                    line_number += value.count('\n')
                elif token_type not in ('COMMENT', 'BLOCK_COMMENT'):
                    tokens.append({
                        'type': token_type,
                        'value': value,
                        'line': line_number
                    })
                position = match.end()
                break
        if not match:
            print(f"Caracter no identificado en la posicion {position} (línea {line_number}): '{input_code[position]}'")
            position += 1
    return tokens

def ejecutarLex(casoPrueba):
    token_specs = cargar_tokens('tokensList.json')
    codigo = leer_archivo('./inputs/codigo'+casoPrueba+'.minic')
    tokens = lexer(codigo, token_specs)
    guardar_json(tokens, './outputs/tokensResults'+casoPrueba+'.json')

    print("Tokens generados y guardados en 'tokens"+casoPrueba+".json'")


if __name__ == '__main__':
    ejecutarLex('1')
    ejecutarLex('2')
    ejecutarLex('3')
    ejecutarLex('4')
    ejecutarLex('5')
