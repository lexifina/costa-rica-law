ANEXO 2
“INFORMACIÓN ELECTRÓNICA DE COMPRAS Y VENTAS”
Con respecto a la generación de la información electrónica de compras y ventas, cada uno de los archivos está constituido por: el detalle por documento y el resumen de la información por período, que se genera una vez al mes.
Cada vez que se emita un documento electrónico por compras, ventas y servicios, así como ajustes a este tipo de operaciones, se debe registrar la información de forma separada en cada archivo de: Información Electrónica de Compras y el de Información Electrónica Ventas, según corresponda.
Al finalizar el período fiscal, se debe incorporar la información de los documentos no electrónicos en cada archivo para generar el resumen del período.
La estructura del archivo-detalle de la Información Electrónica de Compras, es la siguiente:
Información Electrónica de Compras -Detalle del Período- Mes: _________ Año:________
Descripción del campo | Nombre de la etiqueta | Tipo del campo | Tamaño | Obligatorio
Fecha de factura o comprobante de compra | FechaEmisionDoc | Fecha (AAAA-MM-DD) | 10 | SI
Número de la factura o comprobante de compra | NumConsecutivo | Numérico | 13 | SI
Tipo de documento (Ver nota 10/ ) | TipoDoc | Numérico | 2 | SI
Nombre o razón social del emisor | NombreEmisor | Alfanumérico | 80 | SI
Número de cédula física/ jurídica emisor | NumCedulaEmisor | Numérico | 10 | SI
Monto total de las compras exentas | TotalComprasExentas | Numérico | 15 | SI
Monto total de las compras gravadas | TotalComprasgravadas | Numérico | 15 | SI
Monto total impuesto Ventas pagado | TotalImpuestoVtas | Numérico | 15 | SI
Monto total Mensual de compras | TotalMensualCompras | Numérico | 15 | SI
10/ La codificación a utilizar en el campo Tipo de documento es la siguiente, sin embargo para efectos de impresión y visualización se debe mostrar la descripción del nombre:
Tipo de Documento | Código
Factura electrónica | 01
Factura manual | 04
Otros comprobantes manuales | 05
Se debe efectuar un archivo con la Información Electrónica de Compras, para cada tipo de documento con la estructura indicada, debiéndose incorporar la información de los comprobantes físicos, de acuerdo con los códigos definidos en la nota 10/.
La estructura del archivo-detalle de la Información Electrónica de Ventas, es la siguiente:
Información Electrónica de Ventas -Detalle del Período- Mes: _________ Año:________
Descripción del campo | Nombre de la etiqueta | Tipo del campo | Tamaño | Obligatorio
Fecha de factura o comprobante de ventas | FechaEmisionDoc | Fecha (AAAA-MM-DD) | 10 | SI
Número de la factura o comprobante de venta | NumConsecutivo | Numérico | 13 | SI
Nombre o razón social del comprador (receptor) | NombreReceptor | Alfanumérico | 80 | SI
Número de cédula física/ jurídica comprador (receptor) | NumCedulaReceptor | Numérico | 10 | SI
Número de Orden de Compra o documento equivalente (Ver nota 11/ ) | NumOrdenCompra | Numérico | 13 | Condicional
Fecha de Orden de Compra (Ver nota 11/ ) | FechaEmisionOrden | Fecha (AAAA-MM-DD) | 10 | Condicional
Tipo de documento (Ver nota 10/ ) | TipoDoc | Numérico | 2 | SI
Monto total de las ventas exentas | TotalVentasExentas | Numérico | 15 | SI
Monto total de exportaciones | TotalExportaciones | Numérico | 15 | SI
Monto total de las ventas gravadas | TotalVentasgravadas | Numérico | 15 | SI
Monto total impuesto Ventas cobrado | TotalImpuestoVtas | Numérico | 15 | SI
Monto total Mensual de Ventas | TotalVentas | Numérico | 15 | SI
Se debe efectuar un archivo con la Información Electrónica de Ventas, para cada tipo de documento, utilizando la misma estructura, debiéndose incorporar la información de los comprobantes físicos de acuerdo con los códigos definidos en la nota 10/.
11/ Para aquellos que por Ley y Reglamento así esté establecido.
Por último, se genera el resumen del período de la Información Electrónica de Compras y Ventas, conforme el siguiente formato.
Información Electrónica de Compras y Ventas -Resumen del Período- Mes: _________ Año:________
Descripción del campo | Nombre de la etiqueta | Tipo del campo | Tamaño | Tipo de documento (Ver nota 11/ ) TipoDoc
Monto total Mensual de Compras | TotalMensualCompras | Numérico | 15 | 01
Monto total Mensual de Compras | TotalMensualCompras | Numérico | 15 | 04
Monto total Mensual de Compras | TotalMensualCompras | Numérico | 15 | 05
Total Monto de compras | TotalCompras | Numérico | 15 |
Monto total Mensual de Ventas | TotalMensualVentas | Numérico | 15 | 01
Monto total Mensual de Ventas | TotalMensualVentas | Numérico | 15 | 04
Monto total Mensual de Ventas | TotalMensualVentas | Numérico | 15 | 05
Total Monto de Ventas | TotalVentas | Numérico | 15 |
