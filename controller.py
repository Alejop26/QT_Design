from PyQt5.QtWidgets import QMessageBox

def validar_campos_propietario(ui):
    campos = [
        ui.inputDocumento.text(),
        ui.inputNombre.text(),
        ui.inputApellido.text(),
        ui.inputTelefono.text(),
        ui.inputCorreo.text()
    ]

    if any(campo.strip() == "" for campo in campos):
        mostrar_mensaje("Error al insertar Productor", error=True)
    else:
        mostrar_mensaje("¡Productor Agregado!", error=False)

def validar_campos_finca(ui):
    municipio = ui.inputMunicipio.text().strip()
    registro = ui.InputRegistro.text().strip()

    # Si alguno de los campos NO está vacío, mostrar error
    if municipio != "" or registro != "":
        mostrar_mensaje("No se puede agregar la finca: los campos deben estar vacíos", error=True)
    else:
        mostrar_mensaje("¡Finca Agregada!", error=False)


def mostrar_mensaje(mensaje, error=False):
    msg = QMessageBox()
    msg.setWindowTitle(mensaje)
    msg.setText(mensaje)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    if error:
        msg.setIcon(QMessageBox.Critical)
    else:
        msg.setIcon(QMessageBox.Information)

    msg.exec_()
