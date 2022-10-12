from qgis.core import (QgsProject, QgsVectorFileWriter, QgsField, QgsFeature,
                       QgsGeometry, QgsVectorLayer, QgsPointXY)
from PyQt5.QtCore import QVariant

def create_gpkg():
        """
            Metodo que va generar un geopackage
        """
        # create layer
        vl = QgsVectorLayer("Point", "temporary_points", "memory")
        pr = vl.dataProvider()

        # add fields
        pr.addAttributes([QgsField("name", QVariant.String),
                            QgsField("age",  QVariant.Int),
                            QgsField("size", QVariant.Double)])
        vl.updateFields() # tell the vector layer to fetch changes from the provider

        # add a feature
        fet = QgsFeature()
        fet.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(10,10)))
        fet.setAttributes(["Johny", 2, 0.3])
        pr.addFeatures([fet])

        # update layer's extent when new features have been added
        # because change of extent in provider is not propagated to the layer
        vl.updateExtents()

        # generamos la capa .shp
        crs = vl.crs()
        crs.createFromId(6365)
        path_gpkg = "static/my_new_file.gpkg"

        save_options = QgsVectorFileWriter.SaveVectorOptions()
        transform_context = QgsProject.instance().transformContext()

        # Write to a GeoPackage (default)
        error = QgsVectorFileWriter.writeAsVectorFormatV3(vl,
                                                        path_gpkg,
                                                        transform_context,
                                                        save_options)
        if error[0] == QgsVectorFileWriter.NoError:
            print("success!")
        else:
            print(error)

        public_url = f"localhost:8000/{path_gpkg}"
        return {"path_downdload" : public_url}