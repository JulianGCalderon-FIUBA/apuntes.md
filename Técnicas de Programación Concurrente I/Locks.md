Los locks sirven para realizar exlusión mutua entre procesos. 

Se implementan mediante variables del tipo `lock`, que contienen el estado del mismo. Estos tienen dos métodos:
- Método `lock()`: El proceso se bloquea hasta obtener el *lock*
- Método `unlock()`: El proceso libera el lo
