from PySide6.QtWidgets import QApplication
from buttons import ButtonsGrid
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

    buttonsGrid = ButtonsGrid(display)
    window.vLayout.addLayout(buttonsGrid)

    window.adjustFixedSize()
    window.show()
    app.exec()
