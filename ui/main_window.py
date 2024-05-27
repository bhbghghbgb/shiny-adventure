from PySide6.QtWidgets import QButtonGroup, QMainWindow, QMessageBox
from qasync import asyncClose, asyncSlot

import ui_constants
from ui.ui import Ui_MainWindow


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

        self.buttonGroup_subtitle = QButtonGroup(self.groupBox_subtitle)
        self.buttonGroup_subtitle.addButton(
            self.radioButton_subtitle_language_all, ui_constants.SUBTITLE_ALL_GROUP_ID
        )
        self.buttonGroup_subtitle.addButton(
            self.radioButton_subtitle_language_rules,
            ui_constants.SUBTITLE_RULES_GROUP_ID,
        )

        self.buttonGroup_sponsorblock = QButtonGroup(self.groupBox_sponsorblock)
        self.buttonGroup_sponsorblock.addButton(
            self.radioButton_sponsorblock_disable,
            ui_constants.SPONSORBLOCK_DISABLE_GROUP_ID,
        )
        self.buttonGroup_sponsorblock.addButton(
            self.radioButton_sponsorblock_remove,
            ui_constants.SPONSORBLOCK_REMOVE_GROUP_ID,
        )
        self.buttonGroup_sponsorblock.addButton(
            self.radioButton_sponsorblock_mark, ui_constants.SPONSORBLOCK_MARK_GROUP_ID
        )

        self.buttonGroup_sponsorblock_section = QButtonGroup(self.groupBox_sponsorblock)
        self.buttonGroup_sponsorblock_section.addButton(
            self.checkBox_sponsorblock_default,
            ui_constants.SPONSORBLOCK_SECTION_DEFAULT_GROUP_ID,
        )
        self.buttonGroup_sponsorblock_section.addButton(
            self.checkBox_sponsorblock_all,
            ui_constants.SPONSORBLOCK_SECTION_ALL_GROUP_ID,
        )
        self.buttonGroup_sponsorblock_section.addButton(
            self.checkBox_sponsorblock_chapter,
            ui_constants.SPONSORBLOCK_SECTION_CHAPTER_GROUP_ID,
        )
        self.buttonGroup_sponsorblock_section.addButton(
            self.checkBox_sponsorblock_sponsor,
            ui_constants.SPONSORBLOCK_SECTION_SPONSOR_GROUP_ID,
        )
        self.buttonGroup_sponsorblock_section.addButton(
            self.checkBox_sponsorblock_intro,
            ui_constants.SPONSORBLOCK_SECTION_INTRO_GROUP_ID,
        )
        self.buttonGroup_sponsorblock_section.addButton(
            self.checkBox_sponsorblock_outro,
            ui_constants.SPONSORBLOCK_SECTION_OUTRO_GROUP_ID,
        )
        self.buttonGroup_sponsorblock_section.addButton(
            self.checkBox_sponsorblock_selfpromo,
            ui_constants.SPONSORBLOCK_SECTION_SELFPROMO_GROUP_ID,
        )
        self.buttonGroup_sponsorblock_section.addButton(
            self.checkBox_sponsorblock_preview,
            ui_constants.SPONSORBLOCK_SECTION_PREVIEW_GROUP_ID,
        )
        self.buttonGroup_sponsorblock_section.addButton(
            self.checkBox_sponsorblock_filler,
            ui_constants.SPONSORBLOCK_SECTION_FILLER_GROUP_ID,
        )
        self.buttonGroup_sponsorblock_section.addButton(
            self.checkBox_sponsorblock_interaction,
            ui_constants.SPONSORBLOCK_SECTION_INTERACTION_GROUP_ID,
        )
        self.buttonGroup_sponsorblock_section.addButton(
            self.checkBox_sponsorblock_music_offtopic,
            ui_constants.SPONSORBLOCK_SECTION_MUSIC_OFFTOPIC_GROUP_ID,
        )
        self.buttonGroup_sponsorblock_section.addButton(
            self.checkBox_sponsorblock_poi_highlight,
            ui_constants.SPONSORBLOCK_SECTION_POI_HIGHLIGHT_GROUP_ID,
        )
        self.buttonGroup_sponsorblock_section.setExclusive(False)

        self.buttonGroup_pyml = QButtonGroup(self.groupBox_pymlmain)
        self.buttonGroup_pyml.addButton(
            self.radioButton_pyml_export, ui_constants.PYML_EXPORT_GROUP_ID
        )
        self.buttonGroup_pyml.addButton(
            self.radioButton_pyml_tag, ui_constants.PYML_TAG_GROUP_ID
        )
        self.buttonGroup_pyml.addButton(
            self.radioButton_pyml_extend, ui_constants.PYML_EXTEND_GROUP_ID
        )
        self.buttonGroup_pyml.addButton(
            self.radioButton_pyml_split, ui_constants.PYML_SPLIT_GROUP_ID
        )

        self.buttonGroup_afk = QButtonGroup(self.groupBox_afk)
        self.buttonGroup_afk.addButton(
            self.radioButton_afk_nothing, ui_constants.AFK_NOTHING_GROUP_ID
        )
        self.buttonGroup_afk.addButton(
            self.radioButton_afk_shutdown, ui_constants.AFK_SHUTDOWN_GROUP_ID
        )
        self.buttonGroup_afk.addButton(
            self.radioButton_afk_restart, ui_constants.AFK_RESTART_GROUP_ID
        )
        self.buttonGroup_afk.addButton(
            self.radioButton_afk_close, ui_constants.AFK_CLOSE_GROUP_ID
        )
        self.buttonGroup_afk.addButton(
            self.radioButton_afk_command, ui_constants.AFK_COMMAND_GROUP_ID
        )

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
