4. Requerimientos operacionales del ciclo de vida del certificado
4.1 Solicitud de certificado
4.1.1 Quién puede presentar una solicitud de certificado
En la siguiente lista se detallan las personas que pueden presentar una solicitud de certificado:
· Para el caso de certificados de CA de políticas, el Director de Certificadores de Firma Digital.
· Para el caso de certificados de CA emisoras, el representante legal o apoderado con poderes suficientes de la entidad a ser registrada.
· Para el caso de certificados de firma digital y autenticación de persona física, cualquier persona mayor de edad con un documento de identidad legalmente aceptado, que será el sujeto a cuyo nombre se emita el certificado.
· Para el caso de certificados de sello electrónico y agente electrónico de persona jurídica, el personero o representante con facultades suficientes de la persona jurídica a la que representa (por ejemplo un tramitador de certificados digitales de persona jurídica debidamente registrado ante el Registro Nacional).
· Para los certificados de Autoridad de Sellado de Tiempo, el representante legal o apoderado con poderes suficientes de la entidad de sellado de tiempo (TSA).
4.1.2 Proceso de inscripción y responsabilidades
Durante el proceso de inscripción, el solicitante debe firmar un acuerdo de suscriptor, donde se establecen las responsabilidades y deberes asumidos con el uso del certificado.
La DCFD tiene la responsabilidad de:
· Ejecutar el proceso de registro y verificación de identidad de las CA emisoras.
· Velar porque la entidad solicitante cumpla los requisitos establecidos en la Ley 8454, Ley de certificados, firmas digitales y documentos electrónicos y su reglamento.
· Informar al suscriptor de sus deberes y responsabilidades con respecto al uso del certificado.
· Emitir el certificado de acuerdo con la información suministrada en la solicitud de certificado.
La CA emisora tiene la responsabilidad de:
· Validar la identidad de la RA que remite las solicitudes.
· Validar la información suministrada en la solicitud.
· Emitir el certificado de acuerdo con la información suministrada en la solicitud.
· Enviar el certificado a la RA para que sea entregado al suscriptor.
La RA tiene la responsabilidad de:
· Ejecutar el proceso de registro y verificación de identidad y de las facultades del solicitante para solicitar un determinado certificado dependiendo del tipo de certificado.
· Remitir la solicitud de certificado digital a la CA emisora, firmada digitalmente.
· Informar al suscriptor de sus deberes y responsabilidades con respecto al uso del certificado.
El solicitante tiene las siguientes responsabilidades dependiendo del tipo de certificado:
Certificados de CA emisora
· Completar el formulario de inscripción de certificado y proveer información correcta y verdadera. Esta información debe presentarse ante la RA, para este caso la DCFD.
· Presentar un documento de identificación legalmente aceptado y vigente, así como una personería jurídica vigente (con menos de un mes de emitida) donde se establezca su relación como representante legal o apoderado con poderes suficientes de la empresa o institución a certificar.
· Generar la solicitud de certificado de forma que se demuestre la posesión de la llave privada correspondiente a la llave pública entregada, cumpliendo lo estipulado en el apartado 3.2.1.
· Firmar el acuerdo de suscriptor.
Certificados de firma digital y autenticación de persona física
Completar el formulario de inscripción de certificado y proveer información correcta y verdadera.
· Presentar un documento de identificación legalmente aceptado y vigente.
· Ingresar confidencialmente la “frase de desafío” (“challenge phrase”), que será requerida en el proceso de revocación del certificado.
· Generar la solicitud de certificado de forma que se demuestre la posesión de la llave privada correspondiente a la llave pública entregada, cumpliendo con lo dispuesto en el apartado 3.2.1.
· Firmar el acuerdo de suscriptor.
Certificados de sello electrónico y agente electrónico de persona jurídica
Completar el formulario de inscripción de certificados y proveer información correcta y verdadera.
· Presentar un documento de identificación legalmente aceptado y vigente, así como una personería jurídica con menos de un mes de emitida, o los documentos legales suficientes que garanticen su relación como personero o representante con facultades suficientes de la persona jurídica solicitante. Para los certificados de agente electrónico, en el caso de requerir que uno o varios nombres DNS formen parte del campo nombre alternativo del sujeto (Subject Alternative Name o SAN por sus siglas en inglés) es necesario que el personero o representante con facultades suficientes de la persona jurídica solicitante, presente evidencia de que el nombre de dominio solicitado está registrado a nombre de la persona jurídica que representa (ver sección 7.1.2.3).
· Generar la solicitud de certificado cumpliendo con el apartado 3.2.1 de este CP y presentarla ante la CA, con lo que se demuestra la posesión de la llave privada correspondiente a la llave pública entregada.
· Firmar el acuerdo de suscriptor.
Certificados de Autoridad de Sellado de Tiempo (TSA)
· Completar el formulario de inscripción de certificado y proveer información correcta y verdadera ante la DCFD.
· Cumplir con todas las responsabilidades señaladas anteriormente para solicitante de certificados de sello electrónico y agente electrónico de persona jurídica.
4.2 Procesamiento de la solicitud de certificado
4.2.1 Ejecución de las funciones de identificación y autenticación
Certificados de CA emisora y de autoridad de sellado de tiempo
La encargada de estas funciones es la DCFD, entidad que debe velar por el cumplimiento de la identificación y la autenticación de acuerdo con las disposiciones establecidas en la sección 3.2.
Certificados de firma digital y autenticación de persona física o certificados de sello electrónico y agente electrónico de persona jurídica
La encargada de estas funciones es la autoridad de registro (RA), o donde aplique la CA, que debe velar por el cumplimiento de la identificación y la autenticación de acuerdo con las disposiciones establecidas en la sección 3.2.
4.2.2 Aprobación o rechazo de solicitudes de certificado
Certificados de CA emisora y de autoridad de sellado de tiempo (TSA)
La DCFD debe administrar y supervisar el proceso de certificación, en particular lo concerniente a la aceptación o rechazo de las aplicaciones para certificados de autoridad certificadora.
Para optar por un certificado de autoridad certificadora, la CA solicitante debe cumplir con todos los requisitos establecidos en la Ley 8454, su Reglamento y demás lineamientos establecidos por la DCFD.
Certificados de firma digital y autenticación de persona física o certificados de sello electrónico y agente electrónico de persona jurídica
La RA debe rechazar cualquier solicitud de certificado que no cumpla con la Ley, su Reglamento y demás lineamientos establecidos por la DCFD. Asimismo, la CA emisora debe rechazar cualquier solicitud proveniente de una RA que no cumpla con los requisitos para la emisión del certificado.
4.2.3 Tiempo para procesar solicitudes de certificado
El tiempo de procesamiento de solicitudes de certificados (tiempo entre la solicitud emitida a la CA y la emisión del certificado al suscriptor) de persona física, cuando el proceso se realice en forma automática, no debe ser mayor a diez minutos.
En cualquier otro caso, las CA y RA procesarán las solicitudes de certificados dentro de un tiempo razonable, a menos que se especifiquen otros parámetros en el acuerdo de suscriptor, en la CPS o en otros acuerdos entre los participantes.
4.3 Emisión de certificado
4.3.1 Acciones de la CA durante la emisión de certificados
Certificados de CA y certificados de autoridad de sellado de tiempo (TSA)
La CA debe verificar que el solicitante cumple con los requisitos de esta política, con las normas técnicas y con la legislación aplicable.
Certificados de firma digital y autenticación de persona física o certificados de sello electrónico y agente electrónico de persona jurídica
La CA debe verificar que las solicitudes de certificado provengan de RAs autorizadas. Una vez creado el certificado, la CA debe remitirlo a la RA desde la cual ingresó la solicitud.
4.3.2 Notificación al suscriptor por parte de la CA sobre la emisión del certificado
Certificados de CA emisora y certificados de autoridad de sellado de tiempo (TSA)
La DCFD debe notificar a la CA emisora o la TSA solicitante sobre la emisión del certificado, de acuerdo a los procedimientos definidos para tales efectos.
Certificados de firma digital y autenticación de persona física
En este caso, la entrega del certificado es presencial por lo tanto la notificación es inmediata.
Certificados de sello electrónico y agente electrónico de persona jurídica
Cuando las circunstancias lo permitan, la RA, o donde aplique la CA, entregará los certificados en forma presencial, en cuyo caso la notificación será inmediata. En cualquier otro caso, la notificación se realizará de acuerdo a los procedimientos definidos para tales efectos.
4.4 Aceptación de certificado
4.4.1 Conducta constitutiva de aceptación de certificado
Certificados de CA emisora y certificados de autoridad de sellado de tiempo (TSA)
El proceso de instalación del certificado respectivo por parte de la CA emisora o TSA solicitante, constituirá la aceptación del certificado.
Certificados de firma digital y autenticación de persona física
El certificado se da por aceptado cuando la persona firma digitalmente un comprobante de aceptación del certificado entregado, esta es la primera vez que se usa y permite al suscriptor verificar que el certificado está funcionando correctamente.
Certificados de sello electrónico y agente electrónico de persona jurídica
El proceso de instalación de los certificados respectivos por parte de la persona jurídica que utiliza los certificados, constituirá la aceptación de los certificados.
4.4.2 Publicación del certificado por la CA
La CA no debe publicar información de los certificados emitidos en los repositorios de acceso público.
4.4.3 Notificación de la emisión del certificado por la CA a otras entidades
No se definen entidades externas que necesiten o requieran ser notificadas acerca de los certificados emitidos por las CA.
4.5 Uso del par de llaves y del certificado
4.5.1 Uso de la llave privada y del certificado por el suscriptor
El uso de la llave privada correspondiente a la llave pública contenida en el certificado solamente debe ser permitido una vez que el suscriptor haya aceptado el certificado emitido. Dicho uso debe realizarse en concordancia con la normativa aplicable, lo estipulado en este CP, y los contratos de suscriptor respectivos.
Los suscriptores deben proteger sus llaves privadas del uso no autorizado y deben descontinuar su uso después de la expiración o revocación del certificado.
Certificados de CA
· CA raíz: la llave privada sólo puede ser utilizada para firmar certificados de CA de políticas.
· CA políticas: Las CA de políticas son CA emisoras cuya llave privada únicamente puede ser utilizada para firmar certificados de CA emisoras subordinadas (SubCa) y autoridades certificadoras de sellado de tiempo.
· CA emisora de persona física o persona jurídica: la llave privada solo debe ser utilizada para firmar certificados de autenticación y firma digital de personas físicas o certificados de sello electrónico y agente electrónico de personas jurídicas.
Certificados de firma digital y autenticación de persona física
El uso que se le dé a los certificados de persona física debe ser acorde con lo dispuesto en la sección 6.1.7.
Certificados de sello electrónico de persona jurídica
Los certificados de sello electrónico serán utilizados para actos de la persona jurídica suscriptora, salvo aquellos casos donde se determine su inadmisibilidad legal o administrativa. Dichos actos generan responsabilidad de conformidad con el Artículo 10 de la Ley de Certificados, Firmas Digitales y Documentos Electrónicos No. 8454. 6
6 Artículo 10.- Presunción de autoría y responsabilidad
Todo documento, mensaje electrónico o archivo digital asociado a una firma digital certificada se presumirá, salvo prueba en contrario, de la autoría y responsabilidad del titular del correspondiente certificado digital, vigente en el momento de su emisión.
Cada persona jurídica deberá desarrollar y establecer los mecanismos de seguridad informática y de infraestructura física, así como los reglamentos, procedimientos o políticas que considere pertinentes para resguardar y delimitar el uso de dicho certificado en su organización.
Las personas jurídicas que hagan uso de los certificados de sello electrónico deberán proveer las herramientas necesarias y adecuadas para que tanto los ciudadanos como otras administraciones puedan verificar la validez de sus sellos electrónicos.
Con respecto a la utilización de las llaves, el uso que se le dé a los certificados de sello electrónico debe ser acorde con lo dispuesto la sección 6.1.7.
Certificados de agente electrónico de persona jurídica
Con respecto a la utilización de las llaves, el uso que se le dé a los certificados de agente electrónico debe ser acorde con lo dispuesto la sección 6.1.7.
Certificados autoridad de sellado de tiempo (TSA)
La llave privada solo debe ser utilizada para prestar el servicio de sellado de tiempo.
4.5.2 Uso de la llave pública y del certificado por la parte que confía
Las partes que confían deben aceptar las estipulaciones establecidas en este CP, en lo que les resulte aplicable, como condición indispensable para confiar en el certificado.
La confianza en un certificado debe ser razonable, de acuerdo con las circunstancias. Si las circunstancias indican la necesidad de verificaciones adicionales, la parte que confía debe obtener tales verificaciones para que la confianza sea considerada razonable.
Antes de cualquier acto de confianza las partes que confían deben evaluar en forma independientemente:
· La pertinencia del uso del certificado para cualquier propósito dado y determinar que la voluntad del certificado, de hecho, sea utilizada para un propósito apropiado que no está prohibido o de otra forma restringido por este CP. Las CA o RA no son responsables por la evaluación de la pertinencia en el uso de un certificado.
· Que el certificado sea utilizado de acuerdo con las disposiciones de esta CP (por ejemplo: Si en el certificado faltan los propósitos de firma y no repudio en el atributo de KeyUsage, entonces el certificado no puede ser confiable para validar la firma de un suscriptor).
· El estado del certificado y el estado de todos los certificados de las CA en la cadena que emitieron el certificado. Si cualquiera de los certificados en la cadena del certificado ha sido revocado, la parte que confía es la única responsable de investigar si la confianza en una firma digital efectuada por un suscriptor antes de la revocación de un certificado en la cadena es razonable. Cualquier confianza de este tipo es asumida únicamente bajo el riesgo de la parte que confía.
Si se determina que el uso del certificado es apropiado, las partes que confían deben utilizar el hardware y software necesario para ejecutar la verificación de la firma digital u otra operación criptográfica que ellos deseen efectuar, como una condición para confiar en los certificados relacionados con tales operaciones.
4.6 Renovación de certificado
La renovación del certificado no está permitida por esta CP, cuando un certificado requiera ser renovado debe solicitarse un nuevo certificado, de acuerdo con la sección 4.1 de este CP.
4.6.1 Circunstancias para renovación de certificado
No aplica.
4.6.2 Quién puede solicitar renovación
No aplica.
4.6.3 Procesamiento de solicitudes de renovación de certificado
No aplica.
4.6.4 Notificación al suscriptor sobre la emisión de un nuevo certificado
No aplica.
4.6.5 Conducta constitutiva de aceptación de un certificado renovado
No aplica.
4.6.6 Publicación por la CA del certificado renovado
No aplica.
4.6.7 Notificación por la CA de la emisión de un certificado a otras entidades
No aplica.
4.7 Re-emisión de llaves de certificado
La re-emisión del certificado no está permitida por esta CP, cuando un certificado requiera ser re-emitido debe solicitarse un nuevo certificado, de acuerdo con la sección 4.1 de este CP.
4.7.1 Circunstancia para re-emisión de llaves de certificado
No aplica.
4.7.2 Quién puede solicitar la certificación de una nueva llave pública
No aplica.
4.7.3 Procesamiento de solicitudes de re-emisión de llaves de certificado
No aplica.
4.7.4 Notificación al suscriptor sobre la reemisión de un nuevo certificado
No aplica.
4.7.5 Conducta constitutiva de aceptación de un certificado reemitido
No aplica.
4.7.6 Publicación por la CA de los certificados reemitidos
No aplica.
4.7.7 Notificación por la CA de la reemisión de un certificado a otras entidades
No aplica.
4.8 Modificación de certificados
4.8.1 Circunstancias para modificación del certificado
Cuando se requiera la modificación de la información contenida en un certificado debe revocarse y realizar una solicitud para un nuevo certificado, de acuerdo con la sección 4.1.
4.8.2 Quién puede solicitar modificación del certificado
No aplica.
4.8.3 Procesamiento de solicitudes de modificación del certificado
No aplica.
4.8.4 Notificación al suscriptor de la emisión de un nuevo certificado
No aplica.
4.8.5 Conducta constitutiva de aceptación del certificado modificado
No aplica.
4.8.6 Publicación por la CA de los certificados modificados
No aplica.
4.8.7 Notificación por la CA de emisión de certificado a otras entidades
No aplica.
4.9 Revocación y suspensión de certificado
4.9.1 Circunstancias para la revocación
Certificados de CA:
 A petición de la CA que considera o sospecha que su llave privada fue comprometida.
 Identificación o componentes de afiliación inválidos.
 Violación del acuerdo de suscriptor.
 Insolvencia, cese de actividades, quiebra o liquidación de la CA.
 Se comprueba la expedición de certificados falsos.
 Reincidencia en cualquiera de las infracciones que le hayan merecido una sanción de suspensión, dentro de los cinco años siguientes.
 Cuando se tienen razones para creer que el certificado no fue emitido de acuerdo a los lineamientos de la CP aplicable.
 Cuando se determina que los pre-requisitos para la emisión del certificado no fueron satisfechos.
Certificados de firma digital y autenticación de persona física, de sello electrónico y agente electrónico de persona jurídica, y de sellado de tiempo:
 A petición del suscriptor, a favor de quién se expidió, quién tiene razones o sospechas para creer que su llave privada ha sido comprometida.
 Cuando se confirme que el suscriptor ha comprometido su confiabilidad, desatendiendo los lineamientos de seguridad establecidos, suplido información falsa al certificador u omitido otra información relevante, con el propósito de obtener o re-emitir el certificado.
 Por fallecimiento (en el caso de persona física), ausencia legalmente declarada, interdicción o insolvencia.
 Cuando el suscriptor finaliza el contrato por voluntad propia.
 Por errores de información del certificado, por ejemplo el nombre del suscriptor o alguno de los atributos.
 El acuerdo entre el suscriptor y la CA emisora se ha terminado.
 Cuando se tienen razones para creer que el certificado no fue emitido de acuerdo a los lineamientos de la CP aplicable.
 Cuando se determina que los pre-requisitos para la emisión del certificado no fueron satisfechos.
 Cuando la información incluida dentro del certificado es incorrecta o ha cambiado.
 Para el caso de los certificados de persona jurídica, cuando venza el plazo social de la persona jurídica o cuando la misma sea disuelta.
Adicionalmente, cuando se determine que el uso del certificado atenta contra la seguridad del Sistema Nacional de Certificación Digital. Esto se determinará con base en la legislación aplicable, la naturaleza y el número de denuncias recibidas, la identidad del denunciante, y cualquier otra que la DCFD determine.
4.9.2 Quién puede solicitar revocación
De pleno derecho el suscriptor del certificado puede solicitar la revocación de su certificado, ya sea por voluntad propia o por compromiso de su llave privada. En caso de sospecha o compromiso de su llave privada, la notificación debe realizarla en forma inmediata a la CA correspondiente.
Para todos los casos, la CA emisora del certificado y la autoridad judicial competente pueden solicitar la revocación del certificado.
Asimismo, pueden solicitar la revocación los siguientes participantes según el tipo de certificado:
Para certificados de CA emisora o TSA
 El representante legal o apoderado con poderes suficientes de la CA emisora o TSA.
 La DCFD.
Para certificados de firma digital y autenticación de persona física
 El Tribunal Supremo de Elecciones, en caso de fallecimiento.
Para certificados de sello electrónico y agente electrónico de persona jurídica
 El personero o representante con facultades suficientes de la persona jurídica suscriptora del certificado (por ejemplo el tramitador de certificados digitales de persona jurídica vigente y debidamente registrado ante el Registro Nacional).
 El Registro Nacional, por medio de su registro de personas jurídicas.
Además, cualquier persona puede solicitar la revocación de un certificado ante la CA correspondiente presentando evidencia contundente que revele el compromiso de la llave privada del suscriptor.
4.9.3 Procedimiento para la solicitud de revocación
Verificar que la solicitud de revocación ha sido presentada por el suscriptor del certificado o por una autoridad competente, de acuerdo con la sección 3.4.
Las solicitudes para la revocación de certificados de CA emisoras deben ser autenticadas por sus entidades superiores dentro de la jerarquía nacional de certificadores registrados, para asegurar
que la revocación de una CA emisora ha sido solicitada por una entidad autorizada para tales efectos.
Para los casos donde un suscriptor posea dos o más certificados vigentes del mismo tipo y propósito, la CA emisora tendrá la responsabilidad de brindar al suscriptor la información suficiente que le permita determinar con exactitud cuál de los certificados es el que dicho suscriptor desea revocar, así como de informarle al momento de la revocación del estado de sus otros certificados vigentes.
4.9.4 Periodo de gracia para solicitud de revocación
No se estipulan periodos de gracia para revocación de certificados, salvo los impuestos por la ley para realizar apelaciones.
4.9.5 Tiempo dentro del cual la CA debe procesar la solicitud de revocación
Las solicitudes de revocación deben ser procesadas en un rango de tiempo razonable, de acuerdo con el procedimiento para la solicitud de revocación (ver sección 4.9.3). Cuando la solicitud provenga del suscriptor y se utilicen mecanismos electrónicos automatizados, la revocación debe realizarse en forma inmediata.
4.9.6 Requerimientos de verificación de revocación para las partes que confían
Las partes que confían deben evaluar el estado del certificado y el estado de todos los certificados de las CA en la cadena a la que pertenece el certificado, antes de confiar en él.
En caso de que cualquiera de los certificados en la cadena del certificado haya sido revocado, la parte que confía es la única responsable de investigar si la confianza en una firma digital efectuada por un suscriptor antes de la revocación de un certificado en la cadena es razonable. Cualquier confianza de este tipo es asumida únicamente bajo el riesgo de la parte que confía. Para estos propósitos las partes que confían pueden verificar el estado del certificado mediante el servicio de OCSP o la lista de revocación más reciente, de acuerdo con su grado de tolerancia al riesgo.
4.9.7 Frecuencia de emisión de CRL
CA Raíz
La CA Raíz debe actualizar su lista de revocación cada cuatro meses y cada vez que se presente una revocación del certificado de una CA de Políticas, en cuyo caso se debe notificar a las CA subsecuentes.
CA de Políticas
La CA de Políticas debe actualizar su lista de revocación cada dos meses y cada vez que se presente una revocación del certificado de una CA emisora, en cuyo caso se debe notificar a todas las CA emisoras.
CA emisora
La CA emisora debe actualizar y publicar las listas de revocación al menos una vez a la semana. Además deberá publicar los Delta CRL una vez al día.
4.9.8 Latencia máxima para CRLs
La CA o TSA debe publicar la CRL en el repositorio en un plazo no mayor a dos horas posterior a su generación.
4.9.9 Disponibilidad de verificación de revocación/estado en línea
Todas las CA o TSA deben mantener disponible un repositorio con información del estado de los certificados emitidos por ésta, el cual puede ser accedido vía Web. Adicionalmente, para la CA emisora registrada es obligatorio implementar el servicio de validación en línea OCSP.
4.9.10 Requerimientos para verificar la revocación en línea
La parte que confía debe verificar el estado de un certificado en el cual desea confiar, utilizando los mecanismos de verificación del estado de certificados establecidos en la sección anterior.
4.9.11 Otras formas de advertencias de revocación disponibles
No se estipulan.
4.9.12 Requerimientos especiales por compromiso de llaves reemitidas
La DCFD debe notificar en el menor tiempo posible a todos los participantes de la jerarquía nacional de certificadores registrados acerca del compromiso de la llave privada de alguna de las CA.
4.9.13 Circunstancias para suspensión
4.9.13.1 Suspensión de certificados para personas físicas o certificados para de personas jurídicas
De conformidad con el artículo 14 de la ley 8454 de certificados digitales, las circunstancias de suspensión son:
a. Por petición del propio usuario a favor de quién se expidió el certificado.
b. Como medida cautelar, cuando el certificador que lo emitió tenga sospechas fundadas de que el propio usuario haya comprometido su confiabilidad, para obtener el certificado.
c. Si contra el usuario se ha dictado auto de apertura a juicio, por delitos en cuya comisión se haya utilizado la firma digital.
d. Por no cancelar oportunamente el costo del servicio.
Para los efectos prácticos se puede implementar la suspensión de certificados de personas físicas o de personas jurídicas, como la anulación técnica del certificado, que evite que pueda seguir siendo utilizado para el propósito de firma por parte del suscriptor. Además, ninguna CA emisora podrá expedirle un certificado de firma o sello electrónico mientras el estado de suspensión se encuentre vigente. Este aspecto será determinado por las declaraciones de prácticas de certificación o el acuerdo de suscriptor definido por la CA que emita los certificados.
4.9.13.2 Suspensión de una CA
Se puede suspender una CA emisora, si existe una orden judicial o por decisión de la DCFD, o cuando el ECA acredite que la CA emisora incumple las obligaciones que le impone la ley 8454 y su reglamento. Para este caso en particular el reglamento define la suspensión de la CA emisora en el artículo 32, como la imposibilidad para el certificador sancionado de expedir nuevos certificados digitales o de renovar los que expiren durante el plazo de suspensión. Esta suspensión no afectará a los certificados emitidos previamente.
4.9.14 Quién puede solicitar la suspensión
De pleno derecho, el suscriptor del certificado puede solicitar la suspensión de su propio certificado.
Asimismo, pueden solicitar la suspensión otros participantes según el tipo de certificado:
Certificados de CA y certificados de autoridad de sellado de tiempo (TSA)
· El representante legal o apoderado con poderes suficientes de la CA emisora o TSA.
· El Ente Costarricense de Acreditación.
· La autoridad judicial competente.
· La DCFD.
Certificados de firma digital y autenticación de persona física
· La autoridad judicial competente.
· La CA emisora.
Certificados de sello electrónico y agente electrónico de persona jurídica
· El personero o representante con facultades suficientes de la persona jurídica suscriptora del certificado, o el tramitador de certificados digitales de persona jurídica vigente y debidamente registrado ante el Registro Nacional.
· La autoridad judicial competente.
· La CA emisora.
4.9.15 Procedimiento para la solicitud de suspensión
El procedimiento de suspensión depende del tipo de certificado y del solicitante de la suspensión, de acuerdo con:
Certificados de CA emisora o TSA
 El representante legal o apoderado con poderes suficientes de la CA emisora debe:
o Presentar un documento de identificación legalmente aceptado y vigente, así como la personería jurídica vigente (con menos de un mes de emitida) donde se establezca su relación como representante legal o apoderado con poderes suficientes de la empresa o institución suscriptora del certificado.
o Implementar los controles y procedimientos para no expedir nuevos certificados digitales o de renovar los que expiren durante el plazo de suspensión.
 Ente Costarricense de Acreditación (ECA)
o Comunicar a la DCFD el incumplimiento de la acreditación o de las obligaciones que imponen la ley 8454, Ley de certificados, firmas digitales y documentos electrónicos y su reglamento.
 La autoridad judicial competente
o Remitir a la DCFD la resolución en la que se ordena la suspensión, los alcances y los plazos de la misma.
 La DCFD
o Notificar a la CA correspondiente las razones por las cuales se le va a suspender.
o Recibir las pruebas de descargo correspondientes, en caso de que las hubieran.
o Comunicar a las CA emisoras la resolución correspondiente.
Certificados de firma digital y autenticación de persona física
 Suscriptor del certificado
o Puede presentarse ante una RA de la CA que emitió el certificado y solicitar la suspensión.
o Puede solicitar la suspensión vía web, proporcionando la respuesta a la “frase desafío” (challenge phrase) que suministró durante el proceso de aplicación del certificado.
o Puede solicitar la suspensión a través del centro de atención al cliente de la CA que emitió el certificado.
o Por cualquier otro medio autorizado por la DCFD y que cumpla con un mecanismo de autenticación robusto.
 La autoridad judicial competente
o Remitir a la DCFD la resolución en la que se ordena la suspensión, los alcances y los plazos de la misma.
o La DCFD comunica a la CA emisora respectiva, la resolución judicial para suspender el certificado de firma digital emitido para el suscriptor en cuestión.
 La CA emisora
o Contar con las justificaciones para emitir la suspensión.
o Si la suspensión es recurrida ante la Dirección de Certificadores de Firma Digital, la CA emisora debe esperar la resolución de la DCFD para suspender el certificado.
o Si fuera el caso, se procede con la suspensión (o revocación) del certificado.
Certificados de sello electrónico y agente electrónico de persona jurídica
 El personero o representante con facultades suficientes de la persona jurídica suscriptora del certificado, o el tramitador de certificados digitales de persona jurídica vigente y debidamente registrado ante Registro Nacional debe:
o Presentar ante la autoridad de registro correspondiente, la documentación que lo acredita como personero o representante con facultades suficientes o tramitador de certificados digitales de la persona jurídica.
o Solicitar la suspensión del certificado.
 La autoridad judicial competente:
o Remitir a la DCFD la resolución en la que se ordena la suspensión, los alcances y los plazos de la misma.
 La CA emisora:
o Contar con las justificaciones para emitir la suspensión.
o Si la suspensión es recurrida ante la Dirección de Certificadores de Firma Digital, la CA emisora debe esperar la resolución de la DCFD para suspender el certificado.
o Si fuera el caso, se procede con la suspensión (o revocación) del certificado.
4.9.16 Límites del periodo de suspensión
De acuerdo con el artículo 8 del reglamento de la Ley 8454 de certificados, firmas digitales y documentos electrónicos, la suspensión (o revocación) se mantendrá por todo el plazo en que subsista la causal que le dio origen.
4.10 Servicios de estado de certificado
4.10.1 Características operacionales
El estado de los certificados debe estar disponible a través de los CRL publicados en un sitio Web (en el URL especificado en el CP) y para las CA emisoras de certificados de firma digital de personas físicas, es obligatorio implementar un servicio OCSP.
4.10.2 Disponibilidad del servicio
La CA debe mantener los servicios de verificación del estado de los certificados disponibles 24 x 7 x 365.
4.10.3 Características opcionales
El servicio OCSP, que permite consultar el estado de certificados es una característica opcional para la CA de la Raíz y las CAs de políticas. Sin embargo, para las CA emisoras constituye una característica obligatoria.
4.11 Finalización de la suscripción
Un suscriptor puede finalizar su suscripción de las siguientes formas:
 Revocando su certificado antes del vencimiento (fecha de expiración).
 Cuando expira el certificado.
4.12 Custodia y recuperación de llave
4.12.1 Política y prácticas de custodia y recuperación de llave
La CA no debe custodiar llaves de suscriptores para ningún certificado cuyo propósito sea de firma digital, únicamente se mantienen respaldos de sus propias llaves privadas de acuerdo con el Plan de Continuidad de Negocio.
Para los efectos de Plan de Continuidad de Negocio, las llaves privadas de las CA deben estar en custodia y respaldadas bajo estrictas normas de seguridad, y almacenadas en dispositivos criptográficos FIPS 140-2 nivel 3, que garantizan la no divulgación de las llaves.
4.12.2 Políticas y prácticas de recuperación y encapsulación de llave de sesión
Sin estipulaciones para esta sección.
