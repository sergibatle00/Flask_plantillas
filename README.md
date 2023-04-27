# Flask_plantillas

El archivo base.html contiene la plantilla que se usara en las diferentes páginas de la aplicación web 
en los archivos html de la aplicación se introduce el contenido usando las etiquetas:

>{% extends "base.html" %}

>{% block title %} {% endblock %}

>{% block title2 %} {% endblock %}

>{% block content %} {% endblock %}

Las etiquetas block title y block title2 nos permiten modificar el contenido del elemento title y h2 respectivamente.
La etiqueta block content nos permite insertar el contenido principal a cada página

Todos los archivos html se encuentran en un fichero llamado 'Templates', tambien tenemos un fichero llamado 'static' donde guardaremos las imagenes.

## Nota

En el tutorial de vscode Flask se mencionan unos pasos en el que se crea un archivo json para poder debuggear la aplicacion en caso de que queramos insertar variables en la aplicacion web desde el archivo de Python como se nos muestra en el ejemplo con:

> now = datetime.now

El archivo json nos permitira observar el comportamiento de estas variables, yo no lo he incluido en mi aplicaion puesto que no lo he considerado necesario para cumplir el objetivo de crear una aplicacion web usando plantillas Flask.
