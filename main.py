from consultaufv import BCBAPIUFV

# Ejemplo de uso
cliente = BCBAPIUFV()

fecha_inicio = "2023-05-17"
fecha_fin = "2023-05-20"

resultado1 = cliente.consumir_endpoint(fecha_inicio, fecha_fin)

resultado2 = cliente.consumir_endpoint(fecha_inicio)

if resultado1 is not None:
    # Procesar el resultado de acuerdo a tus necesidades
    # ...
    print(resultado1)

if resultado2 is not None:
    # Procesar el resultado de acuerdo a tus necesidades
    # ...
    print(resultado2)