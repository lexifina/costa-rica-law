DIRECCIÓN GENERAL DE ADUANAS
San José, 06 de noviembre del 2007
Circular DGT-153-2007
Señores
Transportistas Navieros
Autoridades Portuarias y Aeroportuarias
Agencias y Agentes de Aduanas
Directores, Jefes de Departamento,
Gerentes y Subgerentes de Aduana
Funcionarios Aduaneros
Servicio Nacional de Aduanas
Estimados Señores
Asunto: Intercambio de Información Navieras-Autoridades Portuarias.
Con el fin de mejorar el intercambio de información generada desde los manifiestos de carga marítimos en el Sistema TICA, así como lo relacionado con la transmisión de la información de los contenedores que se indican en los mismos, se emiten las siguientes directrices.
1. Sobre la transmisión de contenedores y su listado:
1.1. A partir de la fecha de vigencia de esta circular, se deberá transmitir al Sistema Tic@, además de los datos de los contenedores llenos que se transmiten actualmente, los inherentes a los contenedores vacíos.
1.2. El contenido de la descripción de la matrícula (Nº de unidad de transporte) deberá responder a lo indicado en el “Formato de Mensaje de Ingresos y Salidas” versión 1.56”, bloque “unidades de transporte” (YCGCNTDR), campo denominado “Nº de unidad de transporte” (YCGNROCONT). Dicho formato indica que la descripción toma como base la combinación alfa numérica “AAAA-999999-9”. Para interpretar la combinación alfa numérica precedente, se deberá entender que:
1.2.1. Los primeros cuatro dígitos, identificados con la letra “A”, corresponden a los caracteres alfabéticos.
1.2.2. Los siguientes seis dígitos, identificados con el “9”, corresponden a una numeración consecutiva.
1.2.3. El último dígito, identificado con el número “9”, corresponde al dígito verificador
1.2.4. Cada grupo de datos descritos en los tres sub apartes anteriores, deben estar separados por un guión “-”
1.3. Constituyen casos de excepción, las matrículas que no cuentan con la totalidad de los dígitos descritos; bien sea por el tipo particular de contenedor o por alguna otra razón de carácter operativo que se genere. Cuando se presenten estos casos, no debe dejarse ningún espacio en blanco ni colocar caracter especial alguno, para “rellenar” la totalidad de espacios. En otras palabras, la ausencia de uno o varios de los dígitos de la identificación de la matrícula, simplemente debe obviarse, al momento de realizar la digitación. Sobre este particular, caben cinco ejemplos:
1.3.1. Si la matrícula no cuenta con los descriptores alfabéticos, se empezará a digitar a partir de los descriptores numéricos, así: “999999-9”
1.3.2. Si la matrícula cuenta con menos de cuatro descriptores alfabéticos, se empezará a digitar a partir de los descriptores existentes, así: “AA-999999-9”
1.3.3. Si la matrícula no cuenta con los descriptores numéricos, se empezará a digitar a partir de los descriptores alfabéticos, así: “AAAA-9”
1.3.4. Si la matrícula cuenta con menos de seis descriptores numéricos, se empezará a digitar a partir de los descriptores existentes, así: “AAAA-9999-9”
1.3.5. Si la matrícula no cuenta con el dígito verificador, se omitirá su digitación, así: “AAAA-999999”
1.4. El formato de matrícula aquí descrito deberá respetarse para cualquier operación aduanera: viajes (traslado), tránsitos, importación y similares que haga referencia al número de la matrícula.
1.5. A partir de la vigencia de esta circular, el listado exigido por las autoridades portuarias para la autorización de la salida de los patios, la podrá emitir directamente el transportista naviero desde el Sistema Tic@. Dicha opción se encuentra en la consulta WEB, en el apartado “manifiesto/contenedores”.
2. Sobre la movilización de los contenedores:
2.1. A todo contenedor transmitido al Sistema Tic@ se le deberá asociar un viaje, para efectos de verificar su ingreso al territorio nacional.
2.2. La movilización de los contenedores llenos, cuya mercancía no se ha nacionalizado, desde puerto aduanero (ubicación=P) hasta otra ubicación dentro de la misma jurisdicción, se realizará por medio de un viaje. Se exceptúan las movilizaciones hacia empresas de los regímenes de Perfeccionamiento Activo y Zona Franca, para las cuales se deberá confeccionar un DUA de tránsito.
2.3. La movilización de los contenedores llenos, cuya mercancía no se ha nacionalizado, desde puerto aduanero (ubicación=P) hasta otra ubicación en diferente jurisdicción, se realizará por medio de un DUA de tránsito.
2.4. La movilización de los contenedores llenos, cuya mercancía ha sido nacionalizada en puerto aduanero (ubicación=P), deberá hacerse por medio de un viaje, que será generado automáticamente con la declaración de importación. Dicho viaje, no tendrá lugar de llegada y se completará cuando se le de la salida, de manera que el viaje quede cancelado al momento de dar la salida de la instalación en la cual se ubica la mercancía. No obstante, hasta tanto se desarrolle una opción, en el tipo de viaje “TRS”, que posibilite lo anterior, en los primeros 5 días de cada mes, la gerencia de cada aduana, mediante resolución razonada, solicitará a la Dirección General de Informática que proceda a completar los viajes que se produzcan, en forma automática, según lo aquí descrito; para balancear la información.
2.5. La movilización de los contenedores vacíos, desde la zona portuaria (ubicación=P) hasta el estacionamiento transitorio (ubicación=E) se realizará por medio de un viaje.
2.6. Si la movilización de un contenedor vacío se va a llevar a cabo hacia un recinto aduanero de la misma jurisdicción de la aduana de ingreso, se confeccionará un viaje
2.7. Cualquier contenedor vacío puede contar con uno o más precintos, si la empresa naviera o el propietario del mismo estiman que, por razones de seguridad, es necesario aplicar este mecanismo. En tal evento, se deberá registrar, en la transmisión del contenedor al Sistema Tic@, la identificación de los marchamos, al igual que se hace con los contenedores llenos.
2.8. Cualquier contenedor que se declare en condición de vacío, que venga o no con marchamo, deberá ser revisado por la autoridad portuaria, al momento de su salida, sin detrimento de los controles aduaneros.
2.9. Para todo contenedor que se le haya generado un viaje, se le deberán indicar los siguientes valores:
2.9.1. La cantidad de bultos va a ser igual a 1, pues corresponde al contenedor que se está movilizando.
2.9.2. El peso sería igual al registrado bajo la denominación “tara” el cual se entiende como el peso de la unidad de transporte cuando está vacía.
3. Sobre el control por parte de los auxiliares:
3.1. Ningún auxiliar de la función pública tramitará archivo alguno, si el formato de la matrícula del contenedor no se ajusta a lo descrito en el presente documento. Ello con fundamento en el artículo 219 del Reglamento a la Ley General de Aduanas.
3.2. De encontrarse alguna inconsistencia en la matrícula, de acuerdo con lo descrito en el este documento, el auxiliar comunicará el error al transportista internacional, quién estará en la obligación de realizar las correcciones que procedan.
4. Sobre la intervención de la autoridad portuaria:
4.1. En los mismos términos del aparte anterior, la autoridad portuaria no permitirá la salida de ningún contenedor cuya matrícula física no se ajuste a lo aquí estipulado.
5. Vigencia:
5.1. Esta disposición rige a partir del 27 de noviembre del 2007.
Envíese la presente circular al casillero de cada uno de los auxiliares indicados.
Publíquese en el Diario Oficial La Gaceta.
