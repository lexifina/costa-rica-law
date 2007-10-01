ANEXO 1
“ESPECIFICACIONES TÉCNICAS Y FORMATO DE LOS
DOCUMENTOS ELECTRÓNICOS”
I. INTRODUCCIÓN
En la definición del contenido del presente documento, se ha considerado tanto la necesidad desde el punto de vista tributario, como comercial. El objetivo es tener un documento que sea un instrumento adecuado para el respaldo de la transacción, desde el punto de vista de las partes y que contenga la información que se requiere para efectos de un control tributario efectivo.
En este anexo se describe el formato electrónico de la Factura Electrónica, Nota de Crédito Electrónica y Nota de Débito Electrónica.
De seguido se mencionan algunos requisitos de la Factura Electrónica y otros documentos, así como se reiteran algunas obligaciones de los emisores electrónicos, las cuales se establecen de forma amplia en la resolución.
II. ESPECIFICACIONES TÉCNICAS Y FORMATO DE LOS DOCUMENTOS ELECTRÓNICOS
La Administración Tributaria (DGT) ha decidido que el formato en que se generarán los documentos tributarios electrónicos sea XML (eXtensible Markup Language) o Lenguaje Extensible de “Etiquetado”. Este metalenguaje proporciona una forma de aplicar etiquetas para describir las partes que componen un documento, permitiendo además el intercambio de documentos entre diferentes plataformas.
El tipo de información puede ser alfanumérica (ALFA) o numérica (NUM), en ambos tipos de información el tamaño indicado es el largo máximo. En la información de tipo numérica, los decimales se separan con punto. No debe separarse las miles con carácter alguno. En la información alfanumérica, algunos caracteres como ‘&’ y ‘<’ tienen un significado especial para XML y deben ser reemplazados por la secuencia de escape que el estándar define para dichos caracteres.
La modalidad tecnológica de transmisión del documento electrónico, desde el emisor al receptor electrónico, debe ser acordada entre ambos, respetando el estándar mínimo establecido por la DGT.
Toda corrección de un documento electrónico debe ser realizada vía Notas de Crédito o de Débito electrónicas.
La solución de Facturación Electrónica debe contar, como mínimo, con las siguientes funcionalidades:
• Administración, generación y recepción de respuestas de envíos hechos a otros emisores electrónicos.
• Generación de mensajes de aceptación o rechazo, dirigidas al emisor electrónico.
• Generación, recuperación y visualización de la representación impresa del documento electrónico.
• Generación del acuse de recibo electrónico de las mercancías entregadas o servicios prestados y los ajustes correspondientes.
• Identificar los documentos electrónicos emitidos para los que no se haya recibido una respuesta de envío y un acuse de recibo de las mercancías -si corresponde- de parte del receptor. De esta forma, se tendrá certeza de que cada documento emitido haya sido recibido.
• No se podrán generar documentos electrónicos con fecha anterior o posterior a la de su emisión.
• Todos los documentos electrónicos deben ser incluidos y a la vez, actualizar todos los registros.
• Contar con las validaciones necesarias que controlen la numeración para que impidan la duplicidad de números.
• Impedir la anulación de documentos electrónicos.
• Incluir validaciones lógicas y aritméticas en los campos que requieren de algún cálculo.
• Contar con los controles requeridos para el desarrollo de auditorias de tecnología de la información y comunicación.
Se debe considerar la necesidad de almacenamiento y conservación de toda la información electrónica por el plazo de prescripción vigente, independientemente que la solución lo considere o no.
El documento electrónico está constituido por las siguientes partes:
A) Datos de encabezado: corresponden a la versión, numeración e identificación del documento electrónico, condiciones de la venta, información del emisor y la información del receptor.
B) Detalle de la mercancía o servicio prestado: En esta parte se debe detallar una línea por cada artículo, especificando cantidad, valor, impuestos adicionales y valor neto, así como descuentos y recargos que afectan al total del documento y que no se requiere especificar individualmente, así como el monto total de la transacción.
C) Información de referencia: se deben detallar la razón y/o los documentos de referencia, por ejemplo se debe identificar la factura que se está modificando con una Nota de crédito o de débito.
D) Autorización: corresponde al número y fecha de la presente resolución.
E) Otros: comprende la información requerida para las relaciones de comercio electrónico entre las partes, que no contravenga lo establecido en la presente resolución.
El formato para los documentos electrónicos es único, así como en su forma electrónica o impresa, lo que los diferencia es la obligatoriedad de los campos según el tipo de documento. Los códigos que se utilizarán son los siguientes:
CÓDIGOS DE OBLIGATORIEDAD:
0: No corresponde. Significa que el dato no debe ir en un determinado documento.
1: Dato obligatorio. El dato debe estar en el documento siempre, independiente de las características de la transacción.
2: Dato condicional. El dato no es obligatorio en todos los documentos, pero pasa a ser obligatorio en determinadas operaciones si se cumple una cierta condición. Por ejemplo si hay descuentos o recargos, éstos deben estar registrados porque en caso contrario los montos del documento son inconciliables, en relación con los montos de Neto, Impuesto de Ventas y Total.
3: Opcional.
ENCABEZADO
Descripción del campo | Nombre de la etiqueta | Tipo del campo | Tamaño | Obligatoriedad
| | | | FACTURA | NOTA CRÉDITO | NOTA DÉBITO
Versión del documento electrónico (V1.0) | VersionDoc | Numérico | 4 | 1 | 1 | 1
Tipo de documento electrónico (ver nota 1/ 2/ 6/ ) | TipoDoc | Numérico | 2 | 1 | 1 | 1
Numeración consecutiva del comprobante (ver notas 1/ 3/) | NumConsecutivoCompr | Numérico | 13 | 1 | 1 | 1
Fecha y hora de Emisión del documento electrónico (ver nota 4/) | FechaEmisionDoc | Fecha (AAAA-MM-DD: HH:MM:SS) | 19 | 1 | 1 | 1
Condiciones de la venta: crédito, contado, otros. (ver notas 5/6/ ) | CondicionVenta | Numérico | 2 | 1 | 1 | 1
Nombre o razón social del emisor | NombreEmisor | Alfanumérico | 80 | 1 | 1 | 1
Número de cédula física/ jurídica emisor | NumCedulaEmisor | Numérico | 10 | 1 | 1 | 1
Nombre comercial emisor | NombreComercialEmisor | Alfanumérico | 80 | 1 | 1 | 1
Dirección Emisor | DireccionEmisor | Alfanumérico | 80 | 1 | 0 | 0
Número de teléfono emisor | NumeroTelEmisor | Numérico | 7 | 1 | 0 | 0
Número de fax emisor | NumeroFaxEmisor | Numérico | 7 | 3 | 0 | 0
Dirección del correo electrónico del emisor | CorreoElectronicoEmisor | Alfanumérico | 30 | 1 | 0 | 0
Nombre o razón social del comprador (receptor) | NombreReceptor | Alfanumérico | 80 | 1 | 1 | 1
Número de cédula física/ jurídica comprador (receptor) | NumCedulaReceptor | Numérico | 10 | 1 | 1 | 1
Dirección comprador (receptor) | DireccionReceptor | Alfanumérico | 80 | 2 | 0 | 0
1/ Los campos Tipo de documento electrónico y Numeración consecutiva del comprobante deben quedar a la par.
2/ La codificación a utilizar en el campo Tipo de documento se deben utilizar los siguientes códigos:
Tipo de Documento | Código
Factura electrónica | 01
Nota de débito electrónica | 02
Nota de crédito electrónica | 03
3/ La numeración de los comprobantes electrónicos iniciará en 1 y la asignará el sistema automáticamente en el momento de la confirmación del envío.
4/ En la representación impresa del documento electrónico, el campo Fecha de Emisión del documento, no necesariamente tiene que visualizarse en el formato AAAA-MM-DD, sino que puede
ser con el mes en letras o cambiando el orden en que aparecen el año, el mes y día; con el fin de facilitar su lectura.
5/ En las Condiciones de la venta, se debe utilizar la siguiente codificación:
Condiciones de la venta | Código
Contado | 01
Crédito | 02
Consignación | 03
Apartado | 04
Arrendamiento con opción de compra | 05
6/ Para efectos de visualización e impresión se mostrará su descripción.
B. DETALLE DE LA MERCANCIA O SERVICIO PRESTADO
Descripción del campo | Nombre de la etiqueta | Tipo del campo | Tamaño | Obligatoriedad
| | | | FACTURA | NOTA CRÉDITO | NOTA DÉBITO
Código de producto/servicio | CódigoProducto | Alfanumérico | 13 | 3 | 2 | 2
Cantidad | Cantidad | Numérico | 13 | 1 | 2 | 2
Unidad de medida | UnidadMedida | Alfanumérico | 13 | 1 | 2 | 2
Detalle de la mercancía transferida o servicio prestado | DetalleMerc | Alfanumérico | 160 | 1 | 2 | 2
Precio unitario | PrecioUnitario | Numérico | 15 | 1 | 2 | 2
Monto total | MontoTotal | Numérico | 15 | 1 | 2 | 2
Monto de descuentos concedidos | MontoDescuento | Numérico | 15 | 3 | 2 | 2
Naturaleza del descuento | NaturalezaDescuento | Alfanumérico | 80 | 2 | 2 | 2
Subtotal | Subtotal | Numérico | 15 | 1 | 1 | 1
Código del impuesto (ver notas 6/ 7/) | CodigoImpuesto | Numérico | 2 | 2 | 2 | 2
Monto del impuesto selectivo de consumo u otros tributos aplicables (calculado después de aplicar la tasa de impuesto respectiva) | MontoOtrosImp | Numérico | 15 | 2 | 2 | 2
Total servicios gravados | TotalSerGravados | Numérico | 15 | 2 | 2 | 2
Total servicios exentos | TotalSerExentos | Numérico | 15 | 2 | 2 | 2
Total mercancías gravadas | TotalMerGravadas | Numérico | 15 | 2 | 2 | 2
Total mercancías exentas | TotalMerExentas | Numérico | 15 | 2 | 1 | 1
Monto total neto | TotalNeto | Numérico | 15 | 1 | 1 | 1
Tasa del impuesto de ventas | TasaImpVentas | Numérico | 2 | 2 | 2 | 2
Impuesto de ventas (monto calculado después de aplicar la tasa del impuesto) | MontoImpVentas | Numérico | 15 | 2 | 2 | 2
Total de la factura | TotalFactura | Numérico | 15 | 1 | 1 | 1
7/ El desglose de los códigos de impuesto es el siguiente:
Impuesto | Código
Impuesto General sobre las Ventas | 01
Impuesto Selectivo de Consumo | 02
Otros tributos aplicables | 35
Servicio | 40
Impuesto I.C.T. | 41
C. INFORMACIÓN DE REFERENCIA
Las referencias se utilizarán para los siguientes casos:
a) Nota de Crédito que elimina un documento de referencia en forma completa, ya sea una Factura de venta o Nota de débito.
b) Nota de crédito que corrige un texto del documento de referencia (ver campo Corrección Factura).
c) Nota de Débito que elimina una Nota de Crédito en la referencia en forma completa.
d) Notas de crédito o débito que corrigen montos de otro documento.
Los casos a) b) y c) deben tener un único documento de referencia.
Descripción del campo | Nombre de la etiqueta | Tipo del campo | Tamaño | Obligatoriedad
| | | | FACTURA | NOTA CRÉDITO | NOTA DÉBITO
Código de referencia (ver nota 8/) | CodigoReferencia | Numérico | 1 | 0 | 2 | 2
Razón de referencia | RazonReferencia | Alfanumérico | 180 | 0 | 2 | 2
8/ Los códigos de referencia a utilizar son:
| Código
Anula Documento de Referencia | 1
Corrige texto documento de referencia | 2
Corrige monto | 3
D. AUTORIZACIÓN
Descripción del campo | Nombre de la etiqueta | Tipo del campo | Tamaño | Obligatorio
Número de Resolución | NumResolucion | Alfanumérico | 13 | SI
Fecha y hora de resolución 4/ | FechaResolucion | Fecha (AAAA-MM-DD: HH: MM:SS) | 19 | SI
E. OTROS
Descripción del campo | Nombre de la etiqueta | Tipo del campo | Tamaño | Obligatoriedad
| | | | FACTURA | NOTA CRÉDITO | NOTA DÉBITO
Otros | Otros | Alfanumérico | 2000 | 3 | 3 | 3
III. FORMATO PARA LA CONFIRMACIÓN DE ACEPTACIÓN O RECHAZO DE LOS DOCUMENTOS ELECTRÓNICOS
Para la aceptación o rechazo de los documentos electrónicos recibidos, deben utilizar el siguiente formato.
Descripción del campo | Nombre de la etiqueta | Tipo del campo | Tamaño | Obligatorio
Nombre o razón social del emisor | NombreEmisor | Alfanumérico | 80 | SI
Número de cédula física/ jurídica emisor | NumCedulaEmisor | Numérico | 10 | SI
Fecha y hora de la transacción (Ver nota 4/) | FechaEmisionDoc | Fecha (AAAA-MM-DD: HH: MM:SS) | 19 | SI
Número de comprobante | NumConsecutivoCompr | Numérico | 13 | SI
Tipo de documento | TipoDoc | Numérico | 2 | SI
Mensaje (ver nota 9/) | Mensaje | Numérico | 1 | SI
Detalle del mensaje | DetalleMensaje | Alfanumérico | 80 | Opcional
Número Consecutivo de recepción | NumConsecutivorecep | Numérico | 15 | SI
9/ Los códigos para la descripción del mensaje son:
Mensaje | Código
Aceptado | 1
Rechazado | 9
