import logging
from PySide6.QtWidgets import QTreeView, QDockWidget
from PySide6.QtCore import Qt

from ..data_models.file_system import FileSystemModel

logger = logging.getLogger(__name__)

class Explorer(QDockWidget):
    def __init__(self):
        super().__init__()

        logger.debug("Initialized exploreer")

        self.file_system_model=FileSystemModel()
        self.view_files = QTreeView()

        self.view_files.setModel(self.file_system_model)

        self.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea)

        self.setWidget(self.view_files)