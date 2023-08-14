El campo de la seguridad de red se trata de que formas una persona puede atacar una red de computadoras y como nosotros podemos defendernos antes estos ataques, o mejor, diseñar arquitecturas inmunes a estos ataques.

## The Bad Guys Can Put Malware into Your Host Via the Internet

Al recibir información de internet, podemos encontrar archivos maliciosos conocidos como ***malware***. Estos infectan nuestro dispositivo y toman control del mismo. Nuestro host puede ser agregado a una red de miles de disipativos conocida como ***botnet***, utilizada para distribuir ataques o *spam emails*.

Muchas veces, el ***malware*** es ***self-replicating***. Una vez infecta un ***host***, busca entrada al siguiente a través del internet. Los ***malware*** se dividen en dos categorías según el método de contagio:

- ***Viruses:*** Requieren algún tipo de interacción del usuario para infectar un dispositivo, como la ejecución de un código malicioso. Una vez infectado, pueden propagarse reenviando mails a todos los contactos, entre otras cosas.
- ***Worms***: Entran al dispositivo sin ninguna interacción explícita con el usuario. Por ejemplo, el usuario puede estar ejecutando una aplicación de red vulnerable. Una vez infectado, escanean la ***web*** buscando ***hosts*** con la misma vulnerabilidad.

## The Bad Guys Can Attack Servers and Network Infrastructure

Otra amplia clase de las amenazas de seguridad son las conocidas ***DoS Attacks*** (***Denial-of-Service)***. Como sugiere el nombre, un ataque *DoS* busca dejar inutilizable un host, red, o componente de la infraestructura.

La mayoría de estos ataques recaen en tres categorías:

- ***Vulnerability Attack***: Consiste en enviar una serie ingeniosamente diseñada de mensajes a una aplicación vulnerable para hacer que frene su funcionamiento, o peor, que ***crashee***.
- ***Bandwidth Flooding:*** El atacante envía un diluvio de mensajes al ***host, atascando la red y previniendo*** la llegada de ***packets*** legítimos.
- ***Connection Flooding:*** El atacante establece un gran número de conexiones TCP semiabiertas o totalmente abiertas. Esto entorpece al ***host*** con todas estas conexiones falsas, impidiendo que acepte conexiones legítimas.

Si toda la fuente del ataque proviene de una sola computadora, entonces la red puede bloquear los **packets** de esa dirección antes de que lleguen al servidor. Debido a esto, se suele utilizar un ataque ***Distributed DoS (DDos).*** En este tipo de ataques, el atacante controla múltiples fuentes y envía altas cantidades de tráfico desde cada una. Para este tipo de ataque, se suelen utilizar las ***botnets*** para controlar un gran número de computadoras.

## The Bad Guys Can Sniff Packets

Al colocar un receptor pasivo en la cercanía de un transmisor inalámbrico, podemos obtener una copia de todos los paquetes que son enviados. Estos dispositivos son conocidos como ***sniffers***, y

Los ***sniffers*** también son útiles en los ambientes cableados. Se colocan en él ***access router*** e interceptan todos los mensajes que son enviados por allí.

Al ser pasivos (no inyectan información, sino que leen) son difíciles de detectar. La mejor solución a esta técnica consiste en involucrar criptografía.

## The Bad Guys Can Masquerade as Someone You Trust

Es sorprendentemente fácil crear un paquete con una dirección de fuente arbitrario y transmitirlo a la red, la cual va a exitosamente hacer llegar el paquete a destino. La habilidad de inyectar paquetes con una dirección falsa de envío se conoce como ***IP spoofing***.

Para solucionar este problema, necesitaremos ***end-point authentication***. Un mecanismo que nos permitirá determinar la veracidad del origen de un mensaje.

El internet fue originalmente diseñado para ser usado entre un grupo de usuario con confianza en una red transparente. Pero este ya no es el caso, muchas veces es necesario comunicarnos con usuarios con los que no tenemos confianza.
