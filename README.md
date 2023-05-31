# Consultas de la UFV - Bolivia

[![PyPI version][pypi-version]][pypi]

El sitio oficial de Banco Central de Bolivia a traves de su pagina web pone a disposicion un sitio web para consultas de la cotizacion de la UFV.

Sitio Web: https://www.bcb.gob.bo/librerias/indicadores/ufv/ultimo.php

Este paquete le permite realizar la misma verificacion haciendo uso de los mismos servicios con el fin de poder integrar dicha verificacion en sus desarrollo; por ejemplo rellenando de forma masiva las cotizaciones pasadas de UFV de un sistema.

## Instalacion
```shell

pip install consulta-ufv-bolivia

```

## Ejemplo

```python
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

```

## Salida de Ejemplo Varias Fechas

```shell
[
{'fecha': '17/05/2023', 'val_ufv': '2.434800000000000000'}, 
{'fecha': '18/05/2023', 'val_ufv': '2.434970000000000000'}, 
{'fecha': '19/05/2023', 'val_ufv': '2.435140000000000000'}, 
{'fecha': '20/05/2023', 'val_ufv': '2.435310000000000000'}
]
```

## Salida de Ejemplo Una Fecha
```shell
[
{'fecha': '17/05/2023', 'val_ufv': '2.434800000000000000'}
]
```

## Disclaimer

El paquete funcionara siempre y cuando el Banco Central de Bolivia siga permitiendo que el servicio sea de acceso publico y sin autenticacion.


[pypi-version]: https://img.shields.io/pypi/v/consulta-ufv-bolivia
[pypi]: https://pypi.org/project/consulta-ufv-bolivia