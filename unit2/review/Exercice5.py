HOUSE_RATING_OPTIONS = ('A', 'B', 'C')
DISPLAY_MENU = 1
RETRIEVE_INFORMATION = 2
PROGRAM_OPTIONS = {
    'REQUEST_INFORMATION': 1,
    'RETRIEVE_INFORMATION': 2,
    'AVERAGE_ROOM': 3,
    'END': 4
}

DISPLAY_INFORMATION_OPTIONS = {
    'SHOW_ADDRESS': 1,
    'NUMBER_OF_FLOORS': 2,
    'NUMBER_OF_ROOMS': 3,
    'HOUSE_SQUARE_METERS': 4,
    'HOUSE_RATING': 5,
    'IS_RESIDENTIAL': 6
}
fullAddress = None
floorsNumber = None
roomsNumber = None
houseSize = None  # square meter
houseRoomsSizeAverage = None
houseRating = None
houseIsResidential = None
exitProgram = False


def display_menu():
    print('\nMENÚ')
    print('-------------------------------')
    print('1-Solicitar datos de la vivienda.')
    print('2-Consultar un dato.')
    print('3-Calcular tamaño medio de una habitación.')
    print('4-Salir')
    return int(input('Introduce una opción (1-4): '))


def ask_house_is_residential():
    _is_residential = input('¿Es residencial? ')
    return 'S' in _is_residential.upper()


def ask_house_rating():
    _house_rating = input('Que calificacion tiene la vivienda, ¿A, B o C? ')
    _valid_rating = False
    while not _valid_rating:
        if _house_rating and _house_rating in HOUSE_RATING_OPTIONS:
            _valid_rating = True
        else:
            _house_rating = input('La calificacion no es valida, debe ser A, B o C: ')
    return _house_rating


def request_house_information():
    global fullAddress, floorsNumber, roomsNumber, houseSize, houseRating, houseIsResidential, houseRoomsSizeAverage
    fullAddress = input('Introduzca la direccion completa de la vivienda: ')
    floorsNumber = int(input('Introduzca el numero de plantas de la vivienda: '))
    roomsNumber = int(input('Cuantas habitaciones tiene la vivienda? '))
    houseSize = float(input('¿Cuantos metros cuadrados tiene? ').replace(',', '.'))
    houseRating = ask_house_rating()
    houseIsResidential = ask_house_is_residential()
    houseRoomsSizeAverage = houseSize / roomsNumber


def display_house_information_options():
    print('Los datos almacenados son: ')
    print('1. Direccion')
    print('2. Numero de plantas')
    print('3. Numero de habitaciones')
    print('4. Metros cuadrados de la vivienda')
    print('5. Calificacion')
    print('6. Indicador de si es de uso residencial.')
    _option = int(input('¿Que dato le gustaria consultar?'))
    if 1 <= _option <= 6:
        return _option
    else:
        print('El valor introducido no es valido')
        display_house_information_options()


def retrieve_house_information(display_option):
    global fullAddress, floorsNumber, roomsNumber, houseSize, houseRating, houseIsResidential
    if display_option == DISPLAY_INFORMATION_OPTIONS['SHOW_ADDRESS']:
        print('La direccion es: ', fullAddress)

    elif display_option == DISPLAY_INFORMATION_OPTIONS['NUMBER_OF_FLOORS']:
        print('La vivienda tiene ', floorsNumber, 'pisos')

    elif display_option == DISPLAY_INFORMATION_OPTIONS['NUMBER_OF_ROOMS']:
        print('La vivienda tiene ', roomsNumber, 'habitaciones')

    elif display_option == DISPLAY_INFORMATION_OPTIONS['HOUSE_SQUARE_METERS']:
        print('La vivienda tiene ', houseSize, 'metros cuadrados')

    elif display_option == DISPLAY_INFORMATION_OPTIONS['HOUSE_RATING']:
        print('La vivienda tiene calificacion de tipo: ', houseRating)

    elif display_option == DISPLAY_INFORMATION_OPTIONS['IS_RESIDENTIAL']:
        if houseIsResidential:
            print('La vivienda es residencial')
        else:
            print('La vivienda no es residencial')


def display_rooms_average_size():
    global houseRoomsSizeAverage
    print('Las habitaciones tienen un tamanio medio de: ', houseRoomsSizeAverage, ' metros cuadrados.')


def end_program():
    global exitProgram
    exitProgram = True


while not exitProgram:
    action = display_menu()

    if action == PROGRAM_OPTIONS['REQUEST_INFORMATION']:
        request_house_information()

    elif action == PROGRAM_OPTIONS['RETRIEVE_INFORMATION']:
        displayOption = display_house_information_options()
        retrieve_house_information(displayOption)

    elif action == PROGRAM_OPTIONS['AVERAGE_ROOM']:
        display_rooms_average_size()

    elif action == PROGRAM_OPTIONS['END']:
        end_program()
        
    else:
        print('La opcion elegida no es valida.')
