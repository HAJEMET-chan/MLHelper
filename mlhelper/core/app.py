import sys
from PySide6.QtWidgets import QApplication

from ..ui import MainWindow
from .logging_setup import setup_logger


def start():
    logger = setup_logger(__name__)
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
