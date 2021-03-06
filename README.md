# Python-AppConsole 💻

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Descripción Y Contexto

Es una aplicación open-source que permita firmar un documento PDF. Consiste en insertar la imagen de la firma manuscrita de una o varias personas.

## Requerimientos 📑

Número | Descripción |
:--: | -- |
1 | Registrarse en la aplicación para poder usarla. |
2 | Registrar una firma, lo que consiste en subir una imagen. Es deseable una funcionalidad inteligente que verifique si la imagen corresponde a una firma. |
3 | Subir un documento PDF y solicitar la firma de usuarios registrados en la plataforma. La solicitud es notificada al correo electrónico y en la aplicación debe existir una sección de solicitudes pendientes por firma y solicitudes firmadas. |
4 | Firmar un documento PDF para el cual se ha solicitado la firma. La aplicación debe permitir visualizar el PDF, insertar la firma y guardarlo. |
5 | Debe quedar el registro histórico de las firmas. |

## Comenzando 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

## Requisitos de la Aplicación 📋

Primero, instalar Python 3.9.0  o superior en tu maquina local.

para Windows:

[Python 3.9.0](https://www.python.org/downloads/)


para Linux:

```bash
    $ sudo apt-get install python3.9.0
```
## Instalación 🔧

Primero, clone el repositorio en su máquina local:
```bash
git clone https://github.com/Arquitectura-de-Software-UFPS-2022-I/Python-AppConsole.git
```

Después de clonar el repositorio, desea crear un entorno virtual, por lo que tiene una instalación de python limpia.
Puedes hacer esto ejecutando el comando:
```
python -m venv venv
```

Después de esto, es necesario activar el entorno virtual, puede obtener más información al respecto [Aqui](https://docs.python.org/3/tutorial/venv.html)
```
venv\Scripts\activate
```

Luego instalar todas las dependencias requeridas ejecutando el comando:
```
pip install -r requirements.txt
```

### Ejecutar el proyecto localmente

Finalmente, ejecute el servidor de desarrollo:
```bash
python main.py
```

## Demo de la Aplicación 📦

para Windows:

[DocuSing](https://mega.nz/file/fRRRCYQK#HrmyYIgHk2jUnoH8ful0_JF4IxvEWFQpSGb6Tx6iifo)

para Linux:
```bash
    $ sudo https://mega.nz/file/fRRRCYQK#HrmyYIgHk2jUnoH8ful0_JF4IxvEWFQpSGb6Tx6iifo
    $ sudo chmod +x main.exe
```

## Menu Opciones

En la siguiente tabla se describe el menu de operaciones establecido en la aplicacion:

Número | Opción | Descripción
:--: | :--: | -- |
1 | [Upload a signature](#upload-signature) | Subir una firma. |
2 | [Upload pdf file](#upload-pdf-file) | Subir un documento PDF. |
3 | [Request a signature](#request-signature) | Solicitar una firma. |
4 | [Sign a document](#sign-document) | Firmar un documento. |
5 | [Generate pdf file](#generate-pdf-file) | Generar un documento PDF. |
6 | [List all signature requests approved](#list-signature-requests-approved) | Listar todas las solicitudes de firma aprobadas. |
7 | [List all signature requests pending](#list-signature-requests-pending) | Listar todas las solicitudes de firma pendientes. |
8 | [List all of my pending signature requests](#list-pending-signature-requests) | Listar todas mis solicitudes de firma pendientes. |
9 | [Signature history](#signature-history) | Historial de firmas. |
10 | [Logout](#logout) | Cerrar sesión. |

### <a id="upload-signature">Upload a signature</a>

Selecciona la opción 1 y ingresa la ruta de la imagen de la firma.

![Upload a signature](/public/img/upload-signature.PNG "Esta es una imagen de muestra.")

### <a id="upload-pdf-file">Upload pdf file</a>

Selecciona la opción 2 y ingresa la ruta del documento PDF.

![Upload pdf file](/public/img/upload-file.PNG "Esta es una imagen de muestra.")

### <a id="request-signature">Request a signature</a>

Selecciona la opción 3 y ingresa el id de la petición.

![request-signature](/public/img/request-signature.PNG "Esta es una imagen de muestra.")

ingresa el id del usuario, la pagina y la posición de la firma.

![request-signature](/public/img/request-signature-II.PNG "Esta es una imagen de muestra.")


para finalizar, una vez que se haya ingresado la información, presiona 0 para envíar la petición de firma a los usuarios registrados.

![request-signature](/public/img/request-signature-III.PNG "Esta es una imagen de muestra.")

### <a id="sign-document">Sign a document</a>

Selecciona la opción 4 y ingresa el id de la solicitud de firma.

### <a id="generate-pdf-file">Generate pdf file</a>

Selecciona la opción 5 y genera un documento PDF con las firmas.

### <a id="list-signature-requests-approved">List all signature requests approved</a>

Selecciona la opción 6 y lista todas las solicitudes de firma aprobadas.

### <a id="list-signature-requests-pending">List all signature requests pending</a>

Selecciona la opción 7 y lista todas las solicitudes de firmas pendientes.

### <a id="list-pending-signature-requests">List all of my pending signature requests</a>

Selecciona la opción 8 y lista todas mis solicitudes de firma pendientes.

### <a id="signature-history">Signature history</a>

Selecciona la opción 9 y lista el historial de firmas.

### <a id="logout">Logout</a>

Selecciona la opción 10 y cierra la sesión.

## Construido con 🛠️

* [Python](https://docs.python.org/3/) - Lenguaje de programación interpretado

## Autores ✒️

**David Fernando Rojas Sáchica - Desarrollador**

-   <https://github.com/Sachica>
 
**Manuel Alejandro Coronel Andrade - Desarrollador**

-   <https://github.com/ManuelCoronelAndrade>
   
**Stiward Jherikof Carrillo Ramírez - Desarrollador**

-   <https://github.com/stiwardjherikofcr>
 
**Carlos Duvan Labrador Hernandez - Desarrollador**

-   <https://github.com/DuvanLabrador27>

## Institución Académica 🏛️

**[Programa de Ingeniería de Sistemas]** de la **[Universidad Francisco de Paula Santander]**

[Programa de Ingeniería de Sistemas]: https://ingsistemas.cloud.ufps.edu.co/
[Universidad Francisco de Paula Santander]: https://ww2.ufps.edu.co/

## Licencia 📄

El código fuente se publica bajo la [MIT License](https://github.com/Arquitectura-de-Software-UFPS-2022-I/Python-AppConsole/blob/develop-sjcr/LICENSE).

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.