import asyncio
import sys

from PySide6.QtWidgets import QMainWindow, QMessageBox
from qasync import QApplication, QEventLoop, asyncClose, asyncSlot

from ui.ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_About_shiny_adventure.triggered.connect(self.aboutMe)

    @asyncClose
    async def closeEvent(self, event):
        pass

    @asyncSlot()
    async def aboutMe(self):
        QMessageBox.about(
            self,
            "About shiny-adventure",
            "<h2>shiny-adventure is a one-paragraph blurb bruh blah</h2>"
            "<p align='center'>This application was created by bhbghghbgb.<br>"
            "MIT License<br>"
            "Copyright 2024-2024 Such-and-such.<br>"
            "For more information, visit my <a href='https://github.com/bhbghghbgb/shiny-adventure'>GitHub page</a>.</p>",
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    event_loop = QEventLoop(app)
    asyncio.set_event_loop(event_loop)

    app_close_event = asyncio.Event()
    app.aboutToQuit.connect(app_close_event.set)

    main_window = MainWindow()
    main_window.show()

    with event_loop:
        event_loop.run_until_complete(app_close_event.wait())
