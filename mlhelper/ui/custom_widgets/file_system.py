from PySide6.QtWidgets import QFileSystemModel

class FileSystemModel(QFileSystemModel):
    def __init__(self):
        super().__init__()

        self.setRootPath("")