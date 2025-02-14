from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot

from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isValidNumber
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from info import Info


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info',  *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.display = display
        self.info = info
        self._equation = ''
        self._left = None
        self._right = None
        self._op = None
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.',  '=']
        ]
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)
                button.setMinimumHeight(80)
                slot = self._makeSlot(
                    self._insertButtonTextToDisplay,
                    button)
                self._connectButtonClicked(button, slot)
                if not isNumOrDot(button.text()):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)
                if button.text() == '0':
                    self.addWidget(button, i, j - 1, 1, 2)
                else:
                    self.addWidget(button, i, j)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text in '+-/*':
            self._connectButtonClicked(
                button, self._makeSlot(self._operatorClicked, button))

        if text in '=':
            self._connectButtonClicked(
                button, self._eq)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button: Button):
        buttonText = button.text()
        newDisplayText = self.display.text() + buttonText

        if not isValidNumber(newDisplayText):
            return
        self.display.insert(button.text())

    def _clear(self):
        self.display.clear()
        self.equation = ''
        self._left = None
        self._right = None
        self._op = None

    def _operatorClicked(self, button):
        text = button.text()
        displayText = self.display.text()
        self.display.clear()
        if not isValidNumber(displayText) and self._left is None:
            print('Não tem nada para colocar no valor da esquerda')
            return
        if self._left is None:
            self._left = float(displayText)

        self._op = text
        self.equation = f'{self._left} {self._op} '

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        self.display.clear()
        try:
            result = eval(self.equation)
        except ZeroDivisionError:
            result = ''
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
