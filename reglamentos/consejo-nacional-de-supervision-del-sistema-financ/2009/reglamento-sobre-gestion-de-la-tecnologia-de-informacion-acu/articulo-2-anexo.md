ANEXO 2
PROCEDIMIENTO PARA OBTENER LA CALIFICACIÓN
SOBRE LA GESTIÓN DE TI
El procedimiento para obtener la calificación sobre la gestión de TI, consta de cuatro pasos: (1) calificación del cumplimiento de los objetivos de control asociados a cada proceso, (2) Calificación del nivel de madurez alcanzado por cada proceso, (3) determinación de la calificación para cada proceso y (4) Calificación ponderada de la Gestión de TI.
[imagen]
Para los efectos, la metodología se expondrá a lo largo de este anexo mediante un ejemplo.
Planteamiento del ejemplo:
La evaluación de la gestión de TI considera cada uno de los dominios del marco Cobit®; a través del cumplimiento de los objetivos de control y el nivel de madurez, para un número específico de procesos contenidos en el maco para la gestión de TI.
El desarrollo de los cálculos se efectúa únicamente para el proceso denominado “Proceso A” del dominio Monitoreo y Evaluación; para los procesos B, C y D se asumen calificaciones que luego se integran en el paso 4 al cálculo de la Calificación ponderada de la Gestión de TI.
Dominio | Proceso | Calificación del proceso supuesta
Planeación y Organización | B | 50%
Adquisición e implementación | C | 80%
Entrega y soporte | D | 65%
A. Calificación del proceso evaluado.
Factor 1: Calificación del cumplimiento de los objetivos de control asociados a cada proceso. (PASO 1)
1. Mediante la “Matriz de Calificación de la Gestión de TI” se determina el nivel de cumplimiento de cada objetivo de control asociado a un proceso en particular.
2. La “Matriz de Calificación de la Gestión de TI” establece un conjunto de preguntas de respuesta cerrada, asociado a cada objetivo de control; según corresponda se asigna alguna de las siguientes respuestas:
Respuesta | Descripción
SI | La entidad cumple con lo requerido para el objetivo de control evaluado
NO | La entidad no cumple con lo requerido para el objetivo de control evaluado
NA | El objetivo de control no aplica. Este resultado debe observarse como un caso excepcional
Para el ejemplo, la siguiente imagen muestra la forma en que se presenta la calificación para cada objetivo de control que compone el “Proceso A”.
[imagen]
3. La Calificación de cada Objetivo de Control (COC) se obtiene a partir de la siguiente formulación:
COC= (Total de respuestas en SI / Total de preguntas aplicables del Objetivo de Control evaluado) * 100
En nuestro ejemplo, para el objetivo de control 1.3, la calificación es 75%, determinada como (3/4)*100
La calificación total para el factor 1 se obtiene a partir de la siguiente formulación:
Σ COC / (100 * número de objetivos de control evaluados)
Para el ejemplo, 275% / 100 * 3 = 0.9166, donde:
275% = sumatoria de las calificaciones individuales de cada objetivo de control
3 = número de objetivos de control evaluados
Factor 2: Nivel de madurez alcanzado en cada proceso (PASO 2)
1. Mediante la “Matriz de Calificación de la Gestión de TI” se determina el nivel de madurez alcanzado en un proceso en particular.
2. La “Matriz de Calificación de la Gestión de TI” establece un conjunto de preguntas de respuesta cerrada, asociado a cada proceso. Las preguntas se formulan atendiendo a un nivel de exigencia creciente, de manera que para ascender en la escala, es requisito cumplir con la totalidad de las exigencias del nivel precedente.
3. Las respuestas en la “Matriz de Calificación de la Gestión de TI” deben corresponder a alguno de los siguientes estados:
Respuesta | Descripción
SI | La entidad cumple con lo requerido para el nivel de madurez evaluado
NO | La entidad no cumple con lo requerido para el nivel de madurez evaluado
NA | El ítem no aplica. Este resultado debe observarse como un caso excepcional
4. La calificación para cada Nivel de Madurez (CNM) se obtiene a partir de la siguiente formulación:
CNM = Total de respuestas en SI / Total de preguntas del Nivel de madurez evaluado
5. La asignación del nivel de madurez se inicia en el Nivel 1, para ascender en la escala es requisito indispensable cumplir con la totalidad de las exigencias del nivel inmediato precedente (CNM = 1). Se procede a sumar de forma ascendente en la escala los resultados del CNM = 1, deteniéndose en el nivel con un valor CNM diferente a 1.
Se muestra en la siguiente imagen la forma en que se determina la calificación del nivel de madurez para el “Proceso A” del ejemplo.
[imagen]
6. La calificación obtenida según el procedimiento indicado en el punto anterior para el nivel de madurez, debe ubicarse en el rango de valor que corresponda, según el cuadro siguiente:
Rango | Nivel | Descripción
De 0 a 0.99 | 0 | No existente
De 1 a 1.99 | 1 | Inicial
De 2 a 2.99 | 2 | Repetible
De 3 a 3.99 | 3 | Definido
De 4 a 4.99 | 4 | Administrado
Igual a 5 | 5 | Optimizado
En el ejemplo, una calificación de 2.67 corresponde el Nivel 2 “Repetible”, para una desviación respecto al nivel de madurez requerido (Nivel 3) de -0.33
7. La calificación total para el factor 2 se obtiene a partir de la siguiente formulación:
CNM *100 / (100 * Nivel Requerido)
Para el ejemplo, 2.67*100 / 100 * 3 = 0.89, donde:
2.67 = CNM
3 = Nivel de madurez requerido
Factor 3: Calificación de cada Proceso evaluado (PASO 3)
La Calificación de cada Proceso evaluado (CP) se establece mediante la suma del producto de cada uno de los factores por su peso, según la siguiente formulación:
CP = Factor 1 * peso factor 1 + Factor 2 * peso factor 2
En donde el peso de los factores es:
Factor | Dimensión | Peso
1 | Resultado de la calificación del Objetivos de Control (COC) | 70%
2 | Resultado de la calificación del Nivel de Madurez (CNM) | 30%
Para el ejemplo, corresponden los siguientes resultados:
Factor | Dimensión | Peso | Resultado
1 | COC = 0.92 | 70% | 0.6416
2 | CNM = 0.89 | 30% | 0.267
| | Suma | 0.9086
La calificación del “Proceso A” es 90.86%.
B. Calificación de la gestión de TI (paso 4)
1. Una vez establecida la calificación para cada uno de los procesos incluidos en la evaluación del marco para la gestión de TI, se procede a establecer la Calificación sobre la Gestión de TI (CGTI); la cual se obtiene mediante la suma de las calificaciones ponderadas de los procesos evaluados.
La calificación se obtiene mediante la siguiente formulación:
CGTI = Σ (CP ponderada)
Donde CP ponderada, se obtiene al multiplicar cada CP por el peso asignado al proceso y luego dividirlo entre el total de los pesos.
Para expresar la calificación final se utilizarán dos dígitos decimales sin redondeo.
Para el ejemplo, la CP ponderada del “Proceso A” es 22.71% como resultado de (90.86% * 3) /12.
La imagen muestra el cálculo y resultado final para el ejemplo:
[imagen]
2. El peso asignado (ponderador) lo determina la SUGEF, considerando la importancia relativa del proceso en virtud del dominio al que pertenece y de su eventual impacto en los procesos de negocio. La siguiente tabla presenta los valores asignables:
| | Impacto a procesos de negocio
| PESO | Alto | Medio | Bajo
Importancia relativa | Primario | 3 | 3 | 2
Secundario | 3 | 2 | 1
Residual | 2 | 2 | 1
