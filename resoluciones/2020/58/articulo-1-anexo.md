Anexo 1
Consideraciones técnicas para los DUAS anticipados
en puerto de ingreso terrestre, optativo en la
Aduana Paso Canoas (P012)
a. La Declaración Única Aduanera (en adelante DUA) deberá asociarse directamente al DUCA T mediante el bloque de documentos (IMPDOC) en donde se deberá:
i. Utilizar el código 0341 en el campo <COD_DOCCER>.
ii. Incluir el número de DUCAT en el campo <NRO_DOCCER>.
El número de DUCAT incluido en el certificado 0341 declarado en la línea 0000, debe estar en el sistema TICA en estado INI, y no debe haber sido utilizado en otro DUA. El viaje de la DUCAT debe tener como recinto de entrada y salida la misma ubicación y esa ubicación debe ser igual a la de los campos del DUA B12 Lugar de Ubicación de la Mercancía (CODI_ALMA). Si al momento de la aceptación existe más de una DUCA T en estado INI asociado a la misma matrícula de vehículo, no se podrá llevar a cabo la aceptación del DUA.
b. Además en el mensaje del DUA:
i. El campo C37 Código documento de inventario debe declararse con código 70: DUCAT- Declaración Única Centro América para tránsito (COD_DOCCA=70)
ii. El campo B30 Modalidad de transporte debe declararse con código 7: Carretera (VIA_TRANSP=7)
iii. El campo B10 Clase de Medio de Transporte debe declararse con código 7: Camión (UNID_TRANS=7)
iv. El campo B32 Origen del Tipo de Inventario debe declararse con código 2: Terrestre (TIPO_CARGA=2)
v. El campo B31 Momento de Declaración del Inventario debe declararse con código 0: En aceptación y anticipada (MON_ASOC=0) y
vi. El campo B9 Forma de Despacho Elegida por el Declarante debe declararse con código A: Anticipada (DESP_URGE=A).
c. Con la aceptación del DUA, la aplicación informática creará una retención hasta que el DUCAT ingrese a CR y sea autorizado en la Ventanilla Única de Tránsito y se asigne el canal de revisión.
d. El DUA debe contemplar el despacho de todos los bultos declarados en el DUCAT y se validará que el consignatario y las partidas arancelarias a seis dígitos sean las mismas que vienen declaradas en el DUCA T.
e. Deberán cumplirse con las notas técnicas y requisitos no arancelarios establecidos.
