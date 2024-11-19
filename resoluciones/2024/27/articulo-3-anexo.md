ANEXO 3. "INFORMACIÓN PARA LA CONEXIÓN CON EL API DE COMPROBANTES ELECTRÓNICOS DEL MINISTERIO DE HACIENDA"
Bitácora de Cambios
Cambios 20/02/2017 (Resolución DGT-R-13-2017) versión 4.1
1. Se actualizan los URL con la información del dominio final.
2. Se amplía la información del método de seguridad que utilizará el API.
3. Se agrega información del Access Token URL y Grant Type.
4. Se explica con más detalle como funciona el Callback.
5. Se agrega el proceso para solicitar el usuario y contraseña desde el ATV.
La Dirección General de Tributación (DGT) ha decidido que para la recepción de comprobantes electrónicos se utilizará un API RESTful, este expondrá los recursos disponibles al contribuyente para que pueda enviar y consultar el estado de los comprobantes electrónicos.
Información para la conexión
El API se encuentra publicado en la URI https://api.comprobanteselectronicos.go.cr/recepcion/v1/.
Para utilizar el servicio es obligatorio el uso de un canal HTTPS.
Todos los mensajes serán de tipo JSON.
Los mensajes recibidos y enviados atraves del API deberán utilizar el mapa de caracteres UTF8.
Se habilitará el URI https://api.comprobanteselectronicos.go.cr/recepcion-sandbox/v1/ para que sea utilizado como un ambiente de pruebas del contribuyente para la integración con sus sistemas. La base de datos que utiliza este API de sandbox se puede limpiar en cualquier momento para reiniciar el ambiente.
Seguridad
Todos los recursos del API se encuentran protegidos, es requerido iniciar sesión en el API para poder consumirlos.
El API utiliza un modelo de seguridad con Open ID Connect (OIDC - http://openid.net/connect/) el cual funciona como una capa de identidad sobre el protocolo OAuth2.0, el OIDC utiliza JSON Web Tokens (JWT) para almacenar la información de los Tokens.
Desde la aplicación cliente se debe consumir el Identity Provider (IdP) que se encuentra en el URI https://idp.comprobanteselectronicos.go.cr/auth, este IdP permite crear nuevos Tokens (JWT) o refrescar los existentes ya que estos tienen un tiempo de expiración de 5 minutos.
Cuando se tiene el Token generado por el IdP, este se envía en el contenido del Header "Authorization" con el prefijo "bearer". (Ver ejemplo en la documentación Web).
Para los efectos prácticos el OIDC es una extensión del estándar de OAuth2.0 (RFC 6749), para esta implementación se utiliza de la misma forma que un OAuth2.0 con el Grant Type llamado "Resource Owner Password Credential". Para utilizarlo va a requerir de un Username, Password y Access Token URL, el IdP le genera un Token el cuál el contribuyente en su aplicación debe enviar para consumir el API de Recepción de Documentos. Este Token que se generó tiene un tiempo de expiración que es parte del estándar de OAuth2.0, la aplicación del contribuyente debe encargarse de renovar este Token cuando expira para mantener la continuidad del servicio y cerrar la sesión al terminar.
El estándar de OAuth2.0 solicitará usuario y contraseña para generar el Access Token, este usuario y contraseña son exclusivos para cada contribuyente. Para obtener la contraseña se deben realizar los siguientes pasos.
1. Deben ingresar al Sistema de Administración Tributaria Virtual (ATV), haciendo uso de los mecanismos de seguridad ya proporcionados. En aquellos casos que los obligados tributarios no posean dicho acceso, deben realizar su respectivo registro en este sistema.
2. Una vez que se ingrese al sistema, se debe presionar la opción denominada "Comprobantes Electrónica"; la cual mostrará la funcionalidad de generación de contraseña.
3. El sistema le estará enviando al buzón electrónico la contraseña generada que será utilizada para el API de Recepción de Comprobantes Electrónicos.
Información para OAuth2.0:
Access Token URL = https://idp.comprobanteselectronicos.go.cr/auth/realms/rut/protocol/openid-connect/token
Grant Type = Resource Owner Password Credential
Authorization Grants = password
Client Id = api-prod
Client Secret = [Vacio]
Scope = [Vacio]
Username = [Identificación del contribuyente. Ej: cpf-01-1234-5678@comprobanteselectronicos.go.cr]
Password = [Password generado en ATV]
NOTA: El "Client Secret" y el "Scope" se dejan vacíos.
Recursos disponibles
/recepcion:
Recepción de comprobantes electrónicos y respuestas del receptor.
POST: Recibe el comprobante electrónico o respuesta del receptor. (Ver más información en la documentación Web).
/{clave}:
GET: Obtiene el estado del comprobante indicado por la clave. (Ver más información en la documentación Web).
/comprobantes:
Comprobantes electrónicos que ha enviado el obligado tributario.
GET: Obtiene un resumen de todos los comprobantes electrónicos que ha enviado el obligado tributario ordenado de forma descendente por la fecha. (Ver más información en la documentación Web).
/{clave}:
GET: Obtiene el comprobante indicado por la clave. (Ver más información en la documentación Web).
Para obtener más información acerca del API, ejemplos de los mensajes y la información de los JSON Schemas, ver la documentación en el Portal de Hacienda.
Funcionamiento del Callback
En el recurso /recepcion del REST API de Recepción de Comprobantes Electrónicos, para el POST se define en el Json Schema un atributo llamado "callbackUrl", la función de este atributo es que el contribuyente al momento de consumir el API y enviar un comprobante, pueda elegir un URL donde recibir la respuesta de forma asincrónica, y de esta forma facilitar la automatización de los procesos para los contribuyentes.
Se recuerda que en el mismo recurso, para el método GET con la {clave} se puede validar y obtener el mismo Json que se recibiría utilizando el "callbackUrl".
Este URL que el contribuyente indique debe permitir el enviar una petición POST con un body (contenido) application/json que sería igual al Json que responde el GET con la {clave}, ejemplo:
{
"clave": "50601011600310112345600100010100000000011999999999",
"fecha": "2016-01-01T00:00:00-0600",
"indEstado": "RECIBIDO",
"respuestaXml":
"PD94bWwgdmVyc2lvbj0iMS4wIiA/Pg0KDQo8ZG9tYWluIHhtbG5zPSJ1cm46amJvc3M6ZG9tYWluOjQuMCI+DQogICAgPGV4dGVuc2lvbnM+DQogICAgICAgIDxleHRlbnNpb24gbW9kdWxlPSJvcmcuamJvc3MuYXMuY2x1c3RlcmluZy5pbmZpbmlzcGFuIi8+DQogICAgICAgIDxleHRlbnNpb24gbW9kdWxlPSJvcmcuamJvc3MuYXMuY2x1c3RlcmluZy5qZ3JvdXBzIi8+DQogICAgICAgIDxleHRlbnNpb24gbW9kdWxlPSJvcmcuamJvc3MuYXMuY29ubmVjdG9yIi8+DQogICAgICAgIDxleHRlbnNpb24gbW..."
}
Y el URL debe responder con un HTTP_OK (200), si no se recibe el HTTP_OK o se recibe un error de timeout, se realizarían 3 reintentos. Si aún así no se recibió la respuesta HTTP_OK, no se enviaría más y se guarda en bitácoras que el contribuyente tenía problemas para recibir el Callback en ese momento. El contribuyente podrá consultarlo en el API de Recepción.
