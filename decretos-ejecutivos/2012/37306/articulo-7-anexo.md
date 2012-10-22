Anexo 7
PROTOCOLO DE SISTEMA DE INFORMACIÓN
Definición de la estructura de los archivos del módulo de importación de eventos y vacunas
Todos los archivos que importa el Sistema de Información de Vigilancia de Enfermedades Integrada (SIVEI) son de tipo Extensible Markup Language (XML). A continuación se define la estructura de cada de los mismos según tipo de evento.
Importación de personas
Formato
<persona>
<tipoIdentificacion></tipoIdentificacion>
<numeroIdentificacion></numeroIdentificacion>
<nombre></nombre>
<apellido1></apellido1>
<apellido2></apellido2>
<fechanac></fechanac>
<sexo></sexo>
<nombreEncargado></nombreEncargado>
<apellido1Encargado></apellido1Encargado>
<apellido2Encargado></apellido2Encargado>
<lugarTrabajo></lugarTrabajo>
<celular></celular>
<telefono></telefono>
<codigoProvincia></ codigoProvincia >
<codigoCanton></codigoCanton>
<codigoDistrito></codigoDistrito>
<otrasSenas></otrasSenas>
</persona>
Tabla 1: Definición de etiquetas de persona
Etiqueta | Tipo de dato | Es Requerido | Descripción
tipoIdentificacion | Texto | X | INDOCUMENTADO CEDULA_FISICA_NACIONAL NUMERO_ASEGURADO PASAPORTE CEDULA_RESIDENCIA
numeroIdentificacion | Texto (20) | Depende de tipoIdentificacion: Si el valor de tipoIdentificación es INDOCUMENTADO este campo no es requerido; si el valor es cualquiera de los otros sí |
nombre | Texto (30) | X |
apellido1 | Texto (30) | X |
apellido2 | Texto (30) | X |
fechanac | Fecha: dd/MM/aaaa | X | NO DEFINIDO_ MASCULINO FEMENINO
sexo | Texto | |
nombreEncargado | Texto (90) | |
apellido1Encargado | Texto (30) | |
apellido2Encargado | Texto (30) | |
lugarTrabajo | Texto (30) | |
celular | Numérico | |
telefono | Numérico | |
codigoProvincia | Numérico | X | Debe indicarse el código de la provincia
codigoCanton | Numérico | X | Debe indicarse el código del cantón
codigoDistrito | Numérico | X | Debe indicarse el Código del distrito
otrasSenas | Texto(150) | X | Indica la dirección exacta de la persona
NOTA
La fase de importación de personas antecede a la importación de cualquier evento. Todos los eventos que se importan al SIVEI deben incluir el XML correspondiente a una persona.
Importación de casos
Formato
<caso>
<diagnostico></diagnostico>
<NombreInformante></nombreInformante>
<apellido1Informante></apellido1Informante>
<apellido2Informante></apellido2Informante>
<fecha></fecha>
<fechaInicioSint></fechaInicioSint<
<establecimiento></establecimiento>
<muestra></muestra>
<fechaMuestra></fechaMuestra>
<cerrado></cerrado>
<clasificacion<</clasificación>
<observaciones></observaciones>
<sistema></sistema>
<fechaExportacion></fechaExportacion>
</caso>
Tabla 2: Definición de etiquetas de caso
Etiqueta | Tipo de dato | Nota | Valores
Diagnóstico | Texto | | Código del diagnóstico
nombreInformante | Texto | | Nombre del informante 1 1 Si el nombre del informante y sus apellidos se insertan dentro de la etqueta nombreInformante los daros se procesan de la siguiente forma: si hay dos palabras separadas por espacio se asume que la primera corresponde al nombre y la segunda al apellido, si hay tres palabras separadas por espacios se asume lo anterior y la tercera corresponde al segundo apellido, si hay cuatro palabras separadas por espacios se asume que la primera corresponde al nombre, la penúltima al primer apellido y la última al segundo apellido
Apellido1Informante | Texto | | Primer apellido del informante
Apellido2Informante | Texto | | Segundo apellido del informante
Fecha | Fecha: dd/MM/aaaa | |
fechaInicioSint | Fecha: dd/MM/aaaa | |
Establecimiento | Texto | | Código del establecimiento
Muestra | Texto | Si los valores no corresponden con los indicados en la columna descripción se almacena | LABORATORIO_LOCAL INCIENSA NO_HUBO
fechaMuestra | | |
cerrado | caracter | Si el valor es diferente de S se almacena N | S N
Clasificación | Texto | Si los valores no corresponden con los indicadores en la columna descripción se almacena_ | PENDIENTE SOSPECHOSO PROBABLE DESCARTADO CONFIRMADO_LABORATORIO CONFIRMADO_NEXO_EPIDEMIOLOGICO CONFIRMADO_CLINICA_
Observaciones | Texto (200) | |
fuenteContagio | Texto (100) | |
sistema | Texto (15) | | Sistema del cual provienen el registro.
fechaExportación | Fecha: dd/MM/aaaa | | Fecha en la que se generó el archivo XML (fecha en la que se exportaron los datos)
Importación de exámenes
Formato
<examen>
<tipoExamen></tipoExamen>
<diagnostico></diagnostico>
<diagnosticoPresuntivo>/diagnosticoPresuntivo>
<numeroBoleto></numeroBoleta>
<codigoReferencia></codigoReferenci>
fechaInicicoSint></fechaInicioSint>
<fechaTomaMuestra></fechaTomaMuestra>
<fechaIngresoMuestra></fechaIngresoMuestra>
<tipoResultado></tipoResultado>
<establecimiento></establecimiento>
<observaciones></observaciones>
<nombreInformante></nombreInformante>
Apellido1Informante></apellido1Informante>
Apellido2Informante></apellido2Informante>
<fechaRecepcionMuestra></fechaRecepcionMuestra>
<sistema></sistema>
<fechaExportacion></fechaExportacion
</examen>
Tabla 3: Definición de etiquetas de examen
Etiqueta | Tipo de dato | Es Requerido | descripción
tipoExamen | Texto | | Nombre del tipo de exámen
Diagnostico | Texto | | Código del diagnóstico
diagnosticoPresuntivo | Texto | | Codigo del diagnóstico presuntivo
numeroBoleta | Numérico | |
codigoReferencia | Numérico | |
fechaInicioSint | Fecha:dd/MM/aaaa | |
fechaTomaMuestra | Fecha:dd/MM/aaaa | |
fechaIngresoMuestra | Fecha:dd/MM/aaaa | |
tipoResultado | texto | Si los calores no corresponden con los indicados en la columna de descripción de almacena_ | NO_REALIZADO POSITIVO NEGATIVO PENDIENTE INADECUADO_
Estalecimiento | Texto | | Código del estabecimiento
observaciones | Texto | |
NombreInformante | Texto | | Nombre del informante 2 2 Si el nombre del informante y sus apellidos se insertan dentro de la etiqueta nombreInformante los datos se procesan de la siguiente forma: si hay dos palabras separadas por espacio se asume que la primera corresponde la nombre y la segunda al apellido, si hay tres palabras separadas por espacios se asume lo anterior y que la tercera corresponde al segundo apellido, si hay cuatro palabras separadas por espacio se asume que la primera corresponde al nombre, la penúltima al primer apellido y la última al segundo apellido.
Apellido1Informante | Texto | | Primer apellido del informante
Aéllido2Informante | Texto | | Segundo apellido del informante
fechaRecepcionMuestra | Fecha:dd/MM/aaaa | |
Sistema | Texto (15) | | Sistema del cual provienen el registro
fechaExportacion | Fecha: dd/MM/aaaa | | Fecha en la que generó el archivo XML (fecha en la que se exportaron los datos).
Importación de vacunas
Formato
<vacuna>
<tipoVacuna></tipoVacuna>
<nombreInformante></nombreInformante>
<apellido1Informante></apellido1Informante>
<apellido2Informante></apellido2Informante>
<aplicación></aplicación>
<dosis></dosis>
<establecimiento<</establecimiento>
<aplicada></aplicada>
<sistema></sistema>
<fechaExportación<>/fechaExportación>
</vacuna>
Etiqueta | Tipo de dato | Es Requerido | Descripción
lipovacuna | Texto (30) | X | Nombre completo del tipo de vacuna.
nombreInformante | Texto(90) | | Nombre del informante 3 3 Si el nombre del informante y sus apellidos se insertan dentro de la etiqueta nombreInformante los datos se procesan de la siguiente forma: si hay dos palabras separadas por espacio se asume que la primera corresponde la nombre y la segunda al apellido, si hay tres palabras separadas por espacios se asume lo anterior y que la tercera corresponde al segundo apellido, si hay cuatro palabras separadas por espacio se asume que la primera corresponde al nombre, la penúltima al primer apellido y la última al segundo apellido.
Apellido1Informante | Texto (30) | | Primer apellido del informante
Apellido2Informante | Texto (30) | | Segundo apellido del informante
Aplicación | Fecha: dd/MM/aaaa | X | Fecha en la que se aplicó la vacuna
Dosis | Texto. Si los valores no corresponden con los indicados en la columna de descripción se almacena_ | X | I_DOSIS II_DOSIS III_DOSIS I_REFUERZO II_REFUERZO I_ADICIONAL II_ADICIONAL_
Establecimiento | Texto | X | Código del establecimiento
Sistema | Texto (15) | X | Sistema del cual provienen el registro
fechaExportacion | Fecha: dd/MM/aaaa | X | Fecha en la que se generó el archivo XML (fecha en la que se exportaron los datos
