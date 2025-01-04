import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from main_window import MainWindow
from display import Display
from info import Info
from variables import WINDOW_ICON_PATH
from styles import setupTheme
from buttons import Button


if __name__ == '__main__':
    # Recomenda-se utilizar um ou outro nunca variar entre os tipos
    # snake_case -> métodos e variáveis
    # PascalCase -> classes
    # camelCase -> métodos e variáveis

    # Cria aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    # É interessante setar tanto no window quanto no
    # app por questões de compatibildiade entre Windows e Mac.
    # No meu teste funcionou das duas formas
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)

    # Display
    display = Display()
    # Adiciona um Placeholder
    # display.setPlaceholderText('Digite algo')
    window.addToVLayout(display)

    # Button
    button = Button('Texto do botão')
    window.addToVLayout(button)

    # label1 utilizado apenas para exemplo
    # label1 = QLabel('O meu texto')

    # é chamado de QSS = a CSS do HTML
    # label1.setStyleSheet('font-size: 50px;')
    # window.addWidgetToVLayout(label1)

    # Executa tudo
    # Caso quisesse alterar por aqui
    # A última alteração é a que prevalece
    # window.setWindowTitle('Novo título')
    window.adjustFixedSize()  # No professor teve que adicionar
    #                           aqui pois estava aparecendo o ícone
    #                           de redimencionar a tela. No meu caso bugava
    #                           o redimencionamento de alguns componentes
    window.show()
    app.exec()
