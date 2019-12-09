"""

"""


def seleccionar(corte: str, *palabras: str):
    palabras_encontradas = []
    for letra in corte:
        palabras_encontradas += [palabra for palabra in palabras if letra in palabra]

    return set(palabras_encontradas)


seleccionadas = seleccionar('dan', 'uno', 'dos', 'tres', 'veinte', 'dos')
print(seleccionadas)
