6. Controles técnicos de seguridad
En esta sección se definen las medidas de seguridad tomadas por la CA para proteger sus llaves criptográficas y los datos de activación. La gestión de las llaves es un factor crítico que permite asegurar que todas las llaves privadas están protegidas y solamente pueden ser activadas por personal autorizado.
6.1 Generación e instalación del par de llaves
La CA mantendrá controles para brindar seguridad razonable de que los pares de llaves de la CA, se generan e instalan de acuerdo con el protocolo definido para la generación de llaves.
6.1.1 Generación del par de llaves
El proceso de generación de llaves ejecutado por la CA previene la pérdida, divulgación, modificación o acceso no autorizado a las llaves privadas que son generadas. Este requerimiento aplica para toda la jerarquía nacional de certificadores registrados hasta llegar a los suscriptores.
Certificados de CA emisora
La CA debe generar las llaves mediante un proceso seguro por medio del módulo criptográfico de hardware, que cumple como mínimo el estándar Fips 140-2 nivel 3 y a un procedimiento acorde con la “ceremonia de generación de llaves” definida en el anexo D de la norma INTE/ISO 21188 “Infraestructura de llave pública para servicios financieros — Estructura de prácticas y políticas.”. La CA garantiza que la llave privada de firma nunca permanecerá fuera del módulo donde fue generada, a menos que se almacene en un mecanismo de recuperación de llaves.
El proceso de generación de llaves de CA debe producir llaves que:
a. sean apropiadas para la aplicación o propósito destinado y que sean proporcionales a los riesgos identificados;
b. usen un algoritmo aprobado en este CP, de acuerdo a la sección 7.1.3;
c. tengan una longitud de llave que sea apropiada para el algoritmo y para el período de validez del certificado de la CA, de acuerdo con la sección 6.1.5 de tamaños de llave;
d. tomen en cuenta los requisitos del tamaño de llave de la CA padre (la CA que le emitió el certificado) y subordinada (la CA que recibe el certificado);
Certificados de firma digital y autenticación de persona física
La generación de las llaves de los suscriptores requiere que los módulos de criptografía asociados cumplan al menos con el estándar Fips 140-2 nivel 2, o bien que posean al menos la certificación Common Criteria EAL 4+ en el perfil de protección SSCD tipo 3.
Certificados de sello electrónico y agente electrónico de persona jurídica
La generación de las llaves de los certificados de persona jurídica requiere que los módulos de criptografía asociados cumplan al menos con el estándar Fips 140-2 nivel 3, o bien que posean al menos la certificación Common Criteria EAL 4+ en el perfil de protección SSCD tipo 3.
Certificados de autoridad de sellado de tiempo (TSA)
La TSA debe generar las llaves mediante un proceso seguro, con un módulo criptográfico de hardware, que cumpla al menos con el estándar Fips 140-2 nivel 3.
6.1.2 Entrega de la llave privada al suscriptor
Se debe generar y mantener la llave privada dentro de los límites del módulo criptográfico, es decir el módulo criptográfico debe generar la llave privada localmente.
6.1.3 Entrega de la llave pública al emisor del certificado
Las llaves públicas transferidas deben ser entregadas a través de mecanismos que aseguren que la llave pública no se altera durante el tránsito.
Certificados de CA emisora
La llave pública debe ser entregada mediante un método fuera de banda, tal como:
· almacenado en un módulo criptográfico de la entidad;
· otros medios seguros que garanticen autenticidad e integridad.
Certificados de firma digital y autenticación de persona física
La llave pública debe ser entregada por la RA a través de medios legibles por computadoras desde una fuente autenticada;
Certificados de sello electrónico y agente electrónico de persona jurídica
La llave pública debe ser distribuida utilizando uno de los siguientes métodos:
· medios legibles por computadoras desde una fuente autenticada;
· almacenado en un módulo criptográfico de la entidad;
· otros medios seguros que garanticen autenticidad e integridad.
Certificados de autoridad de sellado de tiempo (TSA)
La llave pública debe ser entregada mediante un método fuera de banda, tal como:
· almacenado en un módulo criptográfico de la entidad;
· otros medios seguros que garanticen autenticidad e integridad.
6.1.4 Entrega de la llave pública de la CA a las partes que confían
La distribución de la llave pública se realiza a través del certificado digital y del repositorio público respectivo.
6.1.5 Tamaños de llave
El tamaño de las llaves debe ser suficientemente largo para prevenir que otros puedan determinar la llave privada utilizando cripto-análisis durante el periodo de uso del par de llaves.
Certificados de CA emisora
La llave de la CA raíz debe tener un tamaño mínimo de 4096 bits. La CA de Políticas debe mantener llaves con un tamaño mínimo de 2048 bits. Para las CA emisoras debe tener un tamaño de 2048 bits.
Certificados de firma digital y autenticación de persona física y certificados de sello electrónico y agente electrónico de persona jurídica y de TSA
El tamaño de las llaves para el suscriptor debe ser de 2048 bits. La longitud de la llave pública que será certificada por la CA, debe ser menor o igual al tamaño de la llave privada de firma de la CA.
6.1.6 Generación de parámetros de llave pública y verificación de calidad
La CA genera y verifica los parámetros de llave pública de acuerdo con el estándar FIPS 186-2 (Digital Signature Standard-DSS) que define el cripto-algoritmo utilizado en la generación.
6.1.7 Propósitos de uso de llave (Campo “keyusage” de X.509 v3)
Certificados de CA emisora
La CA Raíz únicamente podrá emitir certificados de firma para las Autoridades de Políticas y para las CRL respectivas. Las CAs de políticas únicamente podrán emitir certificados de firma a las CA emisoras y para sus CRLs.
La CA emisora no puede emitir certificados con el uso de encripción.
Certificados de firma digital y autenticación de persona física
Los suscriptores tendrán dos certificados emitidos uno con el uso de firma digital y el otro con el uso de autenticación.
· Para firmar: digitalSignature + nonRepudiation
· Para autenticarse: digitalSignature + keyEncipherment
Certificados de sello electrónico y agente electrónico de persona jurídica
Los suscriptores tendrán dos certificados emitidos uno con el uso de sello electrónico (firma digital) y el otro con el uso de agente electrónico (autenticación).
· Para sello electrónico: digitalSignature + nonRepudiation
· Para agente electrónico: digitalSignature + keyEncipherment + dataEncipherment
6.2 Controles de ingeniería del módulo criptográfico y protección de la llave privada
6.2.1 Estándares y controles del módulo criptográfico
Certificados de CA emisora
La CA debe mantener controles para asegurar que las llaves privadas de la CA permanecen confidenciales y mantienen su integridad y el acceso al hardware criptográfico de la CA está limitado a individuos autorizados.
Las llaves privadas de la CA deben ser respaldadas, guardadas y recuperadas por personal autorizado con roles de confianza, utilizando controles múltiples en un ambiente físicamente seguro.
Las copias de respaldo de las llaves privadas de la CA Raíz deben estar sujetas al mismo o mayor nivel de controles de seguridad que las llaves que actualmente están en uso. La recuperación de las llaves de la CA debe llevarse a cabo de una forma tan segura como el proceso de respaldo.
El estándar de módulos criptográficos es el “Security Requirements for Cryptographics Modules” (actualmente FIPS140). Los módulos criptográficos para las CAs Emisoras deben certificarse como mínimo con el FIPS 140-2 nivel 3.
Certificados de firma digital y autenticación de persona física
El suscriptor debe cumplir con los controles definidos en el acuerdo de suscriptor y utilizar módulos criptográficos basados como mínimo en el estándar FIPS 140-2 nivel 2, o bien que posean al menos la certificación Common Criteria EAL 4+ en el perfil de protección SSCD tipo 3.
Certificados de sello electrónico y agente electrónico de persona jurídica
Los suscriptores de certificados de persona jurídica deben cumplir con los controles definidos en el acuerdo de suscriptor y utilizar un módulo criptográfico basado como mínimo en el estándar FIPS 140-2 nivel 3, o bien que posean al menos la certificación Common Criteria EAL 4+ en el perfil de protección SSCD tipo 3.
Certificados de autoridad de sellado de tiempo (TSA)
El certificado de TSA debe cumplir con los controles definidos en el acuerdo de suscriptor y utilizar un módulo criptográfico basado como mínimo en el estándar FIPS 140-2 nivel 3.
6.2.2 Control multi-persona de llave privada (m de n)
Certificados de CA emisora
Para la activación de la llave privada de firma de la CA se debe utilizar controles de acceso de múltiples partes (es decir, “m” de “n”) con un valor mínimo de 3 para “m”.
Si las llaves privadas de la CA son respaldadas, estas deben ser respaldadas, guardadas y recuperadas por personal autorizado con roles de confianza, utilizando controles múltiples en un ambiente físicamente seguro. La cantidad de personal autorizado para llevar a cabo esta función debe mantenerse al mínimo.
Certificados de firma digital y autenticación de persona física
Sin estipulaciones.
Certificados de sello electrónico y agente electrónico de persona jurídica
Para la activación de la llave privada de sello electrónico y/o agente electrónico de persona jurídica se debe utilizar controles de acceso que resguarden la llave privada. Una vez activado el dispositivo de firma, se debe mantener resguardado físicamente y monitoreado, para evitar uso inapropiado.
Certificados de autoridad de sellado de tiempo (TSA)
Para la activación de la llave privada de firma del TSA se debe utilizar controles de acceso de múltiples partes (es decir, “m” de “n”) con un valor mínimo de 3 para “m”. Una vez activado el dispositivo de firma se debe mantener resguardado físicamente y monitoreado, para evitar otros usos.
6.2.3 Custodia de llave privada
No se deben implementar servicios de custodia de llaves de firmas emitidas a terceros.
6.2.4 Respaldo de llave privada
Los respaldos de llaves privadas de la CA son únicamente para propósitos de recuperación en caso de una contingencia o desastre. Los planes de continuidad del negocio de la CA deben incluir procesos de recuperación de desastres para todos los componentes críticos del sistema de la CA, incluyendo el hardware, software y llaves, en el caso de falla de uno o más de estos componentes.
Las copias de respaldo de las llaves privadas de la CA deberían estar sujetas al mismo o mayor nivel de controles de seguridad que las llaves que actualmente están en uso. La recuperación de las llaves de la CA debe llevarse a cabo de una forma tan segura como el proceso de respaldo.
Las llaves privadas de certificados de firma digital de los suscriptores no son respaldadas por ningún motivo en la CA, y estas permanecen dentro de los límites de los dispositivos criptográficos donde fueron generadas.
6.2.5 Archivado de llave privada
La CA no archiva la llave privada de ninguno de los suscriptores. En el caso de la CA, ésta debe archivar su par de llaves (pública y privada) en forma encriptada en concordancia con las disposiciones de protección de llaves definidas en este CP, por un plazo acorde con la legislación aplicable.
6.2.6 Transferencia de llave privada hacia o desde un módulo criptográfico
Las llaves privadas de la CA son generadas por un módulo criptográfico seguro. En el evento que una llave privada es transportada desde un módulo criptográfico a otro, la llave privada debe estar encriptada durante su transporte.
La llave privada usada para encriptar el transporte de la llave privada debe estar protegida contra divulgación no autorizada.
6.2.7 Almacenamiento de la llave privada en el módulo criptográfico
Los dispositivos criptográficos utilizados para el almacenamiento del respaldo de las llaves privadas de la CA deben ser guardados de forma segura, en un sitio alterno, para que sean recuperados en el caso de un desastre en el sitio primario
Las partes de la clave secreta o los componentes necesarios para usar y gestionar los dispositivos criptográficos de recuperación de desastres, deberían estar también guardados con seguridad en una ubicación fuera del sitio primario.
Las llaves privadas de la CA deben ser almacenadas y utilizadas dentro de un dispositivo criptográfico seguro que cumpla como mínimo con el perfil de protección apropiado de los requisitos del estándar FIPS 140-2 nivel 3
6.2.8 Método de activación de llave privada
Certificados de CA emisora
Los métodos de activación de llaves de la CA están protegidos y para accederlos se deben contar con mecanismos de autenticación de al menos dos factores de seguridad. Los datos de activación deben estar distribuidos en roles de confianza que ejecutan diversas personas.
Certificados de firma digital y autenticación de persona física
Los métodos de activación de llaves para un usuario deben contar con al menos un factor de seguridad.
Certificados de sello electrónico y agente electrónico de persona jurídica
Los métodos de activación de llaves para un usuario deben contar con al menos un factor de seguridad.
Certificados de autoridad de sellado de tiempo (TSA)
Los métodos de activación de llaves de autoridades de sellado de tiempo están protegidos mediante una combinación de al menos dos factores de seguridad. Los datos de activación deben estar distribuidos en roles de confianza que ejecutan diversas personas.
6.2.9 Método de desactivación de llave privada
Certificados de CA emisora
Para la CA Raíz y de Políticas es obligatorio que los módulos criptográficos, los cuales han sido activados, no estén desatendidos o abiertos al acceso no autorizado. Después de usarlos, estos deben ser desactivados manualmente o por un tiempo de expiración por estado pasivo. Los módulos de hardware criptográfico deben ser removidos y almacenados cuando no estén en uso.
En el caso de las CA emisoras los equipos se mantienen en línea, para dichos efectos una vez activados los dispositivos criptográficos, estos se deben mantener monitoreados y protegidos contra accesos no autorizados.
Certificados de firma digital y autenticación de persona física
Sin estipulaciones.
Certificados de sello electrónico y agente electrónico de persona jurídica
Cuando los equipos que hospedan los certificados de persona jurídica se encuentran en línea, estos se deben mantener monitoreados y protegidos contra accesos no autorizados. Cuando los equipos no estén en uso entonces los módulos de hardware criptográfico deben ser removidos y almacenados.
Certificados de autoridad de sellado de tiempo (TSA)
Cuando los equipos que hospedan el certificado sellado de tiempo se encuentran en línea, estos se deben mantener monitoreados y protegidos contra accesos no autorizados. Cuando los equipos no estén en uso entonces los módulos de hardware criptográfico deben ser removidos y almacenados.
6.2.10 Método de destrucción de llave privada
El procedimiento para la destrucción de llaves privadas debe incluir la autorización para destruirla.
Certificados de CA emisora
La CA raíz, las CA de políticas y la CA emisora deben destruir los respaldos de las llaves privadas que han expirado. Para los módulos criptográficos de hardware, estos deben ser limpiados por medio de inicialización de ceros (Zeroize Command).
Certificados de firma digital y autenticación de persona física
Los módulos criptográficos de hardware que hospedan la llave privada deben ser limpiados por medio de inicialización de ceros (Zeroize Command).
Certificados de sello electrónico y agente electrónico de persona jurídica
Los módulos criptográficos de hardware que hospedan la llave privada deben ser limpiados por medio de inicialización de ceros (Zeroize Command).
Certificados de autoridad de sellado de tiempo (TSA)
La TSA debe destruir los respaldos de las llaves privadas que han expirado. Para los módulos criptográficos de hardware, estos deben ser limpiados por medio de inicialización de ceros (Zeroize Command).
6.2.11 Clasificación del módulo criptográfico
Certificados de CA emisora
La capacidad del módulo criptográfico de la CA emisora es expresada en cumplimiento como mínimo del estándar Fips 140-2, nivel 3.
Certificados de firma digital y autenticación de persona física
El módulo criptográfico para los suscriptores de certificados de firma digital y autenticación debe cumplir como mínimo con el estándar Fips 140-2, nivel 2, o bien debe poseer al menos la certificación Common Criteria EAL 4+ en el perfil de protección SSCD tipo 3.
Certificados de sello electrónico y agente electrónico de persona jurídica
El módulo criptográfico para los certificados de persona jurídica debe cumplir como mínimo con el estándar Fips 140-2, nivel 3, o bien que posean al menos la certificación Common Criteria EAL 4+ en el perfil de protección SSCD tipo 3.
Certificados de autoridad de sellado de tiempo (TSA)
La TSA debe cumplir como mínimo con el estándar Fips 140-2, nivel 3
6.3 Otros aspectos de gestión del par de llaves
Las CA de la jerarquía nacional de certificadores registrados deben establecer los medios necesarios para gestionar en forma segura las llaves de los suscriptores durante el ciclo de vida de las mismas.
6.3.1 Archivado de la llave pública
La CA debe mantener controles para sus propias llaves, de acuerdo a lo estipulado en la sección 5.5. Las llaves archivadas de la CA deberían estar sujetas al mismo o mayor nivel de control de seguridad que las llaves que están en uso actualmente.
6.3.2 Periodo operacional del certificado y periodo de uso del par de llaves
Los periodos de uso de la llave son descritos en la sección 5.6, de acuerdo a la siguiente tabla:
Nivel de jerarquía | Tiempo de uso en años | Tiempo operacional en años
Certificado de usuario | 4 | 4
CA emisoras | 8 | 12
CA Políticas | 12 | 24
CA Raíz | 24 | 48
6.4 Datos de activación
La CA mantiene estrictos controles en los datos de activación para operar los módulos criptográficos y que necesitan ser protegidos (ejemplo un PIN, una frase de paso o “password”, una medida biométrica o una parte de llave mantenida manualmente).
6.4.1 Generación e instalación de los datos de activación
Certificados de CA emisora
Se debe contar con datos de activación de múltiples factores para protección de los accesos al uso de llaves privadas y su activación requiere de un control de múltiples partes (es decir, “m” de “n”) con un valor mínimo de tres para “m”.
Certificados de firma digital y autenticación de persona física
Se deben generar e instalar sus propios datos de activación para proteger y prevenir perdidas, robos, modificación, divulgación o uso no autorizado de sus llaves privadas.
Certificados de sello electrónico y agente electrónico de persona jurídica
Se debe contar con controles para protección de los accesos al uso de llaves privadas. En particular, se requiere generar sus propios datos de activación para prevenir uso no autorizado de la llave privada.
Certificados de autoridad de sellado de tiempo (TSA)
Se debe generar e instalar sus propios datos de activación para proteger y prevenir perdidas, robos, modificación, divulgación o uso no autorizado de sus llaves privadas. Adicionalmente, como parte de los datos de activación se requiere de un control de múltiples partes (es decir, “m” de “n”) con un valor mínimo de tres para “m”.
6.4.2 Protección de los datos de activación
Los datos de activación deberían ser memorizados, sin mantener respaldo escrito. Si se escriben, estos deberían de estar almacenados en un nivel de seguridad semejante al de los módulos criptográficos para protegerlos, y en una localización diferente a la de los módulos criptográficos.
6.4.3 Otros aspectos de los datos de activación
Los datos de activación de los módulos criptográficos de la CA Raíz y CA de Políticas deben ser cambiados al menos una vez cada año. Y en el caso de las CA emisoras o TSA la frecuencia debe ser al menos una vez cada dos meses.
6.5 Controles de seguridad del computador
El equipo de la CA debe usar sistemas operativos que:
· Requieran autenticación para poder ser accedidos
· Provean capacidad para mantener bitácoras y registros de seguridad con fines de auditoría
· Cumplan con requerimientos y controles de seguridad, al menos tan estrictos como los definidos en este CP.
Luego de que la plataforma donde opera el equipo de la CA ha sido aprobada, debe continuar operando bajo los mismos parámetros aprobados.
6.5.1 Requerimientos técnicos de seguridad de computador específicos
Los equipos donde operan los sistemas de la CA, que requieran acceso remoto deben poseer autenticación mutua y los sistemas operativos deberían estar configurados de acuerdo con los estándares del sistema operativo de la CA y ser revisados periódicamente.
Las actualizaciones y parches de los sistemas operativos deberían ser aplicados de manera oportuna y la utilización de programas utilitarios del sistema debería ser restringida al personal autorizado, y debe estar estrictamente controlado.
6.5.2 Clasificación de la seguridad del computador
Los sistemas sensibles de la CA requieren un ambiente informático dedicado y aislado, que implemente el concepto de sede computacional confiable con procesos de auditoria que ejecuten pruebas de seguridad al menos dos veces al año.
6.6 Controles técnicos del ciclo de vida
La CA debe mantener controles en los equipos de seguridad (hardware y software) requeridos para operar en una infraestructura PKI desde el momento de la compra hasta su instalación, de forma que reduzcan la probabilidad que cualquiera de sus componentes sea violentado.
Todo el hardware y software que ha sido identificado para operar las CA debe ser enviado y entregado con métodos que provean una adecuada cadena de custodia.
6.6.1 Controles para el desarrollo de sistemas
La CA debe mantener controles que proporcionen una seguridad razonable de las actividades de desarrollo y mantenimiento de los sistemas de la CA.
Los nuevos sistemas o para la expansión de los sistemas existentes, deben especificar los requisitos de control, seguir procedimientos de prueba de software y control de cambios para la implementación de software.
La CA debe mantener controles sobre el acceso a las bibliotecas fuente de programas.
6.6.2 Controles de gestión de seguridad
Los Administradores de la CA son los responsables de garantizar que se cumplan los procedimientos de seguridad correctamente. Además de ejecutar revisiones periódicas para asegurar el cumplimiento de los estándares de implementación de seguridad.
6.6.3 Controles de seguridad del ciclo de vida
La CA debe incluir controles en la gestión de seguridad por medio de herramientas y procedimientos que verifiquen la adherencia a la configuración de seguridad de los sistemas operativos y redes.
6.7 Controles de seguridad de red
El equipo de la CA debe estar dentro de los límites de la red interna, operando bajo un nivel de seguridad de red crítico. La red de la CA debe estar protegida contra ataques. Los puertos y servicios que no se requieran deben estar apagados.
En el caso de la CA Raíz debe estar off-line y aislada de la red organizacional.
Los niveles críticos de seguridad de red, deben incluir:
· La encripción de las conexiones involucradas con las operaciones de la CA.
· Los sitios Web están provistos de certificados SSL.
· La red está protegida por firewalls y sistemas de detección de intrusos.
· Los accesos externos a información de bases de datos de la CA están prohibidos.
· La CA debe controlar la ruta de acceso del usuario desde la Terminal hasta los servicios.
· Los componentes de la red local deben mantenerse en un ambiente físicamente seguro y sus configuraciones deben ser auditadas periódicamente.
· Los datos sensibles deben encriptarse cuando se intercambian sobre redes públicas o no confiables.
La CA debe definir los procedimientos de control del cambio para el hardware, los componentes de la red y los cambios de configuración del sistema.
6.8 Sellado de tiempo (“Time-Stamping”)
Los certificados, CRL y otras entradas en la base de datos de revocaciones deben contener la fecha y hora, sincronizadas utilizando los servicios UTC-6. El sellado de tiempo es una característica opcional.
