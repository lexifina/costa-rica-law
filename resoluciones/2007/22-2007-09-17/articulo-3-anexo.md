ANEXO 3
ESQUEMA Y EJEMPLO DE FACTURA EN XML
Seguidamente, se presenta el esquema y un ejemplo de factura electrónica en XML.
<?xml version=“1.0” encoding=“UTF-8”?>
<xs:schema xmlns:xs=“http://www.w3.org/2001/XMLSchema”
elementFormDefault=“qualified” attributeFormDefault=“unqualified”>
<xs:element name=“FacturaElectronicaXML”>
<xs:annotation>
<xs:documentation>Para los efectos de facilitar la implementación de sistemas computacionales se definió el esquema XML para los Documentos Electrónicos (Factura, Nota de Débito y Nota de Crédito)</xs:documentation>
</xs:annotation>
<xs:complexType>
<xs:sequence>
<xs:element name=“Encabezado”>
<xs:complexType>
<xs:sequence>
<xs:element
name=“VersionDoc” nillable=“false”>
<xs:annotation>
<xs:documentation>Versión del Documento Electrónico</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:int”>
<xs:totalDigits value=“4”/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element name=“TipoDoc”
nillable=“false”>
<xs:annotation>
<xs:documentation>Tipo de Documento Electrónico: 01 Factura, 02 Nota de Débito, 03
Nota de Crédito</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:int”>
<xs:totalDigits value=“2”/>
<xs:pattern value=“”/>
<xs:pattern value=“”/>
<xs:enumeration value=“01”/>
<xs:enumeration value=“02”/>
<xs:enumeration value=“03”/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element
name=“NumConsecutivoCompr” type=“xs:int”>
<xs:annotation>
<xs:documentation>Número consecutivo del Documento Electrónico</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:int”>
<xs:totalDigits value=“13”/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element
name=“FechaEmisionDoc” type=“xs:dateTime”>
<xs:annotation>
<xs:documentation>Fecha en la que se genera el documento
Electrónico</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element
name=“CondicionVenta”>
<xs:annotation>
<xs:documentation>Condicion de Venta: 01 Contado, 02 CrÃ©dito, 03 Consignación, 04
Apartado, 05 Arrendamiento con Opción de Compra</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:int”>
<xs:totalDigits value=“2”/>
<xs:enumeration value=“01”/>
<xs:enumeration value=“02”/>
<xs:enumeration value=“03”/>
<xs:enumeration value=“04”/>
<xs:enumeration value=“05”/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element name=“Emisor”>
<xs:annotation>
<xs:documentation>Información completa de los Datos del Emisor del Documento
Electrónico</xs:documentation>
</xs:annotation>
<xs:complexType>
<xs:attribute name=“NombreEmisor” use=“required”>
<xs:annotation>
<xs:documentation>Nombre del la persona Física o Jurídica que emite el Documento
Electrónico</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:string”>
<xs:maxLength value=“80”/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name=“NumCedulaEmisor” use=“required”>
<xs:annotation>
<xs:documentation>Cédula Física o Jurídica del Emisor del Documento
Electrónico</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:integer”>
<xs:totalDigits value=“10”/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name=“NombreComercialEmisor” use=“required”>
<xs:simpleType>
<xs:restriction base=“xs:string”>
<xs:maxLength value=“80”/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name=“DireccionEmisor” use=“required”>
<xs:simpleType>
<xs:restriction base=“xs:string”>
<xs:maxLength value=“80”/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name=“NumeroTelEmisor” use=“required”>
<xs:simpleType>
<xs:restriction base=“xs:integer”>
<xs:totalDigits value=“7”/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name=“NumeroFaxEmisor” use=“optional”>
<xs:simpleType>
<xs:restriction base=“xs:integer”>
<xs:totalDigits value=“7”/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name=“CorreoElectronicoEmisor” use=“required”>
<xs:simpleType>
<xs:restriction base=“xs:string”>
<xs:maxLength value=“30”/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name=“Receptor”
minOccurs=“0”>
<xs:annotation>
<xs:documentation>Información de los Datos del Receptor del Documento Electrónico
</xs:documentation>
</xs:annotation>
<xs:complexType>
<xs:attribute name=“NombreReceptor” use=“required”>
<xs:annotation>
<xs:documentation>Nombre de la entidad Física o Jurídica que recibe el Documento
Electrónico</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:string”>
<xs:maxLength value=“80”/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name=“NumCedulaReceptor” use=“required”>
<xs:annotation>
<xs:documentation>Número de Cédula Física o Jurídica del receptor del Documento
Electrónico</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:integer”>
<xs:totalDigits value=“10”/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name=“DireccionReceptor” use=“required”>
<xs:simpleType>
<xs:restriction base=“xs:string”>
<xs:maxLength value=“80”/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
</xs:complexType>
</xs:element>
</xs:sequence>
</xs:complexType>
</xs:element>
<xs:element name=“Detalle”>
<xs:annotation>
<xs:documentation>Detalle del
Documento ElectrÃ³nico</xs:documentation>
</xs:annotation>
<xs:complexType>
<xs:sequence maxOccurs=“unbounded”>
<xs:annotation>
<xs:documentation>El detalle del documento electrónico se podrá repetir
ilimitadamente</xs:documentation>
</xs:annotation>
<xs:element
name=“CodigoProducto” minOccurs=“0”>
<xs:annotation>
<xs:documentation>Código del Producto o Servicio que esta reportando en el
documento electrónico</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:string”>
<xs:totalDigits value=“13”/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element
name=“Cantidad”>
<xs:annotation>
<xs:documentation>Cantidad del Producto o Servicio</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:long”>
<xs:totalDigits value=“13”/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element
name=“UnidadMedida”>
<xs:annotation>
<xs:documentation>Unidad de Medida del Producto o Servicio</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:string”>
<xs:maxLength value=“13”/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element
name=“DetalleMerc”>
<xs:annotation>
<xs:documentation>Detalle de la Mercancía o Servicio prestado</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:string”>
<xs:maxLength value=“160”/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element
name=“PrecioUnitario”>
<xs:annotation>
<xs:documentation>Precio Unitario del Mercancía o Servicio
Prestado</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:long”>
<xs:totalDigits value=“15”/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element
name=“MontoTotal”>
<xs:annotation>
<xs:documentation>Monto Total Bruto sin Descuentos ni Impuestos.</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:long”>
<xs:totalDigits value=“15”/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element
name=“MontoDescuento”>
<xs:annotation>
<xs:documentation>Monto de descuento aplicado a la línea de
detalle</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:long”>
<xs:totalDigits value=“15”/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element
name=“NaturalezaDescuento”>
<xs:annotation>
<xs:documentation>Es la descripción o nombre del Descuento aplicado a la línea de
detalle</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:string”>
<xs:maxLength value=“80”/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element
name=“Impuestos”>
<xs:annotation>
<xs:documentation>Impuestos aplicable a la línea de detalle
</xs:documentation>
</xs:annotation>
<xs:complexType>
<xs:sequence minOccurs=“0” maxOccurs=“unbounded”>
<xs:element name=“CodigoImpuesto”>
<xs:annotation>
<xs:documentation>Código de Impuesto aplicado a la línea de detalle según
tabla del Ministerio de Hacienda</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:string”>
<xs:maxLength value=“2”/>
<xs:enumeration value=“01”/>
<xs:enumeration value=“02”/>
<xs:enumeration value=“35”/>
<xs:enumeration value=“40”/>
<xs:enumeration value=“41”/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element name=“MontoImpuesto”>
<xs:annotation>
<xs:documentation>Monto de Impuesto aplicado a la línea de
detalle</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:long”>
<xs:totalDigits value=“15”/>
</xs:restriction>
</xs:simpleType>
</xs:element>
</xs:sequence>
</xs:complexType>
</xs:element>
</xs:sequence>
</xs:complexType>
</xs:element>
<xs:element name=“TotalesFactura”>
<xs:annotation>
<xs:documentation>Totales Finales
del Documento Electrónico. Estos totales se derivan de cada una de las líneas del
detalle del Documento Electrónico.</xs:documentation>
</xs:annotation>
<xs:complexType>
<xs:attribute name=“SubTotal”
type=“xs:double” use=“required”/>
<xs:attribute
name=“TotalSerGravado” type=“xs:double” use=“required”/>
<xs:attribute name=“TotalSerExento”
type=“xs:double” use=“required”/>
<xs:attribute
name=“TotalMerGravado” type=“xs:double” use=“required”/>
<xs:attribute name=“TotalMerExento”
type=“xs:double” use=“required”/>
<xs:attribute name=“TotalNeto”
type=“xs:double” use=“required”/>
<xs:attribute name=“TotalImpuestos”
type=“xs:double” use=“required”/>
</xs:complexType>
</xs:element>
<xs:element name=“InformacionDeReferencia”>
<xs:annotation>
<xs:documentation>Las referencias
son para cuando se deben de emitir Notas de Crédito o Débito que anulan o modifican
documentos anteriores</xs:documentation>
</xs:annotation>
<xs:complexType>
<xs:attribute
name=“CodigoReferencia” use=“required”>
<xs:annotation>
<xs:documentation>Son los códigos de referencia definidos por la DGT: 1 Anula
Documento de Referencia, 2 Corrige Texto Documento de referencia, 3 Corrige
monto</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction
base=“xs:int”>
<xs:totalDigits value=“1”/>
<xs:enumeration value=“1”/>
<xs:enumeration value=“2”/>
<xs:enumeration value=“3”/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute
name=“RazonReferencia” use=“required”>
<xs:annotation>
<xs:documentation>Texto para aclaraciones adicionales</xs:documentation>
</xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name=“Autorizacion”>
<xs:annotation>
<xs:documentation>Etiqueta para
anotar el número de resolución de la DGT</xs:documentation>
</xs:annotation>
<xs:complexType>
<xs:attribute name=“NumResolucion”
use=“required”>
<xs:annotation>
<xs:documentation>Número de resolución como usuario de documentos
electrónicos</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction
base=“xs:string”>
<xs:maxLength value=“13”/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute
name=“FechaResolucion” type=“xs:dateTime” use=“required”>
<xs:annotation>
<xs:documentation>Fecha y Hora de la resolución emitida por la DGT al
usuario</xs:documentation>
</xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name=“Otros” minOccurs=“0”>
<xs:annotation>
<xs:documentation>Etiqueta para ser
utilizada en el Intercambio Electrónico de Datos</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base=“xs:string”>
<xs:maxLength
value=“2000”/>
</xs:restriction>
</xs:simpleType>
</xs:element>
</xs:sequence>
</xs:complexType>
</xs:element>
</xs:schema>
[imagen]
[imagen]
