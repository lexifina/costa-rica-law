ANEXO 3
Estructura de Archivo Comunicación de Afiliaciones
Origen : SICERE / Destino : Entidades Autorizadas
Periodicidad: Diaria (Lunes a Viernes) - Tipo de Transferencia : Depósito automático en el FTP de la CCSS
Nombre: scraXX_afil_YYYYMMDDHHMISS.lzh (Donde XX corresponde al Código de la Entidad Destino)
POSICIÓN | NOMBRE CAMPO | DESCRIPCIÓN | TIPO | LONGITUD (MÁXIMA)
1 | Tip_Movimiento | Indicador del tipo de afiliación (N=Nueva Afiliación Voluntaria, A=Nueva Afiliación Automática, T=Libre Transferencia, J=Ajuste de Afiliación, P=Corrección dato erróneo, O=Cambio de Comisión, F=Fusión y Q=Cierre de Operadora) | Carácter | 1
2 | Cod_Entidad_Destino | Código de Entidad Destino | Alfanumérico | 3
3 | Tip_Fondo | Tipo de Fondo (FCL = L, ROP = P) | Alfabético | 1
4 | Fec_Generación | Fecha de generación del archivo | Fecha (Formato AAAAMMDD) | 8
5 | Num_Formulario_Destino | Número de formulario | Alfanumérico | 30
6 | Tip_Identificación_Destino | Tipo de Identificación Destino | Numérico | 1
7 | Num_Identificacion_Destino | Número Identificación Destino | Numérico | 25
8 | Nom_Nombre_Destino | Nombre Persona | Alfanumérico | 60
9 | Nom_Apellido1_Destino | Primer Apellido de la Persona | Alfanumérico | 40
10 | Nom_Apellido2_Destino | Segundo Apellido de la Persona | Alfanumérico | 40
11 | Num_Seguro | Número se Seguro Social Identificación Destino | Numérico | 25
12 | Cod_Pais | Código del país | Numérico | 3
13 | Cod_Sexo | Código de Género de la Persona | Alfabético | 1
14 | Fec_Nacimiento | Fecha de Nacimiento | Fecha (Formato DD/MM/AAAA) | 10
15 | Num_Telefono_Res | Teléfono residencial | Numérico | 10
16 | Cod_Provincia | Provincia | Numérico | 3
17 | Cod_Cantón | Cantón | Numérico | 3
18 | Cod_Distrito | Distrito | Numérico | 3
19 | Dir_Correspondencia | Dirección de correspondencia. | Alfanumérico | 70
20 | Apartado_Postal | Apartado Postal | Alfanumérico | 15
21 | Num_Fax | Número de Fax | Numérico | 10
22 | Dir_Electronica | Dirección de Correo Electrónico (E-mail) | Alfanumérico | 70
23 | Cod_Estado_Civil | Código de Estado Civil | Alfanumérico | 1
24 | Cod_Promotor | Número de Credencial del Promotor (Solo se informa en transacciones realizadas por un promotor de Operadora de Pensiones) | Numérico | 9
POSICIÓN | NOMBRE CAMPO | DESCRIPCIÓN | TIPO | LONGITUD (MÁXIMA)
25 | Fec_Formulario | Fecha del Formulario de afiliación | Fecha (Formato DD/MM/AAAA) | 10
26 | Cod_Entidad_Origen | Entidad de afiliación Origen (Solo se informa en transacciones de movimientos de afiliación) | Alfanumérico | 3
27 | Tip_Identificación_Origen | Tipo de Identificación Origen (Solo se informa en transacciones de movimientos de afiliación) | Numérico | 1
28 | Num_Identificacion_Origen | Número de Identificación Origen (Solo se informa en transacciones de movimientos de afiliación) | Numérico | 25
Todos los campos se encuentra separados por un pipe-line (‘|’)
