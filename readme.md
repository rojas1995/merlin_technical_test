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

Para ejecutar el script de python lo único que se necesita es tener la versión de python 3.10 instalada (esta es la versión que tengo instalada, pero es seguro que corra con versiones anteriores 3.x).

Para ejecutarlo solo tienes que ejecutar el siguiente comando:

```
python request.py
```
or

```
python3 request.py
```
