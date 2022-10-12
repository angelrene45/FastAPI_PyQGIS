from qgis.core import *
from qgis.gui import * 
from qgis.utils import * 
from qgis.PyQt.QtCore import QVariant
from qgis.analysis import QgsNativeAlgorithms
from osgeo import ogr
import numpy as np

# Necesario para cargar los DLL de los algoritmos de processing
import processing
from processing.core.Processing import Processing
Processing.initialize()

def prueba_herramientas_pyqgis():
    # crear una capa en memoria y asignamos feature y geometria
    layer_point = QgsVectorLayer("Point", "temp", "memory")
    pr = layer_point.dataProvider()
    pr.addAttributes([QgsField("name", QVariant.String),
                    QgsField("age",  QVariant.Int),
                    QgsField("size", QVariant.Double)])
    layer_point.updateFields() 
    eature_point = QgsFeature()
    eature_point.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(10,10)))
    eature_point.setAttributes(["Ada L.", 2, 0.3])
    pr.addFeature(eature_point)
    e = layer_point.extent()
    features_point = [ [f.id(), f.attributes(), f.geometry().asWkt()] for f in layer_point.getFeatures()]


    print ("BUFFER a capa en memoria")
    result = processing.run("native:buffer", {'INPUT': layer_point, 'DISTANCE': 2.0, 'SEGMENTS': 10, 'DISSOLVE': True, 'END_CAP_STYLE': 0, 'JOIN_STYLE': 0, 'MITER_LIMIT': 10, 'OUTPUT': 'memory:buffer_layer'})
    layer_buffer = result['OUTPUT']
    ext = layer_buffer.extent()
    print ("Name : ",layer_buffer.name())
    print ("Extension : ",ext.asWktCoordinates())
    for f in layer_buffer.getFeatures(): print("Feature:", f.id(), f.attributes(), f.geometry())

    print("="*45)
    print("OSGEO")
    point = ogr.Geometry(ogr.wkbPoint)
    point.AddPoint(1198054.34, 648493.09)
    print(point.ExportToWkt(),'\n')

    print("=======================")
    print("NUMPY")
    a = np.arange(15).reshape(3, 5)
    print(a, '\n')

    msg = {
        "Capa Punto" : layer_point.isValid(),
        "Num Features" : layer_point.featureCount(),
        "Features" : features_point,
        "Extent:": f" {e.xMinimum()}, {e.yMinimum()}, {e.xMaximum()}, {e.yMaximum()}",
        "Geometry Buffer": f.geometry().asWkt()
    }

    return msg