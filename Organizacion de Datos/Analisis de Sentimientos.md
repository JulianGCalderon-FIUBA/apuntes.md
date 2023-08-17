---
title: Análisis de Sentimientos
---

Es una tarea de clasificación de textos. Se utiliza para diversas tareas complejas.

- Calcular confianza de un consumidor
- Predecir el mercado de valores

## Tipología de Scherer

- **Emoción**: Respuesta relativamente corta del organismo a un estímulo externo.
- **Estado de ánimo**: Sentimiento de baja intensidad y larga duración.
- **Postura Interpersonal**: Posición afectiva respecto a otra persona
- **Actitudes**: Predisposición de una persona respecto a otras personas.
- **Rasgos de Personalidad**: Tendencias del comportamiento típico de una persona

En un análisis de sentimientos, trataremos de predecir la actitud.

- El portador
- El destinatario
- La Actitud
- El documento que contiene la actitud

## Algoritmo de Pang y Lee

1. Tokenización del texto
2. Extraemos características del texto, palabras claves.
3. Clasificación utilizando distintos algoritmos de clasificación

Utilizar todas las palabras da mejores resultados, en términos generales (por lo menos en IBMD).

**Problemas comunes:**

- Lidiar con *tags* XML o HTML
- Reconocer marcas de Twitter, usuarios, hashtags
- Tener en cuenta el uso de mayúsculas.
- Despreciar fechas y números de teléfono
- Emoticones, son útiles para detectar un sentimiento.
- Lidiar con la negación. Una forma es reemplazar las palabras que le siguen a un no, por ejemplo: *NO_palabra*

Otros problemas más complejos son:

- Sutilezas: Los textos tienen un sentido negativo oculto

	*"Si usted está leyendo esto porque es su fragancia favorita, por favor úsela exclusivamente en su casa y cierre bien las ventanas"*

- Expectativas Frustradas: El significado del texto cambia totalmente por algún comentario en particular

	*"La película debería ser excelente, ya que cuenta con grandes actores y una banda sonora fantástica, sin embargo, es terriblemente aburrida"*

## Lexicón de Sentimientos

Utilizar un diccionario de sentimientos, donde las palabras se categorizan según su sentimiento. Podemos usar este diccionario para clasificar un texto.

### Algoritmo de Hatzivassiloglou y MecKeown

- Adjetivos unidos por 'y' tienen la misma polaridad
- Adjetivos unidos por 'pero' tienen distinta polaridad

El algoritmo tiene 4 pasos:

1. Construyeron a mano un lexicón de 1336 adjetivos
2. Buscaron en Google cada uno de los adjetivos con la fórmula *was … and*. Recolectaron la palabra que seguía a continuación
3. Repitieron esto con *was … but*.
4. De esta forma, obtuvieron muchas más palabras, pero con algunos errores

### Algoritmo de Turney

1. Extraer frases de opiniones y armar un lexicón
2. Aprender la polaridad de cada frase
3. Puntuar casa críticas según el promedio de las polaridades

Para extraer frases, se crearon reglas.

Para encontrar la polaridad de una frase, se verificó cuan cerca aparecían las palabras de las palabras con polaridad conocida.

**Pointwise mutual information** es una fórmula matemática que indica la probabilidad de que dos eventos estén relacionados, o que sean independientes entre sí.

$$
P(palabra) = \frac{\text{$\#$ palabra}}{\text{$\#$ totales}}
$$

$$
P(palabra1, palabra2) = \frac{\text{$\#$ palabra 1 cerca de palabra 2}}{\text{$\#$totales$^2$}}
$$

$$
PMI(palabra1, palabra2) =Log_2 \frac{P(palabra)}{P(palabra1,palabra2)}
$$

Entonces, la polaridad de la frase, se calculará como

$$
Polaridad(frase) = PMI(frase, "excelente") - PMI(farse, "pobre")
$$

## Aspectos

Debemos detectar más de un sentimiento en una sola frase.

### Método de Mingqing Hu y Bing Liu

**Frecuencia:** Buscaron todas las frases frecuentes, llamaron a estas frases "aspectos", u "objetos de sentimiento".

**Reglas:** Filtraron todas esas frases frecuentes como: Ocurre después de una palabra que indica sentimientos.

Algunas consideraciones del método:

- El aspecto puede no ser mencionado
- Los aspectos a veces son fácilmente identificables
- Es posible utilizar clasificación supervisada y luego entrenar un clasificador
- Si la cantidad de críticas no está balanceada, se puede degradar el rendimiento
