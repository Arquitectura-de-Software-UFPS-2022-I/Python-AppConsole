# Python-AppConsole

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Descripción Y Contexto
Es una aplicación open-source que permita firmar un documento PDF. Consiste en insertar la imagen de la firma manuscrita de una o varias personas.

## Requerimientos
Numero |Descripcion
-- | --
1 | Registrarse en la aplicación para poder usarla.
2 | Registrar una firma, lo que consiste en subir una imagen. Es deseable una funcionalidad inteligente que verifique si la imagen corresponde a una firma.
3 | Subir un documento PDF y solicitar la firma de usuarios registrados en la plataforma. La solicitud es notificada al correo electrónico y en la aplicación debe existir una sección de solicitudes pendientes por firma y solicitudes firmadas.
4 | Firmar un documento PDF para el cual se ha solicitado la firma. La aplicación debe permitir visualizar el PDF, insertar la firma y guardarlo.
5 | Debe quedar el registro histórico de las firmas.

## Instalación
Primero, clone el repositorio en su máquina local:
```bash
git clone https://github.com/Arquitectura-de-Software-UFPS-2022-I/Python-AppConsole
```

Después de clonar el repositorio, desea crear un entorno virtual, por lo que tiene una instalación de python limpia.
Puedes hacer esto ejecutando el comando:
```
python -m venv venv
```

Después de esto, es necesario activar el entorno virtual, puede obtener más información al respecto [here](https://docs.python.org/3/tutorial/venv.html)
```
venv\Scripts\activate
```

Luego instalar todas las dependencias requeridas ejecutando el comando:
```
pip install -r requirements.txt
```

## Ejecutar el Proyecto
Finalmente, ejecute el servidor de desarrollo:
```bash
python manage.py runserver
```

El proyecto estará disponible en **127.0.0.1:8000/signature-recognition/**

## Menu Opciones
En la siguiente tabla se describe el menu de operaciones establecido en la aplicacion:


Numero | Opcion | Descripcion
:--: | :--: | --
1 | [Upload a signature](#upload-signature) |
2 | [Upload pdf file](#upload-pdf-file) |
3 | Request a signature |
4 | Sign a document |
5 | Generate pdf file |
6 | List all signature requests approved |
7 | List all signature requests pending |
8 | List all of my pending signature requests |
9 | Signature history |
10 | Logout |

### Upload a signature
### Upload pdf file	
### Request a signature	
### Sign a document	
### Generate pdf file	
### List all signature requests approved	
### List all signature requests pending	
### List all of my pending signature requests	
### Signature history	
### Logout

## Autor(es)

**David Fernando Rojas Sáchica - Desarrollador**

-   <https://github.com/Sachica>
 
**Manuel Alejandro Coronel Andrade - Desarrollador**

-   <https://github.com/ManuelCoronelAndrade>
   
**Stiward Jherikof Carrillo Ramírez - Desarrollador**

-   <https://github.com/stiwardjherikofcr>
 
**Carlos Duvan Labrador Hernandez - Desarrollador**

-   <https://github.com/stiwardjherikofcr>

## Institución Académica

**[Programa de Ingeniería de Sistemas]** de la **[Universidad Francisco de Paula Santander]**

[Programa de Ingeniería de Sistemas]: https://ingsistemas.cloud.ufps.edu.co/
[Universidad Francisco de Paula Santander]: https://ww2.ufps.edu.co/

## Licencia
El código fuente se publica bajo la [MIT License](https://github.com/sibtc/django-multiple-user-types-example/blob/master/LICENSE).