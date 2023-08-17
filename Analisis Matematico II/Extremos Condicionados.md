## Extremos en conjuntos compactos

Al limitar una función a un conjunto compacto, se generan nuevos extremos que antes no existían.

**Teorema de Weierstras:** Si $f$ es continua en el conjunto $D\subset\mathbb{R}^n$ compacto, va a tener en $D$ un máximo o mínimo absoluto

### Encontrar extremos

1. Buscar los puntos críticos en todo el dominio
2. Descartar los puntos externos a $D$
3. Clasificar los puntos críticos
4. Analizar extremos en la frontera de $D$
5. Comparar los extremos obtenidos

### Métodos

- **Evaluar la función en los puntos de la frontera $g$:**
	Calculamos $h(t) = f\big|_g$, y calculamos los extremos de $h$ buscando los ceros de la derivada primera y analizamos el signo de la derivada segunda. Al estar en un conjunto cerrado, también debemos analizar los puntos en los extremos del mismo.

- **Parametrizar la curva y componer $h = f \circ g$:**
	Este método se complica más, pero es útil conocer este procedimiento porque a veces no es tan fácil aplicar el primero

### Multiplicadores de Lagrange

Los puntos donde las curvas de nivel son tangentes a la curva de la frontera, son considerados puntos críticos

$$
\underbrace{\nabla f}_{\perp C_k} = \lambda\underbrace{\nabla G}_{\perp g}
$$
