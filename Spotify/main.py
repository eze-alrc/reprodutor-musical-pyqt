import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# from verificar import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_verificar.clicked.connect(self.verificar_idade)

    def verificar_idade(self):
        idade = int(self.ui.lineEdit_idade.text())

        if idade >= 18:
            
            self.ui.label_2.setText(f"Entrada Liberada.")

        else:
            self.ui.label_2.setText(f"Entrada Negada.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())