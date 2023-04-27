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
