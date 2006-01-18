SUGEF-A-002. Superintendencia General de Entidades Financieras. Despacho del Superintendente General de Entidades Financieras, a las 11 horas del 6 de enero del 2006.
Considerando:
1. Que el Consejo Nacional de Supervisión del Sistema Financiero, mediante el artículo 14 de la sesión 547 del 5 de enero del 2006 aprobó el Reglamento sobre la Suficiencia Patrimonial de Entidades Financieras, Acuerdo SUGEF 3-06.
2. Que de conformidad con el artículo 4 del Reglamento sobre la Suficiencia Patrimonial de Entidades Financieras, Acuerdo SUGEF 3-06, le corresponde al Superintendente emitir los Lineamientos Generales.
3. Que para este efecto los Lineamientos Generales deben definir los aspectos necesarios para la aplicación del Reglamento 3-06 según lo establecido en esa normativa.
4. Que de conformidad con el Artículo 131, inciso b) de la Ley Orgánica del Banco Central de Costa Rica (Ley 7558) corresponde al Superintendente tomar las medidas necesarias para ejecutar los acuerdos del Consejo Nacional de Supervisión.
Por tanto dispone:
Emitir los “Lineamientos Generales para la Aplicación del Reglamento sobre la Suficiencia Patrimonial de Entidades Financieras, Acuerdo SUGEF 3-06”, según el siguiente texto:
ACUERDO DEL SUPERINTENDENTE
SUGEF-A-002
LINEAMIENTOS GENERALES PARA LA APLICACIÓN DEL REGLAMENTO SOBRE LA SUFICIENCIA PATRIMONIAL DE ENTIDADES FINANCIERAS, ACUERDO SUGEF-3-06
Objetivo general: Determinar la metodología de cálculo del Valor en Riesgo (VeR), la metodología para la homologación de las calificaciones otorgadas por agencias calificadoras autorizadas por la Superintendencia General de Valores (SUGEVAL), presentar las cuentas contables y datos adicionales utilizadas en el cálculo de la suficiencia patrimonial y las deducciones al resultado del periodo que por ley corresponde
I. METODOLOGÍA DE CÁLCULO DEL VALOR EN RIESGO
Objetivo: Presentar la metodología de cálculo de valor en Riesgo (VeR) con simulación histórica.
A. Datos requeridos:
a) La cantidad de cada emisión que forma parte de la cartera de inversiones sujeta al cálculo del VeR a la fecha de corte, definida la emisión según el código ISIN, y de no contar la emisión con este código, definida como aquélla con igual emisor, instrumento, moneda, fecha de vencimiento, premio y periodicidad. La cantidad en el caso de títulos de deuda, certificados de inversión, etc. es igual al monto facial, en el caso de acciones, participaciones de fondos de inversión, etc. es igual a la cantidad de acciones/ participaciones.
b) Vector de Precios para cada uno de los 521 días que intervienen en el cálculo del VeR (fuente: Bolsa Nacional de Valores (BNV), Bloomberg u otro servicio que permita acceder a la información de precios de las emisiones negociadas en mercados internacionales, que sean reconocidos por la SUGEVAL). No se consideran las emisiones para las cuales no existen cotizaciones.
c) Tipo de cambio del colón en la fecha de corte con respecto a cada una de las monedas extranjeras en que están denominadas las emisiones de la cartera.
B. Parámetros:
a) Número de observaciones: 500 observaciones diarias de la cartera.
b) Nivel de confianza: 95%. c) Periodo de tenencia: 21 días.
C. Método de cálculo:
1.Calcular las participaciones relativas de cada emisión de la cartera de inversionistas, de acuerdo con la siguiente fórmula:
W 1 = X 1
N
Σ X 1
(N)
Donde:
W 1 participación dentro de la cartera de la emisión i.
X 1 valor de mercado de la emisión I de la fecha de corte.
Para calcular el valor de mercado X 1 de una emisión denominada en una moneda diferente al colón costarricense, debe colonizarse su valor utilizando la siguiente fórmula:
ME
X1 = PI * TC *Q 1
Donde:
Q 1 = cantidad de participantes o acciones (instrumento de capital) o valor facial (instrumento de deuda) de la emisión i
ME
P I = precio de la emisión I en moneda extranjera.
TC = tipo de cambio de referencia para la compra según el Banco Central de Costa Rica para la fecha de corte, del colón con respecto a la moneda extranjera en la cual está denominada la emisión I.
Nota: Para calcular el tipo de cambio del colón con respecto a una moneda extranjera diferente al dólar estadounidense, se debe multiplicar el tipo de cambio de referencia para la compra del dólar estadounidense con el tipo de cambio del dólar estadounidense con respecto a la moneda extranjera en la cual está denominada la emisión I según el Banco Central de Costa Rica, todo para la fecha de corte. La unidad de Desarrollo debe tratarse como moneda extranjera para efectos de este cálculo.
2. Identificar la serie de precios para cada emisión que conforma la cartera de inversiones. Cuando una emisión no cuenta con una serie de precios completa para las 521 observaciones, se debe completar la serie con el primer precio de la serie.
3. Calcular la variación relativa a 21 días para cada emisión según la siguiente fórmula:
1 1
R = In ( P 1)
1 ( P 1-21
1
Donde:
1
R 1 = Rendimiento en tiempo continuo de la emisión I en el día t
1
P 1 = Precio de la emisión I en el día t
4. se calcula la variación relativa a 21 días de la cartera de inversión según la siguiente fórmula:
1 1
RC = Σ (W 1 * R 1)
Donde:
1
RC = rendimiento en tiempo continuo de la cartera el día t
El resultado en una serie de 500 observaciones de pérdidas y ganancias relativas a 21 días de la cartera de inversiones.
5. ordenar de mayor a menor los valores absolutos de la serie ( sin incluir el signo del rendimiento) obtenida en el punto anterior y se identifica el vigésimo sexto mayor valor (porcentual 95% )
6. El valor identificado del punto anterior se multiplique por el valor de mercado de la cartera de inversiones a la fecha de corte (igual al denominador utilizado en el punto 1). El resultado es igual al VeR a 21 días.
