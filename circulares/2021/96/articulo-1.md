CIRCULAR N° 96-2021
ASUNTO: Creación de un reporte informático denominado "Duración del circulante activo"
A TODOS LOS DESPACHOS JUDICIALES DEL PAÍS
QUE CONOCEN MATERIA DE FAMILIA
Y PENSIONES ALIMENTARIAS
SE LES HACE SABER QUE:
El Consejo Superior del Poder Judicial en sesión N° 36- 2021, celebrada el 04 de mayo de 2021, artículo LVI, dispuso hacer de conocimiento el oficio 021-JVA-2021 del 21 de abril de 2021 remitido por la Magistrada Julia Varela Araya en su condición de coordinadora de la Comisión de Familia, Niñez y Adolescencia del Poder Judicial, el cual literalmente indica:
La Comisión de Familia, Niñez y Adolescencia del Poder Judicial acordó comunicarles a todos los Despachos del país, que tramitan materia de Pensiones Alimentarias y Familia que las Direcciones de Tecnología de la Información y Planificación han creado un reporte informático denominado "Duración del circulante activo" para que los Despachos verifiquen al menos cada tres meses y certifiquen dicha revisión al Subproceso de Estadística, los expedientes activos que presentan mayor duración en trámite (fase demanda-demostrativa conclusiva) según plazo legal y criterio experto sin ser resueltos para que procedan a estar promoviendo una pronta resolución del proceso.
[imagen]
La importancia y obligatoriedad de realizar lo anterior, es conforme a lo acordado por el Consejo Superior en sesión 111- 20, del 17 de noviembre del 2020, artículo 2020 para atender la recomendación 4.4 y el punto 2.37. del informe de la Contraloría General de la República DFOE-PG-IF-00002-2020 "Informe de Auditoría Operativa sobre la gestión del Poder Judicial en cuanto a la oportunidad de la prestación del servicio público de administración de la justicia de los juzgados de Familia y de Pensiones alimentarias". Y en atención a las recomendaciones del informe 389-PLA-RH-MI-2021 de la Dirección de Planificación.
. Se adjunta el manual elaborado por el Subproceso de Estadística de la Dirección de Planificación sobre el uso del reporte. Ref.: 450-2021 / 4050-2021/Andrea
[imagen]
https://secretariacorte.poder-judicial.go.cr/index.php/documentos?download=5135:informe-de-inconsistencias-para-familia-y-pensiones-alimentarias-plataforma-sigma
(Nota de Sinalevi: El manual elaborado por el Subproceso de Estadística de la Dirección de Planificación sobre el uso del reporte, se extrajo del sitio Web del Nexus, y se transcribe a continuación:
Informe "Informe de Inconsistencias para Familia y Pensiones Alimentarias" Plataforma SIGMA
Informe Tecnico [imagen] Licda Marlen Vargas Benavides, Coordinadora de Unidad, Subproceso de Estadística, Dirección de Planificación Manfred Tosso Jara, Unidad de Inteligencia de la información. Dirección de Tecnología de la Información | Tareas Ejecutadas: · Diseño completo del informe en SIGMA · Modelado de la información · Monitoreo y pruebas Por parte Estadística se hacen los ajustes y pruebas en el informe, y se coloca en producción en la carpeta de "Informes de Inconsistencias de Estadística" para consumo del usuario.
| [imagen]
Ubicación del informe en la plataforma Sigma
[imagen]
Contenido del informe
[imagen]
Parámetros de ejecución para el usuario
Año: solo permite seleccionar un año
Mes: solo permite seleccionar un mes
Materia: Permite seleccionar una o varias materias según desee el usuario
Tipo de caso: Permite seleccionar uno o varios tipos de caso según desee el usuario
Tipo de despacho: Se recomienda el uso opcional de este parámetro para filtrar por juzgados o tribunales en el caso de materia penal.
Cod Despacho: es opcional, por si se requiere ver un solo despacho
[imagen]
Parámetros predeterminados
-Indicador Circulante Final: CF
-la construcción de las consultas: "Incidentes, legajos, circulante", "Monto pensiones" y "pase a fallo" se realizaron por medio de diseño personalizado en SQL, para que las mismas brinden la información requerida. El ajuste o mantenimiento de dichas consultas, solo debe ser manipulado por los compañeros de la Unidad de la Inteligencia de la Información.
Descripción de las cejillas que conforman el informe
Cejilla n°1 "Fecha de término menor a la fecha de entrada". [imagen] Reporte que permita visualizar los expedientes que la fecha de entrada es mayor a la fecha de término del expediente. [imagen] | Despliega las siguientes variables: [imagen] Número de expediente único [imagen] Tipo de Caso: Registra todos los tipos de carpetas existentes en el periodo que se consulta. [imagen] Código de despacho [imagen] Descripción del despacho o nombre del despacho [imagen] Materia [imagen] Fecha Entrada: del expediente [imagen] Fecha de estado: del expediente [imagen] Nombre estado estadístico: se refiere a terminado, entrado o reentrado [imagen] Estado: estados que terminan estadísticamente el expediente [imagen] Duración: en meses [imagen] Cantidad: muestra la cantidad de estados
Cejilla n°2 "Clases de asunto del circulante desactualizadas". [imagen] [imagen] Identificar las clases de asuntos que no corresponden a las aprobadas por la Comisión. | Despliega las siguientes variables: [imagen] Número de expediente único [imagen] Tipo de Caso: Regístra todos los tipos de carpetas existentes en el periodo que se consulta. [imagen] Clase de asunto [imagen] Estado [imagen] Código de despacho [imagen] Descripción del despacho o nombre del despacho [imagen] Materia [imagen] Fecha Entrada: del expediente [imagen] Mes Circulante [imagen] Cantidad: muestra la cantidad de estados
Cejilla n°3 "Procedimientos del circulante desactualizadas". [imagen] [imagen] Identificar en el módulo de procedimiento variables que no corresponde a procedimiento según lo aprobado por la Comisión. | Despliega las siguientes variables: [imagen] Número de expediente único [imagen] Tipo de Caso: Registra todos los tipos de carpetas existentes en el periodo que se consulta. [imagen] Materia [imagen] Código de despacho [imagen] Descripción del despacho o nombre del despacho [imagen] Fecha Entrada: del expediente [imagen] Estado: estados que terminan estadísticamente el expediente [imagen] Procedimiento [imagen] Cantidad: muestra la cantidad de estados
Cejilla n°4 "Casos activos con el principal terminado". [imagen] Reporte que permita detectar expedientes que el principal se encuentra cerrado estadísticamente, pero tiene un incidente, legajo de apremio que se está tramitando [imagen] | Despliega las siguientes variables: [imagen] Número de expediente único [imagen] Tipo de Caso: Registra todos los tipos de carpetas existentes en el periodo que se consulta. [imagen] Descripción tipo de caso [imagen] Código de despacho [imagen] Descripción del despacho o nombre del despacho [imagen] Fecha Entrada: del expediente [imagen] Procedimiento [imagen] Clase de asunto [imagen] Estado [imagen] Materia [imagen] Cantidad: muestra la cantidad de estados
Cejilla n°5 "Montos de pensiones". [imagen] Reporte que permita visualizar un listado de expedientes activos en pensiones alimentarias de montos alimentarios por rango y tipo de moneda. [imagen] | La consulta es viable para ser ejecutada de forma mensual, esto significa que la información que extrae corresponde a las carpetas activas de los expedientes cuyo principal se terminó en ese mes o bien durante el año. Lo anterior, siendo que queda un rezago de lo más viejo. [imagen]
Cejilla n°6 "Duración del circulante activo". [imagen] Reporte que permita identificar la duración de los expedientes judiciales en procesos activos. [imagen] | Despliega las siguientes variables: [imagen]
Cejilla n°7 "Duración de los expedientes Terminados". [imagen] Reporte que permita identificar el tiempo de resolución de las causas terminadas [imagen] | Despliega las siguientes variables: [imagen]
Cejilla n°8 "Errores en fechas de pase a fallo". [imagen] [imagen] Reporte que permita identificar inconsistencias en los plazos de pase a fallo | Despliega las siguientes variables: [imagen] Número de expediente único [imagen] Materia [imagen] Tipo de Caso: Registra todos los tipos de carpetas existentes en el periodo que se consulta. [imagen] Código de despacho [imagen] Descripción del despacho o nombre del despacho [imagen] Fecha de pase a fallo [imagen] Fecha de resolución [imagen] Estado sentencia: se refiere a dictada, apelada, en borrador, etc [imagen] Cantidad: muestra la cantidad de estados
San José, 11 de mayo de 2021.
