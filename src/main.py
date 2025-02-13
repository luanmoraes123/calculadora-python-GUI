from PySide6.QtWidgets import QApplication
from buttons import Button
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

    info = Info('Label principal')
    window.addToVLayout(info)

    display = Display()
    window.addToVLayout(display)
    icon = QIcon(str(WINDOW_ICON_DIR))
    window.setWindowIcon(icon)

    button = Button('Texto do botao')
    window.addToVLayout(button)

    window.adjustFixedSize()
    window.show()
    app.exec()
