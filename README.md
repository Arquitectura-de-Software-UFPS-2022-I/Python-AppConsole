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

Primero, instalar Python 3.6.5 o superior.

para Windows:

[Python 3.6.5](https://www.python.org/downloads/)


para Linux:

```bash
    $ sudo apt-get install python3.6
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

[DocuSing](https://mega.nz/file/2NxjzA7A#EVdtx4Ug7LKg9T0qXQROs91713reVr3mkFGRlkSHhb0)

para Linux:
```bash
    $ sudo https://mega.nz/file/2NxjzA7A#EVdtx4Ug7LKg9T0qXQROs91713reVr3mkFGRlkSHhb0
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


### <a id="upload-pdf-file">Upload pdf file</a>


### <a id="request-signature">Request a signature</a>


### <a id="sign-document">Sign a document</a>


### <a id="generate-pdf-file">Generate pdf file</a>


### <a id="list-signature-requests-approved">List all signature requests approved</a>


### <a id="list-signature-requests-pending">List all signature requests pending</a>


### <a id="list-pending-signature-requests">List all of my pending signature requests</a>


### <a id="signature-history">Signature history</a>


### <a id="logout">Logout</a>



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