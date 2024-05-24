import ui_constants
from ui.ui import Ui_MainWindow


from PySide6.QtWidgets import QMainWindow, QMessageBox, QButtonGroup
from qasync import asyncClose, asyncSlot


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setupButtonGroups()

        self.action_About_shiny_adventure.triggered.connect(self.aboutMe)

    def setupButtonGroups(self):
        self.buttonGroup_quality = QButtonGroup(self.groupBox_quality)
        self.buttonGroup_quality.addButton(
            self.radioButton_quality_best, ui_constants.QUALITY_BEST_GROUP_ID
        )
        self.buttonGroup_quality.addButton(
            self.radioButton_quality_worst, ui_constants.QUALITY_WORST_GROUP_ID
        )
        self.buttonGroup_quality.addButton(
            self.radioButton_quality_at_most, ui_constants.QUALITY_AT_MOST_GROUP_ID
        )
        self.buttonGroup_quality.addButton(
            self.radioButton_quality_at_least, ui_constants.QUALITY_AT_LEAST_GROUP_ID
        )

        self.buttonGroup_stream = QButtonGroup(self.groupBox_stream)
        self.buttonGroup_stream.addButton(
            self.radioButton_stream_both, ui_constants.STREAM_BOTH_GROUP_ID
        )
        self.buttonGroup_stream.addButton(
            self.radioButton_stream_audio, ui_constants.STREAM_AUDIO_GROUP_ID
        )

        # TODO: remaining radio button groups
        # TODO: sponsorblock groups

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
