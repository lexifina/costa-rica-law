Artículo 92.—Cumplimiento niveles de retardo a nivel internacional. Corresponde al retardo extremo a extremo de la transferencia de datos a nivel internacional considerando el retardo de la red local, para la hora cargada media del servicio en estudio.
Tomando como referencia las recomendaciones UIT-T G.1010, Y.1541 y la IEEE 802.1p, se establecen los umbrales máximos de retardo para las siguientes clases de servicio:
Clase de calidad de servicio | Descripción | Umbral de retardo internacional (ms)
0 | Tiempo real, alta interacción, sensibles al retardo. (Voz y video en tiempo real) | 80
1 | Tiempo real, interactivos, sensibles al retardo (Voz y video en tiempo real de menor calidad) | 120
2 | Datos de alta prioridad (transaccionales, altamente interactivos) | 160
3 | Datos de mediana prioridad (Datos transaccionales interactivos) | 200
4 | Datos de baja prioridad (transacciones cortas, datos en grandes cantidades, flujo continuo de video streaming) | 240
5 | Datos de mejor esfuerzo | 280
Para el caso de redes satelitales se aplicará lo dispuesto en la recomendación UIT-R M.1636, para los tipos de satélites GEO (Geostationary Earth Orbit, órbita terrestre geoestacionaria), MEO (Medium Earth Orbit, órbita terrestre mediana) y MEO (Low Earth Orbit, órbita terrestre baja), conforme la siguiente tabla:
Tipo de satélite | GEO | MEO | LEO
Retardo de propagación máximo (dos vías) (ms) | 280 | 120 | 60
Todos los operadores deberán asegurar el cumplimiento de los umbrales de retardo internacional para cada tipo de servicio independientemente de la agrupación, priorización de flujos, manejo de colas y demás mecanismos que empleen en sus enlaces internacionales.
El cumplimiento de los niveles de retardo internacional, se obtiene mediante la siguiente fórmula:
[imagen]
Donde:
Retardo: corresponde al valor de retardo obtenido para el servicio en estudio para la hora cargada media.
Umbral: corresponde a los umbrales de retardo de la tabla anterior para cada tipo de servicio
k: constante de rigurosidad, fijada en un valor de 0,5.
El cumplimiento de niveles de retardo internacional para cada tipo de servicio de datos, se evaluarán por separado con base en la fórmula anterior.
