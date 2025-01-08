import math

from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot

from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from display import Display

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from main_window import MainWindow
    from info import Info


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
    def __init__(
        self, display: 'Display', info: 'Info', window: 'MainWindow',
        *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0',  '', '.', '='],
        ]
        self.display: 'Display' = display
        self.info: 'Info' = info
        self.window = window
        self._equation: str = ''
        self._equationInitialValue: str = 'Sua conta'
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def vouApagarVocê(self, *args):
        print(
            'Sinal recebido por "vouApagarVocê" em',
            type(self).__name__,
            args
        )

    def _makeGrid(self):
        self.display.eqPressed.connect(self.vouApagarVocê)
        self.display.delPressed.connect(self.display.backspace)
        self.display.clearPressed.connect(self.vouApagarVocê)
        self.display.inputPressed.connect(self.vouApagarVocê)

        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                # Melhor sempre por boa prática utilizar uma variável para
                # receber pois se não utilizar irá dar bug no index 0 0,
                # igual abaixo
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                if buttonText == '0':
                    self.addWidget(button, i, j, 1, 2)
                elif buttonText != '':
                    self.addWidget(button, i, j)

                slot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button: Button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button: Button):
        buttonText = button.text()

        if buttonText == 'C':
            # Versão mais rápida porém como vamos dar clear
            # em mais coisas, vamos fazer dessa outra forma
            # button.clicked.connect(self.display.clear)
            self._connectButtonClicked(button, self._clear)
        elif buttonText == 'D':
            self._connectButtonClicked(button, self.display.backspace)
        elif buttonText in '+-/*^':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._operatorClicked, button)
            )
        elif buttonText == '=':
            self._connectButtonClicked(button, self._eq)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button: Button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)
        # Tive que colocar este setFocus() pois ao clicar nos botões
        # ele tirava o foco do display, desssa forma tinha que ficar
        # clicando no display para retomar o foco correto
        self.display.setFocus()

    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button: Button):
        buttonText = button.text()  # +-/* (etx...)
        displayText = self.display.text()  # Deverá ser meu número _left
        self.display.clear()  # Limpa o display

        # Se a pessoa clicou no operador
        # sem configurar qualquer número
        if not isValidNumber(displayText) and self._left is None:
            self._showError('Você não digitou nada.')
            return

        # Se houver algo no número da esquerda, não
        # fizemos nada. Aguardaremos o número da direita
        if self._left is None:
            self._left = float(displayText)

        self._op = buttonText
        self.equation = f'{self._left} {self._op} ??'

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            self._showError('Conta incompleta.')
            return

        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'

        result = 'error'
        try:
            if '^' in self.equation and isinstance(self._left, float):
                # duas formas de serem feitas
                # result = eval(self.equation.replace('^', '**'))
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Divisão por zero.')
        except OverflowError:
            self._showError('Essa conta não pode ser realizada.')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')

        self._left = result
        self._right = None

        if result != 'error':
            self._left = None
        else:
            self._clear()

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        # Mostra uma mensagem no MsgBox
        # msgBox.setInformativeText('Algo de errrado não está certo nisso')
        msgBox.setIcon(msgBox.Icon.Critical)

        # Adicionar opções de botões para mostrar ao usuário.
        # Para adicionar mais de um botão deve-se utilizar pipe
        # msgBox.setStandardButtons(
        #     msgBox.StandardButton.Ok |
        #     msgBox.StandardButton.Cancel
        # )

        # Caso queira alterar o texto de um botão pode-se fazer desta forma
        # msgBox.button(msgBox.StandardButton.NoToAll).setText('Não pra todos')
        # result = msgBox.exec()

        # Conseguir saber o que o usuário clicou
        # if result == msgBox.StandardButton.Ok:
        #     print('Usuário clicou em Ok')
        msgBox.exec()

    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
