from PySide6.QtWidgets import QMainWindow

from .custom_widgets.explorer import Explorer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.explorer: Explorer = Explorer()

    def set_dock_widgets(self):
        self.addDockWidget(self.explorer)