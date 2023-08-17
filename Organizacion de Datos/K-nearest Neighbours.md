---
title: K-nearest Neighbours
---

Es un método de clasificación que permite identificar la clase de una observación a partir de la distancia a sus vecinos.

## Hiperparámetros

- Definimos el valor $k$ como la cantidad de vecinos de cada observación.
- Definimos el tipo de métrica que se utilizará para medir la distancia
- Definimos el peso de cada observación, para medir su importancia en el algoritmo.

## Desventajas

El método tiene dos problemas principales:

- Si el conjunta está desbalanceado, el algoritmo tenderá a clasificar para esa clase
- Si hay puntos mal clasificados (outliers), estos afectarán el algoritmo.
