Anexo 8
PROTOCOLO DE SISTEMA DE INFORMACIÓN
Definición de la estructura de los archivos del módulo de importación de eventos y vacunas
Todos los archivos que importa el Sistema de Información de Vigilancia de Enfermedades Integrada (SIVEI) son de tipo
Extensible Markup Language (XML). A continuación se define la estructura de cada uno de los mismos según el tipo de evento.
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
[imagen]
[imagen]
[imagen]
[imagen]
La fase de importación de personas antecede a la importación de cualquier evento. Todos los eventos que se importan al SIVEI deben incluir el XML correspondiente a una persona.
Importación de casos
Formato
<caso>
<diagnostico> </diagnostico>
<nombreInformante> </nombreInformante>
<apellido1Informante> </apellido1Informante>
<apellido2Informante> </apellido2Informante>
<fecha></fecha>
<fechaInicioSint></fechaInicioSint>
<establecimiento></establecimiento>
<muestra> </muestra>
<fechaMuestra></fechaMuestra>
<cerrado> </cerrado>
<clasificacion> </clasificacion>
<observaciones></observaciones>
<sistema></sistema>
<fechaExportacion></fechaExportacion>
</caso>
Tabla 2: Definición de etiquetas de caso
[imagen]
[imagen]
1 Si el nombre del informante y sus apellidos se insertan dentro de la etiqueta nombre Informante los datos se procesan de la siguiente forma: si hay dos palabras separadas por espacio se asume que la primera corresponde al nombre y la segunda al apellido, si hay tres palabras separadas por espacio se asume lo anterior y que la tercera corresponde al segundo apellido, si hay cuatro palabras separadas por espacio se asume que la primera corresponde al nombre, la penúltima al primer apellido y la última al segundo apellido.
[imagen]
[imagen]
Importación de exámenes
Formato
<examen>
<tipoExamen></ tipoExamen >
<diagnostico> </diagnostico>
<diagnosticoPresuntivo> </diagnosticoPresuntivo>
<numeroBoleta></numeroBoleta>
<codigoReferencia></codigoReferencia>
<fechaInicioSint></fechaInicioSint>
<fechaTomaMuestra></fechaTomaMuestra>
<fechaIngresoMuestra></fechaIngresoMuestra>
<tipoResultado></tipoResultado>
<establecimiento></establecimiento>
<observaciones> </observaciones>
<nombreInformante> </nombreInformante>
<apellido1Informante> </apellido1Informante>
<apellido2Informante></apellido2Informante>
<fechaRecepcionMuestra></fechaRecepcionMuestra>
<sistema></sistema>
<fechaExportacion></fechaExportacion>
</examen>
Tabla 3: Definición de etiquetas de examen
[imagen]
[imagen]
2 Si el nombre del informante y sus apellidos se insertan dentro de la etiqueta nombre Informante los datos se procesan de la siguiente forma: si hay dos palabras separadas por espacio se asume que la primera corresponde al nombre y la segunda al apellido, si hay tres palabras separadas por espacio se asume lo anterior y que la tercera corresponde al segundo apellido, si hay cuatro palabras separadas por espacio se asume que la primera corresponde al nombre, la penúltima al primer apellido y la última al segundo apellido.
[imagen]
Importación de vacunas
Formato
<vacuna>
<tipoVacuna></tipoVacuna>
<nombreInformante> </nombreInformante>
<apellido1Informante> </apellido1Informante>
<apellido2Informante> </apellido2Informante>
<aplicacion></aplicacion>
<dosis></dosis>
<establecimiento></establecimiento>
<aplicada></aplicada>
<sistema></sistema>
<fechaExportacion></fechaExportacion>
</vacuna>
[imagen]
[imagen]
3 Si el nombre del informante y sus apellidos se insertan dentro de la etiqueta nombre Informante los datos se procesan de la siguiente forma: si hay dos palabras separadas por espacio se asume que la primera corresponde al nombre y la segunda al apellido, si hay tres palabras separadas por espacio se asume lo anterior y que la tercera corresponde al segundo apellido, si hay cuatro palabras separadas por espacio se asume que la primera corresponde al nombre, la penúltima al primer apellido y la última al segundo apellido.
[imagen]
[imagen]
