import os
import shlex
from dataclasses import dataclass

import string_utils
import yt_dlp

from exceptions import UiCorruptionError
from ui.main_window import MainWindow


@dataclass
class GeneralTabInput:
    """The General tab has inputs that must be given to yt-dlp as positional
    arguments and must be passed at the end of the command (path and link).

    There are options that can be loaded with a .conf file and manually passed
    args. So we seperate those to allow for changes to overriding behavior if needed."""

    regular_options: list[str]
    path_and_link: tuple[str, str]
    conf_file_options: list[str]
    typed_args_options: list[str]


class MainController:
    def __init__(self, main_window: MainWindow) -> None:
        self.ui = main_window

    def build_config_from_ui(self):
        args = []

    def build_config_from_general_tab(self) -> GeneralTabInput:
        """Path and filename will be joined to an output path.
        File extension is appended to filename."""
        # path and link
        parent_path = self.ui.lineEdit_argument_path.text()
        filename = f"{self.ui.lineEdit_argument_filename.text()}.%(ext)s"
        path = os.path.join(parent_path, filename)
        link = self.ui.lineEdit_argument_link.text()
        path_and_link = path, link

        # load .conf file
        conf_file_options = []
        conf_file_path = self.ui.lineEdit_argument_ytdlp_conf.text()
        conf_file_enabled = self.ui.checkBox_argument_ytdlp_conf.isChecked()
        if conf_file_enabled and string_utils.is_full_string(conf_file_path):
            conf_file_options = yt_dlp.utils._utils.Config.read_file(conf_file_path)

        # typed args
        typed_args = self.ui.lineEdit_argument_ytdlp_args.text()
        typed_args_options = shlex.split(typed_args)

        # regular options
        opts = []
        if self.ui.radioButton_stream_both.isChecked():
            stream_opt = "both"
        elif self.ui.radioButton_stream_audio.isChecked():
            stream_opt = "audio"
        else:
            raise UiCorruptionError(
                [self.ui.radioButton_stream_both, self.ui.radioButton_stream_audio],
                "None of the Stream RadioButtons in General tab is selected",
            )
        # TODO: continue the General tab
