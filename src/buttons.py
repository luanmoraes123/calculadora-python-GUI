from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)


class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

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
                self.addWidget(Button(buttonText), i, j)
