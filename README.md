# API RSS READER

Requerimientos:
 - Python 3.7 >

Pasos para instalarlo:

1. Clonar el repositorio:

```.shell script
    git clone https://github.com/stevematos/api_rss_reader
```
  
2. Crear y activar el entorno virtual:
```.shell script
    virtualenv env -p python3
    source env/bin/activate
```
   

3. Instalar los requerimientos:
```.shell script
    pip install -r requirements.txt
```

4. Ejecutar la aplicacion, si desea ejecutarlo con el cron que actualiza los feeds solo agregue el argumento --feed_cron 1:
```.shell script
    python main.py [--feed_cron 1]
```

La aplicacion estar corriendo en el localhost:8000

Si es la primera que lo corre la aplicacion , se creara la base de datos de forma automatica
 en sqllite llamada sql_app.db.
 
Si desea ejecutar las pruebas unitarias lo hace con el comando
```shell script
    python -m unittest tests/__init__.py  
```