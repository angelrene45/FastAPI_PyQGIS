# FastApi PyQGIS App

## Instrucciones
* Abrir el cmd y ejecutar el archivo bat "C:\\Program Files\\QGIS 3.22.10\\bin\\python-qgis-ltr-processing.bat"
* Instalar la libreria de fast api con sus dependencias
```python
    python -m pip install "fastapi[all]"
```
* Para levantar el backend muevete a la carpeta donde se encuentra el proyecto y ejecuta
```python
    python -m uvicorn app.main:app --reload --host 0.0.0.0
```