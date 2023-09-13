La corrección implica que el programa haga lo que tiene que hacer.

Existen dos propiedades de la corrección:

- **Safety:** Debe ser verdadera siempre
- **Liveness:** Debe volverse verdadera eventualmente.

## Safety

Existen dos principales propiedades que deben cumplirse para satisfacer la propiedad de *safety*.

- **Exclusión mutua:** Dos procesos no deben intercalar ciertas secuencias de instrucciones
- **Ausencia de deadlocks:**
