from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.cw = QWidget()  # cw = Central Widget
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        # Título da janela
        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        # Última coisa a ser feita
        self.adjustSize()
        # Interessante ter o .adjustSize(), pois ele ajusta o
        # tamanho da tela com o conteúdo
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)
        # Teve que ser criado esse método para que ele
        # ajuste a tela aos itens que estão nela
        self.adjustFixedSize()
