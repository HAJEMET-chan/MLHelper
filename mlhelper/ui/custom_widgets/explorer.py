from PySide6.QtWidgets import QTreeView

from .file_system import FileSystemModel

class Explorer(QTreeView):
    def __init1__(self):
        super().__init__()

        self.file_system_model=FileSystemModel()

        self.setModel(self.file_system_model)