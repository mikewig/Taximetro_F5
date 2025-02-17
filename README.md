# Taximetro_F5

## Proyecto Python: 🚕 Taximetro Digital

### Descripción

Creación de una app con python (Taximetro Digital)

## Nivel de Implementación logrado

## 🟢 Nivel escencial

- Al iniciar, el programa debe dar la bienvenida y explicar su funcionamiento.
- Implementar las siguientes funcionalidades básicas:
  - Iniciar un trayecto.
  - Calcular tarifa mientras el taxi está parado (2 céntimos por segundo).
  - Calcular tarifa mientras el taxi está en movimiento (5 céntimos por segundo).
  - Finalizar un trayecto y mostrar el total en euros.
  - Permitir iniciar un nuevo trayecto sin cerrar el programa.

## Mi proyecto

### Descripción
Este taximetro tiene tres funcionalidades distintas:
  1. Iniciar el taxímetro: empieza a contar los segundos mientras el taxi esta en movimiento (tecla "w" presionada) o
  detenido (tecla "s" presionada).
  2. Detener el taximetro: detiene el taximetro, imprime el tiempo total y la tarifa total acumulada.
  3. Salir: permite salir del programa.


> [!TIP]
> ### Requisitos
> Python 3.x
> Importar las siguientes librerias:
>  - time (ya viene incluida en Python)
>  - os (ya viene incluida)
>  - keyboard (con pip install keyboard)

### Funcionalidades

#### Menú Principal
Cuando inicies el programa, verás un menú con tres opciones:

 1. Iniciar el taxímetro: Comienza a calcular el tiempo y el precio del servicio.
 2. Detener el taxímetro: Detiene el taxímetro y muestra el precio final y el tiempo total.
 3. Salir: Termina la aplicación.

#### Interacciones
El programa responde a las siguientes teclas:

 - "w": El taxi comienza a moverse y el precio por movimiento aumenta.
 - "s": El taxi se detiene y el precio por segundo detenido aumenta.
 - "p": Detiene el taxímetro por completo y muestra la tarifa final, regresando al menú de opciones.

#### Cálculo del precio
 - Tarifa de inicio: 10.20€
 - Precio por movimiento: 0.05€ cada vez que el taxi avanza.
 - Precio por segundo detenido: 0.02€ por cada segundo que el taxi esté detenido.

[Trello](https://trello.com/invite/b/67a60e150cb325f7a7587d41/ATTIeeb476ee40c9266f62c1a905536405c2D4FDB6B9/taximetro)
