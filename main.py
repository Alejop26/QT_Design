# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.form_main import Ui_MainWindow
from controller import validar_campos_propietario, validar_campos_finca

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar botones
        self.ui.btnAgregarPropietario.clicked.connect(self.accion_agregar_propietario)
        self.ui.btnAgregarFinca.clicked.connect(self.accion_agregar_finca)

    def accion_agregar_propietario(self):
        validar_campos_propietario(self.ui)

    def accion_agregar_finca(self):
        validar_campos_finca(self.ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec_())
