from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_DIR
from display import Display
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle('Calculadora')

    display = Display()
    window.addToVLayout(display)
    icon = QIcon(str(WINDOW_ICON_DIR))
    window.setWindowIcon(icon)
    window.show()
    app.exec()
