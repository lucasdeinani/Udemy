import sys

from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from main_window import MainWindow
from variables import WINDOW_ICON_PATH


if __name__ == '__main__':
    # Cria aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    # É interessante setar tanto no window quanto no
    # app por questões de compatibildiade entre Windows e Mac.
    # No meu teste funcionou das duas formas
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    label1 = QLabel('O meu texto')

    # é chamado de QSS = a CSS do HTML
    label1.setStyleSheet('font-size: 50px;')
    window.addWidgetToVLayout(label1)

    # Caso quisesse alterar por aqui
    # A última alteração é a que prevalece
    # window.setWindowTitle('Novo título')
    window.adjustFixedSize()  # No professor teve que adicionar
    #                           aqui pois estava aparecendo o ícone
    #                           de redimencionar a tela
    window.show()
    app.exec()
