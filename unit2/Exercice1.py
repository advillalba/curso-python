"""
Ejercicio1.En un programaque gestiona las características de un
producto necesitamos preguntar al usuario si:-El producto es caro o barato.-
El producto tiene descuento o no.-El precio base del producto.E
stos datos deben almacenarse en una única variable entera usando unformato
binario como el siguiente

"""

productIsExpensive = input('¿Es caro el producto? ')
productHasDiscount = input('¿Tiene descuento? ')
prize = int(input('Cual es el precio del producto: '))


def format_prize(prize):
    return format(prize, "b")


def format_product_information(arg):
    flag = 0b0
    if arg is 'S':
        flag = 0b1
    return flag


def encode_product(prize, product_has_discount, product_is_expensive):
    return str(format_prize(prize)) + str(format_product_information(product_has_discount)) + str(
        format_product_information(
            product_is_expensive))


def decode_product(product):
    decoded_is_expensive = product[len(product)-1:]
    decoded_discount = product[-2:-1]
    decoded_price = product[:-2]
    return decoded_price, decoded_discount, decoded_is_expensive


product = encode_product(prize, productHasDiscount, productIsExpensive)
print(product)

productAttributes = decode_product(product)
print(productAttributes)
print('Precio: ', productAttributes[0])
print('Descuento: ', productAttributes[1])
print('Es caro: ', productAttributes[2])
