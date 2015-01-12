Anexo 3: descripción de las variables requeridas para conformar la base de envió de la información estadística del gasto en compras de energía, potencia y transmisión.
Cons | Nombre de la variable | Nombre dela Columna en la Base de datos | Descripción/ Observaciones | Tipo de dato en la base
1 | Nombre de la empresa que reporta | Empresa_reporta | Es el nombre de la empresa que reporta la información | Variable tipo Cadena restringida a los siguientes valores: ICE CNFL ESPH JASEC COOPELESCA COOPEGUANACASTE COOPESANTOS COOPELAFARORUIZ CONELÉCTRICAS
2 | Nombre de la empresa que vende | Empresa_vende | Es el nombre de la planta eléctrica o empresa que vende la energía, potencia o transmisión | Variable abierta de tipo cadena
3 | Periodo: Año de la información | ano_cobro | Es el año al que refiere la información. | Numérica restringida a 4 espacios. Ej. 2013
4 | Periodo: Mes de la información | mes_cobro | Es el mes al que refiere la información. | Numérica restringida a 1 o 2 espacios, utilizando el código: 1- enero; 2-febrero;….; y 12-diciembre
5 | energía recibida durante el periodo punta | ene_punta | • Los datos a registrar para unidades físicas de energía deben expresarse siempre en Kilowatt hora (kWh). • Se refiere a la energía eléctrica total recibida, por parte de la empresa vendedora, durante el mes y año de referencia. | Variable numérica cuyos valores se muestran con el punto como delimitador decimal.
6 | energía recibida durante el periodo valle | ene_valle
7 | energía recibida durante el periodo noche | ene_noche
Nota: Esta base deben presentarla aquellas empresas distribuidoras que realizan transferencias de energía y potencia eléctrica con otros sistemas de generación o transmisión.
Cons | Nombre de la variable | Nombre de la columna en la base de datos | Descripción/Observaciones | Tipo de dato en la base
8 | Demanda máxima durante el periodo punta | pot_punta | Los datos a registrar para unidades físicas de demanda de potencia en Kilowatt (KW). Las compras de potencia en KW se refieren al promedio más alto en Kilovatios para cualquier intervalo de quince minutos, para los periodos punta, valle y noche | Variable numérica cuyos valores se muestran con el punto como delimitador decimal.
9 | Demanda máxima durante el periodo valle | pot_valle | |
10 | Demanda máxima durante el periodo Nocturno | pot_noct | |
11 | Energía trasegada | Ene_peaje | Se refiere al valor facturado por concepto de la energía trasegada por la red de transmisión (en KWh) (cuando vendedor sea el ICE) |
12 | Tipo de cambio | tipo | Se refiere al tipo de cambio utilizado para transformar los importes en dólares u otras monedas a colones (acorde con la factura) |
13 | Importe por energía durante el periodo punta | imp_kwh_punta | Se refiere al importe respectivo por el homólogo del consumo. Utilizar el valor en colones. En el caso de tarifas en dólares u otra moneda, realizar la transformación a colones y reportar en la variable "tipo de cambio" el valor de cambio empleado. Este monto debe incluir el cargo variable por combustible (caso que vendedor sea ICE- Generación) |
14 | Importe por energía durante el periodo valle | imp_kwh_valle | |
15 | Importe por energía durante el periodo Nocturno | imp_kwh_noct | |
16 | Importe por potencia durante el periodo punta | imp_kw_punta | |
17 | Importe por potencia durante el periodo valle | imp_kw_valle | |
18 | Importe por potencia durante el periodo Nocturno | imp_kw_noct | |
19 | Importe por Energía trasegada | Imp_peaje | |
20 | Importe por ajustes | Imp_ajustes | Se refiere a cualquier otro importe adicional a los conceptos de energía, potencia y transmisión, pero que se incorporan dentro de la factura. (penalizaciones, indemnizaciones, etc.). No deben considerarse impuestos. |
21 | Importe total | Imp_total | Es el importe total por la entrega del servicio. Resulta de la sumatoria del importe de la energía, potencia, peaje y ajustes, Este monto debe incluir el cargo variable por combustible (caso que vendedor sea ICE-Generación) |
22 | Importe por costo variable de combustible | Costo_CVC | Cuando la empresa que vende es el ICE- Generación. Se refiere al importe por concepto del cargo variable por combustible |
