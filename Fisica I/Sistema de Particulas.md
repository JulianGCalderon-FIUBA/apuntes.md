---
title: Sistema de Partículas
---

Definimos dos tipos de fuerzas:

- **Fuerzas Internas:** Par de interacción actúa dentro del sistema
- **Fuerzas Externas:** Par de interacción queda por fuera del sistema

## Centro de Masa

$$
\vec r_{CM} = \frac{\sum m_i\cdot\vec r_i}M
$$

$$
\vec v_{CM} = \frac{\sum m_i\cdot\vec v_i}M = \frac{d\vec r_{CM}}{dt}
$$

$$
\vec a_{CM} = \frac{\sum m_i\cdot\vec a_i}M = \frac{d\vec v_{CM}}{dt}
$$

> [!note]
> Si en lugar de partículas son cuerpos, el cálculo se hace a partir de los centros de masa de cada cuerpo

## Cantidad de Movimiento

$$
\vec p = \sum \vec p_i= M\vec v_{CM}
$$

### Teorema de conservación del momento lineal

$$
\sum \vec F = \frac{d\vec p}{dt} \implies \vec p = \text{cte} \iff \sum \vec F = 0
$$

> [!note]
> Si se conserva la cantidad de movimiento en un sistema, la velocidad del mismo es constante.

> [!note]
> Se tienen en cuenta solo las fuerzas externas al sistema, ya que las fuerzas internas se cancelan entre sí

## Momento Cinético y Torque

$$
\vec L_o = \sum \vec r_i \times \vec p_i
$$

$$
\vec M_o=\vec  T_o = \sum \vec r_i \times \vec F_i = \frac{d\vec L_o}{dt}
$$

> [!note]
> Se tienen en cuenta solo fuerzas externas al sistema, ya que las fuerzas internas se cancelan entre sí

### Teorema de conservación del momento angular

$$
\sum \vec\tau_o = \frac{d\vec L_o}{dt} \implies \vec L_o = \text{cte} \iff \sum \vec\tau_o = 0
$$

## Energía

$$
\boxed{\Delta E_c =\frac 1 2\sum m_iv_i^2}
$$

> [!note]
> En el cálculo de energía, se tienen en cuenta los trabajos internos y externos

## Las transformaciones de Galileo

$$
L^{\text{Sist}}_o = \underbrace{L^{\text{Sist}}_{cm}}_{L\text{ Spin }} + \underbrace{L^{\text{cm}}_{o}}_{L\text{ Orbital}}
$$

$$
E_c^{\text{Sist}} = E_c^{\text{Sist/cm}} + E_c^{\text{cm}}
$$
