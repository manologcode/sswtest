### Easy ScreenShort testing

Este es un proyecto para poder hacer testing de aplicaciones web de forma fácil y sencilla mediante la comparación de capturas de pantalla

Se trata de un artefacto dockerizado de varias librerías de python combinadas para testear aplicaciones web mediante la comparación de capturas de pantalla.


Para correr la aplicación necesitamos pásenle la información mediante un archivo yml con las instrucciones:


ejemplo de archivo básico.

```
config:
  name: manolog_es
  folder: inicial
  size_screen: 1420,1080
  compare: 
pages:

- url: https://manolog.es/blog/
  actions:
  - photo:
- url: https://manolog.es/blog/formacion/
  actions:
  - photo:
- url: https://manolog.es/blog/2022/05/27/_netdata_monitorizacion_con_docker_auth/
  actions:
  - photo:
- url: https://manolog.es/blog/2022/05/18/raspberry_servidor_archivos_audio/
  actions:
  - photo:
- url: https://manolog.es/blog/2022/05/12/wireguard-docker-crea-una-vps-en-5-minutos/
  actions:
  - photo:

```

Donde la parte de configuración podemos modificar:

| option | tipo  | required  |  description  |
|--------|--------|----------|------------|
| name  |  string  | true | Nombre de la carpeta del proyecto, si existe se toma el nombre del archivo yml   |
| folder  |  string  | true | Nombre de la carpeta de almacenamiento de las capturas actuales, si existe la crea con la fecha actual |
| size_screen  | array  |  false  | resoluciones a las que queremos las capturas  |
| compare  | array  |  false  | carpeta con la que va a comparar las imágenes de las capturas actuales |


## correr el contenedor

Para ejecutar el contenedor sin argumentos, el creador del archivos yml inicial

    docker run -it --rm -v $(pwd):/app/data_ext manologcode/sswtest

Para ejecutar el contenedor pesándole un archivo yml de con las configuración y las acciones

    docker run -it --rm -v $(pwd)/app:/app -e mypath=$(pwd) manologcode/sswtest python app.py manolog_es.yml

He creado una archivo sh para ejecutar el contenedor y no escribir tantas sentencia docker **sswtest.sh**. Copiándose a nuestro source, se nos cargar los comandos cortos para usarlos rápidamente en esta sesión de terminal:

    source <(curl -s https://raw.githubusercontent.com/manologcode/sswtest/master/sswtest.sh)

ya podemos ejecutar los siguientes comandos

    sswtest -> ejecutar la aplicación.
    sswtest archivourls.yml
    sswtest-rmi -> borrar la imagen del contenedor

## Eliminar la imagen de docker

Si no vamos a utilizar mas la aplicación y no queremos que nos ocupe espacio en disco la podemos borrar

    docker rmi manologcode/sswtest