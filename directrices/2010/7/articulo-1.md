DIRECCIÓN GENERAL DE ADUANAS
DIRECTRIZ DIR-DGT-007-2010
San José, 12 de mayo del 2010
Señores
Auxiliares de la Función Pública
Desarrolladores de Software
S. O.
ASUNTO: Web services de consulta para verificar el estado de los archivos .POL enviados al TIC@.
Estimados señores y señoras:
Por medio de la presente, la Dirección General de Aduanas, emite la directriz denominada “Web services de consulta para verificar el estado de un archivo .POL para la creación de DUAs en el sistema TIC@” con fundamento en las potestades otorgadas en los artículos 9, 11 y 12 de la Ley General de Aduanas N° 7557 del 20 de octubre de 1995 y sus reformas, artículos 18 y 20 inciso m) de su Reglamento, Decreto Nº 25270-H del 14 de junio de 1996 y sus reformas.
MOTIVACIÓN
Como parte importante de la labor de la Dirección General de Aduanas, está la dirección técnica y administrativa de las funciones aduaneras previstas en Ley General de Aduanas y demás disposiciones. En el desarrollo de esa labor se busca atender los requerimientos planteados por los usuarios para mejorar la eficiencia del Sistema Informático TIC@.
Es por ello que con la finalidad de mejorar el rendimiento del Sistema TIC@ se han puesto a disposición de los auxiliares de la función pública, tres web services (WS) que permite:
1) Consultar el estado que tienen los archivos .POL enviado por medio de la VAN para la creación de DUAs. En este caso, con el número del archivo, el WS retorna la posición en la cola de procesamiento.
2) Consultar los errores y avisos por carpeta generados cuando se ha procesado el archivo enviado por el auxiliar. En este caso, con el número de carpeta (campo NUME_ORDEN del mensaje del DUA) el WS retorna los errores, avisos y advertencias encontrados en el procesamiento.
3) Consultar los errores y avisos dado un número de archivo .POL. En este caso, el WS retorna los errores, avisos y advertencias generados en el procesamiento del archivo.
OBJETIVO
La presente directriz tiene como objetivo mejorar el rendimiento del Sistema TiC@ y su capacidad de procesamiento, poniendo a disposición de los usuarios del sistema TiC@, los Web Services antes mencionados. Lo que se persigue es que el usuario antes de reenviar el mismo archivo, consulte la respuesta del envío anterior.
Esta directriz, así como los documentos y características técnicas para accesar los Web Services, podrán ser consultadas a través de la página WEB del Ministerio de Hacienda.
https://www.hacienda.go.cr/Msib21/Espanol/Direccion+General+de+Aduanas/DIRECTRICES+2010.htm
RESPONSABLES
Esta Directriz es de acatamiento obligatorio para los auxiliares de la función pública aduanera que generen archivos POL, así como para los desabolladores de software certificados y los que en el futuro quieran certificarse para estar autorizados para el intercambio de información entre los Auxiliares de la función pública y el Sistema TIC@.
FUNDAMENTO LEGAL
La presente Directriz encuentra fundamento los artículos 9, 11 y 12 de la Ley General de Aduanas Nº 7557 del 20 de octubre de 1995 y sus reformas, artículos 18 y 20 inciso m) de su Reglamento, Decreto Nº 25270-H del 14 de junio de 1996 y sus reformas.
VIGENCIA
Rige a partir del 5 de julio de 2010. Comuníquese y publíquese en el Diario Oficial La Gaceta.
“WEB SERVICES DE CONSULTA PARA VERIFICAR EL ESTADO
DE LOS ARCHIVOS .POL ENVIADOS AL TIC@.”
I.—Sujetos competentes para su aplicación. Los sujetos competentes para la aplicación de esta directriz son los auxiliares de la función pública aduanera que generen archivos .POL y los desarrolladores de software autorizados para el intercambio de información entre los Auxiliares de la función pública y el Sistema TIC@.
II.—Ámbito de aplicación. Los presentes lineamientos deben ser observados en el intercambio de información vías mensajes XML, para la creación de DUAs mediante el envío de archivos con la extensión .POL y sus respectivas respuestas mediante archivos .POR.
III.—Contenido. Para efectos del intercambio de información, específicamente para la creación de DUAs, debe tomarse en consideración, en primer término, que el software del auxiliar debe consultar el estado en la cola de proceso de un archivo previo a su reenvío, con el fin de eliminar la posibilidad de tener en la cola de proceso más de un archivo con el mismo número. Para ello deben utilizar los web services de acuerdo con su finalidad, de conformidad con lo siguiente:
Web service posición en cola (TD): para que el auxiliar pueda enviar un archivo con el mismo número en varias ocasiones, el software del auxiliar deberá permitir consultar el estado que tiene el archivo .POL enviado por medio de la VAN para la creación de DUAs, el WS retornará la posición en la cola de procesamiento, una vez realizado este proceso, el software podrá permitir el reenvío del archivo.
Web service errores y avisos por carpeta: se pone a disposición de los auxiliares un WS que le permite conocer los errores y avisos por carpeta, generados cuando se ha procesado un archivo, dado un número de carpeta (campo NUME_ORDEN del mensaje de DUA) el WS retorna los errores, avisos y advertencias encontrados en el procesamiento.
Web service errores y avisos por nombre de archivo: se pone a disposición de los auxiliares un WS que le permite consultar los errores y avisos dado un número de archivo .POL, el WS retorna los errores, avisos y advertencias generados en el procesamiento de ese archivo.
IV.—Anexos. Con el fin aclarar el proceso, se encuentran disponibles en el sitio WEB tanto los requerimientos técnicos como los esquemas con la nueva funcionalidad del sistema.
https://www.hacienda.go.cr/Msib21/Espanol/Direccion+General+de+Aduanas/DIRECTRICES+2010.htm
