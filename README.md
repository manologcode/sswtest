### Easy ScreenShort testing

Este es un proyecto para poder hacer testing de aplicaciones web de forma fácil y sencilla mediante la comparación de capturas de pantalla

Se trata de un artefacto dockerizado de varias librerías de python combinadas para testear aplicaciones web mediante la comparación de capturas de pantalla.

para correr la aplicación necesitamos pásenle la información mediante un archivo yml con las instrucciones:


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


donde la parte de configuracion podemos modificar:

| option | tipo  | required  |  description  |
|--------|--------|----------|------------|
| name  |  string  | true | Nombre de la carpeta del proyecto, si existe se toma el nombre del archivo yml   |
| folder  |  string  | true | Nombre de la carpeta de almacenamiento de las capturas actuales, si existe la crea con la fecha actual |
| size_screen  | array  |  false  | resoluciones a las que queremos las capturas  |
| compare  | array  |  false  | carpeta con la que va a comparar las imagenes de las capturas actuales |


crear las capturas en un carpeta con la fecha por defecto


pasar parametros



-compare="namefolder"
-autourls
-photos=false
