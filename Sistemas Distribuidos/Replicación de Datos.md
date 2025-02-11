Hay distintas formas de replicar datos:

## Leader Based

Una réplica se designa como *master* o *leader*, y el resto de réplicas se designan como *mirrors*, *slaves*, o *followers*.

Solo se aceptan escrituras en el *leader*, los cuales se sincronizan de forma sincrónica o asincrónica. Las lecturas se aceptan sobre todos los nodos.

Cuando se escribe en el líder, las réplicas no reciben la información de forma instantánea.

## Multi-Leader Based

Es común en escenarios con múltiples data-centers, donde hay separación entre los usuarios.

Frente a caídas en un data-center, se puede promover a otro como *leader* global.

Un problema común es como resolver conflictos entre distintos *leaders*. Otros problemas comunes incluyen:

- Manejo de triggers.
- Claves incrementales.
- Integridad de relaciones

## Leaderless Based

Es un sistema totalmente distribuido, y las réplicas deben sincronizarse mutuamente. Se pueden definir [[Topología de Comunicación|topologías]] de sincronización.

Son muy comunes los conflictos, a menos que se particionen los datos. Una forma de resolver los conflictos es el de conseguir consenso entre las réplicas para aplicar escrituras.

En estos casos, es común tener un middleware que sincronice a las replicas.

Es un modelo útil cuando tenemos una gran cantdiad de datos y/o de usuarios.
