Artículo 7º—Información de programación. Los valores para los parámetros service_type y service_number se definen dentro del parámetro “Service_id” que se encuentra en la tabla de información de red (NIT) en el multiplexor. Dicho parámetro está formado por una trama de 16 bits por cada programación, la cual consta de los siguientes campos:
a) Original_network_id: Campo de 11 bits que corresponde a la identificación única de cada operador.
b) Service_type: Campo de 2 bits que debe especificar obligatoriamente el tipo de servicio, es decir si es full-seg o one-seg. Este campo puede adquirir 2 posibles valores para el periodo de transición:
i. 00 = Indica que el servicio de esta programación es full-seg (valor decimal de “0” en el receptor).
ii. 11 = Indica que el servicio de esta programación es one-seg (valor decimal de “3” en el receptor).
c) Service_number: Campo de 3 bits que debe especificar obligatoriamente el número del servicio. Al consistir de 3 bits, este campo puede adquirir únicamente 8 posibles valores:
i. 000 = canal primario. Correspondiente en decimal al canal X.01 si es full-seg, o X.31 si es one-seg;
ii. 001 = canal secundario. Correspondiente en decimal al canal X.02 si es full-seg, o X.32 si es one-seg;
iii. 010 = canal secundario. Correspondiente en decimal al canal X.03 si es full-seg, o X.33 si es one-seg;
iv. 011 = canal secundario. Correspondiente en decimal al canal X.04 si es full-seg, o X.34 si es one-seg;
v. 100 = canal secundario. Correspondiente en decimal al canal X.05 si es full-seg, o X.35 si es one-seg;
vi. 101 = canal secundario. Correspondiente en decimal al canal X.06 si es full-seg, o X.36 si es one-seg;
vii. 110 = canal secundario. Correspondiente en decimal al canal X.07 si es full-seg, o X.37 si es one-seg;
viii. 111 = canal secundario. Correspondiente en decimal al canal X.08 si es full-seg, o X.38 si es one-seg;
Ilustración 2: Service_id
[imagen]
