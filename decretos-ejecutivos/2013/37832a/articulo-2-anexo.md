ANEXO B
(NORMATIVO)
Las siguientes características serán obligatorias:
A. Memorias
Especificaciones Técnicas | Observaciones
Mínimo de 6 MB de memoria volátil | Obligatorio para receptor Full-seg.
Mínimo de 1 MB de memoria volátil | Obligatorio para receptor One-seg.
B. Arquitectura de software en el receptor
Especificaciones Técnicas | Observaciones
Gestor de autenticación | Obligatorio para receptor Full-seg, no aplica para One-seg. Especificaciones aplicables para receptores que acceden al canal de interactividad por puerto USB.
C. Arquitectura de software de instalación
Especificaciones Técnicas | Observaciones
Autenticación de la aplicación del dispositivo externo | Opcional para receptor Full-seg, no aplica para One-seg.
Device-driver
Protocolo de la capa física
Archivo de configuración
D. Arquitectura de hardware
Especificaciones Técnicas | Observaciones
Puerto USB | Obligatorio para receptor Full-seg, No aplica para One-seg.
Modo de Instalación
E. Formatos Monomedia
E.1. Imagen Mapa de bits
Especificaciones Técnicas | Observaciones
PNG con restricciones | Obligatorio para receptor Full-seg y One-seg.
JPEG con restricciones
MNG con restricciones | Obligatorio para receptor Full-seg, no aplica para One-seg.
GIF | No aplica para receptor Full-seg, Obligatorio para One-seg.
E.2. Clip de video
Especificaciones Técnicas | Observaciones
MPEG-1 parte 2 | Obligatorio para receptor Full-seg y One-seg. Extensiones del archivo: mp2, mpeg, mpg, mpe
E.3. Audio
Especificaciones Técnicas | Observaciones
MPEG-4 audio AAC-LC | Obligatorio para receptor Full-seg y One-seg.
MPEG-1 clips de audio (Capas 1 y 2)
E.4. Codificación de texto
Especificaciones Técnicas | Observaciones
Código de caracteres de 8 bits (UTF8) | Obligatorio para receptor Full-seg, no aplica para One-seg.
UCS (Universal multi-octet coded Character set UCS)
E.5. Formato de exhibición
Especificaciones Técnicas | Observaciones
Formato de texto - html | Obligatorio para receptor Full-seg y One-seg.
Formato de texto - xml
Formato de texto - css
Formato de texto - txt
E.6. Aplicación
Especificaciones Técnicas | Observaciones
Formato de archivo de fuentes | Obligatorio para receptor Full-seg y One-seg.
Aplicación Ginga-NCL
Aplicación Ginga-NCL Lua
Aplicación Ginga-NCLet | Obligatorio para receptor Full-seg, no aplica para One-seg.
Aplicación Ginga-J Xlet
Aplicación Ginga-zlib
F. Colores
Especificaciones Técnicas | Observaciones
Cantidad mínima de colores | Obligatorio para receptor Full-seg y One-seg.
8-bis alfa blending | Obligatorio para receptor Full-seg, no aplica para One-seg.
G. Fuentes
Especificaciones Técnicas | Observaciones
Residentes | Tiresias | Obligatorio para receptor Full-seg, no aplica para One-seg.
Verdana | No aplica para receptor Full-seg, Obligatorio para One-seg.
Descargables | PFR0 (Recurso de Fuentes Portátil) | Obligatorio para receptor Full-seg, no aplica para One-seg.
Open types |
H. Ámbito de ejecución de la aplicación
Especificaciones Técnicas | Observaciones
NCL | Obligatorio para receptor Full-seg y One-seg.
Java | Obligatorio para receptor Full-seg, no aplica para One-seg.
I. Puente para conectar lenguajes
Especificaciones Técnicas | Observaciones
Puente Ginga-NCL – Ginga-J | Obligatorio para receptor Full-seg, no aplica para One-seg.
J. Motor de Ejecución
Especificaciones Técnicas | Observaciones
Máquina virtual Java | Obligatorio para receptor Full- seg, no aplica para One-seg.
Formateador NCL
JMF 1.0
LUA | Obligatorio para receptor Full-seg y One-seg.
K. Protocolo de canal de radiodifusión
Especificaciones Técnicas | Observaciones
Filtro de sección MPEG-2 | Obligatorio para receptor Full-seg y One-seg.
Carrusel de objetos – DSM-CC
L. Funcionalidades de Ginga
Especificaciones Técnicas | Observaciones
Protocolo dependiente de servicio de información API | Obligatorio para receptor Full-seg, no aplica para One-seg.
Extensión de API para sintonización
Soporte de plano gráfico
M. Especificación del protocolo del canal interactivo
Las siguientes especificaciones se aplican a los receptores con canal de interactividad.
M.1. TCP/IP
Especificaciones Técnicas | Observaciones
TCP (Transmission Control Protocol | Obligatorio para receptor Full-seg y One-seg.
IP (Protocolo de internet)
IPv4
M.2. UDP/IP
Especificaciones Técnicas | Observaciones
IP (Protocolo de internet) | Obligatorio para receptor Full-seg y One-seg.
UDP (Protocolo datagrama del usuario)
M.3. HTTP
Especificaciones Técnicas | Observaciones
HTTP 1.1 | Obligatorio para receptor Full-seg y One-seg.
HTTPS
M.4. DNS
Especificaciones Técnicas | Observaciones
DNS | Obligatorio para receptor Full-seg y One-seg.
M.5. Hibrido DSM-CC/HTTP
Especificaciones Técnicas | Observaciones
Cuando está presente una aplicación Ginga, debe mostrar simultáneamente los objetos recibidos a través de DSM-CC y por el canal de interactividad. | Obligatorio para receptor Full-seg y One-seg.
N. Mando a distancia
Para los receptores que dispongan de mecanismo de interactividad, las teclas, o cualquier otra forma de interfaz, deben suministrar obligatoriamente las siguientes funcionalidades:
a) Ok o confirmar: confirma la operación;
b) salir : abandona la operación;
c) volver: retornar a la operación anterior;
d) direccionales (arriba, abajo, derecha e izquierda): navegación;
e) de colores (roja, verde, amarilla y azul): atajos para funcionalidades contextuales;
f) info: informaciones sobre programación;
g) Menú: presenta opciones de acuerdo con el contexto.
