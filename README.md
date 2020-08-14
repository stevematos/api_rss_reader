# API RSS READER

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

4. Ejecutar la aplicacion:
```.shell script
    python main.py
```

Si es la primera que lo corre la aplicacion , se creara la base de datos de forma automatica
 en sqllite.