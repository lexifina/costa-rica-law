ANEXO 2. "MECANISMO DE SEGURIDAD PARA LA AUTENTICACIÓN E INTEGRIDAD DE LOS COMPROBANTES ELECTRÓNICOS DEL MINISTERIO DE HACIENDA"
Control Histórico de Cambios
Versión 4.4.
Rige a partir del 01 de junio del 2025, a partir de dicha fecha se deroga la Versión 4.3, esta y versiones anteriores, únicamente se podrán utilizar para generar notas de crédito y débito que ajusten comprobantes emitidos durante su vigencia.
Bitacora 4.4.0
1. Se incorporan ejemplos ampliando el uso del estándar actual donde se utilizan la contra firma del receptor en comprobantes de crédito y las contra firmas para endosante y endosatario en casos de endoso.
2. Se cambia el ejemplo de firma para que tenga la información del Policy en la versión v4.4
Cambios 20/02/2017 (Resolución DGT-R-13-2017) versión 4.1
1. Se ajusta la versión del ETSI TS 101 903 a v1.3.2 o superior.
2. Se agrega el URL a utilizar para la pólitica del XAdES-EPES.
3. Se aclara que el empaquetado del XAdES será ENVELOPED.
4. Se indica que los algoritmos de encriptación de los certificados deben ser RSA 2048 o RSA 4096.
5. Se indica que los algoritmos de digest de la firma deben ser SHA-256 y SHA-512.
6. Se agrega texto acerca de la Ley 8454.
7. Se agrega ejemplo de una etiqueta ds:Signature.
8. Se modifica el valor del ID de la política a versión v4.1
9. Se cambia el ejemplo de firma para que tenga la información del Policy en la versión v4.1
La Dirección General de Tributación (DGT) ha decidido que el método de autenticación e integridad de los comprobantes electrónicos será firma digital de los archivos XML por medio de la inclusión de una etiqueta Signature según lo indica el estándar XMLDSig, el contenido de esta etiqueta será una firma de tipo XAdES-EPES según lo define el estándar ETSI TS 101 903 v1.3.2 o superior. El empaquetado para utilizar con la firma será ENVELOPED, no se aceptará ningún otro. La etiqueta de firma se debe encontrar dentro del documento en el XPath: /FacturaElectronica/ds:Signature.
Para la firma XAdES-EPES se requiere agregar el URL del documento PDF de la política, este documento sería el PDF de la resolución de factura electrónica que se encuentra en el URL: URLXXXXV4.4. (Ver ejemplo de firma)
Las firmas que se generen deben utilizar certificados con algoritmos de encriptación de tipo RSA 2048 o RSA 4096 y algoritmos de digest de tipo SHA-256 o SHA-512. El digest de la firma debe ser SHA-256 o SHA-512.
Este nodo ds:Signature por medio del estándar de XAdES, permite el realizar varias firmas al documento XML. Se utilizará para aquellos casos donde el "Emisorreceptor- electrónico" requiera que dicho comprobante cuente con la firma del receptor con el objetivo de cumplir con lo establecido en la Ley 8454 denominada "Ley de certificados, firmas digitales y documentos electrónicos", para que dicho comprobante se convierta en un título ejecutivo tal como lo establece los artículos 460 y 460 bis del código de comercio, debe utilizar el atributo <xades:ClaimedRole> indicando la función que está ejerciendo, en este caso del "Receptor".
En caso de requerirse el endoso de los comprobantes Factura Electrónica o Factura Electrónica de Exportación, tanto el endosante como el endosatario, posteriormente a la emisión del comprobante electrónico, deberán incorporar la firma, la cual debe estar al amparo bajo la Ley 8454 denominada "Ley de certificados, firmas digitales y documentos electrónicos, emitidas por las entidades bancarias. Para esto debe utilizar el atributo <xades:ClaimedRole> indicando la función que está ejerciendo, en este caso, si es para el primer endoso, para el endosante el nombre "Endosante1" y para el endosatario el nombre "Endosatario1" y así sucesivamente.
Todo archivo XML generado por un emisor-receptor electrónico y receptor electrónico-no emisor, que se encuentre obligado de hacer uso de comprobantes electrónicos debe de ser enviado a la Dirección General de Tributacion para su respectiva validación conforme lo indicado en el artículo 21, del Decreto N°41820-H Reglamento de comprobantes electrónicos para efectos tributarios, no obstante, el comprobante electrónico que posea las firmas del receptor o endosante y endosatario, no debe enviarse a la Dirección General de Tributacion al ser este comprobante únicamente para fines comerciales, ya que para fines tributarios será válido únicamente el primer archivo enviado por el emisor y aceptado por el Ministerio de Hacienda en el proceso de validación conforme lo indicado en el artículo 21 en mención, así como sus respectivos mensajes de confirmación. Los emisores electrónicos que no requieran estas firmas adicionales, no tendrán obligación de utilizar el atributo <xades:ClaimedRole>
Se le permite al contribuyente escoger entre dos modelos independientes para la autenticación e integridad de los Comprobantes Electrónicos.
Formato Firma Digital
Para él envió de los comprobantes electrónicos y para garantizar la integridad, autenticidad y autoría de los comprobantes electrónicos, podrán utilizar la Firma Digital tanto de Personas Físicas como Personas Jurídicas, emitidas bajo la Ley 8454 Ley de Certificados, Firmas Digitales y Documentos electrónicos.
Cada contribuyente deberá de tramitar la obtención de la Firma Digital de Persona Física emitida por el SINPE en los diferentes Bancos o cooperativas del sistema financiero nacional.
En el caso de empresas que por su volumen de transacciones prefieran utilizar la Firma Digital de Personas Jurídicas deberá tramitar la solicitud ante el COS del Banco Central de Costa Rica y cumplir con los requerimientos que ellos les exijan para este fin.
Luego de que se obtiene la Firma Digital y el identificador del usuario con su respectiva contraseña, cada contribuyente se conectará a un aplicativo para firmar y enviar los archivos XML al Sistema de Comprobantes Electrónicos del Ministerio de Hacienda, mediante la conexión a un RESTful API (ver Anexo 3).
Luego de la recepción de cada uno de los comprobantes, el sistema de Comprobantes Electrónicos del Ministerio de Hacienda generará un archivo XML como acuse de recibo, este archivo irá firmado digitalmente con el certificado de Persona Jurídica del Ministerio de Hacienda.
Llave criptográfica del Ministerio de Hacienda
Dado que la utilización de la Firma Digital no es de uso obligatorio para el Sistema de Comprobantes Electrónicos del Ministerio de Hacienda, les brindará la opción del siguiente método alternativo para el envío y recepción de los comprobantes electrónicos.
El Ministerio de Hacienda brindará a sus obligados tributarios un método de seguridad por medio de llaves criptográficas, estas llaves criptográficas serán RSA 2048 + SHA-256. Y se podrán utilizar para realizar las firmas XAdES-EPES de los comprobantes electrónicos; para lo cual podrán generar tanto la llave criptográfica que será utilizada en el ambiente de pruebas como la llave criptográfica para el ambiente de producción.
Para obtener las llaves criptográficas se deben realizar los siguientes pasos.
1. Deben ingresar al Sistema de Administración Tributaria Virtual (ATV), haciendo uso de los mecanismos de seguridad ya proporcionados. En aquellos casos que los obligados tributarios no posean dicho acceso, deben realizar su respectivo registro en este sistema.
2. Una vez que se ingrese al sistema, se debe presionar la opción denominada "Comprobantes Electrónica"; la cual mostrará la funcionalidad para la generación de las llaves criptográficas; para lo cual el obligado tributario debe proporcionar la información solicitada.
3. Al concluir con el paso anterior, el sistema le estará enviando al buzón electrónico la llave criptográfica que será utilizada en los comprobantes electrónicos.
4. En aquellos casos donde el obligado tributario decida revocar la llave criptográfica, deberá de presionar la opción "Factura Electrónica"; la cual mostrará la funcionalidad de revocación de llave criptográfica.
5. Al concluir con el paso anterior, se estará revocando la llave criptográfica del obligado tributario.
Ejemplo de la etiqueta de firma y su contenido:
<ds:Signature Id="id-e34ffbff277e8d1432e864436aa11882" xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
<ds:SignedInfo>
<ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
<ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
<ds:Reference Id="r-id-1" Type="" URI="">
<ds:Transforms>
<ds:Transform Algorithm="http://www.w3.org/TR/1999/REC-xpath-19991116">
<ds:XPath>not(ancestor-or-self::ds:Signature)</ds:XPath>
</ds:Transform>
<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
</ds:Transforms>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
<ds:DigestValue>ql0urtXTsc9W0GMIhTdzYHXnQYfnieoIttOBn9fGw7A=</ds:DigestValue>
</ds:Reference>
<ds:Reference Type="http://uri.etsi.org/01903#SignedProperties" URI="#xades-id-e34ffbff277e8d1432e864436aa11882">
<ds:Transforms>
<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
</ds:Transforms>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
<ds:DigestValue>5JVZPTwN5Lj0sGTfFzaUeMKCo/xbCAj7fw6TLUFtZIk=</ds:DigestValue>
</ds:Reference>
</ds:SignedInfo>
<ds:SignatureValueId="valueide34ffbff277e8d1432e864436aa11882">Mt1TUuPK3W8/0eRtJX5t45GV9bHvMjwL2I5GKkz9FEExrcqLDY5SiR5ncrhZckJVx0n0FvY4n1ZBvguyEWHqZFoFsAjK8hFfJCfVOQCfrjh3E9L7wfUTZz1aLUFV8AVX07c6e7vSqHE2utta3Qz9dFT+sGX4NXHLggMYcE+jv/kqM9/+MQzppmmDx2VAEmGlR2haLPqyjUJ1dEGcRfZ8uUG+Lgq7ptSdzeziGhfaATBV/8+dIq+u4Gw3LQu8nB5LlTS/ZJEszKq+JyCosp9Er6aHVac6iVF6QEO6QQ4kITopu/BZrWKna09cZHJ5pcifwhb/G/LYThHgbwnbRYqrlQ==</ds:SignatureValue>
<ds:KeyInfo>
<ds:X509Data>
<ds:X509Certificate>MIIFpTCCBI2gAwIBAgIKK+xhaAABAARyvDANBgkqhkiG9w0BAQUFADCBmjEVMBMGA1UEBRMMNC0wMDAtMDA0MDE3MQswCQYDVQQGEwJDUjEkMCIGA1UEChMbQkFOQ08gQ0VOVFJBTCBERSBDT1NUQSBSSUNBMSowKAYDVQQLEyFESVZJU0lPTiBERSBTRVJWSUNJT1MgRklOQU5DSUVST1MxIjAgBgNVBAMTGUNBIFNJTlBFIC0gUEVSU09OQSBGSVNJQ0EwHhcNMTYwMjEyMTk0MTI2WhcNMTgwMjExMTk0MTI2WjCBszEZMBcGA1UEBRMQQ1BGLTAxLTEzMDItMDQ4NzEVMBMGA1UEBBMMTU9OR0UgQ0hBVkVTMRcwFQYDVQQqEw5NQVJWSU4gVklOSUNJTzELMAkGA1UEBhMCQ1IxFzAVBgNVBAoTDlBFUlNPTkEgRklTSUNBMRIwEAYDVQQLEwlDSVVEQURBTk8xLDAqBgNVBAMTI01BUlZJTiBWSU5JQ0lPIE1PTkdFIENIQVZFUyAoRklSTUEpMIIBIjANBgkqhkiG9w0BAQE34ghAQ8AMIIBCgKCAQEAtMLNAbhh2TzTB+Q6TBgLHCQGtn73eyOMH2ESIuam9jrnx50gOxM13QD8vXw3fyiyFxvbkxmrVgmihsQ3DC3sVo7S+zwtgp40RiDhEEgSqg8JaZcU+BPiLTNmO0J9lKU9nvYrOCam02oxVNiBUxR8jq7QZ2yG4QREgCQ68/yXOdPLWAJf6afdxn2CiV1Tkeq11J+UDlPdWj65LG/JSQv1vJj0fGw3el/C+WDbIkY/g1ksZ44AdIJwSlhmgwrjOU7Z+bibbYdkN5Ky62bPvFk0irI6/oWV9K8mBgzLla1Zyj7CI2k5hi6vQF0doDSE0js5dFTIwCUDIsHvo4WwFZegoQIDAQABo4IB0DCCAcwwHQYDVR0OBBYEFEy03328b5QRrhdnwoLwjpwSNkfYMB8GA1UdIwQYMBaAFEjUipShoDKIP6qxNhCUK+6UQYKsMFwGA1UdHwRVMFMwUaBPoE2GS2h0dHA6Ly9mZGkuc2lucGUuZmkuY3IvcmVwb3NpdG9yaW8vQ0ElMjBTSU5QRSUyMC0lMjBQRVJTT05BJTIwRklTSUNBKDEpLmNybDCBkwYIKwYBBQUHAQEEgYYwgYMwKAYIKwYBBQUHMAGGHGh0dHA6Ly9vY3NwLnNpbnBlLmZpLmNyL29jc3AwVwYIKwYBBQUHMAKGS2h0dHA6Ly9mZGkuc2lucGUuZmkuY3IvcmVwb3NpdG9yaW8vQ0ElMjBTSU5QRSUyMC0lMjBQRVJTT05BJTIwRklTSUNBKDEpLmNydDAOBgNVHQ8BAf8EBAMCBsAwPQYJKAGCNxUHBDAwLgYmKwYBBAGCNxUIhcTqW4LR4zWVkRuC+ZcYhqXLa4F/gb3yRYe7oj4CAWQCAQQwEwYDVR0lBAwwCgYIKwYBBQUHAwQwFQYDVR0gBA4wDDAKBghggTwBAQEBAjAbBgkrBgEEAYI3FQoEDjAMMAoGCCsGAQUFBwMEMA0GCSqGSIb3DQEBBQUAA4IBAQBnHXQC+D4U7DdZuq0iaqOs4NTqrLfTkYGIo6adAnUWWpN/XjC4y/4EUjRSbhQc/l2pRAlYG4pFJ1ftVvwSZMlcukHR/i6uLo1mWCE2SwWpKyw+5b58eHlJkomzExT92chv1gicHJdb7ZazXKa/0Bkf3+Olh9Nruqo2qs6uCetScCyqc+NTEwSTded4x+wbYIecElkxHje6pqr367zF0rL3khHJYPYCHsadOx0w9XR3K+yFsXksasZzBrsMzZ6/m3+23E0OC2oTb24/z3cn5dNm2y4Hm/fxYl/CE3cQf5NOn7yt80Kdu+jaKDqIkGdSkuf6QppyoxkhuKK1x27fg</ds:X509Certificate>
</ds:X509Data>
</ds:KeyInfo>
<ds:Object>
<xades:QualifyingProperties xmlns:xades="http://uri.etsi.org/01903/v1.3.2#" Target="#id-e34ffbff277e8d1432e864436aa11882">
<xades:SignedProperties Id="xades-id-e34ffbff277e8d1432e864436aa11882">
<xades:SignedSignatureProperties>
<xades:SigningTime>2021-11-27T19:35:06Z</xades:SigningTime>
<xades:SigningCertificate>
<xades:Cert>
<xades:CertDigest>
<ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
<ds:DigestValue>LoXZC86JwDL7zWC35qj7Q4AzrRQ=</ds:DigestValue>
</xades:CertDigest>
<xades:IssuerSerial>
<ds:X509IssuerName>CN=CA SINPE - PERSONA FISICA,OU=DIVISION DE SERVICIOS FINANCIEROS,O=BANCO CENTRAL DE COSTA RICA,C=CR,2.5.4.5=#130c342d3030302d303034303137</ds:X509IssuerName>
<ds:X509SerialNumber>207422209224813750547132</ds:X509SerialNumber>
</xades:IssuerSerial>
</xades:Cert>
</xades:SigningCertificate>
<xades:SignaturePolicyIdentifier>
<xades:SignaturePolicyId>
<xades:SigPolicyId>
<xades:Identifier> URLXXXXV4.4</xades:Identifier>
</xades:SigPolicyId>
<xades:SigPolicyHash>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
<ds:DigestValue>NmI5Njk1ZThkNzI0MmIzMGJmZDAyNDc4YjUwNzkzODM2NTBiOWUxNTBkMmI2YjgzYzZjM2I5NTZlNDQ4OWQzMQ==</ds:DigestValue>
</xades:SigPolicyHash>
</xades:SignaturePolicyId>
</xades:SignaturePolicyIdentifier>
</xades:SignedSignatureProperties>
<xades:SignedDataObjectProperties>
<xades:DataObjectFormat ObjectReference="#r-id-1">
<xades:MimeType>application/octet-stream</xades:MimeType>
</xades:DataObjectFormat>
</xades:SignedDataObjectProperties>
</xades:SignedProperties>
</xades:QualifyingProperties>
</ds:Object>
</ds:Signature>
Ejemplo de la etiqueta de contra firma de receptor y su contenido cuando corresponda:
<ds:Signature Id="id-e34ffbff277e8d1432e864436aa11882">
<ds:SignedInfo>
<ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
<ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
<ds:Reference Id="r-id-1" URI="">
<ds:Transforms>
<ds:TransformAlgorithm="http://www.w3.org/TR/1999/REC-xpath-19991116">
<ds:XPath>not(ancestor-or-self::ds:Signature)</ds:XPath>
</ds:Transform>
<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
</ds:Transforms>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
<ds:DigestValue>ql0urtXTsc9W0GMIhTdzYHXnQYfnieoIttOBn9fGw7A=</ds:DigestValue>
</ds:Reference>
<ds:Reference Type="http://uri.etsi.org/01903#SignedProperties" URI="#xades-id-e34ffbff277e8d1432e864436aa11882">
<ds:Transforms>
<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
</ds:Transforms>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
<ds:DigestValue>5JVZPTwN5Lj0sGTfFzaUeMKCo/xbCAj7fw6TLUFtZIk=</ds:DigestValue>
</ds:Reference>
</ds:SignedInfo>
<ds:SignatureValueId="valueide34ffbff277e8d1432e864436aa11882">Mt1TUuPK3W8/0eRtJX5t45GV9bHvMjwL2I5GKkz9FEExrcqLDY5SiR5ncrhZckJVx0n0FvY4n1ZBvguyEWHqZFoFsAjK8hFfJCfVOQCfrjh3E9L7wfUTZz1aLUFV8AVX07c6e7vSqHE2utta3Qz9dFT+sGX4NXHLggMYcE+jv/kqM9/+MQzppmmDx2VAEmGlR2haLPqyjUJ1dEGcRfZ8uUG+Lgq7ptSdzeziGhfaATBV/8+dIq+u4Gw3LQu8nB5LlTS/ZJEszKq+JyCosp9Er6aHVac6iVF6QEO6QQ4kITopu/BZrWKna09cZHJ5pcifwhb/G/LYThHgbwnbRYqrlQ==</ds:SignatureValue>
<ds:KeyInfo>
<ds:X509Data>
<ds:X509Certificate>MIIFpTCCBI2gAwIBAgIKK+xhaAABAARyvDANBgkqhkiG9w0BAQUFADCBmjEVMBMGA1UEBRMMNC0wMDAtMDA0MDE3MQswCQYDVQQGEwJDUjEkMCIGA1UEChMbQkFOQ08gQ0VOVFJBTCBERSBDT1NUQSBSSUNBMSowKAYDVQQLEyFESVZJU0lPTiBERSBTRVJWSUNJT1MgRklOQU5DSUVST1MxIjAgBgNVBAMTGUNBINJTlBFIC0gUEVSU09OQSBGSVNJQ0EwHhcNMTYwMjEyMTk0MTI2WhcNMTgwMjExMTk0MTI2WjCBszEZMBcGA1UEBRMQQ1BGLTAxLTEzMDItMDQ4NzEVMBMGA1UEBBMMTU9OR0UgQ0hBVkVTMRcwFQYDVQQqEw5NQVJWSU4gVklOSUNJTzELMAkGA1UEBhMCQ1IxFzAVBgNVBAoTDlBFUlNPTkEgRklTSUNBMRIwEAYDVQQLEwlDSVVEQURBTk8xLDAqBgNVBAMTI01BUlZJTiBWSU5JQ0lPIE1PTkdFIENIQVZFUyAoRklSTUEpMIIBIjANBgkqhkiG9w0BAQE34ghAQ8AMIIBCgKCAQEAtMLNAbhh2TzTB+Q6TBgLHCQGtn73eyOMH2ESIuam9jrnx50gOxM13QD8vXw3fyiyFxvbkxmrVgmihsQ3DC3sVo7S+zwtgp40RiDhEEgSqg8JaZcU+BPiLTNmO0J9lKU9nvYrOCam02oxVNiBUxR8jq7QZ2yG4QREgCQ68/yXOdPLWAJf6afdxn2CiV1Tkeq11J+UDlPdWj65LG/JSQv1vJj0fGw3el/C+WDbIkY/g1ksZ44AdIJwSlhmgwrjOU7Z+bibbYdkN5Ky62bPvFk0irI6/oWV9K8mBgzLla1Zyj7CI2k5hi6vQF0doDSE0js5dFTIwCUDIsHvo4WwFZegoQIDAQABo4IB0DCCAcwwHQYDVR0OBBYEFEy03328b5QRrhdnwoLwjpwSNkfYMB8GA1UdIwQYMBaAFEjUipShoDKIP6qxNhCUK+6UQYKsMFwGA1UdHwRVMFMwUaBPoE2GS2h0dHA6Ly9mZGkuc2lucGUuZmkuY3IvcmVwb3NpdG9yaW8vQ0ElMjBTSU5QRSUyMC0lMjBQRVJTT05BJTIwRklTSUNBKDEpLmNybDCBkwYIKwYBBQUHAQEEgYYwgYMwKAYIKwYBBQUHMAGGHGh0dHA6Ly9vY3NwLnNpbnBlLmZpLmNyL29jc3AwVwYIKwYBBQUHMAKGS2h0dHA6Ly9mZGkuc2lucGUuZmkuY3IvcmVwb3NpdG9yaW8vQ0ElMjBTSU5QRSUyMC0lMjBQRVJTT05BJTIwRklTSUNBKDEpLmNydDAOBgNVHQ8BAf8EBAMCBsAwPQYJKAGCNxUHBDAwLgYmKwYBBAGCNxUIhcTqW4LR4zWVkRuC+ZcYhqXLa4F/gb3yRYe7oj4CAWQCAQQwEwYDVR0lBAwwCgYIKwYBBQUHAwQwFQYDVR0gBA4wDDAKBghggTwBAQEBAjAbBgkrBgEEAYI3FQoEDjAMMAoGCCsGAQUFBwMEMA0GCSqGSIb3DQEBBQUAA4IBAQBnHXQC+D4U7DdZuq0iaqOs4NTqrLfTkYGIo6adAnUWWpN/XjC4y/4EUjRSbhQc/l2pRAlYG4pFJ1ftVvwSZMlcukHR/i6uLo1mWCE2SwWpKyw+5b58eHlJkomzExT92chv1gicHJdb7ZazXKa/0Bkf3+Olh9Nruqo2qs6uCetScCyqc+NTEwSTded4x+wbYIecElkxHje6pqr367zF0rL3khHJYPYCHsadOx0w9XR3K+yFsXksasZzBrsMzZ6/m3+23E0OC2oTb24/z3cn5dNm2y4Hm/fxYl/CE3cQf5NOn7yt80Kdu+jaKDqIkGdSkuf6QppyoxkhuKK1x27fg
</ds:X509Certificate>
</ds:X509Data>
</ds:KeyInfo>
<ds:Object>
<xades:QualifyingProperties xmlns:xades="http://uri.etsi.org/01903/v1.3.2#" Target="#id-e34ffbff277e8d1432e864436aa11882">
<xades:SignedProperties Id="xades-id-e34ffbff277e8d1432e864436aa11882">
<xades:SignedSignatureProperties>
<xades:SigningTime>2021-12-10T15:24:18Z</xades:SigningTime>
<xades:SigningCertificate>
<xades:Cert>
<xades:CertDigest>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha512"/>
<ds:DigestValue>LoXZC86JwDL7zWC35qj7Q4AzrRQ=</ds:DigestValue>
</xades:CertDigest>
<xades:IssuerSerial>
<ds:X509IssuerName>CN=CA SINPE - PERSONA FISICA,OU=DIVISION DE SERVICIOS FINANCIEROS,O=BANCO CENTRAL DE COSTA RICA,C=CR,2.5.4.5=#130c342d3030302d303034303137</ds:X509IssuerName>
<ds:X509SerialNumber>207422209224813750547132</ds:X509SerialNumber>
</xades:IssuerSerial>
</xades:Cert>
</xades:SigningCertificate>
<xades:SignaturePolicyIdentifier>
<xades:SignaturePolicyId>
<xades:SigPolicyId>
<xades:Identifier> URLXXXXV4.4</xades:Identifier>
</xades:SigPolicyId>
<xades:SigPolicyHash>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
<ds:DigestValue>NmI5Njk1ZThkNzI0MmIzMGJmZDAyNDc4YjUwNzkzODM2NTBiOWUxNTBkMmI2YjgzYzZjM2I5NTZlNDQ4OWQzMQ==</ds:DigestValue>
</xades:SigPolicyHash>
</xades:SignaturePolicyId>
</xades:SignaturePolicyIdentifier>
<xades:SignerRole>
<xades:ClaimedRoles>
<xades:ClaimedRole>Receptor</xades:ClaimedRole>
</xades:ClaimedRoles>
</xades:SignerRole>
</xades:SignedSignatureProperties>
<xades:SignedDataObjectProperties>
<xades:DataObjectFormat ObjectReference="#r-id-1"> <xades:MimeType>application/octet-stream</xades:MimeType>
</xades:DataObjectFormat>
</xades:SignedDataObjectProperties>
</xades:SignedProperties>
</xades:QualifyingProperties>
</ds:Object>
</ds:Signature>
Ejemplo de la etiqueta de contra firma de endosante-endosatario y su contenido cuando corresponda:
<ds:Signature Id="id-e34ffbff277e8d1432e864436aa11882">
<ds:SignedInfo>
<ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
<ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
<ds:Reference Id="r-id-1" URI="">
<ds:Transforms>
<ds:Transform Algorithm="http://www.w3.org/TR/1999/REC-xpath-19991116">
<ds:XPath>not(ancestor-or-self::ds:Signature)</ds:XPath>
</ds:Transform>
<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
</ds:Transforms>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
<ds:DigestValue>ql0urtXTsc9W0GMIhTdzYHXnQYfnieoIttOBn9fGw7A=</ds:DigestValue>
</ds:Reference>
<ds:Reference Type="http://uri.etsi.org/01903#SignedProperties" URI="#xades-id-e34ffbff277e8d1432e864436aa11882">
<ds:Transforms>
<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
</ds:Transforms>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
<ds:DigestValue>5JVZPTwN5Lj0sGTfFzaUeMKCo/xbCAj7fw6TLUFtZIk=</ds:DigestValue>
</ds:Reference>
</ds:SignedInfo>
<ds:SignatureValueId="valueide34ffbff277e8d1432e864436aa11882">Mt1TUuPK3W8/0eRtJX5t45GV9bHvMjwL2I5GKkz9FEExrcqLDY5SiR5ncrhZckJVx0n0FvY4n1ZBvguyEWHqZFoFsAjK8hFfJCfVOQCfrjh3E9L7wfUTZz1aLUFV8AVX07c6e7vSqHE2utta3Qz9dFT+sGX4NXHLggMYcE+jv/kqM9/+MQzppmmDx2VAEmGlR2haLPqyjUJ1dEGcRfZ8uUG+Lgq7ptSdzeziGhfaATBV/8+dIq+u4Gw3LQu8nB5LlTS/ZJEszKq+JyCosp9Er6aHVac6iVF6QEO6QQ4kITopu/BZrWKna09cZHJ5pcifwhb/G/LYThHgbwnbRYqrlQ==</ds:SignatureValue>
<ds:KeyInfo>
<ds:X509Data>
<ds:X509Certificate>MIIFpTCCBI2gAwIBAgIKK+xhaAABAARyvDANBgkqhkiG9w0BAQUFADCBmjEVMBMGA1UEBRMMNC0wMDAtMDA0MDE3MQswCQYDVQQGEwJDUjEkMCIGA1UEChMbQkFOQ08gQ0VOVFJBTCBERSBDT1NUQSBSSUNBMSowKAYDVQQLEyFESVZJU0lPTiBERSBTRVJWSUNJT1MgRklOQU5DSUVST1MxIjAgBgNVBAMTGUNBIFNJTlBFIC0gUEVSU09OQSBGSVNJQ0EwHhcNMTYwMjEyMTk0MTI2WhcNMTgwMjExMTk0MTI2WjCBszEZMBcGA1UEBRMQQ1BGLTAxLTEzMDItMDQ4NzEVMBMGA1UEBBMMTU9OR0UgQ0hBVkVTMRcwFQYDVQQqEw5NQVJWSU4gVklOSUNJTzELMAkGA1UEBhMCQ1IxFzAVBgNVBAoTDlBFUlNPTkEgRklTSUNBMRIwEAYDVQQLEwlDSVVEQURBTk8xLDAqBgNVBAMTI01BUlZJTiBWSU5JQ0lPIE1PTkdFIENIQVZFUyAoRklSTUEpMIIBIjANBgkqhkiG9w0BAQE34ghAQ8AMIIBCgKCAQEAtMLNAbhh2TzTB+Q6TBgLHCQGtn73eyOMH2ESIuam9jrnx50gOxM13QD8vXw3fyiyFxvbkxmrVgmihsQ3DC3sVo7S+zwtgp40RiDhEEgSqg8JaZcU+BPiLTNmO0J9lKU9nvYrOCam02oxVNiBUxR8jq7QZ2yG4QREgCQ68/yXOdPLWAJf6afdxn2CiV1Tkeq11J+UDlPdWj65LG/JSQv1vJj0fGw3el/C+WDbIkY/g1ksZ44AdIJwSlhmgwrjOU7Z+bibbYdkN5Ky62bPvFk0irI6/oWV9K8mBgzLla1Zyj7CI2k5hi6vQF0doDSE0js5dFTIwCUDIsHvo4WwFZegoQIDAQABo4IB0DCCAcwwHQYDVR0OBBYEFEy03328b5QRrhdnwoLwjpwSNkfYMB8GA1UdIwQYMBaAFEjUipShoDKIP6qxNhCUK+6UQYKsMFwGA1UdHwRVMFMwUaBPoE2GS2h0dHA6Ly9mZGkuc2lucGUuZmkuY3IvcmVwb3NpdG9yaW8vQ0ElMjBTSU5QRSUyMC0lMjBQRVJTT05BJTIwRklTSUNBKDEpLmNybDCBkwYIKwYBBQUHAQEEgYYwgYMwKAYIKwYBBQUHMAGGHGh0dHA6Ly9vY3NwLnNpbnBlLmZpLmNyL29jc3AwVwYIKwYBBQUHMAKGS2h0dHA6Ly9mZGkuc2lucGUuZmkuY3IvcmVwb3NpdG9yaW8vQ0ElMjBTSU5QRSUyMC0lMjBQRVJTT05BJTIwRklTSUNBKDEpLmNydDAOBgNVHQ8BAf8EBAMCBsAwPQYJKAGCNxUHBDAwLgYmKwYBBAGCNxUIhcTqW4LR4zWVkRuC+ZcYhqXLa4F/gb3yRYe7oj4CAWQCAQQwEwYDVR0lBAwwCgYIKwYBBQUHAwQwFQYDVR0gBA4wDDAKBghggTwBAQEBAjAbBgkrBgEEAYI3FQoEDjAMMAoGCCsGAQUFBwMEMA0GCSqGSIb3DQEBBQUAA4IBAQBnHXQC+D4U7DdZuq0iaqOs4NTqrLfTkYGIo6adAnUWWpN/XjC4y/4EUjRSbhQc/l2pRAlYG4pFJ1ftVvwSZMlcukHR/i6uLo1mWCE2SwWpKyw+5b58eHlJkomzExT92chv1gicHJdb7ZazXKa/0Bkf3+Olh9Nruqo2qs6uCetScCyqc+NTEwSTded4x+wbYIecElkxHje6pqr367zF0rL3khHJYPYCHsadOx0w9XR3K+yFsXksasZzBrsMzZ6/m3+23E0OC2oTb24/z3cn5dNm2y4Hm/fxYl/CE3cQf5NOn7yt80Kdu+jaKDqIkGdSkuf6QppyoxkhuKK1x27fg
</ds:X509Certificate>
</ds:X509Data>
</ds:KeyInfo>
<ds:Object>
<xades:QualifyingProperties xmlns:xades="http://uri.etsi.org/01903/v1.3.2#" Target="#id-e34ffbff277e8d1432e864436aa11882">
<xades:SignedProperties Id="xades-id-e34ffbff277e8d1432e864436aa11882">
<xades:SignedSignatureProperties>
<xades:SigningTime>2021-12-10T15:24:18Z</xades:SigningTime>
<xades:SigningCertificate>
<xades:Cert>
<xades:CertDigest>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha512"/>
<ds:DigestValue>LoXZC86JwDL7zWC35qj7Q4AzrRQ=</ds:DigestValue>
</xades:CertDigest>
<xades:IssuerSerial>
<ds:X509IssuerName>CN=CA SINPE - PERSONA FISICA,OU=DIVISION DE SERVICIOS FINANCIEROS,O=BANCO CENTRAL DE COSTA RICA,C=CR,2.5.4.5=#130c342d3030302d303034303137</ds:X509IssuerName>
<ds:X509SerialNumber>207422209224813750547132</ds:X509SerialNumber>
</xades:IssuerSerial>
</xades:Cert>
</xades:SigningCertificate>
<xades:SignaturePolicyIdentifier>
<xades:SignaturePolicyId>
<xades:SigPolicyId>
<xades:Identifier> URLXXXXV4.4</xades:Identifier>
</xades:SigPolicyId>
<xades:SigPolicyHash>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
<ds:DigestValue>NmI5Njk1ZThkNzI0MmIzMGJmZDAyNDc4YjUwNzkzODM2NTBiOWUxNTBkMmI2YjgzYzZjM2I5NTZlNDQ4OWQzMQ==</ds:DigestValue>
</xades:SigPolicyHash>
</xades:SignaturePolicyId>
</xades:SignaturePolicyIdentifier>
<xades:SignerRole>
<xades:ClaimedRoles>
<xades:ClaimedRole>Endosante1</xades:ClaimedRole>
</xades:ClaimedRoles>
</xades:SignerRole>
</xades:SignedSignatureProperties>
<xades:SignedDataObjectProperties>
<xades:DataObjectFormat ObjectReference="#r-id-1"> <xades:MimeType>application/octet-stream</xades:MimeType>
</xades:DataObjectFormat>
</xades:SignedDataObjectProperties>
</xades:SignedProperties>
</xades:QualifyingProperties>
</ds:Object>
</ds:Signature>
<ds:Signature Id="id-e34ffbff277e8d1432e864436aa11882">
<ds:SignedInfo>
<ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
<ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
<ds:Reference Id="r-id-1" URI="">
<ds:Transforms>
<ds:Transform Algorithm="http://www.w3.org/TR/1999/REC-xpath-19991116">
<ds:XPath>not(ancestor-or-self::ds:Signature)</ds:XPath>
</ds:Transform>
<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
</ds:Transforms>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
<ds:DigestValue>ql0urtXTsc9W0GMIhTdzYHXnQYfnieoIttOBn9fGw7A=</ds:DigestValue>
</ds:Reference>
<ds:Reference Type="http://uri.etsi.org/01903#SignedProperties" URI="#xades-id-e34ffbff277e8d1432e864436aa11882">
<ds:Transforms>
<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
</ds:Transforms>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
<ds:DigestValue>5JVZPTwN5Lj0sGTfFzaUeMKCo/xbCAj7fw6TLUFtZIk=</ds:DigestValue>
</ds:Reference>
</ds:SignedInfo>
<ds:SignatureValueId="valueide34ffbff277e8d1432e864436aa11882">Mt1TUuPK3W8/0eRtJX5t45GV9bHvMjwL2I5GKkz9FEExrcqLDY5SiR5ncrhZckJVx0n0FvY4n1ZBvguyEWHqZFoFsAjK8hFfJCfVOQCfrjh3E9L7wfUTZz1aLUFV8AVX07c6e7vSqHE2utta3Qz9dFT+sGX4NXHLggMYcE+jv/kqM9/+MQzppmmDx2VAEmGlR2haLPqyjUJ1dEGcRfZ8uUG+Lgq7ptSdzeziGhfaATBV/8+dIq+u4Gw3LQu8nB5LlTS/ZJEszKq+JyCosp9Er6aHVac6iVF6QEO6QQ4kITopu/BZrWKna09cZHJ5pcifwhb/G/LYThHgbwnbRYqrlQ==</ds:SignatureValue>
<ds:KeyInfo>
<ds:X509Data>
<ds:X509Certificate>MIIFpTCCBI2gAwIBAgIKK+xhaAABAARyvDANBgkqhkiG9w0BAQUFADCBmjEVMBMGA1UEBRMMNC0wMDAtMDA0MDE3MQswCQYDVQQGEwJDUjEkMCIGA1UEChMbQkFOQ08gQ0VOVFJBTCBERSBDT1NUQSBSSUNBMSowKAYDVQQLEyFESVZJU0lPTiBERSBTRVJWSUNJT1MgRklOQU5DSUVST1MxIjAgBgNVBAMTGUNBIFNJTlBFIC0gUEVSU09OQSBGSVNJQ0EwHhcNMTYwMjEyMTk0MTI2WhcNMTgwMjExMTk0MTI2WjCBszEZMBcGA1UEBRMQQ1BGLTAxLTEzMDItMDQ4NzEVMBMGA1UEBBMMTU9OR0UgQ0hBVkVTMRcwFQYDVQQqEw5NQVJWSU4gVklOSUNJTzELMAkGA1UEBhMCQ1IxFzAVBgNVBAoTDlBFUlNPTkEgRklTSUNBMRIwEAYDVQQLEwlDSVVEQURBTk8xLDAqBgNVBAMTI01BUlZJTiBWSU5JQ0lPIE1PTkdFIENIQVZFUyAoRklSTUEpMIIBIjANBgkqhkiG9w0BAQE34ghAQ8AMIIBCgKCAQEAtMLNAbhh2TzTB+Q6TBgLHCQGtn73eyOMH2ESIuam9jrnx50gOxM13QD8vXw3fyiyFxvbkxmrVgmihsQ3DC3sVo7S+zwtgp40RiDhEEgSqg8JaZcU+BPiLTNmO0J9lKU9nvYrOCam02oxVNiBUxR8jq7QZ2yG4QREgCQ68/yXOdPLWAJf6afdxn2CiV1Tkeq11J+UDlPdWj65LG/JSQv1vJj0fGw3el/C+WDbIkY/g1ksZ44AdIJwSlhmgwrjOU7Z+bibbYdkN5Ky62bPvFk0irI6/oWV9K8mBgzLla1Zyj7CI2k5hi6vQF0doDSE0js5dFTIwCUDIsHvo4WwFZegoQIDAQABo4IB0DCCAcwwHQYDVR0OBBYEFEy03328b5QRrhdnwoLwjpwSNkfYMB8GA1UdIwQYMBaAFEjUipShoDKIP6qxNhCUK+6UQYKsMFwGA1UdHwRVMFMwUaBPoE2GS2h0dHA6Ly9mZGkuc2lucGUuZmkuY3IvcmVwb3NpdG9yaW8vQ0ElMjBTSU5QRSUyMC0lMjBQRVJTT05BJTIwRklTSUNBKDEpLmNybDCBkwYIKwYBBQUHAQEEgYYwgYMwKAYIKwYBBQUHMAGGHGh0dHA6Ly9vY3NwLnNpbnBlLmZpLmNyL29jc3AwVwYIKwYBBQUHMAKGS2h0dHA6Ly9mZGkuc2lucGUuZmkuY3IvcmVwb3NpdG9yaW8vQ0ElMjBTSU5QRSUyMC0lMjBQRVJTT05BJTIwRklTSUNBKDEpLmNydDAOBgNVHQ8BAf8EBAMCBsAwPQYJKAGCNxUHBDAwLgYmKwYBBAGCNxUIhcTqW4LR4zWVkRuC+ZcYhqXLa4F/gb3yRYe7oj4CAWQCAQQwEwYDVR0lBAwwCgYIKwYBBQUHAwQwFQYDVR0gBA4wDDAKBghggTwBAQEBAjAbBgkrBgEEAYI3FQoEDjAMMAoGCCsGAQUFBwMEMA0GCSqGSIb3DQEBBQUAA4IBAQBnHXQC+D4U7DdZuq0iaqOs4NTqrLfTkYGIo6adAnUWWpN/XjC4y/4EUjRSbhQc/l2pRAlYG4pFJ1ftVvwSZMlcukHR/i6uLo1mWCE2SwWpKyw+5b58eHlJkomzExT92chv1gicHJdb7ZazXKa/0Bkf3+Olh9Nruqo2qs6uCetScCyqc+NTEwSTded4x+wbYIecElkxHje6pqr367zF0rL3khHJYPYCHsadOx0w9XR3K+yFsXksasZzBrsMzZ6/m3+23E0OC2oTb24/z3cn5dNm2y4Hm/fxYl/CE3cQf5NOn7yt80Kdu+jaKDqIkGdSkuf6QppyoxkhuKK1x27fg
</ds:X509Certificate>
</ds:X509Data>
</ds:KeyInfo>
<ds:Object>
<xades:QualifyingProperties xmlns:xades="http://uri.etsi.org/01903/v1.3.2#" Target="#id-e34ffbff277e8d1432e864436aa11882">
<xades:SignedProperties Id="xades-id-e34ffbff277e8d1432e864436aa11882">
<xades:SignedSignatureProperties>
<xades:SigningTime>2021-12-10T15:24:18Z</xades:SigningTime>
<xades:SigningCertificate>
<xades:Cert>
<xades:CertDigest>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha512"/>
<ds:DigestValue>LoXZC86JwDL7zWC35qj7Q4AzrRQ=</ds:DigestValue>
</xades:CertDigest>
<xades:IssuerSerial>
<ds:X509IssuerName>CN=CA SINPE - PERSONA FISICA,OU=DIVISION DE SERVICIOS FINANCIEROS,O=BANCO CENTRAL DE COSTA RICA,C=CR,2.5.4.5=#130c342d3030302d303034303137</ds:X509IssuerName>
<ds:X509SerialNumber>207422209224813750547132</ds:X509SerialNumber>
</xades:IssuerSerial>
</xades:Cert>
</xades:SigningCertificate>
<xades:SignaturePolicyIdentifier>
<xades:SignaturePolicyId>
<xades:SigPolicyId>
<xades:Identifier> URLXXXXV4.4</xades:Identifier>
</xades:SigPolicyId>
<xades:SigPolicyHash>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
<ds:DigestValue>NmI5Njk1ZThkNzI0MmIzMGJmZDAyNDc4YjUwNzkzODM2NTBiOWUxNTBkMmI2YjgzYzZjM2I5NTZlNDQ4OWQzMQ==</ds:DigestValue>
</xades:SigPolicyHash>
</xades:SignaturePolicyId>
</xades:SignaturePolicyIdentifier>
<xades:SignerRole>
<xades:ClaimedRoles>
<xades:ClaimedRole>Endosatario1</xades:ClaimedRole>
</xades:ClaimedRoles>
</xades:SignerRole>
</xades:SignedSignatureProperties>
<xades:SignedDataObjectProperties>
<xades:DataObjectFormat ObjectReference="#r-id-1"> <xades:MimeType>application/octet-stream</xades:MimeType>
</xades:DataObjectFormat>
</xades:SignedDataObjectProperties>
</xades:SignedProperties>
</xades:QualifyingProperties>
</ds:Object>
</ds:Signature>
