Artículo 94.—Cumplimiento niveles de variaciones en el retardo a nivel internacional. Corresponde a las variaciones en los retardos en la transferencia de información (conocidos como jitter) de extremo a extremo de la transferencia de datos a nivel internacional considerando el retardo de la red local, que afectan principalmente a servicios con requerimientos de tiempo real como las transmisiones de voz y video. Este indicador se medirá durante la hora de máximo tráfico de la red.
Tomando como referencia las recomendaciones UIT-T G.1010, Y.1541 y la IEEE 802.1p, se establecen los umbrales máximos de retardo para las siguientes clases de servicio:
Clase de calidad de servicio | Descripción | Umbral de jitter internacional (ms)
0 | Tiempo real, alta interacción, sensibles al retardo. (Voz y video en tiempo real) | 25
1 | Tiempo real, interactivos, sensibles al retardo (Voz y video en tiempo real de menor calidad) | 30
2 | Datos de alta prioridad (transaccionales, altamente interactivos) | N/A
3 | Datos de mediana prioridad (Datos transaccionales interactivos) | N/A
4 | Datos de baja prioridad (transacciones cortas, datos en grandes cantidades, flujo continuo de video streaming) | N/A
5 | Datos de mejor esfuerzo | N/A
Nota: N/A corresponde a “no aplica”, dado que los requerimientos de jitter solo se establecen para servicios con naturaleza de tiempo real.
Todos los operadores deberán asegurar el cumplimiento de los umbrales variaciones en el retardo (jitter) para cada tipo de servicio independientemente de la agrupación, priorización de flujos, manejo de colas y demás mecanismos que empleen en sus enlaces internacionales.
El cumplimiento de los niveles de variaciones en el retardo a nivel internacional, se obtiene mediante la siguiente fórmula:
[imagen]
Donde:
Jitter: corresponde al valor de variación en el retardo (jitter) obtenido para el servicio en estudio para la hora cargada media.
Umbral: corresponde a los umbrales de variación en el retardo de la tabla anterior para cada tipo de servicio
k: constante de rigurosidad, fijada en un valor de 0,5.
El cumplimiento de niveles de variaciones en el retardo (jitter) para cada tipo de servicio de datos, se evaluarán por separado con base en la fórmula anterior.
