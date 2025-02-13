from PySide6.QtWidgets import (
    QApplication, QVBoxLayout, QWidget, QLabel)
from main_window import MainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle('Calculadora')
    window.show()
    app.exec()
