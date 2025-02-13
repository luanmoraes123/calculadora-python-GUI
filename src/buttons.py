from PySide6.QtWidgets import QPushButton, QGridLayout
from display import Display
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.display = display
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.',  '=']
        ]
        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)
                button.setMinimumHeight(80)
                buttonSlot = self._makeButtonDisplaySlot(
                    self._insertButtonTextToDisplay,
                    button)
                button.clicked.connect(buttonSlot)
                if not isNumOrDot(button.text()):
                    button.setProperty('cssClass', 'specialButton')
                if button.text() == '0':
                    self.addWidget(button, i, j - 1, 1, 2)
                else:
                    self.addWidget(button, i, j)

    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        def realSlot(checked):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button: Button):
        self.display.insert(button.text())
