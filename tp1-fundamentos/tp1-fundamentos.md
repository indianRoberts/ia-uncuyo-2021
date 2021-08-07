# Fundamentos filosóficos

## IA débil: ¿pueden las máquinas actuar con inteligencia?

Algunos filósofos han intentado demostrar que la IA es imposible; que las máquinas no tendrán la posibilidad de actuar inteligentemente. Obviamente dependerá de cómo se defina. En esencia,
la IA consiste en la búsqueda del mejor programa agente en una arquitectura dada.

«¿Pueden pensar las máquinas? ̈ Desgraciadamente, esta cuestión no está bien definida. Para ver por qué, consideremos las dos cuestiones siguientes:
• ¿Pueden volar las máquinas?
• ¿Pueden nadar las máquinas?

lan Turing, en su famoso artículo «Computing Machinery and Intelligence ̈ (Turing, 1950), sugirió que en vez de preguntar si las máquinas pueden pensar, deberíamos preguntar si las máquinas pueden aprobar un test de inteligencia conductiva (de comportamiento), conocido como el Test de Turing. La prueba se realiza para que el programa mantenga una conversación durante cinco minutos (mediante mensajes escritos en línea, online) con un interrogador (interlocutor). Éste tiene que averiguar si la conversación se está llevando a cabo con un programa o con una persona; si el programa engaña al interlocutor un 30 por ciento del tiempo, este pasará la prueba.

El programa ELIZA y el chatbot en Internet llamado MGONZ han engañado a personas que no se daban cuenta de que estaban hablando con un programa; el programa ALICE engañó a un juez en la competición del Loebner Prize en el año 2001. Sin embargo, ningún programa se ha acercado al criterio del 30 por ciento frente a jueces con conocimiento, y el campo en su conjunto de la IA no ha prestado mucha atención a los tests de Turing

### El argumento de incapacidad

El «argumento de incapacidad ̈ afirma que «una máquina nunca puede hacer X ̈. Como ejemplos de X, Turing enumera las siguientes acciones: Ser amable, tener recursos, ser guapo, simpático, tener iniciativas, tener sentido del humor, distinguir lo correcto de lo erróneo, cometer errores, enamorarse, disfrutar con las fresas con nata, hacer que otra persona también se enamore, aprender de la experiencia, utilizar palabras de forma adecuada, ser el tema de su propio pensamiento, tener tanta diversidad de comportamientos como el hombre, hacer algo realmente nuevo.

Es innegable que los computadores actualmente hacen muchas cosas que anteriormente eran sólo del dominio humano. En el año 1955, Paul Meehl (véase también Grove y Meehl, 1996) estudió los procesos de la toma de decisiones de expertos formados en tareas subjetivas como predecir el éxito de un alumno en un programa de formación, o la reincidencia de un de-
lincuente. De 20 estudios que Meehl examinó, en 19 de ellos encontró que sencillos algoritmos de aprendizaje estadístico (tal como la regresión lineal y Bayes simple) predicen mejor que los expertos.

### La objeción matemática

Es bien conocido, a través de los trabajos de Turing (1936) y Gödel (1931), que ciertas cuestiones matemáticas, en principio, no pueden ser respondidas por sistemas formales concretos. El teorema de la incompletitud de Gödel es el ejemplo más conocido en este respecto

Filósofos como J. R. Lucas (1961) han afirmado que este teorema demuestra que las máquinas son mentalmente inferiores a los hombres, porque las máquinas son sistemas formales limitados por el teorema de la incompletitud, es decir no pueden establecer la verdad de su propia sentencia Gödel, mientras que los hombres no tienen dicha limitación.Sir Roger Penrose (1989,1994) suma a esto la hipótesis de que los hombres son diferentes porque sus cerebros operan por la gravedad cuántica. 
Examinemos solamente tres de los problemas de esta afirmación.
1)la afirmación de Lucas en parte se basa en la afirmación
de que los computadores son máquinas de Turing. Esta es una buena aproximación, pero no es del todo verdadera. Aunque los computadores son finitos, las máquinas de Turing son infinitas, y cualquier computador por tanto se puede describir como un sistema (muy grande) en la lógica proposicional, la cual no está sujeta al teorema de incompletitud de
Gödel.
2)En segundo lugar, un agente no debería avergonzarse de no poder establecer la verdad de una sentencia aunque otros agentes sí puedan. Por ejemplo, ninguna persona podría calcular la suma de 10 billones de números de 10 dígitos en su vida, en cambio un computador podría hacerlo en segundos. Sin embargo, no vemos esto como una limitación fundamental en la habilidad de pensar del hombre. Durante miles de años los hombres se han comportado de forma inteligente antes de que se inventaran las máquinas, de manera que no es improbable que el razonamiento matemático no tenga más que una función secundaria en lo que implica ser inteligente.
En tercer lugar, es imposible demostrar que los hombres no están sujetos
al teorema de incompletitud de Gödel, porque cualquier prueba rigurosa contendría una formalización del talento humano declarado como no formalizable. De manera que nos quedamos con el llamamiento a la intuición de que los hombres, de alguna forma, pueden realizar hazañas superhumanas de comprensión matemática.


### El argumento de la informalidad

Segun Turing el comportamiento humano es demasiado complejo para po-
der captarse mediante un simple juego de reglas y que debido a que los computadores no pueden nada más que seguir un conjunto (juego) de reglas, no pueden generar un comportamiento tan inteligente como el de los hombres.
Bajo el punto de vista de Dreyfus, la pericia del hombre incluye el conocimiento de algunas reglas, pero solamente como un «contexto holístico ̈ o «conocimiento base ̈ (background) dentro del que operan los hombres. Proporciona como ejemplo el comportamiento social adecuado al dar o recibir regalos: «Normalmente se responde simplemente en las circunstancias adecuadas y dando el regalo adecuado ̈. Al parecer hay que «tener un sentido directo de cómo hay que hacer las cosas y qué esperar ̈.
Dreyfus y Dreyfus (1986) proponen un proceso de adquisición de pericia en cinco etapas, comenzando con un procesamiento basado en reglas (del tipo propuesto en GOFAI) y terminando con la habilidad de seleccionar las respuestas correctas instantáneamente. Al realizar esta propuesta, Dreyfus y Dreyfus pasan en efecto de ser críticos a la IA a ser teóricos de IA, ya que proponen una arquitectura de redes neuronales organizadas en una biblioteca de casos extensa, pero señalan algunos problemas. Afortunadamente, se han abordado todos sus problemas, algunos con éxito parcial y otros con éxito total. Entre estos problemas se incluyen los siguientes:
1. No se puede lograr una generalización buena de ejemplos sin un conocimiento básico.Afirman que no se sabe cómo incorporar el conocimiento básico en el proceso de aprendizaje de las redes neuronales. 
2. afirman que no puede funcionar autónomamente sin la ayuda de un entrenador humano. De hecho, el aprendizaje sin un profesor se puede conseguir mediante un aprendizaje no supervisado y un aprendizaje de refuerzo. 
3. Los  algoritmos  de  aprendizaje  no  funcionan  bien  con  muchas  funciones. De hecho, métodos nuevos tales como las máquinas vectoriales de soporte utilizan muy bien conjuntos grandes de funciones.
4.El cerebro es capaz de dirigir sus sensores para buscar la información relevante y procesarla para extraer aspectos relevantes para la situación actual. Sin embargo, afirman que «Actualmente, los detalles de este mecanismo ni se entienden y ni siquiera se hipotetizan para guiar la investigación en la IA ̈. De hecho, el campo de la visión activa, respaldado por la teoría del valor de la información tiene que ver exactamente con el problema de dirigir los sensores, y algunos robots ya han incorporado los resultados teóricos obtenidos

## IA fuerte: ¿pueden las máquinas pensar de verdad?

Hasta que una máquina pueda escribir un soneto o componer un concierto porque sien-
ta los pensamientos y las emociones, y no porque haya una lluvia de símbolos, podría
reconocer que la máquina iguala al cerebro, es decir, no sólo escribirlo sino que sepa que
lo ha hecho. Esto es lo que Turing llama el argumento de la consciencia, la máquina tiene que ser consciente de sus propias acciones y estados mentales.

Turing reconoce que la cuestión de la conciencia (consciencia) es difícil, pero niega que sea relevante para la práctica de la IA. Coincidimos con Turing en que nos interesa crear programas que se comporten de forma inteligente y no en si alguien los declara reales o simulados. Por otro lado, muchos filósofos están especialmente interesados en esta cuestión. 

El problema mente-cuerpo al que se enfrentan los dualistas es la cuestión de cómo la mente puede controlar el cuerpo si los dos están realmente separados.

La teoría monista de la mente, a menudo llamada fisicalismo, evita este problema afirmando que la mente no está separada del cuerpo, que los estados mentales son estados físicos.

El problema para los fisicalistas es explicar cómo estados físicos, en particular, las configuraciones moleculares y los procesos electroquímicos de el cerebro: pueden ser simultáneamente estados mentales, como sentir dolor, disfrutar de una hamburguesa,
saber que se monta a caballo o creer que Viena es la capital de Austria.

### Estados mentales y el cerebro en una tina

Imagínese que al nacer le extraen el cerebro de su cuerpo y lo colocan en una cubeta con una ingeniería maravillosa. Esta cubeta mantiene su cerebro y le permite crecer y desarrollarse. Al mismo tiempo, su cerebro recibe unas señales electrónicas de un simulador informático que pertenece a un mundo totalmente ficticio, y las señales motoras de su cerebro son interceptadas y utilizadas para modificar la simulación cuando sea adecuado. A continuación, el estado del cerebro podría tener el estado mental MueroPor (Yo, Hamburguesa) aunque no tenga un cuerpo con el que sentir hambre ni sentido del gusto para experimentarlo, y puede que tampoco haya hamburguesas en el mundo real. En ese caso, ¿sería el mismo estado mental que el del cerebro en un cuerpo?
La visión del «contenido extenso ̈ interpreta el dilema desde el punto de vista de un observador omnisciente desde fuera con acceso a la situación completa, y que puede distinguir las diferencias del mundo. De esta manera, bajo el contenido extenso, las ideas del cerebro en una cubeta son diferentes de las de una persona «normal ̈. 
El contenido estrecho sólo tiene en cuenta el punto de vista subjetivo interno, y bajo este punto de vista todas las creencias serían las mismas.

El contenido amplio es totalmente apropiado si el objetivo de uno es atribuir estados mentales a los demás que comparten el mundo de uno, para predecir su comportamiento probable y sus efectos, etc. Este es el entorno en el que ha evolucionado nuestro lenguaje ordinario sobre el contenido mental. Por otro lado, si a uno le preocupa la cuestión de si los sistemas de IA realmente están pensando y realmente tienen estados mentales, entonces el contenido limitado es apropiado; simplemente no tiene sentido decir que si un sistema de IA está realmente pensando o no depende de condiciones fuera de ese sistema. El contenido estrecho también es relevante si estamos pensando en diseñar sistemas de IA o comprender su funcionamiento, porque es el contenido estrecho de un estado cerebral lo que determina cuál será el próximo estado cerebral. Esto conduce naturalmente a la idea de que lo que importa sobre un estado cerebral es lo que hace que tenga un tipo de contenido mental y no otro - es su papel funcional dentro de la operación mental de la entidad involucrada.

### El experimento de la prótesis cerebral

suponga que la neurofisiología ha evolucionado hasta tal punto que el comportamiento y las conexiones de entrada y salida de todas las neuronas del cerebro humano se entienden perfectamente. Además, suponga que podemos construir mecanismos electrónicos microscópicos que imitan este comportamiento y que pueden interconectarse con el tejido neuronal. Y finalmente, suponga que una técnica quirúrgica milagrosa puede sustituir las neuronas individuales con los mecanismos electrónicos sin interrumpir el funcionamiento del cerebro por completo. El experimento consiste en sustituir gradualmente todas las neuronas de la cabeza de alguien con mecanismos electrónicos y a continuación invertir el proceso para retornar al sujeto a su estado biológico normal.
Ahora bien, aunque la presencia o ausencia de consciencia no la pueda asegurar fácilmente un tercero, el sujeto del experimento debería por lo menos poder registrar cualquier cambio en su propia experiencia consciente.

### La habitación china

John Searle (1980), quien describe un sistema hipotético que claramente está eje-
cutando un programa y que pasa la prueba de Turing, pero que igualmente y de mane-
ra clara no entiende (según Searle) ninguna entrada ni salida. Su conclusión es que
ejecutar el programa adecuado (es decir, tener las salidas adecuadas) no es una condi-
ción suficiente para ser una mente.
El sistema se compone de un hombre, que solamente entiende inglés, y que está equi-
pado con un libro de reglas escrito en inglés y varias pilas de papel, algunas en blanco
y algunas con inscripciones indescifrables. (El hombre entonces hace el papel de la CPU,
el libro de normas es el programa y los papeles son el dispositivo de almacenamiento.)
El sistema se encuentra dentro de una habitación con una apertura al exterior. A través
de la apertura se van deslizando los papeles con símbolos indescifrables. El hombre en-
cuentra los símbolos correspondientes en el libro de reglas y sigue las instrucciones. Las
instrucciones pueden incluir escritura de símbolos en los papeles nuevos que van saliendo,
encontrar símbolos en las pilas de papeles, reorganizar las pilas, etc. Finalmente las ins-
trucciones harán que un símbolo o más sean transcritos a un trozo de papel que se pasa
otra vez al mundo exterior.
Hasta ahora todo está bien. Pero desde fuera, se observa un sistema que está sacan-
do la entrada en forma de sentencias chinas y generando respuestas chinas que obvia-
mente son tan «inteligentes ̈ como las de la conversación imaginada por Turing5.
Entonces Searle argumenta lo siguiente: la persona que está en la habitación no entiende
el chino (supuestamente). El libro de reglas y las pilas de papel, que son sólo trozos de
papel no entienden el chino. Por consiguiente no está habiendo comprensión del chino.
De aquí que, según dice Searle, ejecutar el programa adecuado no genera necesaria-
mente entendimiento.

Searle y Penrose dicen que los defensores de la “inteligencia artificial fuerte”, aquellos que defienden la postura de que un programa de ordenador eventualmente podrá comprender el lenguaje natural y poseer propiedades de la mente humana (no simplemente simularlas), deben admitir que, o bien la sala comprende el idioma chino, o bien el pasar el test de Turing no es prueba suficiente de inteligencia. 
Searle permite la posibilidad lógica de que el cerebro esté implementando de ver-
dad un programa de IA de la clase tradicional. Sin embargo, si el mismo programa se
ejecuta en la clase inadecuada de máquina no sería una mente. Searle no cree que las
«máquinas no puedan tener mentes ̈, en cambio afirma que algunas máquinas sí que tie-
nen mentes, los hombres son máquinas biológicas con mentes. No nos queda ninguna
guía para ver qué tipos de máquinas califican o no califican


## La ética y los riesgos de desarrollar la Inteligencia Artificial

Se han identificado ocho amenazas potenciales para la sociedad que se exponen tanto ante la IA como ante una tecnología relacionada.

Las personas podrían perder sus trabajos por la automatización.Hasta ahora, la automatización por medio de la tecnología de la IA ha creado más trabajos de los que ha eliminado, y ha creado puestos de trabajo más interesantes y mejor pagados:

• Las personas podrían tener demasiado (o muy poco) tiempo de ocio.
La IA incrementa el ritmo de la innovación tecnológica y contribuye así a esta tendencia general, pero la IA también mantiene la promesa de permitirnos ahorrar tiempo y permitir que nuestros agentes automatizados hagan las cosas por un tiempo.

• Las personas podrían perder el sentido de ser únicos.
La IA aunque sea una materia de gran éxito, quizá sea por lo menos amenazante para las suposiciones morales de la sociedad del siglo XXI al igual que la teoría de la evolución
lo fue para los del siglo XIX.

• Las personas podrían perder algunos de sus derechos privados.

• La utilización de los sistemas de IA podría llevar a la pérdida de responsabilidad.
Al igual que con la tecnología para la reproducción humana, la ley tiene todavía que ponerse a la altura de los nuevos desarrollos.

• El éxito de la IA podría significar el fin de la raza humana.
Si los robots adquieren consciencia, tratarlos entonces como meras «máquinas ̈ (por ejemplo, tratarlos como algo aparte) podría ser inmoral. Los robots también deben actuar moralmente,necesitaríamos programarlos con una teoría de lo que está bien y lo que está mal. Los escritores de ciencia ficción han abordado el tema de los derechos y responsabilidades de los robots, empezando por Isaac Asimov (1942). La famosa película titulada A.I. (Spielberg, 2001) se basó en una historia de Brian Aldiss sobre el robot inteligente que fue programado para creer que él era un humano y que no entiende el abandono final por parte de su madre-propietaria. La historia (y la película) convencen de la necesidad de los robots para moverse por sus derechos civiles.




