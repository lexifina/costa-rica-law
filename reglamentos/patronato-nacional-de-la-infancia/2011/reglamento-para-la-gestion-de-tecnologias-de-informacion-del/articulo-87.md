Artículo 87.—Integridad de la Información
a. Los usuarios de sistemas, deberán ejecutar las transacciones en los sistemas sólo aplicando procedimientos comprobados que no arriesguen la integridad de la información. De comprobarse pérdida de datos o deterioro de estos, atribuidos a mala praxis, el PANI podrá tomar las medidas legales que le resulten aplicables.
b. Todos los sistemas en producción, deberán contemplar controles que garanticen la completitud, la exactitud y la integridad de los datos que se gestionan en ellos. En virtud de lo anterior, se deberán implementar como mínimo, las medidas de control que se detallan seguidamente. No obstante, de existir nuevas técnicas garantes de la integridad de los datos deberán ser implementadas:
• Uso de llaves en las tablas de la Base de Datos; primarias y foráneas (Integridad Referencial).
• Cada ingreso de datos en la interfaz del sistema, deberá ser validado en función de:
o Tipo de dato,
o Longitud (Uso de delimitadores de texto),
o Formato,
o Validación de datos según lógica de negocio. Por ejemplo, validar que la fecha sea igual o anterior a la actual, validar las relaciones de un dato con respecto a otro, etc.,
o Completitud –Validación de datos vacíos o nulos-.
• Confirmación de transacciones mediante: Sí, No, Cancelar, o lo que en su defecto aplique para la transacción.
• Mensajes de aviso de culminación satisfactoria de transacciones.
• Implementación de reverso de transacciones en los casos donde se afecten sensiblemente los datos. Realización -automática o mediante selección en el menú del sistema- de respaldos ANTES de ejecutar transacciones que afectan sensiblemente la base de datos. Lo anterior, en el caso de que se tenga que recurrir a los datos originales. En caso de, se deberá implementar alguna técnica que permita reversar los datos a su estado original.
• Utilizar reportes de validación de transacciones efectuadas (Datos de Verificación).
• Uso de cifras de control.
• Uso de componentes dedicados a datos específicos, por ejemplo, utilización de objetos que manipulan fechas exclusivamente, y no componentes de texto, cuyo uso compromete la exactitud de la información digitada.
• A nivel de Base de Datos, deberán ser implementadas –siempre que sea factible-, las mejores prácticas de aseguramiento de la integridad de la información.
