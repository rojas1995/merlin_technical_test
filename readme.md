### Prueba técnica

Este proyecto de cypress tiene como objetivo resolver el segundo ejercicio de la prueba técnica, consistente en hacer una prueba automática de una web.
En concreto, hay que realizar una búsqueda en Google y escoger el primer resultado de la Wikipedia y encontrar cuando se realizó el primer proceso automático.

Se ha añadido también un fichero python (request.py) para la prueba de la API.

### Requisitos

## Primer ejercicio

Para poder correr el test necesitas clonar este repositorio, tener la última versión estable de node.js (v18.14.2) y ejecutar los siguientes comandos en la raíz del proyecto.

```
npm install cypress

npm install --save-dev typescript

npm i
```

## Correr el test

Para correr el test solo necesitas ejecutar el siguiente comando en la raíz del proyecto:

```
npx cypress open
```

Cuando se abra la ventana de cypress elegimos la opción E2E testing, escogemos cualquier navegador y clickamos en el archivo testWikipedia.cy.ts, luego de esto el test debería ejecutarse.

## Segundo ejercicio

Para ejecutar el script de python lo único que se necesita es tener la versión de python 3.7 instalada e instalar la dependencia 'requests' (esta es la versión que tengo instalada, con la versión 3.11 no corre la versión alternativa del ejercicio con apache beam, si quieres correr la versión alternativa te recomiendo la 3.7).

Para instalar las dependencias de requests y apache beam ejecuta:

```
pip install requests

pip install apache-beam
```

Para ejecutarlo solo tienes que ejecutar el siguiente comando:

```

python request.py
```
or

```
python3 request.py
```
