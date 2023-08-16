---
title: Álgebra de Boole
---

El Álgebra se define a través de las operaciones que se pueden realizar sobre un conjunto de elementos.

Cualquier relación numérica o lógica puede ser expresada en un circuito eléctrico utilizando el Álgebra de Boole

## Postulados de Huntington

1. **Equivalencia:** Se define un conjunto $K$ objetos sujetos a una ley de equivalencia $(=)$ de modo que si $a = b$, puedo sustituir $b$ con $a$ en cualquier expresión sin afectar su validez.
2. **Regla de Combinación:**
	1. Si $a,b$ están en $K$. $a + b$ está en $K$.
	2. Si $a.b$ están en $K$. $a.b$ está en $K$.
3. **Existencia de** $0,1$
	1. tal que para todo $a$ en $K$, $a + 0 = a$
	2. tal que para todo a en $K$, $a.1 = a$
4. **Conmutatividad**
	1. $a+b = b+a$
	2. $a. b = b. a$
5. **Distributividad**
	1. $a. (b + c) = a. b + a. c$
	2. $a+(b.c) = (a+b).(a+c)$
6. **Existencia de un $\overline a$**
	1. tal que $a. \overline a = 0$
	2. tal que $a + \overline a = 1$
7. Existen en $K$ al menos dos elementos que no son equivalentes entre sí

## Principio de Dualidad

Si reemplazo en una expresión todo $0$ por un $1$, y todo $+$ por un $.$, entonces la expresión sigue siendo equivalente.

## Teoremas

- **Idempotencia:** $a+a = a \quad\implies\quad a.a=a$
- **Elemento Absorbente:** $a+1 = 1 \quad\implies\quad a.0 = 0$
- **Absorción:** $a + (a.b) = a \quad\implies\quad a.(a+b) = a$
- **Asociatividad:** $a + (b + c) = (a+b) + c \quad\implies\quad a.(b.c) = (a.b).c$
- **Complemento Único:** $\overline a$ es único
- **Involución:** $\overline{\overline a} = a$
- **En cualquier álgebra booleana**: $\overline 0 = 1\quad\implies\quad \overline 1 = 0$
- **Leyes de Morgan:** $\overline{(a+b)} = \overline a. \overline b \quad\implies\quad \overline{(a.b)} = \overline a + \overline b$
