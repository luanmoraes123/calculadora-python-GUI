from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.cw = QWidget()

        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)

        self.setCentralWidget(self.cw)
