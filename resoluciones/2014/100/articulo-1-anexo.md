Anexo 1: descripción de las variables requeridas para conformar la base de envió de la información estadística de la producción de energía eléctrica
Cons | Nombre de la variable | Nombre de la columna en la base de datos | Descripción/Observaciones | Tipo de dato en la base
1 | Nombre de la empresa que reporta | Empresa_reporta | Es el nombre de la empresa que reporta la información | Variable tipo Cadena restringida a los siguientes valores: ICE CNFL ESPH JASEC COOPELESCA COOPEGUANACASTE COOPESANTOS COOPELAFARORUIZ
2 | Nombre de la empresa que genera | Empresa_genera | Es el nombre de la empresa generadora | Variable abierta de tipo cadena
3 | Periodo: Año de la información | ano_cobro | Es el año al que refiere la información. | Numérica restringida a 4 espacios. Ej. 2013
4 | Periodo: Mes de la información | mes_cobro | Es el mes al que refiere la información. | Numérica restringida a 1 o 2 espacios, utilizando el código: 1-enero; 2-febrero;….; y 12-diciembre
5 | Nombre de la planta | Planta | Es el nombre de la planta eléctrica que genera | Variable abierta de tipo cadena
6 | Fuente de generación | Fuente | Se refiere al tipo de fuente de generación que utiliza la planta para transformar la energía eléctrica | Variable tipo Cadena restringida a los siguientes valores: Hidro Geotérmica Eólica Térmica Solar
7 | Capacidad instalada | Capacidad | Se refiere a la suma de la capacidad (en kW) indicada en la placa de cada uno de los generadores que conforman dicha planta | Variable numérica cuyos valores se muestran con el punto como delimitador decimal.
Nota: Esta base deben presentarla aquellas empresas distribuidoras que cuentan con plantas propias de generación eléctrica
| | | |
8 | Producción de energía eléctrica durante el periodo punta | Energía_punta |  Los datos (suministrados por el medidor de la planta) a registrar para unidades físicas de energía deben expresarse siempre en Kilowatt hora (kWh), las unidades físicas de potencia en Kilowatts (kW).  Se refiere a la producción eléctrica total del mes y año de referencia.  Definición de períodos:  Punta: Entre las 10:01 y las 12:30 horas, y las 17:31 y las 20:00 horas (5 horas diarias)  Valle: Entre las 6:01 y las 10:00 horas y entre las 12:31 y las 17:30 horas (9 horas).  Noche: Entre las 20:01 y las 6:00 horas del siguiente día. (10 horas diarias) | Variable numérica cuyos valores se muestran con el punto como delimitador decimal.
9 | Producción de energía eléctrica durante el periodo valle | Energía_valle
10 | Producción de energía eléctrica durante el periodo noche | Energía_noche
11 | Producción de potencia durante el periodo punta | Potencia_punta
12 | Producción de potencia durante el periodo valle | Potencia_valle
13 | Producción de potencia durante el periodo noche | Potencia_noche
14 | Fecha Carga Máxima | Fecha_ Máx | Fecha en que se produjo la carga máxima | Variable tipo fecha en formato: dd/mm/aaa
15 | Hora Carga Máxima | Hora Máxima | Hora del día en que se produjo la carga máxima | Variable hora con: hh:mm (en formato 24 hrs)
16 | Factor de carga | Factor_carga | Es el cociente entre la energía real generada por la planta o central eléctrica durante el periodo de referencia y la energía generada si hubiera trabajado a plena carga durante ese mismo período, conforme los valores nominales de planta identificados para los diferentes equipos. | Variable numérica en rango de 0 a 100
Variables de 17 al 27 son exclusivas para plantas de fuente térmica
17 | Consumo de combustible diésel | Consumo_diesel | • Se refiere al uso de los combustibles y lubricantes empleados exclusivamente para la generación de energía eléctrica durante el mes y año de referencia. • Los datos a registrar para consumo en unidades físicas deben expresarse siempre en litros. • Los datos a registrar para consumo en unidades monetarias deben expresarse siempre en colones • Las opciones de otro combustible se establece previendo el uso de un combustible para la generación térmica distinto a los establecidos (diésel, azufre y bajo azufre), a la fecha esta columna debe quedar como blanco. | Variable numérica cuyos valores se muestran con el punto como delimitador decimal.
18 | Consumo de combustible Bunker | Consumo_Bun
19 | Consumo de combustible Bunker de bajo azufre | Consumo_Bun_Az
20 | Consumo de otro combustible | Consumo_Otro
21 | Consumo de lubricantes | Consumo_lub
22 | Gasto en combustible diésel | Gasto_diesel
23 | Gasto en combustible Bunker | Gasto_Bun
24 | Gasto en combustible Bunker de bajo azufre | Gasto_Bun_Az
25 | Gasto en otro combustible | Gasto_Otro
26 | Gasto en lubricantes | Gasto_lub
27 | Tipo de cambio | tipo | Se refiere al tipo de cambio utilizado para transformar los importes en dólares u otras monedas a colones (acorde con la factura). Esta variable es estricta para aquellas tarifas establecidas en otras monedas distintas al colón, caso contrario se debe dejar en blanco. |
