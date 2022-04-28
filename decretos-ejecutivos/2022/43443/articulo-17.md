CAPÍTULO II
De los Planos
Artículo 17.-De los planos topográficos. Toda solicitud de formalización de concesión de explotación, cauce de dominio público y/o planta de procesamiento (planta de beneficio) debe presentar un plano topográfico digital que contenga los siguientes requisitos:
a) Derrotero indicando azimuts y distancias entre los vértices del área solicitada. Aportar listado de coordenadas nacionales referido al sistema oficial vigente, de los vértices del área a concesionar y de los puntos de control con sus respectivas elevaciones elipsoídicas.
b) Indicar el acceso o accesos al área de explotación o beneficio, definir si son públicos o privados, acotando las longitudes del camino y distancias a esquina o puntos de referencia. Adicionalmente deberá aportar un shapefile por cada acceso con sus dimensiones exactas y en el sistema de coordenadas oficial vigente.
c) El plano debe ser refrendado y protocolizado por un profesional en topografía incorporado al Colegio respectivo, con indicación de número de protocolo, tomo y folio de levantamiento y sellado por la fiscalía del Colegio respectivo.
d) Indicar nombre completo y número de cédula del gestionante, el que debe coincidir con la solicitud original.
e) El formato del plano no podrá exceder de un máximo 60cm x 90cm. Toda información que se aporte debe ser legible.
f) En caso de explotación de cantera y si el área solicitada no comprende la totalidad de la finca madre, se deberá aportar un plano con todos los requisitos anteriores y referenciado al menos a dos vértices del polígono del plano madre.
g) El plano topográfico deberá indicar vías de transporte, acueductos, obras de generación, líneas eléctricas de alta tensión, oleoductos, depósitos de combustible, puentes o cualquier otra obra de importancia pública dentro del área de interés o fuera de ella, hasta una distancia de 1 km del área a concesionar.
h) Debe incluirse en el cuerpo del plano el diseño de sitio, con la ubicación de la infraestructura existente o a construir, como: quebradores, oficinas administrativas, bodegas, talleres, polvorines, depósitos de combustible, así como indicar los retiros de colindancias y áreas de protección según Ley Forestal Nº 7575 y su reglamento.
i) Todo plano debe ser georreferenciado mediante sistemas de medición GNSS de precisión topográfico (± 3cm horizontal, ± 5cm vertical) o mejor exactitud. Además, deberá indicar a detalle todo lo requerido en el artículo 80 de este reglamento.
j) En caso de canteras deberá realizarse el amojonamiento de 4 puntos de control, con su elevación respectiva.
k) Deberá indicarse las curvas de nivel al menos cada metro de elevación con curvas maestras a cada 5 metros de elevación respecto al elipsoide de referencia WGS84. El levantamiento de curvas de nivel deberá incluir todos los taludes y accidentes geográficos colindantes al área de concesión, como taludes, canales, caminos.
l) Perfil de fondo de río referido a los hitos de control, con ubicación y elevación de confluencias y puntos de basamento expuestos, identificados por el Geólogo. m) Deberá aportarse toda la información topográfica en formato digital, de la siguiente manera:
1. Archivo PDF con todo lo consignado anteriormente.
2. Archivo .dwg y .dxf, a escala 1:1, georreferenciado en el sistema de referencia oficial, sin rotaciones. Debe contener las curvas de nivel (tipo polylíneas) con sus respectivas elevaciones referidas al elipsoide WGS84, el resto de elementos del dibujo deben estar en dos dimensiones, (en el plano z = 0), el archivo debe ser llamado: "Plano Topográfico + número de expediente".dwg y .dxf
3. El usuario deberá aportar los respectivos archivos tipo "shapefile" (.shp) georreferenciados del polígono del área de concesión, además y por separado archivos shapefile del patio de acopio, puntos de control y accesos con la siguiente información en la tabla de atributos:
Archivos shapefile para Cauces de Dominio Público
Shapefile de polígonos de accesos y patios de acopio.
Nombre campo (columnas) | Contenido (Filas) | Tipo de campo | Tamaño
Expediente | Número de expediente o solicitud asociado | Texto | 15
Catastros | Número del o los planos de Catastro afectados | Texto | 30
Campos de la tabla de atributos del shapefile de polígono del área a concesionar en cauces
Nombre campo (columnas) | Contenido (Filas) | Tipo de campo | Tamaño
Expediente | Expediente DGM | Texto | 15
Río | Nombre del río | Texto | 15
Concesiona | Nombre del futuro concesionario. | Texto | 25
Cédula | Cédula física o jurídica | Texto | 12
Material | Material que desea extraer | Texto | 15
N_ARRIBA | Coordenadas Norte río arriba | Número (Doble) |
E_ARRIBA | Coordenadas Este río arriba | Número (Doble) |
N_ABAJO | Coordenadas Norte río abajo | Número (Doble) |
E_ABAJO | Coordenadas Este río abajo | Número (Doble) |
Longitud | Longitud promedio de las dos márgenes del área a concesionar | Número (Doble) |
Jurisdicción | Municipalidad (es) que administra la zona | Texto | 25
Campos de atributos para puntos de control
Shapefile de Puntos
Nombre campo (columnas) | Contenido (Filas) | Tipo de campo | Tamaño
Num-hito | Número relacionado al Plano topográfico | Texto | 15
Elevación | Elevación Elipsóidica respecto al WGS84 | Número (doble) |
Expediente | Número de expediente o solicitud | Texto | 15
Concesiona | Nombre del concesionario | Texto | 30
Cédula | Cédula física o jurídica | Texto | 30
Archivos shapefile para canteras y subterráneos.
Shapefile de polígonos de accesos y patios de acopio.
Nombre campo (columnas) | Contenido (Filas) | Tipo de campo | Tamaño
Expediente | Número de expediente o de solicitud asociado | Texto | 15
Catastros | Número del o los planos de Catastro afectados | Texto | 30
Campos de la tabla de atributos del shapefile de polígono del área a concesionar.
Nombre campo (columnas) | Contenido (Filas) | Tipo de campo | Tamaño
Expediente | Número de expediente o de solicitud asociado | Texto | 15
Catastros | Número del o los planos de Catastro afectados | Texto | 50
Concesiona | Nombre del futuro concesionario. | Texto | 25
Cédula | Cédula física o jurídica | Texto | 12
Material | Material que desea extraer | Texto | 15
Campos de atributos del shapefile para puntos de Control.
Shapelife de Puntos
Nombre campo (columnas) | Contenido (Filas) | Tipo de campo | Tamaño
Num-hito | Número relacionado al Plano topográfico | Texto | 15
Elevación | Elevación Elipsóidica respecto al WGS84 | Número (doble) |
Expediente | Número de expediente o de solicitud asociado | Texto | 15
Archivos shapefile para Exploración.
Campos de la tabla de atributos del shapefile de polígono del área a permisionar.
Nombre campo (columnas) | Contenido (Filas) | Tipo de campo | Tamaño
Expediente | Número de expediente o de solicitud asociado | Texto | 15
Permisionario | Nombre del futuro permisionario. | Texto | 25
Cédula | Cédula física o jurídica | Texto | 12
Material | Material que desea explorar | Texto | 15
