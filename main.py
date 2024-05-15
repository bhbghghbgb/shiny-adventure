import sys
import asyncio

from qasync import QEventLoop, QApplication, asyncClose, asyncSlot
from PySide6.QtWidgets import QMainWindow, QTabWidget

from ui.tab1 import Tab1


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.tab = QTabWidget()
        self.setCentralWidget(self.tab)
        self.tab1 = Tab1()
        self.tab.addTab(self.tab1, "My Tab")

    @asyncClose
    async def closeEvent(self, event):
        pass

    @asyncSlot()
    async def onMyEvent(self):
        pass


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
