def imprimir_factura(titulo: str, conceptos: [()], iva: float) -> None:
    total = 0
    row = f'{"":{"#"}<{60}}'
    print(row)
    print(f'{"# " + titulo:{" "}<{59}}#')
    print(row)
    print(f'{"#     Conceptos":{" "}<{30}}{"Importe":{" "}>{30}}')
    print(row)
    for concepto in conceptos:
        total += concepto[1]
        print(f'{"#  " + concepto[0]:{" "}<{30}}{str(concepto[1]):{" "}>{30}}')
    print(row)
    print(f'{"#  " + "{:.0f}".format(iva*100)+"%":{" "}<{30}}{"Total  "+str((1+iva)*total):{" "}>{30}}')


gastos = [("Informe de gastos", 120), ("Gasto de impresora", 320), ("Comisión", 30)]

imprimir_factura('Facturas de incidencia', gastos, 0.15)
