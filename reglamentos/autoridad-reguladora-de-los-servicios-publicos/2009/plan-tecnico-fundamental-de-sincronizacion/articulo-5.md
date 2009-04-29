CAPÍTULO TERCERO
Sistemas de sincronización
Artículo 5º—Estructura de la red de sincronización. Los sistemas de sincronización de servicios de telecomunicaciones, deberán estructurarse de acuerdo con el modelo de jerarquías utilizado en el plan nacional de encaminamiento. Esto significa que en el sistema de sincronización tipo maestro esclavo existirán nodos de diferentes jerarquías.
Los nodos de jerarquía inferior recibirán las señales de sincronización de los nodos de jerarquía inmediatamente superior.
De esta manera todos los nodos de la red estarán sincronizados al “reloj de referencia de red” y por consiguiente también lo estarán entre sí. Todos los operadores y proveedores, deberán contar con un reloj de referencia común y todas sus centrales de comunicaciones deberán estar sincronizadas con éste.
Con el objeto de obtener una mayor confiabilidad de la sincronización, los operadores y proveedores deberán reforzar estos sistemas con los siguientes elementos:
a) Cada nodo, además de obtener referencias de sincronización del nodo del que depende jerárquicamente, lo hará también, de otros nodos de nivel jerárquico superior o igual al de él mismo. Los nodos de referencia (NR) son aquellos utilizados para obtener la referencia de sincronización. El NR de n ésima elección será aquel del cual se obtendrá la referencia después de estimar que han fallado los enlaces de sincronización (ES) con los NR’s desde el de orden de elección 1 hasta n 1.
b) Con cada NR se establecerán, en general varios enlaces de sincronización (ES).
El conjunto de los ES que un nodo tendrá establecidos en su NR (o sus NR’s) se establecerán atendiendo a criterios de redundancia y disponibilidad de los diversos medios y tecnologías de transmisión. Cada NR deberá contar con al menos 2 ES de enlaces transmisión.
A cada ES de este nodo se le asignará de acuerdo con su nivel disponibilidad, un orden de prioridad en forma automática, para su toma por parte de algún nodo de la red de modo que en caso de falla se pueda tomar la referencia de sincronización del siguiente en prioridad.
c) Además de las referencias de temporización externa obtenidas a partir de sus ES’s, los nodos dispondrán, de relojes de referencia de nodo (RRN’s).
El nodo obtendrá la referencia de sincronización de su propio reloj en último lugar, es decir, cuando todos sus enlaces de sincronización (ES) hayan mostrado falla o avería.
El uso de los enlaces de sincronización no es exclusivo para llevar esta información, por lo que se podrán utilizar también para el transporte de cualquier otro tipo de tráfico.
Al conjunto de todos los enlaces de sincronización de la red, junto con los equipos de sincronización de los nodos, se denomina sistema de sincronización.
Los enlaces utilizados para sincronizar un nodo desde otro de superior categoría se denominan enlaces de sincronización vertical, y los que se utilizan para sincronizar un nodo desde otro de igual categoría se denominan enlaces de sincronización horizontal.
