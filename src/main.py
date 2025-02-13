from PySide6.QtWidgets import QApplication
from buttons import ButtonsGrid, Button
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_DIR
from display import Display
from styles import setupTheme
from info import Info
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()
    window.setWindowTitle('Calculadora')
    icon = QIcon(str(WINDOW_ICON_DIR))

    info = Info('Label principal')
    window.addWidgetToVLayout(info)

    display = Display()
    window.addWidgetToVLayout(display)
    window.setWindowIcon(icon)

    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)

    buttonsGrid.addWidget(Button('0'), 0, 0)
    buttonsGrid.addWidget(Button('1'), 0, 1)
    buttonsGrid.addWidget(Button('2'), 0, 2)

    window.adjustFixedSize()
    window.show()
    app.exec()
