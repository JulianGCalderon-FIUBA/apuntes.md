Se utiliza para identificar de forma temprana vulnerabilidades que podrían ser aprovechadas por un atacante.

## Clasificación

Hay 3 tipos principales de *penetration tests*.

- **Black Box**: Plantea un escenario donde el atacante es externo. Sin disponer de conocimientos sobre las tecnologías existentes e ir aprendiendo sobre las infraestructuras, reconociendo vulnerabilidades y explotándolas. El atacante solo tiene acceso a las direcciones IP o web.
- **Grey Box**: Plantea un escenario donde el atacante tiene con pocos privilegios y la finalidad es tratar de conseguir escalar en privilegios. Simula, por ejemplo, un usuario disconforme.
- **White Box**: Plantea un escenario donde el atacante se encuentra dentro del sistema. Suponiendo que pudiesen existir *backdoors*, tanto en el código fuente como en la configuración del sistema.

## Fases

En la práctica, un *penetration test* se divide en las siguientes fases:

- **Acuerdo de Confidencialidad**: Un contrato donde ambas partes se ponen de acuerdo en no divulgar información. Por ejemplo: vulnerabilidades, credenciales.
- **Reconocimiento**: Se reconoce el campo de trabajo sobre el cual está inmerso el objetivo. Esto involucra utiliza buscadores web, bases de datos, consultas DNS, ingeniería social.
- **Enumeración**: A esta fase se la conoce como reconocimiento activo. Empezaremos a utilizar herramientas para analizar nuestro objetivo profundamente. Es una fase más agresiva.
- **Explotación**: A partir de las vulnerabilidades encontradas, dedicaremos tiempo a investigar herramientas para explotarlas.
	- Se conoce como *payload* a la carga maliciosa. El mismo, comúnmente va junto con el *exploit*. El *exploit* es el encargado de explotar la vulnerabilidad y el *payload* será la porción de código que nos permita realizar la acción posterior.
- **Post Explotación**: Una vez que conseguimos explotar la vulnerabilidad, el siguiente paso será lograr mantener persistencia. Para ellos podemos migrar de proceso, dejar un *backdoor*, un *troyano*, un *rootkit*, etc.
	- La fase de borrar rasgos incluye técnicas *anti-forenses*, para evitar revelar información ante un análisis forense posterior a la explotación.
- **Informes**: Suelen ser dos informes, uno ejecutivo y uno técnico. Se debe utilizar un lenguaje acorde al público del informe.
	- Un informe ejecutivo debe ser corto y resumido sobre la situación. Tiene que contener gráficos. Algunos elementos a mencionar son: objetivo, alcance, línea de tiempo, alcance, resumen.
	- Un informe técnico contiene el detalle completo de las vulnerabilida

## Informes
