Existen dos definiciones importantes:

- **Forwarding:** Es la acción de mover los paquetes de una interfaz de entrada a una interfaz de salida
- **Routing:** Es la acción de decidir a qué interfaz enviar un paquete

## Tablas de Ruteo

En la versión más simple, una tabla de ruteo tiene dos columnas

Cuando se recibe un paquete, se debe comparar con las entradas de la tabla para definir a que puerto de salida debe ir. Por ejemplo, $\text{192.168.0.1/24}$ indica que los primeros $\text{24}$ bits de la dirección de destino del paquete entrante debe coincidir con $\text{192.168.0.1}$.

Generalmente, $/n$ indica que la máscara es un número binario de $\text{32}$ bits, donde los primeros $n$ bits tienen valor $\text 1$ mientras que los restantes tienen valor $\text 0$.

Sea $\text{Prefix}$ el prefijo de una entrada de la tabla y $\text{Mask}$ la máscara asociada a ese prefijo, entonces el paquete con dirección de destino $\text{Destination}$ coincide con dicha entrada de la tabla si y solo si:

$$
\text{Destination} \oplus \text{Mask} == \text{Prefix}
$$

El paquete deberá ser enviado a la interfaz indicada por la entrada de la tabla con el prefijo más restrictivo (más largo) que coincide. Esto se debe a que si una **subred particular** está incluida en otra, entonces debe enviarle el paquete a la particular.

**Default Gateway:** Es el puerto configurado para cualquier entrada que no coincide con la tabla, se denota con el prefijo/mascara $\text{0.0.0.0/0}$, esto se debe a que, por lo que vimos recién, cualquier dirección IP coincidirá con esta entrada, pero no la preferirá por sobre cualquier otra entrada (ya que es de longitud mínima).

## Optimización de Tablas

Existen dos procedimientos para optimizar tablas:

- **Agregación de Entradas:** Se da cuando dos redes vecinas tienen como destino el mismo puerto, por lo que pueden ser simplificadas en una sola entrada. Se debe cumplir que:
	- Las entradas tienen una máscara de igual longitud
	- Las entradas únicamente varían en el último bit mantenido por la máscara
	- Las entradas tienen el mismo puerto de salida

	En ese caso, podremos unificar esas entradas en una sola tabla, disminuyendo en uno la longitud del prefijo. (debemos quedarnos con el prefijo cuyo último bit mantenido es un 0, ya que si no sería una entrada mal configurada).

- **Contención de Entradas:** Se da cuando dos entradas tienen la misma dirección de destino, y una entrada está contenida en otra. En estos casos podremos eliminar la entrada más restrictiva (la incluida en la otra).
- **Entrada Mal Configurada:** Una entrada mal configurada es aquella que tiene un bit de valor 1 en una posición mayor al tamaño de la máscara. Esto implica que ninguna dirección jamás podrá coincidir con ella. El prefijo es más restrictivo de lo que la máscara permite.
