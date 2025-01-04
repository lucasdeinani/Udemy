from PySide6.QtWidgets import QPushButton

from variables import MEDIUM_FONT_SIZE


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
        self.setProperty('cssClass', 'specialButton')

        # Assim não sobrescreve as configurações que já foram feitas
        # self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px;')
