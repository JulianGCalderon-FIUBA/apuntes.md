En física existen dos conceptos fundamentales. Las partículas, que responden a las leyes de Newton, y las ondas

## Clasificación

**Segun el medio:**

- **Ondas Mecánicas**: Vibran las moléculas, necesitan un medio. Un ejemplo de esto es la cuerda de una guitarra, requiere de la misma cuerda para vibrar.
- **Ondas Electromagnéticas:** Vibra el campo, no necesitan un medio. Un ejemplo de esto es la luz, esta atraviesa miles de kilómetros en el vacío y no necesita un medio para propagarse. Solo pueden ser transversales

**Segun la dirección:**

- **Onda Longitudinal:** La velocidad de propagación tiene la misma dirección que la perturbación. Necesitan medio con resistencia a la compresión. Tienen compresiones y dilataciones
- **Onda Transversal:** La velocidad de propagación es perpendicular a la de la perturbación. Necesitan medios con resistencia a la flexión. Tienen crestas y valles.

## Ecuación de Onda

Las ondas verifican la **ecuación diferencial** de onda plana.

$$
\frac{\partial^2y}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2y}{\partial t^2}
$$

Toda función cuyo argumento sea $x\pm vt$, resuelve la ecuación diferencial. $\displaystyle \Big(y = f(x\pm vt)\Big)$

Una **solución** de esta ecuación puede ser: *(Onda Armónica)*

$$
\xi(x,t) = A\cdot\sin(kx \pm wt + \varphi)
$$

### Parámetros

$\xi:$ Perturbación

$x:$ Posición

$t:$ Tiempo

$A:$ Amplitud

$k$ Numero de onda

$w:$ Pulsación de la onda (Frecuencia Angular)

$\varphi:$ Angulo inicial

Si $w$ tiene sentido **negativo**, entonces la onda se desplaza en sentido $\hat x$ **positivo**.

Si $w$ tiene sentido **positivo**, entonces la onda se desplaza en sentido $\hat x$ **negativo**.

**Velocidad de Propagación** $\displaystyle\to v= \frac\lambda T=\frac wk$

**Longitud de Onda** $\displaystyle\to\lambda = \frac vf$

**Número de Onda** $\displaystyle\to k =\frac{2\pi}\lambda$

**Frecuencia** $\displaystyle\to f= \frac 1T=\frac w{2\pi}$

---

### Derivadas Temporales

### Derivadas Espaciales

$$
\frac{\partial\xi}{\partial t} = \pm wA\cos(\dots)
$$

$$
\frac{\partial^2\xi}{\partial t^2} = -w^2A\sin(\dots)
$$

$$
\frac{\partial\xi}{\partial x} = kA\cos(\dots)
$$

$$
\frac{\partial^2\xi}{\partial x^2} = -k^2A\sin(\dots)
$$

## Velocidad de las Ondas

La velocidad de **propagación** depende estrictamente de las propiedades del medio

- **Cuerdas:** la velocidad depende de la tension $F$ de la cuerda y la densidad lineal $\mu$

	$$
    v = \sqrt\frac F\mu
    $$

- **Solidos (Transversales):** la velocidad depende del modulo de *rigidez* $G$ **y de la densidad $\rho$

	$$
    v = \sqrt\frac G\rho
    $$

- **Solidos (Longitudinales):** la velocidad depende del modulo de *Young* $Y$ **y de la densidad $\rho$.

	Se define modulo de Young, como el cociente entre el valor de la fuerza que recibe por unidad de area, y la deformación relativa que se le provoca al cuerpo.

$$
\text{Young}:Y = \frac{\frac FA}{\frac{\Delta l}L}  
$$

$$
v = \sqrt\frac Y\rho
$$

- **Gases:** la velocidad depende del modulo de compresibilidad $B$ y de la densidad $\rho$.

	Tambien se puede expresar en función del coeficiente adiabático $\gamma$, La constante de los gases ideales $R$, la temperatura $T$ medida en *Kelvin*, y la masa molecular $M$.

$$
\text{Compresibilidad} : B = -\frac{\Delta P}{\Delta V/ V}\bigg\rvert_{\text{Adiabatico}}
$$

$$
v = \sqrt{\frac{B}{\rho}}
$$

$$
v = \sqrt{\frac{\gamma RT}{M}}
$$
