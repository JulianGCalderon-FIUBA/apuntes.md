Para armar modelos de vista, el ***front end*** interactúa con la ***API***. Luego devuelve estos modelos para que el navegador lo renderice. Estos pedidos se realizan a través de un request ***HTTP***. La respuesta suele estar en formato ***json,*** el cual es utilizado para armar las vistas.

Para el ***backend***, se suele utilizar ***java*** con ***springboot,*** este es un framework de ***java*** utilizada para múltiples cosas, entre ellas aplicaciones web. Para la base de datos, existen distintos motores (***mySql***)

Para el front end, utilizaremos principalmente ***react,*** el cual se puede ejecutar tanto en la nube como en la web. (*Azure*, *Google Cloud*, *GitHub*).

Nuestro código estará almacenado en un repositorio en la nube, *GitHub*, *GitLab*, *BitBucket*. Para verificar que nuestros cambios cumplan lo esperado, hay distintos servidores para automatización e integración continua.

## Back End

Tendremos un modelo de capas, la primera es la ***API layer***, la cual recibe peticiones. Luego se ejecuta cierta lógica de negocio determinada (capa de servicio), se a la base de datos a través de capa de persistencia y acceso de datos. Finalmente devuelve una respuesta.

## Rest

Es un tipo de ***API,*** que cumple con ciertos requisitos. Se puede implementar de muchas formas, una de ellas es utilizando ***http***.

- **POST:** no idempotente, no es seguro (crea recursos) → C
- ***GET:*** idempotente, safe (lee recursos) → R
- ***PUT***: idempotente, no es seguro (actualiza recursos) → U
- ***DELETE:*** idempotente, no es seguro (borra recursos) → D

Las siglas ***CRUD*** se suelen usar normalmente en el lenguaje de negocio: las altas, bajas, modificaciones y consultas.

Un pedido idempotente es aquel que si se ejecuta dos veces, el cambio ocurre dos veces. *Ej: Con cada pedido de post, se crea un recurso.*

Hay distintos elementos en los mensajes de la ***API***:

- ***Path params:*** Comúnmente utilizado para identificar recursos. ***Ej: /accounts/{accountId}.*** No puede utilizar verbos.
- ***Query params:*** Comúnmente utilizado para filtrar y ordenar. Le sigue a la ***url*** y comienza con un '*?'*. ***Ej: /cars?color=blue***
- ***Body:*** Se utiliza para enviar o recibir un recurso determinado. Usualmente es un json***.***
