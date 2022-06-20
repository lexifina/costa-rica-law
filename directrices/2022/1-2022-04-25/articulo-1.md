INSTITUTO GEOGRÁFICO NACIONAL
DIRECTRIZ DIG-001-2022
PARÁMETROS DE TRANSFORMACIÓN
PARA PASAR DEL DATUM CR05 A CR-SIRGAS
DE: Instituto Geográfico Nacional
PARA: Funcionarios del Instituto Geográfico Nacional en adelante IGN, usuarios internos y externos al IGN, funcionarios de la Dirección de Registro Inmobiliario y Registro Nacional, Centro de Información Registral, Profesionales de la Agrimensura; colegiados del Colegio de Ingenieros Topógrafos y del Colegio de Profesionales en Geografía, entre otros.
ASUNTO: Parámetros de transformación de Molodensky, Bursa-Wolf y Molodensky Badekas para pasar del datum CR05 (ITRF00 época 2005.83) a CR-SIRGAS (ITRF08 época 2014.59).
FECHA: 25 de abril de 2022
La presente Directriz DIG-01-2022, brinda los parámetros de transformación para pasar del datum CR05 a CR-SIRGAS que son necesarios para transformaciones de coordenadas en información geoespacial de conformidad con el sistema vigente. Esta complementa la Directriz DIG-001- 2020 publicada en el Diario Oficial La Gaceta el día 04 de setiembre de 2020.
LISTA DE ACRÓNIMOS:
CR05: Costa Rica 2005
CRTM05: Costa Rica Transversa de Mercator 2005.
GNSS: Global Navigation Satellite System (Sistema Global de Navegación por Satélite).
IERS: International Earth Rotation Service (Servicio Internacional de Rotación Terrestre).
IGb: Acrónimo utilizado para la solución actualizada de una definición del ITRF.
IGS: International GNSS Service (Servicio GNSS Internacional).
IGSMAIL: Comunicados de referencia del IGS.
IGN: Instituto Geográfico Nacional.
ITRF: International Terrestrial Reference Frame (Marco Internacional de Referencia Terrestre.
MJ: Ministerio de Justicia y Paz.
MOPT: Ministerio de Obras Públicas y Transportes.
SNIT: Sistema Nacional de Información Territorial.
SIRGAS: Sistema de Referencia Geodésico de las Américas.
Considerando:
1°-Que la Ley N.° 59 del 04 de julio de 1944 (publicada en la Colección leyes y decretos del año 1944, semestre 2, denominada Creación y Organización del Instituto Geográfico Nacional, y la Ley N.° 8905 del 07 de diciembre de 2010 (publicada en La Gaceta N° 18 del 26 de enero de 2011) titulada Reforma del artículo 2 de la ley N° 5695, Creación del Registro Nacional, y sus reformas; y modificación de la ley N° 59, Creación y Organización del Instituto Geográfico Nacional, de 4 de julio de 1944, y sus reformas, determinan la competencia legal del IGN al señalar, en los artículos 1° y 2°, entre otros, sus áreas técnicas de competencia a saber:
Artículo 1º-Declárase el Instituto Geográfico Nacional (IGN), como una dependencia del Registro Nacional. La Junta Administrativa del Registro Nacional administrará el presupuesto del Instituto, suscribirá los contratos y convenios necesarios para el ejercicio de sus funciones. El IGN será la dependencia científica y técnica rectora de la cartografía nacional, destinada a la ejecución del Mapa básico oficial y la Descripción básica geográfica de la República de Costa Rica y a los estudios, las investigaciones o labores y el desarrollo de políticas nacionales de carácter cartográfico, geográfico, geodésico, geofísico y de índole similar que tenga relación con dichas obras, con el fin de apoyar los procesos de planificación.
2°-Que la Ley N.° 59 citada, establece en su artículo N° 2 que: El Instituto Geográfico Nacional constituirá de manera permanente y en representación del Estado, la autoridad oficial en todo lo relativo a las materias técnicas mencionadas; entendiéndose que su autoridad se extiende a las actividades de cualquier orden que tengan por origen los trabajos confiados a su cargo o sean la consecuencia de éstos.
3°-Que el IGN, es el responsable de la determinación, mantenimiento, ampliación y actualización de la Red Geodésica Nacional de Costa Rica, así como del Marco Geodésico de Referencia para la sostenibilidad del Sistema Oficial de Coordenadas y la representación espacial del territorio nacional.
4°-Que el Decreto Ejecutivo N.° 33797-MJ-MOPT, publicado en La Gaceta 108 del 5 de junio del 2007, declara como Datum Horizontal Oficial para Costa Rica, el CR05, enlazado al Marco Internacional de Referencia Terrestre (ITRF2000) del Servicio Internacional de Rotación de la Tierra (IERS) para la época de medición 2005.83, así también, declara como proyección oficial para la representación cartográfica, la Proyección Transversal de Mercator para Costa Rica con el acrónimo CRTM05, disponiendo que el IGN tendrá para el uso de los interesados en la información cartográfica, las aplicaciones que permitan la transformación de datos referenciados en los anteriores sistemas de proyección cartográfica al nuevo sistema de proyección cartográfica CRTM05.
5°-Que de acuerdo con el comunicado del IGS en el IGSMAIL N.° 3605 se establece el ITRF00 con su primera definición IGS00 que establece desde el 02 de diciembre de 2001 hasta el 10 de enero de 2004 y mediante el IGSMAIL N.° 4748 se actualiza al IGb00 el 11 de enero de 2004. Esta actualización del ITRF2000 estuvo vigente hasta el 04 de noviembre de 2006.
6°-Que de acuerdo con el comunicado del IGS en el IGSMAIL N.° 6354 se establece el IGS08 que establece desde el 17 de abril de 2011 hasta el 06 de octubre de 2012 y mediante el IGSMAIL N.° 6663 se actualiza al IGb08 el 07 de octubre de 2012. Esta actualización del ITRF2008 estuvo vigente hasta el 28 de enero de 2017.
7°-Que el Decreto Ejecutivo N.° 40962-MJP, MJP denominado: Actualización del Sistema Geodésico de Referencia Horizontal Oficial para Costa Rica publicado en La Gaceta Digital 66 del 17 de abril del 2018, establece en su artículo N.° 1 que El sistema geodésico de referencia horizontal oficial para Costa Rica, denominado como CR05 y su materialización mediante la Red Geodésica Nacional, cambia en sus siglas a CR-SIRGAS, como sistema de referencia horizontal oficial para la República de Costa Rica, enlazado al Marco Internacional de Referencia Terrestre ITRF2008 (IGb08), para la época de medición 2014.59, y en adelante, los cambios y su actualización, se regirán de acuerdo a las nuevas definiciones del ITRF que se implementen en la red continental del Sistema de Referencia Geocéntrico para las Américas (SIRGAS) denominada SIRGAS-CON.
8°-Que el Decreto Ejecutivo N.° 40962-MJP, establece en el artículo N.° 2 que: El sistema de proyección cartográfica CRTM05 seguirá siendo el oficial para la representación cartográfica del territorio nacional continental, extendido para efectos de aplicación de esta proyección cartográfica, hasta la línea de base del mar territorial en el océano Pacífico y el mar Caribe, definida esta línea conforme a los artículos 5, 6 y 7 de la Convención de las Naciones Unidas sobre el Derecho del Mar, como punto de partida para el cómputo de la anchura máxima de todas las áreas marinas jurisdiccionales del Estado costarricense.
9°-Que el Decreto Ejecutivo N.° 40962-MJP, indica en el artículo 10 que el IGN está habilitado para publicar oficialmente a través del Diario Oficial La Gaceta, y en el geoportal del Sistema Nacional de Información Territorial (SNIT) los parámetros de actualización del sistema de referencia horizontal CR-SIRGAS en el tiempo, conforme se considere, para los fines geodésicos, topográficos, cartográficos, catastrales, entre otros.
10.-Que según el Decreto Ejecutivo N.° 40962-MJP y artículo 10 referido, el IGN publicó en el apartado de noticias del SNIT el 28 de marzo de 2019, un set de parámetros para realizar la transformación de coordenadas entre los datums geodésicos CR05 y CR-SIRGAS correspondientes con los marcos geodésicos ITRF00 época 2005.83 e ITRF08 época 2014.59 considerando el modelo de Bursa-Wolf con la convención angular Coordinate Frame Rotation.
11.-Que para facilitar el uso de la transformación de datos el IGN procedió a inscribir el sistema CR-SIRGAS en el registro de Sistemas de Coordenadas de Referencia (CRS por sus siglas en inglés) del European Petroleum Survey Group (EPSG) el cual de conformidad con el Decreto Ejecutivo N.° 40962-MJP es el sistema de referencia oficial de Costa Rica y los códigos registrados para CR-SIRGAS son:
. 1225 para el Datum Geodésico CR-SIRGAS,
. 8905 para coordenadas geocéntricas cartesianas,
. 8906 para coordenadas geográficas 3D,
. 8907 para coordenadas geográficas 2D,
. 8908 para coordenadas proyectadas de CR-SIRGAS a CRTM05,
. 8912 para un sistema de coordenadas compuesto que considera coordenadas proyectadas de CR-SIRGAS a CRTM05 con el Datum Altimétrico de Costa Rica de 1952,
. 8909 para coordenadas proyectadas de CR-SIRGAS a UTM zona 16N,
. 8910 para coordenadas proyectadas de CR-SIRGAS a UTM zona 17N,
. 9751 para la transformación de coordenadas del datum geodésico CR05 a CRSIRGAS considerando el modelo de Bursa-Wolf con la convención angular Coordinate Frame Rotation.
12.-Que en el mismo Decreto Ejecutivo N.° 40962-MJP norma 10 citada, el IGN considera necesario brindar otros sets de parámetros correspondientes con los modelos de transformación de Molodensky y Molodensky Badekas.
13.-Que el Decreto Ejecutivo N.° 40962-MJP norma 11, indica para los diferentes fines de las delimitaciones oficiales y las coberturas de información y mapas que las representan, se establece la aplicación del sistema de referencia horizontal CR05, y su actualización a CRSIRGAS.
14.-Que la Directriz DIG-001-2020 denominada Parámetros de transformación para pasar de las épocas 2014.59 a la 2019.24 en el ITRF14 correspondiente con CR-SIRGAS no se ve afectada o anulada por la presente directriz, sino por el contrario se complementa.
Por tanto,
Se emite la siguiente Directriz:1°-Aplicación de la Directriz:
a) Objeto: La presente resolución es de carácter técnico, y tiene por objeto establecer las disposiciones para realizar la transformación de coordenadas entre el datum geodésico CR05 y el CR-SIRGAS.
b) Ámbito de Aplicación: La aplicación de esta resolución técnica es para todos los procesos públicos y privados con coberturas de información geoespacial que requieran estar referidos a la primera definición del datum geodésico CR-SIRGAS correspondiente con el marco geodésico ITRF08 en la época 2014.59.
c) Alcance: La presente directriz constituye una herramienta para la actualización de coordenadas que debe observar el IGN, otras entidades públicas, sector privado y público en general: productores, gestores y usuarios de información geográfica georreferenciada.
2°-El IGN establece los parámetros de transformación para pasar coordenadas del datum geodésico CR05/ ITRF00 época 2005.83 al CR-SIRGAS/ITRF08(IGb08) época 2014.59.
3°-Que los métodos para el uso de los parámetros corresponden con las transformaciones de Molodensky de 3 parámetros, Bursa Wolf de 7 parámetros y Molodensky- Badekas de 10 parámetros. En el caso de Bursa Wolf y Molodensky-Badekas consideran la convención angular Coordinate Frame Rotation.
4°-Parámetros de transformación.
[imagen]
[imagen]
[imagen]
5°-Rige a partir de su publicación en el Diario Oficial La Gaceta.
Dado en Curridabat, San José a los 6 días del mes de junio del año 2022.
