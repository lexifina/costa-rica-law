ANEXO
FORMULARIO D-152
Declaración anual resumen de retenciones
Impuestos únicos y definitivos
INSTRUCTIVO PARA ELABORACIÓN DE ARCHIVO DIGITAL
Instrucciones generales:
1. La información solicitada debe ser suministrada en medio digital en un archivo de formato texto MS-DOS. con codificación ASCII y en disquete de 3'/2" o disco compacto.
2. El nombre del archivo debe ser D152AAAA, donde AAAA corresponde al período fiscal al que se refiera la información.
3. El archivo está con formado JX>r registros de dos tipos distintos: tipo 1 para la información del informador y tipo 2 para las líneas de detalle, ambos en un solo archivo.
4. El soporte magnético debe tener imprescindiblemente una etiqueta externa pegada en la que se hagan constar los datos del informador que se especifican a continuación:
Número de cédula del informador
Nombre o razón social del informador
Número total de registros tipo 2 del archivo
Fecha de entrega
Teléfono y nombre de la persona de contacto, para resolver posibles incidencias.
5. Si el archivo ocupa más de un disquete. deberá presentarse en formato backup, realizado mediante los comandos correspondientes del sistema operativo MS-DOS, Windows o WinZip, especificando el nombre del comando utilizado y la versión de sistema operativo.
Todos los disquetes llevarán una etiqueta numerada en forma consecutiva (1 /N, 2/N, etc., siendo N el número total de disquetes).
En el segundo y posteriores volúmenes solo será necesario consignar Tos datos cíe etiqueta de las letras a), b) y d) del punto 4.
6. Estructura del registro.
Registro tipo 1
Nombre del Campo Tipo de campo Tamaño Posición
Tipo de campo. Constante " 1" Numérico 1 1
Tipo de modelo. Contendrá
siempre "152". Numérico 3 2-4
Registro tipo 1 Tipo de campo Tamaño Posición
Nombre del Campo
Numero de documento. Numérico. 10 5-14
Corresponde a diez posiciones
de derecha a izquierda del número
del formulario de la hoja resumen
Administración Tributaria a que
pertenece el Declarante. Numérico 2 15-16
Ano (las cuatro posiciones del período
fiscal al que pertenece la información). Numérico 4 17-20
Numero de cédula del informador Numérico 12 21- 32
Sombre o Razón Social
Persona Jurídica Alfanumérico 80 33-112
Persona Física:
1° Apellido Alfanumérico 20 33-52
2° Apellido Alfanumérico 20 53-72
le Nombre Alfanumérico 20 73-92
2; Nombre Alfanumérico 20 93-112
Contendrá siempre ^L" (salarios
y demás pagos laborales) Alfa 2 113-114
Cantidad de retenidos Numérico 5 114-119
Total base retención alineado a
La derecha. Numérico 12 120-131
Total impuesto retenido alineado a
La derecha. Numérico 12 131-143
Contendrá siempre "IN" (intereses) Alfa 2 144-145
Cantidad de retenidos Numérico 5 146-150
Total base retención alineado a
La derecha. Numérico 12 151-162
Total impuesto retenido alineado a
La derecha. Numérico 12 163-174
Contendrá siempre "ROM (Operaciones
de recompras o reportes de valores) Alfa 2 175 - 176
Cantidad de retenidos Numérico 5 177-181
Total base de retención alineado a
la derecha Numérico 12 182 - 193
Total impuesto retenido alineado a
La derecha. Numérico 12 194-205
Contendrá siempre **DP" (Dividendos
y participaciones) Alfa 2 206 - 207
Cantidad de retenidos Numérico 5 208-212
Total base de retención alineado a
La derecha Numérico 12 213-224
Total impuesto retenido
La derecha. Numérico 12 225-236
Contendrá siempre "RE" (Remesas al
exterior no incluidas en las partidas
anteriores) Alfa 2 237-238
Cantidad de retenidos Numérico 5 239 - 243
Total base de retención alineado a
La derecha Numérico 12 244-255
Total impuesto retenido alineado a
La derecha. Numérico 12 256-267
Contendrá siempre "NE^ (Otras
retenciones no especificadas). Alfa 2 268-269
Cantidad de retenidos Numérico 5 270-274
Total base de retención alineado a
La derecha. Numérico 12 275-286
Total impuesto retenido alineado a
La derecha. Numérico 12 287-298
Contendrá siempre "TO" (Línea
de totales) Alfa 2 299-300
Cantidad total de retenidos Numérico 5 301 - 305
Base total de retenciones alineado a
La derecha Numérico 12 306-317
Monto total de impuesto retenido,
alineado a la derecha. Numérico 12 318-329
NOTAS:
La cédula de las personas Jurídicas deberá consignarse tal como aparece en el documento de cédula jurídica, completando las doce posiciones respectivas y omitiendo el uso de guiones u otro carácter no numérico, por ejemplo:'la cédula 3-101-153682-12 debe reportarse de la siguiente manera 310115368212. Los dos últimos dígitos son de control,
si no se conocen se deben omitir.
En el caso de las cédulas de personas físicas, éstas deberán consignarse tal como aparecen en el documento de cédula de identidad, omitiendo el uso de guiones o separadores especiales, tampoco se deben adicionar ceros entre los elementos que conforman la cédula. El registro deberá alinearse a la derecha, completando con ceros el resto del campo.
Por ejemplo; si se tiene la cédula de persona física 1-215-965 el campo debe completarse de la siguiente manera: 000001215965. Tratándose de cédulas de residentes permanentes, temporales o de extranjeros deberá comunicarse a la Administración Tributaria de su jurisdicción para solicitar las instrucciones respectivas.
Se han reservado 80 posiciones para el campo de nombre o razón social, tratándose de personas jurídicas el nombre deberá alinearse a la derecha, dejando vacíos los campos que resten en caso de no ocupar las 80 posiciones reservadas. Si se trata de personas físicas los datos de nombre y apellidos deberán indicarse de acuerdo a la estructura solicitada, es decir
ubicando cada uno de los apellidos v el nombre en los bloques correspondientes, alineando los mismo a la derecha y dejando vacías las columnas no utilizados.
El campo de fecha de actualización de datos deberá conformarse de la siguiente manera: las dos primeras posiciones para el día, las dos siguientes para el mes y las cuatro restantes para el año, por ejemplo, la fecha 28 de mayo de 2001, deberá consignarse como sigue: 28052001.
Registro tipo 2
Nombre del Campo Tipo de Campo Tamaño Posición
Tipo de campo. Constante "2" Numérico 1 1
Tipo de modelo. Constante "152" Numérico 3 2-4
Año. (Cuatro posiciones del año al
que corresponde la información) Numérico 4 5-8
Número de cédula Numérico 12 9-20
Nombre o Razón Social
Persona Jurídica Alfanumérico 80 21-100
Persona Física:
l°Apellido Alfanumérico 20 21-40
2° Apellido Alfanumérico 20 41-60
1° Nombre Alfanumérico 20 61-80
2° Nombre Alfanumérico 20 81-100
Base de retención (alineado a
La derecha) Numérico 12 101-112
Impuesto retenido (alineado a
La derecha) Numérico 12 113-124
Tipo de retención Alfanumérico 2 125 - 126
NOTAS:
Todos los campos deberán alinearse a la derecha, completando con
tanto ceros a la izquierda como sea necesario.
Las observaciones respecto a los campos de cédula y nombre o razón social indicadas para el registro tipo 1 son válidas para el registro
tipo 2.
Los números de cédula pueden ser verificados por medio del Sistema SIC, "Sistema de Información de Contribuyentes que se distribuye gratuitamente en todas las Administraciones Tributarias.
Publíquese.—Dr. Adrián Torrealba Navas, Director General.—1
vez.—(Solicitud No 04308).—C-57420.—<85520).
