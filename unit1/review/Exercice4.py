"""
Created on 13 oct. 2019

@author: alvaro
"""
QUESTION = '¿Cual es el resultado de la formula {}? '
FORMULA_1 = '2 + 3 + 1 + 2'
FORMULA_2 = '2 + 3 * 1 + 2'
FORMULA_3 = '(2 + 3) * 1 + 2'
FORMULA_4 = '(2 + 3) * (1 + 2)'
FORMULA_5 = '-+-+6'
FORMULA_6 = '1 - 2 ** 4 - 2'
FORMULA_7 = '1 + 4 ** 2 ** 3'


def validate_input(formula, user_input):
    result = eval(formula)
    if float(result) == float(user_input):
        print('¡Has acertado!')
    else:
        print('Has introducido un valor incorrecto, el resultado es: ' + str(result))


validate_input(FORMULA_1, input(QUESTION.format(FORMULA_1)))
validate_input(FORMULA_2, input(QUESTION.format(FORMULA_2)))
validate_input(FORMULA_3, input(QUESTION.format(FORMULA_3)))
validate_input(FORMULA_4, input(QUESTION.format(FORMULA_4)))
validate_input(FORMULA_5, input(QUESTION.format(FORMULA_5)))
validate_input(FORMULA_6, input(QUESTION.format(FORMULA_6)))
validate_input(FORMULA_7, input(QUESTION.format(FORMULA_7)))

