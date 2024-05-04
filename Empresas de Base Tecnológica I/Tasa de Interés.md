Es el costo de [[Dinero]] en un período de tiempo determinado. También se utiliza como medida de riesgo de una inversión:

- A mayor riesgo, mayor tasa de interés.
- A menor riesgo, menor tasa de interés.

## Interés Simple

El interés simple no se compone con el capital para generar nuevos intereses, sino que siempre el capital original es el que trabaja la tasa.

$$
VF = VP \cdot (1 + n\cdot i)
$$

## Interés Compuesto

En el interés compuesto se ganan intereses sobre la suma inicial, luego sobre la suma inicial más los intereses ganados en el primer periodo que el dinero trabajó, y así sucesivamente. Siempre se suma el interés al capital para ganar más intereses.

$$
VF = VP \dot (1 + i)^n
$$

El interés al cabo de $n$ periodos se calcula como $I = VF - VP$.

## Tasa Nominal Anual (TNA)

La tasa de interés nominal anual (TNA) es la tasa de interés que se declara en las operaciones financieras, en la documentación legal, con fines comerciales, etc.

El problema de trabajar con la TNA es que la información que brinda es incompleta, ya que no menciona la cantidad de veces que los intereses se capitalizan en el año.

Algunas capitalizaciones son:

- Mensual: doce veces al año.
- Trimestral: cuatro veces al año
- Anual: una vez al año

Para adaptar la fórmula, el valor futuro es:

$$
VF = CP \cdot (1 + \frac{TNA}m)^m
$$

Siendo $m$ la cantidad de veces que se capitaliza al año.

## Tasa Efectiva Anual (TEA)

La tasa de interés efectiva anual (TEA) es la tasa de interés que incluye la cantidad de veces que se capitalizan los intereses en el año.

Son las tasas que realmente pagamos y cobramos, y son las que nos interesa conocer.

Puede haber dos tasas son diferente TNA, pero misma TEA (por diferente capitalización). Diremos que son equivalentes.

Para encontrar tasas equivalentes para otros periodos, utilizaremos la fórmula

$$
(1 + TEA) = (1 + TEX)^{Y}
$$

Siendo TEX la tasa equivalente en un periodo determinado e $Y$ la cantidad de veces que ese periodo entra en un año.

La tasa efectiva es nominal respecto a la inflación, por lo que debemos tenerla en cuenta para hallar la tasa real.

## Tasa Real

Para tener en cuenta la tasa de la inflación en una tasa de interés. utilizaremos la siguiente formula.

$$
1 + \text{Tasa Real} = \frac{1 + \text{Tasa Efectiva}}{1 + \text{Tasa de Inflacion}}
$$
