10. Esta normativa entrará en vigencia a partir del mes de julio del presente año, antes de ello continuará rigiendo el acuerdo SUGEF 20-99.
PROCEDIMIENTO PARA EL CÁLCULO DEL CALCE DE PLAZO A UNO Y TRES MESES AJUSTADOS POR LA VOLATILIDAD
Este procedimiento consiste en ajustar en el calce de plazos las obligaciones a la vista con el público que desde el punto de vista contractual no tienen restricciones para su retiro. La herramienta evalúa la liquidez a través del "Índice de calce de plazos a un mes" y el "Índice de calce de plazo a tres meses". El procedimiento que se propone para la medición de ambos indicadores se detalla a continuación:
1) Se utiliza la información del calce de plazos acumulado a uno y tres meses, para lo cual se realizan los siguientes ajustes:
a) En el numerador que contempla la recuperación de activos, se sensibilizan las descoberturas con las inversiones temporales y permanentes no comprometidas que mantienen los supervisados en el Gobierno y en el Banco Central de Costa Rica, por cuanto este tipo de recursos son de alta liquidez en el mercado.
b) En la parte del denominador, se ajustan las captaciones a la vista con el público, las cuales no tienen un plazo contractual de vencimiento y por consiguiente pueden ser retiradas en cualquier momento por los inversionistas. Para lo anterior, se analiza la información para cada supervisado y se determina el retiro máximo realizado en una serie de tiempo dada (12 meses). El detalle de la metodología utilizada se indica a continuación:
1) Se confeccionará una serie de datos para la cuenta 21101 Cuentas Corrientes y otra serie de datos para la cuenta 21103 Depósitos de Ahorro a la Vista. Dichas series de datos contendrán información histórica mensual para los últimos doce meses.
2) Con la información establecida en el aparte anterior, se obtendrá la tasa de crecimiento mensual y trimestral, que consiste en calcular el logaritmo natural para la serie de datos en forma mensual para el indicador a un mes plazo y en forma trimestral para el segundo indicador. A continuación se detalla la fórmula:
Para el calce de plazo un mes plazo es:
Log (xt / x (t-1))
donde:
xt = el saldo de la cuenta de estudio en el mes t.
xt-1 = el saldo de la cuenta de estudio en el mes anterior a t.
Ejemplo:
Si x5 = mayo entonces x5-1 = x4 = abril
Para el calce de plazo a tres meses plazo es:
Log (xt / x (t-3))
donde:
xt = el saldo de la cuenta de estudio en el mes t.
xt-3 = el saldo de la cuenta de estudio del trimestre anterior al mes t.
Ejemplo:
Si xt = abril entonces xt-3 = x4-3 = enero
3) Una vez obtenida las nuevas series de datos, se determina la variabilidad de la serie, la cual consiste en calcular la variancia para ambas series. La fórmula utilizada se describe a continuación:
S2 = S ( xi - x )2 / n-1
4) A la variancia se le calcula su raíz cuadrada, con lo cual se obtiene la desviación estándar, conocida como "La Volatilidad".
5) Para obtener la fluctuación máxima se trabajará con un nivel de confianza del 99%, es decir con una Z = 2.33, la cual se obtiene el valor en la tabla de la distribución normal estándar de probabilidad. Una vez obtenido este valor se procede a multiplicar la volatilidad obtenida en el punto anterior por el 2.33.
6) El porcentaje obtenido se utilizará para establecer la caída máxima potencial de las cuentas corrientes y depósitos a la vista de cada supervisado.
A un mes:
Saldo cuenta 21101 * fluctuación máxima esperada a un mes
Saldo cuenta 21103 * fluctuación máxima esperada a un mes
A tres meses:
Saldo cuenta 21101 * fluctuación máxima esperada a tres meses
Saldo cuenta 21103 * fluctuación máxima esperada a un mes
7) Una vez obtenido el monto correspondiente a la caída máxima potencial a un mes y a tres meses para cada supervisado, se procede a ajustar los índices de calce a uno y tres meses, de la siguiente forma:
Calce a un mes:
Numerador
Del calce de plazos: (Ver capítulo 7 del manual de información del sistema financiero)
C 12110 N 1 + C 12110 N 2 +
C 12210 N 1 + C 12210 N 2
Más
Del reporte de datos adicionales *:
Inversiones temporales no comprometidas del BCCR y sector público con vencimiento superior a un mes
+ Inversiones permanentes no comprometidas del BCCR y sector público
Denominador
Del vaciado de cuentas:
( Saldo cuenta 21101 * fluctuación máxima esperada a un mes ) +
( saldo cuenta 21103 * fluctuación máxima esperada a un mes) +
Saldo cuenta 211 - saldo cuenta 21101 - saldo cuenta 21103 + saldo cuenta 212
Más los siguientes valores que se toman del calce de plazos:
C 12120 N 1 - C 12121 N 1 + C 12120 N 2 +
C 12220 N 1 - C 12221 N 1 + C 12220 N 2
Calce a 3 meses:
Numerador
Del calce de plazos: (Ver capítulo 7 del manual de información del sistema financiero)
C 12110 N 1 + C 12110 N 2 + C 12110 N 3 + C 12110 N 4 +
C 12210 N 1 + C 12210 N 2 + C 12210 N 3 + C 12210 N 4
Más
Del reporte de datos adicionales *:
Inversiones temporales no comprometidas del BCCR y sector público con vencimiento superior a 3 meses
+ Inversiones permanentes no comprometidas del BCCR y sector público
Denominador
Del vaciado de cuentas:
( Saldo cuenta 21101 * fluctuación máxima esperada a tres meses) +
( saldo cuenta 21103 * fluctuación máxima esperada a tres meses) +
Saldo cuenta 211 - saldo cuenta 21101 - saldo cuenta 21103 + saldo cuenta 212
Más los siguientes valores que se toman del calce de plazos:
C 12120 N 1 - C 12121 N 1 + C 12120 N 2 + C 12120 N 3 + C 12120 N 4 +
C 12220 N 1 - C 12221 N 1 + C 12220 N 2 + C 12220 N 3 + C 12220 N 4
8) Otras consideraciones:
a) Los meses en que los saldos de las cuentas objeto de estudio de volatilidad sean cero, para efectos del cálculo de los logaritmos naturales, asumirán un valor de uno.
b) Cuando dos o más entidades fiscalizadas se fusionen, el análisis de la volatilidad se efectuará como si la fusión hubiese ocurrido doce meses atrás, es decir se sumarán los saldos de las cuentas respectivas de los fiscalizados durante los meses precedentes a la fusión, y hasta completar una serie de doce meses.
c) Cuando una entidad inicie operaciones, para efectos del cálculo de volatilidad, se considerará que en los meses que anteceden al del primer reporte financiero, las respectivas cuentas asumen saldos de uno, hasta completar una serie de doce meses.
DETALLE DEL CÁLCULO DEL INDICADOR DE RIESGO CAMBIARIO
Fórmula: [(Valor absoluto de: Activos en moneda extranjera-pasivos en moneda extranjera) / Tipo de cambio de compra] * (Variación máxima esperada en el tipo de cambio para un año) / [Capital primario + capital secundario (hasta una suma que no exceda el capital primario)].
Activos en moneda extranjera: De los saldos del plan de cuentas: sumatoria de todas las partidas de activo que tienen como sexto dígito un 2 (No considerar las cuentas 129012, 139012, 139022, 139032, 139042, 149012, 159012, 169012).
Pasivos en moneda extranjera: De los saldos del plan de cuentas: sumatoria de todas las partidas de pasivo que tienen como sexto dígito un 2.
Variación esperada en el tipo de cambio: La variación máxima esperada del tipo de cambio será calculada siguiendo un procedimiento similar al cálculo de la volatilidad utilizado para los índices de calce de plazos.
· Se calculan los crecimientos interanuales del tipo de cambio de compra para los últimos doce meses. Se toman los valores del último día del mes. Por crecimiento interanual se entiende el logaritmo natural resultante del tipo de cambio del último día de un determinado mes sobre el tipo de cambio del último día para ese mes del año anterior.
· Se calcula la variancia de los crecimientos interanuales. Al valor obtenido se le calcula la raíz cuadrada.
· Al resultado del punto anterior se le aplica un nivel de confianza de 99% por lo cual es multiplicado por 2.33 veces.
· La variación absoluta esperada en el tipo de cambio es el producto del coeficiente obtenido en el punto anterior multiplicado por el tipo de cambio de compra del último día del mes.
DETALLE DEL CÁLCULO DEL INDICADOR DE RIESGO
POR TASAS DE INTERÉS
El indicador de riesgo por tasas de interés se calcula con la siguiente fórmula:
Valor absoluto de [Duración de activos sensibles a tasas menos (duración de pasivos sensibles a tasas * Pasivos sensibles a tasas / activos sensibles a tasas)]
Lo anterior debe ser dividido por
(1 + tasa básica pasiva a 6 meses plazo)
El resultado obtenido se debe de multiplicar por
Cambio máximo esperado en un año en la tasa básica pasiva
a. Las duraciones se calculan a partir del "Reporte de activos y pasivos sensibles a tasas". Este reporte se encontrará en el manual de información. Para efectos de facilitar la compresión del cálculo del indicador se desarrolla un ejemplo:
Rubro \ Plazo
0 - 30 días
31-90
91-180
181-360
361-720
Más de 720
Total
Activos Sensibles a tasas
1,200
2,500
4,700
5,100
4,000
600
18,100
Pasivos
Sensibles a tasas
1,900
2,800
4,000
4,100
3,000
100
15,900
Donde:
Plazo en días
Conversión a Meses
0-30 días
1 mes
31-90 días
3 meses
91-180 días
6 meses
181-360 días
12 meses
361-720 días
24 meses
Más de 720 días
48 meses
b. Con el fin de ajustar los datos, los diferentes plazos deben ser traídos a valor presente. Para lo anterior, se utiliza la fórmula [Dato/ (1+i/12)n ], donde i es la tasa básica pasiva y n son los meses según la banda de tiempo utilizada. Para efectos del ejemplo se utilizará una tasa del 20% anual.
Rubro \ Plazo
1 mes
3 meses
6 meses
12 meses
24 meses
48 meses
Total
Activos
1,180
2,379
4,256
4,183
2,691
271
14,961
Pasivos
1,869
2,665
3,622
3,363
2,018
45
13,582
c. Se calcula el peso relativo que tienen los valores obtenidos en la tabla anterior con respecto al total de dichos valores y se expresa en años, a saber: activo o pasivos sensible a tasas por banda / activo o pasivo total sensible a tasas de todas las bandas * plazo en meses / 12. Lo anterior permite determinar la duración promedio por banda de tiempo para los activos y pasivos.
Rubro \ Plazo
1 mes
3 meses
6 meses
12 meses
24 meses
48 meses
Total
Activos
0.006575
0.039756
0.142254
0.279584
0.359685
0.072582
0.900440
Pasivos
0.011467
0.049047
0.133359
0.247583
0.297153
0.013325
0.751930
d. Una vez obtenido el valor absoluto de la duración, que es la mostrada en la columna de total del cuadro anterior, se aplica la siguiente fórmula: Duración activos - (duración pasivos * (pasivos descontados / activos descontados). En el ejemplo el resultado es 0.21781.
e. También se necesita obtener la variación esperada en la tasa de interés de referencia (Tasa Básica Pasiva). Para lo anterior se requiere obtener la volatilidad de la tasa básica para los últimos 12 meses, según la misma metodología explicada para el elemento de Liquidez. Dicha volatilidad que representa Variación Máxima para el período de tiempo dado, debe de multiplicarse por la tasa básica a la fecha corte, lo que da como resultado el efecto esperado en la tasa y el riesgo que ello deriva para el supervisado. Para mayor detalle se adjunta el siguiente ejemplo:
Mes
Tasa
Logaritmo natural
1
17.10
2
17.30
0.011628038
3
18.00
0.039665256
4
19.00
0.054067221
5
18.20
-0.043017385
6
19.50
0.068992871
7
19.00
-0.025975486
8
20.00
0.051293294
9
21.00
0.048790164
10
21.20
0.009478744
11
20.70
-0.023867481
12 (mes corte)
20.00
-0.034401427
Variancia
0.001654054
Variancia anualizada
0.019848651
Desviación estándar
0.140885241
Volatilidad con nivel de confianza de 99%
Z=2.33
0.328262612
Variación esperada
6.57
f. Se calcula el índice de riesgo por tasas de mercado. Con los datos del ejemplo el resultado es:
0.21781 / (1 + 0.20 ) * 6.57 = 1.19%
Nomenclatura de Datos Adicionales
Utilizados en el cálculo de los indicadores
CODIGO DETALLE
20001
Cartera de créditos al día y con atraso hasta 90 días [3]
20002
Cartera de créditos con atraso mayor a 90 días
20003
Cartera de créditos a grupos de interés vinculados
20004
Cartera de créditos a grupos de interés no vinculados
20005
Pérdida estimada sobre la cartera de créditos total
20006
Pérdida estimada del activo total
20007
Cartera tipo A y B tomada del informe de clasificación de la cartera según SUGEF-1-95
20014
Número de empleados
20015
Total de cartera tomada del informe de clasificación de la cartera según SUGEF-1-95
20016
Créditos específicos para la actividad de vivienda con garantía hipotecaria
20017
Obligaciones por cartas de crédito emitidas sin costo financiero
20018
Obligaciones por otras aceptaciones sin costo financiero
20019
Obligaciones por pactos de recompra de títulos sin costo financiero
20020
Obligaciones por compras a futuro de divisas sin costo financiero
20021
Obligaciones por ventas a futuro de divisas sin costo financiero
20022
Otras obligaciones con entidades financieras a plazo sin costo financiero
20023
Créditos garantizados con inversiones en el Banco Central de Costa Rica y títulos valores del sector público
20024
Número de asociados inactivos
20025
Porcentaje de excedentes netos para ser capitalizados
20026
Número de asociados activos
20027
Inversiones temporales no comprometidas del BCCR y sector público con vencimiento superior a un mes
20028
Inversiones temporales no comprometidas del BCCR y sector público con vencimiento superior a tres meses
20029
Inversiones permanentes no comprometidas del BCCR y sector público
20033
Saldo de los recursos de terceros administrados por el banco o entidad financiera por vía de contratos de fideicomiso que sean similares a los fondos de inversión
20034
Inversiones temporales en títulos valores de gobiernos o bancos centrales de países miembros del Grupo de los Siete
20035
Inversiones permanentes en títulos valores de gobiernos o bancos centrales de países miembros del Grupo de los Siete
20036
Estimaciones creadas para productos por cobrar por inversiones temporales (cuenta 128), participaciones en otras empresas (cuenta 166), otras inversiones permanentes (cuenta 16701) o productos por cobrar por inversiones permanentes (cuenta 168)
20037
Otras captaciones a la vista sin costo financiero
20038
Saldo de los recursos de terceros administrados por el banco o entidad financiera por vía de los contratos de fideicomiso provenientes de Procesos de Titularización
20039
Préstamos para la Banco Estatal que cumplen con lo señalado en el Artículo 59 inciso 1) de la Ley 1644
20040
Préstamos garantizados con títulos emitidos por la misma entidad que cumplen con lo dispuesto en el Artículo 4 c) de las Normas para establecer la Suficiencia Patrimonial de las Asociaciones Mutualistas de Ahorro y Préstamo para la Vivienda (Acuerdo SUGEF 26)
20041
Monto de las obligaciones subordinadas integradas al patrimonio no redimible de acuerdo con nota 1 del Anexo del Acuerdo SUGEF 25
Acuerdo SUGEF-26-00
--------------------------------------------------------------------------------
[1] El grupo de los siete está conformado por Estados Unidos, Canadá, Japón, Italia, Alemania, Gran Bretaña y Francia.
[2] Modificado según el "Reglamento para la regulación y supervisión de los fondos administrados mediante contratos de fideicomiso que sean similares a los fondos de inversión, planes de capitalización o fondos de pensión" aprobado por el CONASSIF mediante Artículo 11, del Acta de la Sesión 130-2000, celebrada el 4 de enero del 2000.
[3] Se calcula con el criterio de morosidad legal.
