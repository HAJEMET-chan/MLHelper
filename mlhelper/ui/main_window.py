import logging
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt

from .dock_widgets.explorer import Explorer

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        logger.info("Initialized main window")

        self.explorer: Explorer = Explorer()
        self.set_dock_widgets()

    def set_dock_widgets(self):
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.explorer)