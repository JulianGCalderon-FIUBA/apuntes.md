Hola @25C2, algunas aclaraciones para el TP:

**Formato del input**

El archivo sigue el siguiente formato

```
+ 1
* 2
/ 3
```

Como algunos ya notaron este no es el protocolo de comunicación con el servidor. Si el servidor recibiera ese archivo tal cual no lo entendería. Es trabajo del cliente, quien conoce el protocolo, leer ese archivo y enviar las operaciones en un formato que el servidor entienda, así como cualquier otra operación que sea necesaria y que no esté incluida en el archivo.

**Estructura del TP**

El TP tiene que estar estructurado de la misma forma que el primer trabajo práctico. Es decir, un solo *crate*, pero con 2 binarios en lugar de uno solo. Nosotros les compartimos un repositorio con algunos ejercicios que hicimos en clase, que tienen similitudes con el trabajo práctico, pero no tienen que usar ese repositorio como base del TP. Si les sirve, pueden copiar cosas de ese repositorio para su TP, pero no tienen que respetar la misma estructura de ese repositorio (pueden copiar y pegar lo que les sirva).

**No Clonar (excepto en algunos casos)**

Nosotros les pedimos que no clonen las estructuras, ya que en la mayoría de los casos se puede resolver con referencias. Hay **algunas** situaciones donde pueden clonar:

- Pueden clonar un stream con *try_clone* en caso de que sea necesario. Tengan en cuenta que si lo hacen, no pueden escribir en las instancias al mismo tiempo, o leer en las dos instancias al mismo tiempo. Si lo hacen, van a aparecer bugs. Solo pueden clonarlo si quieren leer y escribir por separado.
- Pueden clonar un `Arc`, ya que internamente no clona las estructura de datos, simplemente te da una nueva referencia.

¡Espero que les sirvan las aclaraciones! Buena semana.