from PySide6.QtWidgets import QPushButton, QGridLayout

from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        minSize = [75, 75]

        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(*minSize)
        # self.setProperty('cssClass', 'specialButton')

        # Assim não sobrescreve as configurações que já foram feitas
        # self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px;')


class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0',  '', '.', '='],
        ]

        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, button_text in enumerate(row):
                # Melhor sempre por boa prática utilizar uma variável para
                # receber pois se não utilizar irá dar bug no index 0 0,
                # igual abaixo
                button = Button(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')

                if button_text == '0':
                    self.addWidget(button, i, j, 1, 2)
                elif button_text != '':
                    self.addWidget(button, i, j)
