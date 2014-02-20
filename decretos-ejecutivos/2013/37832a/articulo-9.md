9º—Clasificación y bloqueo de programas recomendado para Full-Seg y opcional para One-Seg. De conformidad con la norma brasileña ISDB-Tb (ABNT NBR 15604:2007), a continuación se muestra los parámetros básicos de clasificación y bloqueo de programas. Estas funcionalidades en todo caso dependen también de que el operador brinde este servicio.
9.1 Clasificación indicativa. La implementación en los dispositivos de bloqueo de programación clasificando por edad o contenido es de implementación recomendada.
9.2 Control de acceso a contenidos televisivos. El descriptor de clasificación indicativa (parental rating descriptor) debe estar presente en el primer “loop” de la PMT o en la EIT (tabla de información de eventos) enviada por el proveedor de contenido. El descriptor transmitido debe ser interpretado en el receptor de acuerdo con lo especificado en la norma brasileña ABNT NBR 15603-2:2007.
La semántica para el descriptor de clasificación (“rating”) , el cual consiste en un campo de 8 “bits” debe indicar a través de la combinación de estos, la clasificación por edad y la descripción objetiva del contenido. La distribución de los bits debe estar de acuerdo con la Figura 1.
Figura 1: Distribución de los bits en campo rating
[imagen]
Fuente: Norma brasileña ABNT NBR 15604
Los cuatro bits menos significativos indican la edad recomendada, de conformidad con la Tabla 1.
Tabla 1: Clasificación por edad
Código Binario | Clasificación
0000 | Reservado
0001 | L
0010 | 10
0011 | 12
0100 | 14
0101 | 16
0110 | 18
0111 a 1111 | Reservado
Fuente: Norma brasileña ABNT NBR 15604
Los cuatro bits más significativos indican la descripción objetiva del contenido, de conformidad con la Tabla 2.
Tabla 2: Descripción objetiva del contenido
Código Binario | Clasificación
0001 | Drogas
0010 | Violencia
0011 | Violencia y Drogas
0100 | Sexo
0101 | Sexo y Drogas
0110 | Violencia y Sexo
0111 | Violencia, Sexo y Drogas
Nota: El bit más significativo se reserva para futuras aplicaciones
Fuente: Norma brasileña ABNT NBR 15604
9.3. Bloqueo exclusivamente por la clasificación por edad. Al ser configurada en el receptor la edad de la clasificación indicativa, la unidad receptora debe comparar la configuración definida por el usuario con la información obtenida a partir del campo rating (bits b0 a b3) del descriptor de clasificación indicativa. Si la edad de clasificación indicativa del campo es mayor que la edad configurada por el usuario, el receptor debe bloquear el evento, independientemente de la descripción objetiva del contenido. En este caso se deberán ignorar los bits b4 a b7 del campo rating del descriptor de clasificación indicativa, de conformidad con la Tabla 3.
Tabla 3: Condiciones de Bloqueo por edad
Código Binario (bit0 a bit3) | Clasificación | Condición de Bloqueo
0000 | Reservado
0001 | L | No hay bloqueo
0010 | 10 | Bloquear si la edad es menor que 10 años
0011 | 12 | Bloquear si la edad es menor que 12 años
0100 | 14 | Bloquear si la edad es menor que 14 años
0101 | 16 | Bloquear si la edad es menor que 16 años
0110 | 18 | Bloquear si la edad es menor que 18 años
| | |
9.4. Bloqueo por la clasificación por edad y la descripción objetiva del contenido. Al ser configurado en el receptor el bloqueo por edad asociado a la descripción objetiva del contenido, la unidad receptora debe comparar la edad y la descripción objetiva del contenido configurada por el usuario con la información obtenida desde el campo rating (edad: bits b0 a b3 y contenidos: bits b4 a b7) del descriptor de clasificación indicativa. Si la edad de clasificación indicativa del campo es mayor que la edad configurada por el usuario, el contenido debe ser totalmente bloqueado, independientemente de la descripción. Si es igual o menor, y el contenido está presente en una de las combinaciones, el receptor debe bloquear evento, conforme el ejemplo de la Tabla 4, donde el usuario hipotéticamente seleccionó la edad de 16 años y contenido que involucra drogas.
Tabla 4: Ejemplo de condiciones de bloqueo por edad y contenido
Edad | b0 a b3 | Descripción del contenido | b04 al b07 | Status
16 | 0101 | Drogas | 0001 | Bloqueado
Violencia y drogas | 0011 | Bloqueado
Sexo y Drogas | 0101 | Bloqueado
Violencia, Sexo y Drogas | 0111 | Bloqueado
18 | 0110 | Drogas | 0001 | Bloqueado
Violencia | 0010 | Bloqueado
Violencia y drogas | 0011 | Bloqueado
Sexo | 0100 | Bloqueado
Sexo y drogas | 0101 | Bloqueado
Violencia y Sexo | 0110 | Bloqueado
Violencia, Sexo y Drogas | 0111 | Bloqueado
Fuente: Norma brasileña ABNT NBR 15604
En los métodos especificados anteriormente, por bloqueo se entiende que no se permite la visualización de las informaciones de video y audio, así como las de datos (data broadcasting content) del evento. Sin embargo, es facultativo para el fabricante del receptor la incorporación de una herramienta que permita la exhibición de las informaciones del servicio tales como título, sinopsis, etc., aunque el evento este bloqueado.
9.5. Exhibición de mensaje de evento bloqueado. En cualquiera de las condiciones presentadas es recomendable la exhibición de un mensaje que informe la razón del bloqueo y la inadecuación del contenido con la clasificación indicativa configurada. La forma de redacción del mensaje, así como más informaciones sobre la inadecuación del evento, queda a criterio del fabricante del receptor.
9.6 Forma de implementar la función de bloqueo. La función de bloqueo es de incorporación recomendada en los receptores. La implementación de las siguientes funciones queda a criterio de cada fabricante del receptor:
9.6.1. Interfaz de configuración del nivel de clasificación indicativa;
9.6.2. Contraseña para bloqueo y desbloqueo;
9.6.3. Liberación temporal de bloqueo.
