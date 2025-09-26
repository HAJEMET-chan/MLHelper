import logging
from PySide6.QtWidgets import QFileSystemModel

logger = logging.getLogger(__name__)


class FileSystemModel(QFileSystemModel):
    def __init__(self):
        super().__init__()

        logger.debug("Initialized file system")

        self.setRootPath("")
