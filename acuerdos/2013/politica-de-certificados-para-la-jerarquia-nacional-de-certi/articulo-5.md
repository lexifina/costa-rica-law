5. Controles operacionales, de gestión y de instalaciones
La Autoridad Certificadora Raíz mantiene controles de seguridad no-técnicos (esto es, controles físicos, procedimientos y de personal) para asegurar la ejecución de las funciones de generación de llave, autenticación de los sujetos, emisión del certificado, revocación del certificado, auditoría y almacenamiento.
5.1 Controles físicos
5.1.1 Localización y construcción del sitio
Las operaciones de la CA deben estar dentro de un ambiente de protección física que impida y prevenga usos o accesos no autorizados o divulgación de información sensible.
Las instalaciones de la CA deben contar con al menos cuatro perímetros de seguridad física (área de recepción, área de servicios de soporte - climatización, energía, comunicaciones, etc.-, área de operación de la CA, área de custodia de material criptográfico). Un perímetro es una barrera o entrada que provee un control de acceso para individuos y requiere una respuesta positiva para proceder a ingresar a la siguiente área. Cada perímetro sucesivo se encuentra más restringido, con controles de acceso más estrictos.
Las instalaciones donde se crean los certificados de la CA se deben proteger con su propio y único perímetro físico, y las barreras físicas (paredes, barrotes) deben ser sólidas, extendiéndose desde el piso real al cielo raso real. Asimismo, estas barreras deben prevenir las emisiones de radiación electromagnética.
5.1.2 Acceso físico
Los controles de acceso físico deben evitar el acceso no autorizado a las instalaciones de la CA. Adicionalmente, el acceso al recinto donde se encuentran las operaciones de la autoridad certificadora debe utilizar controles con 2 factores de autenticación como mínimo (al menos uno de ellos debe ser biométrico).
Cuando las instalaciones operacionales de la CA estén desocupadas, deben estar cerradas con llave y con las alarmas debidamente activadas.
Los perímetros deben ser auditados y controlados para verificar que solo puede tener acceso el personal autorizado debidamente identificado.
Los derechos de acceso a las instalaciones de la CA deben revisarse y actualizarse regularmente, al menos cada seis meses o cuando se presente movimiento en el personal relacionado con labores de operación de la CA.
Los visitantes o personal de servicio de soporte tercerizado que requiera acceso a las instalaciones operacionales de la CA, deben ser escoltados y registrarse el responsable de autorizar el acceso, la fecha y hora de entrada y salida.
5.1.3 Energía y aire acondicionado
El equipo de la autoridad certificadora debe protegerse contra fallas en el fluido eléctrico corriente y otras anomalías en la energía.
Las instalaciones de la CA deben estar equipadas con sistemas de energía primario y de respaldo para asegurar continuidad del fluido eléctrico.
Las instalaciones deben contar con sistemas de aire acondicionado redundantes. El equipo instalado para climatizar el recinto, debe ser capaz de controlar la humedad relativa del mismo.
5.1.4 Exposiciones al agua
Las instalaciones de la CA deben ser construidas y equipadas, y contar con procedimientos implementados para prevenir inundaciones y otros daños por exposición al agua.
5.1.5 Prevención y protección contra fuego
Las instalaciones de la CA deberán contar con procedimientos implementados para la prevención y protección al fuego. Además de ser construidas y equipadas para prevenir, detectar y suprimir incendios o daños producidos por la exposición a llamas o humo.
5.1.6 Almacenamiento de medios
La CA debe asegurar el adecuado manejo y protección de los medios de almacenamiento de información, que contengan datos críticos o sensitivos del sistema, contra daños accidentales (agua, fuego, electromagnetismo) y debe impedir, detectar y prevenir su uso no autorizado, acceso o su divulgación.
5.1.7 Eliminación de residuos
La CA debe implementar controles para la eliminación de residuos (papel, medios, equipos y cualquier otro desecho) con el fin de prevenir el uso no autorizado, el acceso o divulgación de información privada y confidencial contenida en los desechos.
5.1.8 Respaldo fuera de sitio
La CA debe mantener respaldos de los datos críticos del sistema y de cualquier otra información sensitiva, incluyendo los datos de auditoría, en una instalación segura fuera del sitio principal.
5.2 Controles procedimentales
5.2.1 Roles de confianza
Los empleados, contratistas y consultores designados para gestionar la infraestructura de confianza deben ser considerados “personas de confianza” sirviendo en “roles de confianza”.
Los roles de confianza deben incluir, al menos, roles que contemplen las siguientes responsabilidades:
a. responsabilidad general de administrar la implementación de las prácticas de seguridad de la CA;
b. aprobación de la generación, revocación y suspensión de los certificados;
c. instalación, configuración y mantenimiento de los sistemas de la CA;
d. operación diaria de los sistemas de la CA, respaldo y recuperación de sistemas;
e. funciones de auditoria interna para ejecutar la inspección y mantenimiento de las bitácoras del sistema de la CA y de los registros de auditoría;
f. funciones de gestión del ciclo de vida de llaves criptográficas (ejemplo, custodios de componentes de llaves);
g. desarrollo de sistemas de la CA.
5.2.2 Número de personas requeridas por tarea
La CA debe establecer, mantener y ejecutar procedimientos de control rigurosos para asegurar la segregación de funciones, basados en las responsabilidades del trabajo y la cantidad de personas de confianza que ejecutan las tareas sensitivas.
5.2.3 Identificación y autenticación para cada rol
La CA debe confirmar la identidad y autorización de todo el personal que intente iniciar labores de confianza. La autenticación de la identidad debe incluir la presencia física de la persona y una verificación por medio de documentos vigentes de identificación legalmente reconocidos, tales como la cédula de identidad para los ciudadanos costarricenses, o el documento único de permanencia, en caso de extranjeros.
5.2.4 Roles que requieren separación de funciones
Los roles que requieren separación de los deberes incluyen (pero no está limitado) a los encargados de ejecutar las siguientes responsabilidades:
 La validación de información en aplicaciones de certificado y de solicitudes o información del suscriptor.
 La aceptación, rechazo, otros procesamientos de la aplicación de certificado, solicitud de revocación, información de afiliación.
 La emisión, o revocación de los certificados, incluyendo personal con acceso a porciones restringidas del repositorio.
 La generación, emisión o destrucción de los certificados de la CA.
 La puesta en operación de la CA en producción.
 La auditoría interna de la operación de la CA y RA debe ser ejecutada por un rol particular.
5.3 Controles de personal
5.3.1 Requerimientos de experiencia, capacidades y autorización
Las personas seleccionadas para laborar en roles de confianza deben contar con un contrato y deben:
 Haber aprobado exitosamente el programa de entrenamiento apropiado.
 Haber demostrado capacidad para ejecutar sus deberes.
 Haber aceptado las cláusulas de confidencialidad.
 No poseer otros deberes que puedan interferir o causar conflicto con los de la CA.
 No tener antecedentes de negligencia o incumplimiento de labores.
 No tener antecedentes penales.
5.3.2 Procedimientos de verificación de antecedentes
La CA debe contar con procedimientos para verificar la experiencia y los antecedentes del personal que intenta obtener un rol de confianza. Algunos aspectos de la investigación de antecedentes incluyen:
 Confirmación de empleos anteriores.
 Verificación de referencias profesionales.
 Título académico obtenido.
 Búsqueda de antecedentes criminales.
 Verificación de registros financieros y crediticios.
La verificación de registros financieros y crediticios debe ser repetida para el personal de confianza al menos una vez cada tres años.
Los antecedentes deben ser evaluados por la CA para tomar las acciones que sean razonables, de acuerdo al tipo, magnitud y frecuencia del comportamiento descubierto por la investigación respectiva. Los factores revelados en el proceso de verificación pueden ser considerados como motivos para retirar al funcionario del puesto de confianza.
5.3.3 Requerimientos de capacitación
Todo el personal involucrado en las operaciones de la CA debe estar capacitado apropiadamente, en aspectos tales como: operación del software y hardware, políticas y procedimientos organizacionales, procedimientos de seguridad y operacionales, y las estipulaciones legales.
5.3.4 Requerimientos y frecuencia de re-capacitación
La CA debe capacitar al personal cuando se presenten cambios significativos en las operaciones de la CA, por ejemplo cuando se producen actualizaciones de hardware o software, cambios en los sistemas de seguridad, etc.
La CA debe proveer los programas de entrenamiento y actualización a su personal para asegurar que el personal mantiene el nivel requerido de eficiencia para ejecutar sus labores satisfactoriamente.
5.3.5 Frecuencia y secuencia en la rotación de las funciones
La CA debe efectuar una rotación de sus roles de trabajo. La frecuencia de la rotación del personal debe ser al menos:
 una vez cada tres años, para la CA emisora.
 una vez cada cinco años, para la CA Raíz.
Antes de asumir las nuevas labores, el personal debe recibir a una actualización de la capacitación que le permita asumir las tareas satisfactoriamente.
5.3.6 Sanciones para acciones no autorizadas
La CA debe ejecutar las acciones administrativas y disciplinarias apropiadas contra el personal que violente las normas de seguridad establecidas en esta política o su CPS, de acuerdo a lo estipulado en el contrato de trabajo definido para los roles de confianza. Además debe llevar un registro de la frecuencia y severidad de las acciones, con el fin de determinar la sanción que debe ser aplicada.
5.3.7 Requerimientos para contratistas independientes
La CA puede contratar personal externo o consultores solamente si existe una relación claramente definida con el contratista y bajo las siguientes condiciones:
 existe un contrato con cláusulas propias de los roles de confianza y estipula sanciones para las acciones no autorizadas.
 no se posee personal disponible para llenar los roles de confianza contratados.
 los contratistas o consultores cumplen con los mismos requisitos del punto 5.3.1.
 una vez finalizado el servicio contratado se revocan los derechos de acceso.
5.3.8 Documentación suministrada al personal
La CA debe suministrar suficiente documentación al personal para que ejecute un rol, donde se definen los deberes y procedimientos para el correcto desempeño de su función.
5.4 Procedimientos de bitácora de auditoría
La CA debe mantener controles para proveer una seguridad razonable de que:
· los eventos relacionados con el ambiente de operación de la CA, la gestión de las llaves y los certificados, son registrados exacta y apropiadamente;
· se mantiene la confidencialidad y la integridad de los registros de auditoría vigentes y archivados;
· los registros de auditoría son archivados completa y confidencialmente;
· los registros de auditoría son revisados periódicamente por personal autorizado.
5.4.1 Tipos de eventos registrados
La CA debe registrar los tipos de eventos que se presentan en sus operaciones. La CA debe mantener las bitácoras manuales o automáticas, indicando para cada evento la entidad que lo causa, la fecha y hora del mismo. La CA debe registrar los eventos relacionados con:
· la gestión del ciclo de vida de las llaves de la CA;
· la gestión del ciclo de vida del dispositivo criptográfico;
· la gestión del ciclo de vida del sujeto de certificado;
· la información de solicitud de certificados;
· la gestión del ciclo de vida del certificado;
· los eventos sensibles de seguridad;
Las bitácoras de auditoría no deben registrar las llaves privadas de ninguna forma y los relojes del sistema de cómputo de la CA deben estar sincronizados con el servicio de tiempo UTC-6 para un registro exacto de los eventos.
5.4.2 Frecuencia de procesamiento de la bitácora
El personal de la CA emisora con el rol de auditor debe realizar al menos tres revisiones por año de las bitácoras de auditoría, sin necesidad de ser avisadas; mientras que la CA de la Raíz debe realizar al menos una revisión anual de las bitácoras.
Además de las revisiones oficiales, las bitácoras de auditoría deben ser revisadas en respuesta a una alerta, por irregularidades o incidentes dentro de los sistemas de la CA.
El procesamiento de la bitácora de auditoría consiste en una revisión de las bitácoras y la documentación de los motivos para los eventos significativos, y todas las acciones deben ser documentadas.
Las bitácoras de auditorías actuales y archivadas deben ser recuperadas solamente por personal autorizado, ya sea por razones válidas del negocio o por seguridad.
5.4.3 Periodo de retención para la bitácora de auditoría
Las bitácoras de auditoría deben ser mantenidas en el sistema por al menos dos meses posterior a su procesamiento y deber ser archivadas de acuerdo a la sección 5.5.2.
5.4.4 Protección de bitácora de auditoría
Las bitácoras de auditorías actuales o archivadas deben mantenerse de forma que se prevenga su revelación, modificación, destrucción no autorizada o cualquier otra intromisión.
5.4.5 Procedimientos de respaldo de bitácora de auditoría
La CA debe mantener copias de respaldo de todos los registros auditados.
5.4.6 Sistema de recolección de auditoría (interno vs. externo)
Los procesos de auditoría de seguridad deben ejecutarse independientemente y no deben, de ninguna forma, estar bajo el control de la CA, los procesos de auditoría deben ser invocados al iniciar el equipo y terminarlos solo cuando el sistema es apagado.
En caso de que el sistema automatizado de auditoría falle, la operación de la CA debe cesar hasta que las capacidades de auditoría puedan ser reestablecidas.
5.4.7 Notificación al sujeto que causa el evento
Cuando un evento es almacenado por la bitácora, no se requiere notificar al causante de dicho evento.
5.4.8 Evaluación de Vulnerabilidades
La CA y el personal operativo deben estar vigilantes de intentos para violar la integridad del sistema de generación de certificados, incluyendo equipo, localización física y personal. Las bitácoras deben ser revisadas por un auditor de seguridad para los eventos que poseen acciones repetitivas, solicitudes para información privilegiada, intentos de acceso al sistema de archivos y respuestas no autenticadas.
Los equipos donde se ejecutan las operaciones de la CA emisora deben someterse a análisis semestrales de vulnerabilidades.
5.5 Archivado de registros
5.5.1 Tipos de registros archivados
La CA debe almacenar los registros para establecer la validez de una firma y de la operación propia de la infraestructura PKI. Se deben archivar los siguientes datos:
Durante la inicialización del sistema de la CA:
· la acreditación de la CA (si es necesaria);
· el CP y el CPS;
· cualquier acuerdo contractual para establecer los límites de la CA;
· la configuración del sistema.
· Durante la operación de la CA:
· modificaciones o actualizaciones de cualquiera de los ítems anteriores;
· solicitudes de certificados o de revocación;
· documentación para autenticar la identidad del suscriptor;
· documentación de recepción y aceptación del certificado;
· documentación de recepción de dispositivos de almacenamiento de llaves;
· todos los certificados y CRLs (información de revocación) tanto emitidos o publicados;
· bitácoras de auditoría;
· otros datos o aplicaciones para verificar el contenido de los archivos;
· todos los trabajos comunicados o relacionados a políticas, otras CA y cumplimiento de auditoría.
5.5.2 Periodos de retención para archivo
Todos los archivos deben mantenerse por un periodo de al menos diez años. Además de mantener los controles para que los archivos puedan ser leídos durante el periodo de retención definido.
5.5.3 Protección de archivo
Los archivos no deben modificarse o eliminarse por alguna operación no autorizada del equipo de la CA. La CA debe mantener la lista de personas autorizadas a mover los registros a otros medios.
Los medios de almacenamientos deben estar guardados en instalaciones seguras, los registros deben ser etiquetados con un nombre distintivo, la fecha y hora de almacenamiento y la clasificación del tipo de información.
5.5.4 Procedimientos de respaldo de archivo
La CA debe mantener procedimientos adecuados de respaldo de archivos (físicos y electrónicos), tanto en el sitio principal como en el alterno, que aseguren la disponibilidad de los mismos, de acuerdo a un análisis de riesgos determinado por los factores de operación de la CA.
5.5.5 Requerimientos para sellado de tiempo de registros
Los certificados, las listas de revocación (CRL) y otras entradas en la bases de datos de revocación debe contener información de fecha y hora. Esta información de fecha y hora no necesita tener una base criptográfica, pero si debe estar sincronizada con el servicio de tiempo de la UTC-6.
5.5.6 Sistema de recolección de archivo (interno o externo)
Los sistemas de archivos de la CA son internos al ámbito de sus operaciones y deben conservar las pistas de auditoría.
5.5.7 Procedimientos para obtener y verificar la información archivada
Solamente el personal de confianza autorizado está habilitado para obtener acceso al archivo. La CA debe realizar pruebas de restauración de la información archivada al menos una vez al año. La integridad de la información debe ser verificada cuando es restaurada.
5.6 Cambio de llave
La CA debe cambiar periódicamente sus llaves de firma, de acuerdo con los años de validez de sus certificados en la jerarquía nacional de certificadores registrados (tiempo de uso) y considerando que el último certificado otorgado debe poder ser verificado durante su vigencia (tiempo operacional), tal como se muestra en el siguiente cuadro:
Nivel de jerarquía | Tiempo máximo de uso en años | Tiempo operacional en años | Descripción
Certificado de suscriptores | 4 | 4 | El certificado emitido al usuario es otorgado por un máximo de 4 años, al finalizar ese periodo pierde su validez.
CA emisoras | 8 | 12 | A la CA emisora se le otorga un certificado con una validez de máximo 8 años, durante ese periodo puede emitir certificados a los usuarios o suscriptores. Sin embargo el último certificado emitido antes de vencer su validez, debe tener la misma efectividad, es decir, cuatro años para el usuario o suscriptor. Entonces su tiempo de uso es 8 años (con capacidad para emitir certificados de suscriptor), pero dura cuatro años más en operación para validar las listas de revocación, de ahí que el tiempo operacional es por 12 años.
CA Políticas | 12 | 24 | La CA de políticas tiene una validez de máximo 12 años, y el último certificado otorgado a una CA emisora debe garantizar la operación por doce años más. Por estos motivos el periodo operacional de la CA de Políticas debe ser de al menos 24 años.
CA Raíz | 24 | 48 | Siguiendo el mismo criterio la validez de la CA Raíz es máximo 24 años, más 24 años que pueda operar la CA de Política, da como resultado los 48 años de tiempo operacional para el certificado de la CA Raíz.
Del cuadro anterior, se deduce que en determinado momento puede haber dos certificados del mismo nivel y tipo activos, donde el tiempo de traslape de la vigencia de los certificados debe ser de al menos el tiempo operacional del certificado de un suscriptor.
Los responsables de las CAs tendrán la obligación de garantizar que el tiempo máximo de uso en años de los certificados de niveles inferiores se ajusta con el tiempo operacional de todos los niveles superiores.
5.7 Recuperación de desastre y compromiso
5.7.1 Procedimientos para el manejo de incidente y compromiso
La CA debe contar con políticas y procedimientos formales para el reporte y atención de incidentes.
La funcionarios ejecutando roles de confianza deben velar por la seguridad de las instalaciones y la CA debe mantener procedimientos para que estos funcionarios reporten los incidentes.
La CA debe mantener un plan de recuperación de desastres, si el equipo de la CA es dañado entonces las operaciones de la CA deben reestablecerse lo más pronto posible, dando prioridad a la capacidad de revocar certificados de suscriptor.
Si la CA no puede ser reestablecida dentro de una semana, entonces su llave se reporta como comprometida y todos sus certificados son revocados. En casos excepcionales, la DCFD puede otorgar extensiones para la CA.
5.7.2 Corrupción de datos, software y/o recursos computacionales
Posterior a una corrupción de recursos computacionales, software o datos, la CA afectada debe realizar, en forma oportuna, un reporte del incidente y una respuesta al evento.
5.7.3 Procedimientos de compromiso de llave privada de la entidad
La CA debe mantener controles para brindar una seguridad razonable de que la continuidad de las operaciones se mantenga en caso de compromiso de las llaves privadas de la CA.
Los planes de continuidad del negocio de la CA deben referirse al compromiso o sospecha de compromiso de las llaves privadas de la CA como un desastre.
En caso de que la llave de la CA se haya comprometido, el superior de la CA deberá revocar el certificado de CA, y la información de la revocación debe publicarse inmediatamente.
5.7.4 Capacidad de continuidad del negocio después de un desastre
La CA debe contar con un proceso administrativo para desarrollar, probar, implementar y mantener sus planes de continuidad del negocio.
La CA debe desarrollar, probar, mantener e implementar un plan de recuperación de desastres destinado a mitigar los efectos de cualquier desastre natural o producido por el hombre. Los planes de recuperación de desastres se enfocan en la restauración de los servicios de sistemas de información y de las funciones esenciales del negocio.
El sitio alterno debe contar con protecciones de seguridad física equivalentes al sitio principal.
El sitio alterno, deben tener la capacidad de restaurar o recobrar operaciones esenciales dentro de las veinticuatro horas siguientes al desastre, con al menos soporte para las siguientes funciones: revocación de certificados y publicación de información de revocación.
5.8 Terminación de una CA o RA
En caso de que la terminación de la CA se dé por conveniencia, reorganización, o por otras razones que no estén relacionadas con la seguridad, entonces se deben tomar las previsiones antes de terminar la CA para evitar el compromiso de toda la infraestructura. En este caso, puede ser que ningún certificado firmado por la CA deba ser revocado.
En caso de que la terminación de la CA esté relacionada con eventos de seguridad, entonces la CA debe considerarse como una CA comprometida.
Antes de la terminación de la CA, toda la información relacionada con la operación de la CA deben ser enviados a la DCFD para su custodia.
Cuando se presenta la terminación de una RA, todos los archivos de datos deben ser enviados a la CA respectiva para su custodia.
Si se presenta un compromiso de la llave de la CA o un desastre donde las instalaciones de la CA están físicamente dañadas y todas las copias de las llaves de firma de la CA están destruidos, entonces la CA debe solicitar que se revoque su certificado.
Cada CA o RA debe desarrollar un plan de terminación que minimice el impacto y la interrupción del servicio provisto a los clientes, suscriptores y partes que confían. Dicho plan debe darle tratamiento al menos a los siguientes puntos:
· Notificación a las partes afectadas asumiendo el costo de la misma.
· Procedimiento de revocación del certificados (de la CA, CA subordinadas, los utilizados en RA para sus operaciones, suscriptores, etc. según sea el caso).
· La preservación de toda la información en concordancia con este CP y la normativa aplicable.
· La continuación de los servicios de validación de los certificados y de soporte a los suscriptores.
· Procedimientos para la eliminación de las llaves privadas y del hardware que las contiene.
· Disposiciones para la transición de los servicios a una CA sucesora.
