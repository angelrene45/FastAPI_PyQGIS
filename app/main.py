from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from qgis.core import QgsApplication

from app.utils.geopackage import create_gpkg
from app.utils.test_tools import prueba_herramientas_pyqgis

# iniciamos app qgis 
QgsApplication.setPrefixPath(r"C:\Program Files\QGIS 3.22.10", True)
app = QgsApplication([], False)
# cargar providers
QgsApplication.initQgis()

# iniciamos app de fastapi
app = FastAPI(title="Prueba PyQGIS")

# montamos una carpeta estatica guardar archivos
app.mount("/static", StaticFiles(directory="static"), name="static")

# habilitamos que otros usuarios puedan ver mi backend
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)


# rutas que escuchan las peticiones
@app.get("/gpkg")
def root():
    msg = create_gpkg()
    return msg


@app.get("/tools")
def root():
    msg = prueba_herramientas_pyqgis()
    return msg