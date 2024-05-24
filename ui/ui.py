# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QStatusBar,
    QTabWidget, QToolButton, QTreeView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(918, 600)
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        self.action_About_shiny_adventure = QAction(MainWindow)
        self.action_About_shiny_adventure.setObjectName(u"action_About_shiny_adventure")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab_general = QWidget()
        self.tab_general.setObjectName(u"tab_general")
        self.gridLayout_3 = QGridLayout(self.tab_general)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_quality = QGroupBox(self.tab_general)
        self.groupBox_quality.setObjectName(u"groupBox_quality")
        self.gridLayout_4 = QGridLayout(self.groupBox_quality)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.radioButton_quality_best = QRadioButton(self.groupBox_quality)
        self.radioButton_quality_best.setObjectName(u"radioButton_quality_best")
        self.radioButton_quality_best.setChecked(True)

        self.gridLayout_4.addWidget(self.radioButton_quality_best, 0, 0, 1, 1)

        self.radioButton_quality_at_most = QRadioButton(self.groupBox_quality)
        self.radioButton_quality_at_most.setObjectName(u"radioButton_quality_at_most")

        self.gridLayout_4.addWidget(self.radioButton_quality_at_most, 2, 0, 1, 1)

        self.radioButton_quality_at_least = QRadioButton(self.groupBox_quality)
        self.radioButton_quality_at_least.setObjectName(u"radioButton_quality_at_least")

        self.gridLayout_4.addWidget(self.radioButton_quality_at_least, 3, 0, 1, 1)

        self.comboBox_quality = QComboBox(self.groupBox_quality)
        self.comboBox_quality.addItem("")
        self.comboBox_quality.addItem("")
        self.comboBox_quality.addItem("")
        self.comboBox_quality.addItem("")
        self.comboBox_quality.addItem("")
        self.comboBox_quality.addItem("")
        self.comboBox_quality.addItem("")
        self.comboBox_quality.addItem("")
        self.comboBox_quality.addItem("")
        self.comboBox_quality.setObjectName(u"comboBox_quality")

        self.gridLayout_4.addWidget(self.comboBox_quality, 2, 1, 2, 1)

        self.radioButton_quality_worst = QRadioButton(self.groupBox_quality)
        self.radioButton_quality_worst.setObjectName(u"radioButton_quality_worst")

        self.gridLayout_4.addWidget(self.radioButton_quality_worst, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_quality, 0, 2, 1, 1)

        self.groupBox_arguments = QGroupBox(self.tab_general)
        self.groupBox_arguments.setObjectName(u"groupBox_arguments")
        self.gridLayout = QGridLayout(self.groupBox_arguments)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_argument_link = QLineEdit(self.groupBox_arguments)
        self.lineEdit_argument_link.setObjectName(u"lineEdit_argument_link")

        self.gridLayout.addWidget(self.lineEdit_argument_link, 0, 2, 1, 1)

        self.label_argument_link = QLabel(self.groupBox_arguments)
        self.label_argument_link.setObjectName(u"label_argument_link")

        self.gridLayout.addWidget(self.label_argument_link, 0, 0, 1, 1)

        self.label_argument_path = QLabel(self.groupBox_arguments)
        self.label_argument_path.setObjectName(u"label_argument_path")

        self.gridLayout.addWidget(self.label_argument_path, 1, 0, 1, 1)

        self.pushButton_argument_link_multiple = QPushButton(self.groupBox_arguments)
        self.pushButton_argument_link_multiple.setObjectName(u"pushButton_argument_link_multiple")

        self.gridLayout.addWidget(self.pushButton_argument_link_multiple, 0, 3, 1, 1)

        self.lineEdit_argument_path = QLineEdit(self.groupBox_arguments)
        self.lineEdit_argument_path.setObjectName(u"lineEdit_argument_path")

        self.gridLayout.addWidget(self.lineEdit_argument_path, 1, 2, 1, 1)

        self.label_argument_ytdlp_args = QLabel(self.groupBox_arguments)
        self.label_argument_ytdlp_args.setObjectName(u"label_argument_ytdlp_args")

        self.gridLayout.addWidget(self.label_argument_ytdlp_args, 4, 0, 1, 1)

        self.toolButton_argument_link_add = QToolButton(self.groupBox_arguments)
        self.toolButton_argument_link_add.setObjectName(u"toolButton_argument_link_add")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButton_argument_link_add.sizePolicy().hasHeightForWidth())
        self.toolButton_argument_link_add.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.toolButton_argument_link_add, 0, 4, 1, 1)

        self.lineEdit_argument_ytdlp_args = QLineEdit(self.groupBox_arguments)
        self.lineEdit_argument_ytdlp_args.setObjectName(u"lineEdit_argument_ytdlp_args")

        self.gridLayout.addWidget(self.lineEdit_argument_ytdlp_args, 4, 2, 1, 1)

        self.lineEdit_argument_filename = QLineEdit(self.groupBox_arguments)
        self.lineEdit_argument_filename.setObjectName(u"lineEdit_argument_filename")

        self.gridLayout.addWidget(self.lineEdit_argument_filename, 2, 2, 1, 1)

        self.label_argument_filename = QLabel(self.groupBox_arguments)
        self.label_argument_filename.setObjectName(u"label_argument_filename")

        self.gridLayout.addWidget(self.label_argument_filename, 2, 0, 1, 1)

        self.toolButton_argument_path_revert = QToolButton(self.groupBox_arguments)
        self.toolButton_argument_path_revert.setObjectName(u"toolButton_argument_path_revert")
        sizePolicy1.setHeightForWidth(self.toolButton_argument_path_revert.sizePolicy().hasHeightForWidth())
        self.toolButton_argument_path_revert.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.toolButton_argument_path_revert, 1, 4, 1, 1)

        self.pushButton_argument_path_browse = QPushButton(self.groupBox_arguments)
        self.pushButton_argument_path_browse.setObjectName(u"pushButton_argument_path_browse")

        self.gridLayout.addWidget(self.pushButton_argument_path_browse, 1, 3, 1, 1)

        self.label_argument_ytdlp_conf = QLabel(self.groupBox_arguments)
        self.label_argument_ytdlp_conf.setObjectName(u"label_argument_ytdlp_conf")

        self.gridLayout.addWidget(self.label_argument_ytdlp_conf, 3, 0, 1, 1)

        self.lineEdit_argument_ytdlp_conf = QLineEdit(self.groupBox_arguments)
        self.lineEdit_argument_ytdlp_conf.setObjectName(u"lineEdit_argument_ytdlp_conf")

        self.gridLayout.addWidget(self.lineEdit_argument_ytdlp_conf, 3, 2, 1, 1)

        self.pushButton_argument_ytdlp_conf_browse = QPushButton(self.groupBox_arguments)
        self.pushButton_argument_ytdlp_conf_browse.setObjectName(u"pushButton_argument_ytdlp_conf_browse")

        self.gridLayout.addWidget(self.pushButton_argument_ytdlp_conf_browse, 3, 3, 1, 1)

        self.checkBox_argument_ytdlp_conf = QCheckBox(self.groupBox_arguments)
        self.checkBox_argument_ytdlp_conf.setObjectName(u"checkBox_argument_ytdlp_conf")

        self.gridLayout.addWidget(self.checkBox_argument_ytdlp_conf, 3, 4, 1, 1)

        self.label_argument_filename_help = QLabel(self.groupBox_arguments)
        self.label_argument_filename_help.setObjectName(u"label_argument_filename_help")
        self.label_argument_filename_help.setTextFormat(Qt.AutoText)
        self.label_argument_filename_help.setAlignment(Qt.AlignCenter)
        self.label_argument_filename_help.setOpenExternalLinks(True)

        self.gridLayout.addWidget(self.label_argument_filename_help, 2, 3, 1, 2)

        self.label_argument_ytdlp_args_help = QLabel(self.groupBox_arguments)
        self.label_argument_ytdlp_args_help.setObjectName(u"label_argument_ytdlp_args_help")
        self.label_argument_ytdlp_args_help.setTextFormat(Qt.AutoText)
        self.label_argument_ytdlp_args_help.setAlignment(Qt.AlignCenter)
        self.label_argument_ytdlp_args_help.setOpenExternalLinks(True)

        self.gridLayout.addWidget(self.label_argument_ytdlp_args_help, 4, 3, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox_arguments, 0, 0, 2, 1)

        self.groupBox_stream = QGroupBox(self.tab_general)
        self.groupBox_stream.setObjectName(u"groupBox_stream")
        self.gridLayout_2 = QGridLayout(self.groupBox_stream)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton_stream_both = QRadioButton(self.groupBox_stream)
        self.radioButton_stream_both.setObjectName(u"radioButton_stream_both")
        self.radioButton_stream_both.setChecked(True)

        self.gridLayout_2.addWidget(self.radioButton_stream_both, 0, 0, 1, 1)

        self.radioButton_stream_audio = QRadioButton(self.groupBox_stream)
        self.radioButton_stream_audio.setObjectName(u"radioButton_stream_audio")

        self.gridLayout_2.addWidget(self.radioButton_stream_audio, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_stream, 0, 1, 1, 1)

        self.groupBox_format = QGroupBox(self.tab_general)
        self.groupBox_format.setObjectName(u"groupBox_format")
        self.gridLayout_5 = QGridLayout(self.groupBox_format)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_format_video = QLabel(self.groupBox_format)
        self.label_format_video.setObjectName(u"label_format_video")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_format_video.sizePolicy().hasHeightForWidth())
        self.label_format_video.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.label_format_video, 0, 0, 1, 1)

        self.comboBox_format_video = QComboBox(self.groupBox_format)
        self.comboBox_format_video.addItem("")
        self.comboBox_format_video.addItem("")
        self.comboBox_format_video.addItem("")
        self.comboBox_format_video.addItem("")
        self.comboBox_format_video.addItem("")
        self.comboBox_format_video.setObjectName(u"comboBox_format_video")

        self.gridLayout_5.addWidget(self.comboBox_format_video, 0, 1, 1, 1)

        self.comboBox_format_audio = QComboBox(self.groupBox_format)
        self.comboBox_format_audio.addItem("")
        self.comboBox_format_audio.addItem("")
        self.comboBox_format_audio.addItem("")
        self.comboBox_format_audio.addItem("")
        self.comboBox_format_audio.addItem("")
        self.comboBox_format_audio.setObjectName(u"comboBox_format_audio")

        self.gridLayout_5.addWidget(self.comboBox_format_audio, 1, 1, 1, 1)

        self.label_format_audio = QLabel(self.groupBox_format)
        self.label_format_audio.setObjectName(u"label_format_audio")
        sizePolicy2.setHeightForWidth(self.label_format_audio.sizePolicy().hasHeightForWidth())
        self.label_format_audio.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.label_format_audio, 1, 0, 1, 1)

        self.checkBox_format_prefer = QCheckBox(self.groupBox_format)
        self.checkBox_format_prefer.setObjectName(u"checkBox_format_prefer")

        self.gridLayout_5.addWidget(self.checkBox_format_prefer, 0, 2, 2, 1)


        self.gridLayout_3.addWidget(self.groupBox_format, 1, 1, 1, 2)

        self.groupBox_info = QGroupBox(self.tab_general)
        self.groupBox_info.setObjectName(u"groupBox_info")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_info)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toolButton_ytdlp_help = QToolButton(self.groupBox_info)
        self.toolButton_ytdlp_help.setObjectName(u"toolButton_ytdlp_help")
        sizePolicy1.setHeightForWidth(self.toolButton_ytdlp_help.sizePolicy().hasHeightForWidth())
        self.toolButton_ytdlp_help.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.toolButton_ytdlp_help)

        self.toolButton_ytdlp_version = QToolButton(self.groupBox_info)
        self.toolButton_ytdlp_version.setObjectName(u"toolButton_ytdlp_version")
        sizePolicy1.setHeightForWidth(self.toolButton_ytdlp_version.sizePolicy().hasHeightForWidth())
        self.toolButton_ytdlp_version.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.toolButton_ytdlp_version)

        self.label_ytdlp_github = QLabel(self.groupBox_info)
        self.label_ytdlp_github.setObjectName(u"label_ytdlp_github")
        self.label_ytdlp_github.setTextFormat(Qt.AutoText)
        self.label_ytdlp_github.setOpenExternalLinks(True)

        self.horizontalLayout_4.addWidget(self.label_ytdlp_github)


        self.gridLayout_3.addWidget(self.groupBox_info, 2, 1, 1, 3)

        self.groupBox_commands = QGroupBox(self.tab_general)
        self.groupBox_commands.setObjectName(u"groupBox_commands")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_commands)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_commands_start = QPushButton(self.groupBox_commands)
        self.pushButton_commands_start.setObjectName(u"pushButton_commands_start")

        self.horizontalLayout_5.addWidget(self.pushButton_commands_start)

        self.pushButton_commands_stop = QPushButton(self.groupBox_commands)
        self.pushButton_commands_stop.setObjectName(u"pushButton_commands_stop")

        self.horizontalLayout_5.addWidget(self.pushButton_commands_stop)

        self.pushButton_commands_remove = QPushButton(self.groupBox_commands)
        self.pushButton_commands_remove.setObjectName(u"pushButton_commands_remove")

        self.horizontalLayout_5.addWidget(self.pushButton_commands_remove)


        self.gridLayout_3.addWidget(self.groupBox_commands, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_general, "")
        self.tab_spices = QWidget()
        self.tab_spices.setObjectName(u"tab_spices")
        self.gridLayout_7 = QGridLayout(self.tab_spices)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_ppspices = QGroupBox(self.tab_spices)
        self.groupBox_ppspices.setObjectName(u"groupBox_ppspices")
        self.groupBox_ppspices.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_ppspices.setFlat(False)
        self.gridLayout_20 = QGridLayout(self.groupBox_ppspices)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.checkBox_ppspices_no_post_overwrites = QCheckBox(self.groupBox_ppspices)
        self.checkBox_ppspices_no_post_overwrites.setObjectName(u"checkBox_ppspices_no_post_overwrites")

        self.gridLayout_20.addWidget(self.checkBox_ppspices_no_post_overwrites, 0, 1, 1, 1)

        self.checkBox_ppspices_keep_video = QCheckBox(self.groupBox_ppspices)
        self.checkBox_ppspices_keep_video.setObjectName(u"checkBox_ppspices_keep_video")

        self.gridLayout_20.addWidget(self.checkBox_ppspices_keep_video, 0, 0, 1, 1)

        self.lineEdit_ppspices_recode = QLineEdit(self.groupBox_ppspices)
        self.lineEdit_ppspices_recode.setObjectName(u"lineEdit_ppspices_recode")

        self.gridLayout_20.addWidget(self.lineEdit_ppspices_recode, 5, 1, 1, 1)

        self.lineEdit_ppspices_remux = QLineEdit(self.groupBox_ppspices)
        self.lineEdit_ppspices_remux.setObjectName(u"lineEdit_ppspices_remux")

        self.gridLayout_20.addWidget(self.lineEdit_ppspices_remux, 5, 0, 1, 1)

        self.checkBox_ppspices_remux = QCheckBox(self.groupBox_ppspices)
        self.checkBox_ppspices_remux.setObjectName(u"checkBox_ppspices_remux")

        self.gridLayout_20.addWidget(self.checkBox_ppspices_remux, 4, 0, 1, 1)

        self.checkBox_ppspices_recode = QCheckBox(self.groupBox_ppspices)
        self.checkBox_ppspices_recode.setObjectName(u"checkBox_ppspices_recode")

        self.gridLayout_20.addWidget(self.checkBox_ppspices_recode, 4, 1, 1, 1)

        self.label_ppspices_remux_recode_help = QLabel(self.groupBox_ppspices)
        self.label_ppspices_remux_recode_help.setObjectName(u"label_ppspices_remux_recode_help")
        self.label_ppspices_remux_recode_help.setTextFormat(Qt.AutoText)
        self.label_ppspices_remux_recode_help.setOpenExternalLinks(True)

        self.gridLayout_20.addWidget(self.label_ppspices_remux_recode_help, 6, 0, 1, 2)


        self.gridLayout_7.addWidget(self.groupBox_ppspices, 1, 2, 2, 1)

        self.groupBox_thumbnail = QGroupBox(self.tab_spices)
        self.groupBox_thumbnail.setObjectName(u"groupBox_thumbnail")
        sizePolicy2.setHeightForWidth(self.groupBox_thumbnail.sizePolicy().hasHeightForWidth())
        self.groupBox_thumbnail.setSizePolicy(sizePolicy2)
        self.gridLayout_9 = QGridLayout(self.groupBox_thumbnail)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.checkBox_thumbnail_write = QCheckBox(self.groupBox_thumbnail)
        self.checkBox_thumbnail_write.setObjectName(u"checkBox_thumbnail_write")

        self.gridLayout_9.addWidget(self.checkBox_thumbnail_write, 0, 0, 1, 1)

        self.comboBox_thumbnail_convert_format = QComboBox(self.groupBox_thumbnail)
        self.comboBox_thumbnail_convert_format.addItem("")
        self.comboBox_thumbnail_convert_format.addItem("")
        self.comboBox_thumbnail_convert_format.addItem("")
        self.comboBox_thumbnail_convert_format.setObjectName(u"comboBox_thumbnail_convert_format")

        self.gridLayout_9.addWidget(self.comboBox_thumbnail_convert_format, 3, 1, 1, 1)

        self.checkBox_thumbnail_convert_format = QCheckBox(self.groupBox_thumbnail)
        self.checkBox_thumbnail_convert_format.setObjectName(u"checkBox_thumbnail_convert_format")

        self.gridLayout_9.addWidget(self.checkBox_thumbnail_convert_format, 3, 0, 1, 1)

        self.checkBox_thumbnail_embed = QCheckBox(self.groupBox_thumbnail)
        self.checkBox_thumbnail_embed.setObjectName(u"checkBox_thumbnail_embed")

        self.gridLayout_9.addWidget(self.checkBox_thumbnail_embed, 4, 0, 1, 1)

        self.checkBox_thumbnail_write_all_formats = QCheckBox(self.groupBox_thumbnail)
        self.checkBox_thumbnail_write_all_formats.setObjectName(u"checkBox_thumbnail_write_all_formats")

        self.gridLayout_9.addWidget(self.checkBox_thumbnail_write_all_formats, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_thumbnail, 1, 0, 1, 1)

        self.groupBox_subtitle = QGroupBox(self.tab_spices)
        self.groupBox_subtitle.setObjectName(u"groupBox_subtitle")
        sizePolicy2.setHeightForWidth(self.groupBox_subtitle.sizePolicy().hasHeightForWidth())
        self.groupBox_subtitle.setSizePolicy(sizePolicy2)
        self.gridLayout_8 = QGridLayout(self.groupBox_subtitle)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_subtitle_language = QLabel(self.groupBox_subtitle)
        self.label_subtitle_language.setObjectName(u"label_subtitle_language")
        self.label_subtitle_language.setTextFormat(Qt.AutoText)
        self.label_subtitle_language.setOpenExternalLinks(True)

        self.gridLayout_8.addWidget(self.label_subtitle_language, 2, 0, 2, 1)

        self.checkBox_subtitle_write = QCheckBox(self.groupBox_subtitle)
        self.checkBox_subtitle_write.setObjectName(u"checkBox_subtitle_write")

        self.gridLayout_8.addWidget(self.checkBox_subtitle_write, 0, 0, 1, 1)

        self.checkBox_subtitle_convert_format = QCheckBox(self.groupBox_subtitle)
        self.checkBox_subtitle_convert_format.setObjectName(u"checkBox_subtitle_convert_format")

        self.gridLayout_8.addWidget(self.checkBox_subtitle_convert_format, 6, 0, 1, 1)

        self.comboBox_subtitle_convert_format = QComboBox(self.groupBox_subtitle)
        self.comboBox_subtitle_convert_format.addItem("")
        self.comboBox_subtitle_convert_format.addItem("")
        self.comboBox_subtitle_convert_format.addItem("")
        self.comboBox_subtitle_convert_format.addItem("")
        self.comboBox_subtitle_convert_format.setObjectName(u"comboBox_subtitle_convert_format")

        self.gridLayout_8.addWidget(self.comboBox_subtitle_convert_format, 6, 1, 1, 1)

        self.checkBox_subtitle_format = QCheckBox(self.groupBox_subtitle)
        self.checkBox_subtitle_format.setObjectName(u"checkBox_subtitle_format")

        self.gridLayout_8.addWidget(self.checkBox_subtitle_format, 5, 0, 1, 1)

        self.comboBox_subtitle_format = QComboBox(self.groupBox_subtitle)
        self.comboBox_subtitle_format.addItem("")
        self.comboBox_subtitle_format.addItem("")
        self.comboBox_subtitle_format.addItem("")
        self.comboBox_subtitle_format.addItem("")
        self.comboBox_subtitle_format.setObjectName(u"comboBox_subtitle_format")

        self.gridLayout_8.addWidget(self.comboBox_subtitle_format, 5, 1, 1, 1)

        self.radioButton_subtitle_language_all = QRadioButton(self.groupBox_subtitle)
        self.radioButton_subtitle_language_all.setObjectName(u"radioButton_subtitle_language_all")
        self.radioButton_subtitle_language_all.setChecked(True)

        self.gridLayout_8.addWidget(self.radioButton_subtitle_language_all, 2, 1, 1, 1)

        self.radioButton_subtitle_language_rules = QRadioButton(self.groupBox_subtitle)
        self.radioButton_subtitle_language_rules.setObjectName(u"radioButton_subtitle_language_rules")

        self.gridLayout_8.addWidget(self.radioButton_subtitle_language_rules, 3, 1, 1, 1)

        self.checkBox_subtitle_autosub = QCheckBox(self.groupBox_subtitle)
        self.checkBox_subtitle_autosub.setObjectName(u"checkBox_subtitle_autosub")

        self.gridLayout_8.addWidget(self.checkBox_subtitle_autosub, 1, 0, 1, 1)

        self.checkBox_subtitle_embed = QCheckBox(self.groupBox_subtitle)
        self.checkBox_subtitle_embed.setObjectName(u"checkBox_subtitle_embed")

        self.gridLayout_8.addWidget(self.checkBox_subtitle_embed, 1, 1, 1, 1)

        self.lineEdit_subtitle_rules = QLineEdit(self.groupBox_subtitle)
        self.lineEdit_subtitle_rules.setObjectName(u"lineEdit_subtitle_rules")

        self.gridLayout_8.addWidget(self.lineEdit_subtitle_rules, 4, 0, 1, 2)


        self.gridLayout_7.addWidget(self.groupBox_subtitle, 1, 1, 3, 1)

        self.groupBox_metadata = QGroupBox(self.tab_spices)
        self.groupBox_metadata.setObjectName(u"groupBox_metadata")
        sizePolicy1.setHeightForWidth(self.groupBox_metadata.sizePolicy().hasHeightForWidth())
        self.groupBox_metadata.setSizePolicy(sizePolicy1)
        self.gridLayout_19 = QGridLayout(self.groupBox_metadata)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.checkBox_metadata_chapter = QCheckBox(self.groupBox_metadata)
        self.checkBox_metadata_chapter.setObjectName(u"checkBox_metadata_chapter")

        self.gridLayout_19.addWidget(self.checkBox_metadata_chapter, 1, 0, 1, 1)

        self.checkBox_metadata_info_json = QCheckBox(self.groupBox_metadata)
        self.checkBox_metadata_info_json.setObjectName(u"checkBox_metadata_info_json")

        self.gridLayout_19.addWidget(self.checkBox_metadata_info_json, 2, 0, 1, 1)

        self.checkBox_metadata_embed = QCheckBox(self.groupBox_metadata)
        self.checkBox_metadata_embed.setObjectName(u"checkBox_metadata_embed")

        self.gridLayout_19.addWidget(self.checkBox_metadata_embed, 0, 0, 1, 1)

        self.checkBox_metadata_xattrs = QCheckBox(self.groupBox_metadata)
        self.checkBox_metadata_xattrs.setObjectName(u"checkBox_metadata_xattrs")

        self.gridLayout_19.addWidget(self.checkBox_metadata_xattrs, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_metadata, 2, 0, 2, 1)

        self.groupBox_spicecmd = QGroupBox(self.tab_spices)
        self.groupBox_spicecmd.setObjectName(u"groupBox_spicecmd")
        self.gridLayout_28 = QGridLayout(self.groupBox_spicecmd)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.toolButton_spicecmd_list_formats = QToolButton(self.groupBox_spicecmd)
        self.toolButton_spicecmd_list_formats.setObjectName(u"toolButton_spicecmd_list_formats")
        sizePolicy1.setHeightForWidth(self.toolButton_spicecmd_list_formats.sizePolicy().hasHeightForWidth())
        self.toolButton_spicecmd_list_formats.setSizePolicy(sizePolicy1)

        self.gridLayout_28.addWidget(self.toolButton_spicecmd_list_formats, 0, 2, 1, 1)

        self.toolButton_spicecmd_list_subs = QToolButton(self.groupBox_spicecmd)
        self.toolButton_spicecmd_list_subs.setObjectName(u"toolButton_spicecmd_list_subs")
        sizePolicy1.setHeightForWidth(self.toolButton_spicecmd_list_subs.sizePolicy().hasHeightForWidth())
        self.toolButton_spicecmd_list_subs.setSizePolicy(sizePolicy1)

        self.gridLayout_28.addWidget(self.toolButton_spicecmd_list_subs, 0, 1, 1, 1)

        self.toolButton_spicecmd_list_thumbnails = QToolButton(self.groupBox_spicecmd)
        self.toolButton_spicecmd_list_thumbnails.setObjectName(u"toolButton_spicecmd_list_thumbnails")
        sizePolicy1.setHeightForWidth(self.toolButton_spicecmd_list_thumbnails.sizePolicy().hasHeightForWidth())
        self.toolButton_spicecmd_list_thumbnails.setSizePolicy(sizePolicy1)

        self.gridLayout_28.addWidget(self.toolButton_spicecmd_list_thumbnails, 0, 0, 1, 1)

        self.toolButton_spicecmd_list_extractors = QToolButton(self.groupBox_spicecmd)
        self.toolButton_spicecmd_list_extractors.setObjectName(u"toolButton_spicecmd_list_extractors")
        sizePolicy1.setHeightForWidth(self.toolButton_spicecmd_list_extractors.sizePolicy().hasHeightForWidth())
        self.toolButton_spicecmd_list_extractors.setSizePolicy(sizePolicy1)

        self.gridLayout_28.addWidget(self.toolButton_spicecmd_list_extractors, 0, 3, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_spicecmd, 3, 2, 1, 1)

        self.tabWidget.addTab(self.tab_spices, "")
        self.tab_miscellaneous = QWidget()
        self.tab_miscellaneous.setObjectName(u"tab_miscellaneous")
        self.gridLayout_10 = QGridLayout(self.tab_miscellaneous)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.groupBox_returnytdislikes = QGroupBox(self.tab_miscellaneous)
        self.groupBox_returnytdislikes.setObjectName(u"groupBox_returnytdislikes")
        self.gridLayout_21 = QGridLayout(self.groupBox_returnytdislikes)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.checkBox_returnytdislikes = QCheckBox(self.groupBox_returnytdislikes)
        self.checkBox_returnytdislikes.setObjectName(u"checkBox_returnytdislikes")

        self.gridLayout_21.addWidget(self.checkBox_returnytdislikes, 0, 0, 1, 1)

        self.label_returnytdislikes_help = QLabel(self.groupBox_returnytdislikes)
        self.label_returnytdislikes_help.setObjectName(u"label_returnytdislikes_help")
        self.label_returnytdislikes_help.setTextFormat(Qt.AutoText)
        self.label_returnytdislikes_help.setOpenExternalLinks(True)

        self.gridLayout_21.addWidget(self.label_returnytdislikes_help, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_returnytdislikes, 0, 2, 1, 1)

        self.groupBox_dontlock = QGroupBox(self.tab_miscellaneous)
        self.groupBox_dontlock.setObjectName(u"groupBox_dontlock")
        self.gridLayout_23 = QGridLayout(self.groupBox_dontlock)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.checkBox_dontlock = QCheckBox(self.groupBox_dontlock)
        self.checkBox_dontlock.setObjectName(u"checkBox_dontlock")

        self.gridLayout_23.addWidget(self.checkBox_dontlock, 0, 0, 1, 1)

        self.label_dontlock_help = QLabel(self.groupBox_dontlock)
        self.label_dontlock_help.setObjectName(u"label_dontlock_help")
        self.label_dontlock_help.setTextFormat(Qt.AutoText)
        self.label_dontlock_help.setOpenExternalLinks(True)

        self.gridLayout_23.addWidget(self.label_dontlock_help, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_dontlock, 0, 1, 1, 1)

        self.groupBox_internetshortcut = QGroupBox(self.tab_miscellaneous)
        self.groupBox_internetshortcut.setObjectName(u"groupBox_internetshortcut")
        self.gridLayout_11 = QGridLayout(self.groupBox_internetshortcut)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.checkBox_internetshortcut_windows = QCheckBox(self.groupBox_internetshortcut)
        self.checkBox_internetshortcut_windows.setObjectName(u"checkBox_internetshortcut_windows")

        self.gridLayout_11.addWidget(self.checkBox_internetshortcut_windows, 1, 0, 1, 1)

        self.checkBox_internetshortcut_mac = QCheckBox(self.groupBox_internetshortcut)
        self.checkBox_internetshortcut_mac.setObjectName(u"checkBox_internetshortcut_mac")

        self.gridLayout_11.addWidget(self.checkBox_internetshortcut_mac, 2, 0, 1, 1)

        self.checkBox_internetshortcut_platform = QCheckBox(self.groupBox_internetshortcut)
        self.checkBox_internetshortcut_platform.setObjectName(u"checkBox_internetshortcut_platform")

        self.gridLayout_11.addWidget(self.checkBox_internetshortcut_platform, 0, 0, 1, 1)

        self.checkBox_internetshortcut_linux = QCheckBox(self.groupBox_internetshortcut)
        self.checkBox_internetshortcut_linux.setObjectName(u"checkBox_internetshortcut_linux")

        self.gridLayout_11.addWidget(self.checkBox_internetshortcut_linux, 3, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_internetshortcut, 0, 0, 1, 1)

        self.groupBox_dearrow = QGroupBox(self.tab_miscellaneous)
        self.groupBox_dearrow.setObjectName(u"groupBox_dearrow")
        self.gridLayout_22 = QGridLayout(self.groupBox_dearrow)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.checkBox_dearrow_title = QCheckBox(self.groupBox_dearrow)
        self.checkBox_dearrow_title.setObjectName(u"checkBox_dearrow_title")

        self.gridLayout_22.addWidget(self.checkBox_dearrow_title, 0, 0, 1, 1)

        self.checkBox_dearrow_thumbnail = QCheckBox(self.groupBox_dearrow)
        self.checkBox_dearrow_thumbnail.setObjectName(u"checkBox_dearrow_thumbnail")

        self.gridLayout_22.addWidget(self.checkBox_dearrow_thumbnail, 1, 0, 1, 1)

        self.label_dearrow_title_help = QLabel(self.groupBox_dearrow)
        self.label_dearrow_title_help.setObjectName(u"label_dearrow_title_help")
        self.label_dearrow_title_help.setTextFormat(Qt.AutoText)
        self.label_dearrow_title_help.setOpenExternalLinks(True)

        self.gridLayout_22.addWidget(self.label_dearrow_title_help, 0, 1, 1, 1)

        self.label_dearrow_thumbnail_help = QLabel(self.groupBox_dearrow)
        self.label_dearrow_thumbnail_help.setObjectName(u"label_dearrow_thumbnail_help")
        self.label_dearrow_thumbnail_help.setTextFormat(Qt.AutoText)
        self.label_dearrow_thumbnail_help.setOpenExternalLinks(True)

        self.gridLayout_22.addWidget(self.label_dearrow_thumbnail_help, 1, 1, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_dearrow, 1, 2, 1, 1)

        self.groupBox_sponsorblock = QGroupBox(self.tab_miscellaneous)
        self.groupBox_sponsorblock.setObjectName(u"groupBox_sponsorblock")
        self.gridLayout_24 = QGridLayout(self.groupBox_sponsorblock)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.radioButton_sponsorblock_remove = QRadioButton(self.groupBox_sponsorblock)
        self.radioButton_sponsorblock_remove.setObjectName(u"radioButton_sponsorblock_remove")

        self.gridLayout_24.addWidget(self.radioButton_sponsorblock_remove, 1, 0, 1, 1)

        self.radioButton_sponsorblock_disable = QRadioButton(self.groupBox_sponsorblock)
        self.radioButton_sponsorblock_disable.setObjectName(u"radioButton_sponsorblock_disable")
        self.radioButton_sponsorblock_disable.setChecked(True)

        self.gridLayout_24.addWidget(self.radioButton_sponsorblock_disable, 0, 0, 1, 1)

        self.radioButton_sponsorblock_mark = QRadioButton(self.groupBox_sponsorblock)
        self.radioButton_sponsorblock_mark.setObjectName(u"radioButton_sponsorblock_mark")

        self.gridLayout_24.addWidget(self.radioButton_sponsorblock_mark, 2, 0, 1, 1)

        self.checkBox_sponsorblock_default = QCheckBox(self.groupBox_sponsorblock)
        self.checkBox_sponsorblock_default.setObjectName(u"checkBox_sponsorblock_default")

        self.gridLayout_24.addWidget(self.checkBox_sponsorblock_default, 0, 2, 1, 1)

        self.checkBox_sponsorblock_chapter = QCheckBox(self.groupBox_sponsorblock)
        self.checkBox_sponsorblock_chapter.setObjectName(u"checkBox_sponsorblock_chapter")

        self.gridLayout_24.addWidget(self.checkBox_sponsorblock_chapter, 0, 4, 1, 1)

        self.checkBox_sponsorblock_all = QCheckBox(self.groupBox_sponsorblock)
        self.checkBox_sponsorblock_all.setObjectName(u"checkBox_sponsorblock_all")

        self.gridLayout_24.addWidget(self.checkBox_sponsorblock_all, 0, 3, 1, 1)

        self.line_sponsorblock = QFrame(self.groupBox_sponsorblock)
        self.line_sponsorblock.setObjectName(u"line_sponsorblock")
        self.line_sponsorblock.setLineWidth(5)
        self.line_sponsorblock.setFrameShape(QFrame.Shape.VLine)
        self.line_sponsorblock.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_24.addWidget(self.line_sponsorblock, 0, 1, 3, 1)

        self.checkBox_sponsorblock_sponsor = QCheckBox(self.groupBox_sponsorblock)
        self.checkBox_sponsorblock_sponsor.setObjectName(u"checkBox_sponsorblock_sponsor")

        self.gridLayout_24.addWidget(self.checkBox_sponsorblock_sponsor, 0, 5, 1, 1)

        self.checkBox_sponsorblock_intro = QCheckBox(self.groupBox_sponsorblock)
        self.checkBox_sponsorblock_intro.setObjectName(u"checkBox_sponsorblock_intro")

        self.gridLayout_24.addWidget(self.checkBox_sponsorblock_intro, 1, 2, 1, 1)

        self.checkBox_sponsorblock_outro = QCheckBox(self.groupBox_sponsorblock)
        self.checkBox_sponsorblock_outro.setObjectName(u"checkBox_sponsorblock_outro")

        self.gridLayout_24.addWidget(self.checkBox_sponsorblock_outro, 1, 3, 1, 1)

        self.checkBox_sponsorblock_selfpromo = QCheckBox(self.groupBox_sponsorblock)
        self.checkBox_sponsorblock_selfpromo.setObjectName(u"checkBox_sponsorblock_selfpromo")

        self.gridLayout_24.addWidget(self.checkBox_sponsorblock_selfpromo, 1, 4, 1, 1)

        self.checkBox_sponsorblock_preview = QCheckBox(self.groupBox_sponsorblock)
        self.checkBox_sponsorblock_preview.setObjectName(u"checkBox_sponsorblock_preview")

        self.gridLayout_24.addWidget(self.checkBox_sponsorblock_preview, 1, 5, 1, 1)

        self.checkBox_sponsorblock_filler = QCheckBox(self.groupBox_sponsorblock)
        self.checkBox_sponsorblock_filler.setObjectName(u"checkBox_sponsorblock_filler")

        self.gridLayout_24.addWidget(self.checkBox_sponsorblock_filler, 2, 2, 1, 1)

        self.checkBox_sponsorblock_interaction = QCheckBox(self.groupBox_sponsorblock)
        self.checkBox_sponsorblock_interaction.setObjectName(u"checkBox_sponsorblock_interaction")

        self.gridLayout_24.addWidget(self.checkBox_sponsorblock_interaction, 2, 3, 1, 1)

        self.checkBox_sponsorblock_music_offtopic = QCheckBox(self.groupBox_sponsorblock)
        self.checkBox_sponsorblock_music_offtopic.setObjectName(u"checkBox_sponsorblock_music_offtopic")

        self.gridLayout_24.addWidget(self.checkBox_sponsorblock_music_offtopic, 2, 4, 1, 1)

        self.checkBox_sponsorblock_poi_highlight = QCheckBox(self.groupBox_sponsorblock)
        self.checkBox_sponsorblock_poi_highlight.setObjectName(u"checkBox_sponsorblock_poi_highlight")

        self.gridLayout_24.addWidget(self.checkBox_sponsorblock_poi_highlight, 2, 5, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_sponsorblock, 1, 0, 1, 2)

        self.tabWidget.addTab(self.tab_miscellaneous, "")
        self.tab_filesystem = QWidget()
        self.tab_filesystem.setObjectName(u"tab_filesystem")
        self.gridLayout_12 = QGridLayout(self.tab_filesystem)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.groupBox_cookies = QGroupBox(self.tab_filesystem)
        self.groupBox_cookies.setObjectName(u"groupBox_cookies")
        sizePolicy1.setHeightForWidth(self.groupBox_cookies.sizePolicy().hasHeightForWidth())
        self.groupBox_cookies.setSizePolicy(sizePolicy1)
        self.groupBox_cookies.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_16 = QGridLayout(self.groupBox_cookies)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_cookies_profile = QLabel(self.groupBox_cookies)
        self.label_cookies_profile.setObjectName(u"label_cookies_profile")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_cookies_profile.sizePolicy().hasHeightForWidth())
        self.label_cookies_profile.setSizePolicy(sizePolicy3)
        self.label_cookies_profile.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_cookies_profile, 3, 1, 1, 1)

        self.label_cookies_container = QLabel(self.groupBox_cookies)
        self.label_cookies_container.setObjectName(u"label_cookies_container")
        self.label_cookies_container.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_cookies_container, 3, 2, 1, 1)

        self.checkBox_cookies = QCheckBox(self.groupBox_cookies)
        self.checkBox_cookies.setObjectName(u"checkBox_cookies")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.checkBox_cookies.sizePolicy().hasHeightForWidth())
        self.checkBox_cookies.setSizePolicy(sizePolicy4)

        self.gridLayout_16.addWidget(self.checkBox_cookies, 0, 0, 1, 3)

        self.lineEdit_cookies_keyring = QLineEdit(self.groupBox_cookies)
        self.lineEdit_cookies_keyring.setObjectName(u"lineEdit_cookies_keyring")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit_cookies_keyring.sizePolicy().hasHeightForWidth())
        self.lineEdit_cookies_keyring.setSizePolicy(sizePolicy5)
        self.lineEdit_cookies_keyring.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_16.addWidget(self.lineEdit_cookies_keyring, 4, 2, 1, 1)

        self.lineEdit_cookies_profile = QLineEdit(self.groupBox_cookies)
        self.lineEdit_cookies_profile.setObjectName(u"lineEdit_cookies_profile")
        sizePolicy5.setHeightForWidth(self.lineEdit_cookies_profile.sizePolicy().hasHeightForWidth())
        self.lineEdit_cookies_profile.setSizePolicy(sizePolicy5)
        self.lineEdit_cookies_profile.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_16.addWidget(self.lineEdit_cookies_profile, 4, 1, 1, 1)

        self.widget_cookies_path = QWidget(self.groupBox_cookies)
        self.widget_cookies_path.setObjectName(u"widget_cookies_path")
        sizePolicy4.setHeightForWidth(self.widget_cookies_path.sizePolicy().hasHeightForWidth())
        self.widget_cookies_path.setSizePolicy(sizePolicy4)
        self.horizontalLayout = QHBoxLayout(self.widget_cookies_path)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_cookies_path = QLineEdit(self.widget_cookies_path)
        self.lineEdit_cookies_path.setObjectName(u"lineEdit_cookies_path")

        self.horizontalLayout.addWidget(self.lineEdit_cookies_path)

        self.toolButton_cookies_path = QToolButton(self.widget_cookies_path)
        self.toolButton_cookies_path.setObjectName(u"toolButton_cookies_path")

        self.horizontalLayout.addWidget(self.toolButton_cookies_path)


        self.gridLayout_16.addWidget(self.widget_cookies_path, 1, 0, 1, 3)

        self.comboBox_cookies_keyring = QComboBox(self.groupBox_cookies)
        self.comboBox_cookies_keyring.addItem("")
        self.comboBox_cookies_keyring.addItem("")
        self.comboBox_cookies_keyring.addItem("")
        self.comboBox_cookies_keyring.addItem("")
        self.comboBox_cookies_keyring.addItem("")
        self.comboBox_cookies_keyring.addItem("")
        self.comboBox_cookies_keyring.setObjectName(u"comboBox_cookies_keyring")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.comboBox_cookies_keyring.sizePolicy().hasHeightForWidth())
        self.comboBox_cookies_keyring.setSizePolicy(sizePolicy6)
        self.comboBox_cookies_keyring.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_16.addWidget(self.comboBox_cookies_keyring, 4, 0, 1, 1)

        self.label_cookies_keyring = QLabel(self.groupBox_cookies)
        self.label_cookies_keyring.setObjectName(u"label_cookies_keyring")
        sizePolicy3.setHeightForWidth(self.label_cookies_keyring.sizePolicy().hasHeightForWidth())
        self.label_cookies_keyring.setSizePolicy(sizePolicy3)
        self.label_cookies_keyring.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_cookies_keyring, 3, 0, 1, 1)

        self.widget_cookies_browser = QWidget(self.groupBox_cookies)
        self.widget_cookies_browser.setObjectName(u"widget_cookies_browser")
        sizePolicy4.setHeightForWidth(self.widget_cookies_browser.sizePolicy().hasHeightForWidth())
        self.widget_cookies_browser.setSizePolicy(sizePolicy4)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_cookies_browser)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_cookies_browser = QCheckBox(self.widget_cookies_browser)
        self.checkBox_cookies_browser.setObjectName(u"checkBox_cookies_browser")

        self.horizontalLayout_2.addWidget(self.checkBox_cookies_browser)

        self.comboBox_cookies_browser = QComboBox(self.widget_cookies_browser)
        self.comboBox_cookies_browser.addItem("")
        self.comboBox_cookies_browser.addItem("")
        self.comboBox_cookies_browser.addItem("")
        self.comboBox_cookies_browser.addItem("")
        self.comboBox_cookies_browser.addItem("")
        self.comboBox_cookies_browser.addItem("")
        self.comboBox_cookies_browser.addItem("")
        self.comboBox_cookies_browser.addItem("")
        self.comboBox_cookies_browser.setObjectName(u"comboBox_cookies_browser")
        sizePolicy4.setHeightForWidth(self.comboBox_cookies_browser.sizePolicy().hasHeightForWidth())
        self.comboBox_cookies_browser.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.comboBox_cookies_browser)


        self.gridLayout_16.addWidget(self.widget_cookies_browser, 2, 0, 1, 3)


        self.gridLayout_12.addWidget(self.groupBox_cookies, 0, 2, 1, 1)

        self.groupBox_filesystem = QGroupBox(self.tab_filesystem)
        self.groupBox_filesystem.setObjectName(u"groupBox_filesystem")
        sizePolicy2.setHeightForWidth(self.groupBox_filesystem.sizePolicy().hasHeightForWidth())
        self.groupBox_filesystem.setSizePolicy(sizePolicy2)
        self.groupBox_filesystem.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_14 = QGridLayout(self.groupBox_filesystem)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.checkBox_filesystem_write_comments = QCheckBox(self.groupBox_filesystem)
        self.checkBox_filesystem_write_comments.setObjectName(u"checkBox_filesystem_write_comments")
        sizePolicy3.setHeightForWidth(self.checkBox_filesystem_write_comments.sizePolicy().hasHeightForWidth())
        self.checkBox_filesystem_write_comments.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_filesystem_write_comments, 5, 2, 1, 1)

        self.checkBox_filesystem_no_part = QCheckBox(self.groupBox_filesystem)
        self.checkBox_filesystem_no_part.setObjectName(u"checkBox_filesystem_no_part")
        sizePolicy3.setHeightForWidth(self.checkBox_filesystem_no_part.sizePolicy().hasHeightForWidth())
        self.checkBox_filesystem_no_part.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_filesystem_no_part, 2, 1, 1, 1)

        self.checkBox_filesystem_no_mtme = QCheckBox(self.groupBox_filesystem)
        self.checkBox_filesystem_no_mtme.setObjectName(u"checkBox_filesystem_no_mtme")
        sizePolicy3.setHeightForWidth(self.checkBox_filesystem_no_mtme.sizePolicy().hasHeightForWidth())
        self.checkBox_filesystem_no_mtme.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_filesystem_no_mtme, 1, 2, 1, 1)

        self.checkBox_filesystem_write_description = QCheckBox(self.groupBox_filesystem)
        self.checkBox_filesystem_write_description.setObjectName(u"checkBox_filesystem_write_description")
        sizePolicy3.setHeightForWidth(self.checkBox_filesystem_write_description.sizePolicy().hasHeightForWidth())
        self.checkBox_filesystem_write_description.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_filesystem_write_description, 2, 2, 1, 1)

        self.checkBox_filesystem_windows_filenames = QCheckBox(self.groupBox_filesystem)
        self.checkBox_filesystem_windows_filenames.setObjectName(u"checkBox_filesystem_windows_filenames")
        sizePolicy3.setHeightForWidth(self.checkBox_filesystem_windows_filenames.sizePolicy().hasHeightForWidth())
        self.checkBox_filesystem_windows_filenames.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_filesystem_windows_filenames, 2, 0, 1, 1)

        self.checkBox_filesystem_restrict_filenames = QCheckBox(self.groupBox_filesystem)
        self.checkBox_filesystem_restrict_filenames.setObjectName(u"checkBox_filesystem_restrict_filenames")
        sizePolicy3.setHeightForWidth(self.checkBox_filesystem_restrict_filenames.sizePolicy().hasHeightForWidth())
        self.checkBox_filesystem_restrict_filenames.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_filesystem_restrict_filenames, 1, 0, 1, 1)

        self.checkBox_filesystem_no_continue = QCheckBox(self.groupBox_filesystem)
        self.checkBox_filesystem_no_continue.setObjectName(u"checkBox_filesystem_no_continue")
        sizePolicy3.setHeightForWidth(self.checkBox_filesystem_no_continue.sizePolicy().hasHeightForWidth())
        self.checkBox_filesystem_no_continue.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_filesystem_no_continue, 1, 1, 1, 1)

        self.checkBox_filesystem_no_overwrites = QCheckBox(self.groupBox_filesystem)
        self.checkBox_filesystem_no_overwrites.setObjectName(u"checkBox_filesystem_no_overwrites")
        sizePolicy3.setHeightForWidth(self.checkBox_filesystem_no_overwrites.sizePolicy().hasHeightForWidth())
        self.checkBox_filesystem_no_overwrites.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_filesystem_no_overwrites, 3, 0, 1, 1)

        self.checkBox_filesystem_force_overwrites = QCheckBox(self.groupBox_filesystem)
        self.checkBox_filesystem_force_overwrites.setObjectName(u"checkBox_filesystem_force_overwrites")
        sizePolicy3.setHeightForWidth(self.checkBox_filesystem_force_overwrites.sizePolicy().hasHeightForWidth())
        self.checkBox_filesystem_force_overwrites.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_filesystem_force_overwrites, 3, 1, 1, 1)

        self.checkBox_filesystem_trim_filenames = QCheckBox(self.groupBox_filesystem)
        self.checkBox_filesystem_trim_filenames.setObjectName(u"checkBox_filesystem_trim_filenames")
        sizePolicy3.setHeightForWidth(self.checkBox_filesystem_trim_filenames.sizePolicy().hasHeightForWidth())
        self.checkBox_filesystem_trim_filenames.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_filesystem_trim_filenames, 5, 0, 1, 1)

        self.spinBox_filesystem_trim_filenames = QSpinBox(self.groupBox_filesystem)
        self.spinBox_filesystem_trim_filenames.setObjectName(u"spinBox_filesystem_trim_filenames")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.spinBox_filesystem_trim_filenames.sizePolicy().hasHeightForWidth())
        self.spinBox_filesystem_trim_filenames.setSizePolicy(sizePolicy7)
        self.spinBox_filesystem_trim_filenames.setMinimum(10)
        self.spinBox_filesystem_trim_filenames.setMaximum(9999)
        self.spinBox_filesystem_trim_filenames.setSingleStep(10)

        self.gridLayout_14.addWidget(self.spinBox_filesystem_trim_filenames, 5, 1, 1, 1)

        self.checkBox_filesystem_write_infojson = QCheckBox(self.groupBox_filesystem)
        self.checkBox_filesystem_write_infojson.setObjectName(u"checkBox_filesystem_write_infojson")
        sizePolicy3.setHeightForWidth(self.checkBox_filesystem_write_infojson.sizePolicy().hasHeightForWidth())
        self.checkBox_filesystem_write_infojson.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_filesystem_write_infojson, 3, 2, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_filesystem, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_filesystem, "")
        self.tab_advanced = QWidget()
        self.tab_advanced.setObjectName(u"tab_advanced")
        self.gridLayout_13 = QGridLayout(self.tab_advanced)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.groupBox_simulation = QGroupBox(self.tab_advanced)
        self.groupBox_simulation.setObjectName(u"groupBox_simulation")
        self.gridLayout_15 = QGridLayout(self.groupBox_simulation)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.checkBox_simulation_no_simulate = QCheckBox(self.groupBox_simulation)
        self.checkBox_simulation_no_simulate.setObjectName(u"checkBox_simulation_no_simulate")

        self.gridLayout_15.addWidget(self.checkBox_simulation_no_simulate, 1, 0, 1, 1)

        self.checkBox_simulation_skip_download = QCheckBox(self.groupBox_simulation)
        self.checkBox_simulation_skip_download.setObjectName(u"checkBox_simulation_skip_download")

        self.gridLayout_15.addWidget(self.checkBox_simulation_skip_download, 6, 0, 1, 2)

        self.checkBox_simulation_ignore_error = QCheckBox(self.groupBox_simulation)
        self.checkBox_simulation_ignore_error.setObjectName(u"checkBox_simulation_ignore_error")

        self.gridLayout_15.addWidget(self.checkBox_simulation_ignore_error, 5, 0, 1, 2)

        self.checkBox_simulation_write_archive = QCheckBox(self.groupBox_simulation)
        self.checkBox_simulation_write_archive.setObjectName(u"checkBox_simulation_write_archive")

        self.gridLayout_15.addWidget(self.checkBox_simulation_write_archive, 7, 0, 1, 1)

        self.checkBox_simulation_simulate = QCheckBox(self.groupBox_simulation)
        self.checkBox_simulation_simulate.setObjectName(u"checkBox_simulation_simulate")

        self.gridLayout_15.addWidget(self.checkBox_simulation_simulate, 2, 0, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_simulation, 0, 0, 2, 1)

        self.groupBox_workaround = QGroupBox(self.tab_advanced)
        self.groupBox_workaround.setObjectName(u"groupBox_workaround")
        self.gridLayout_18 = QGridLayout(self.groupBox_workaround)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.checkBox_workaround_legacy = QCheckBox(self.groupBox_workaround)
        self.checkBox_workaround_legacy.setObjectName(u"checkBox_workaround_legacy")

        self.gridLayout_18.addWidget(self.checkBox_workaround_legacy, 0, 0, 1, 1)

        self.checkBox_workaround_sleep_requests = QCheckBox(self.groupBox_workaround)
        self.checkBox_workaround_sleep_requests.setObjectName(u"checkBox_workaround_sleep_requests")

        self.gridLayout_18.addWidget(self.checkBox_workaround_sleep_requests, 0, 1, 1, 1)

        self.checkBox_workaround_no_certificates = QCheckBox(self.groupBox_workaround)
        self.checkBox_workaround_no_certificates.setObjectName(u"checkBox_workaround_no_certificates")

        self.gridLayout_18.addWidget(self.checkBox_workaround_no_certificates, 1, 0, 1, 1)

        self.checkBox_workaround_sleep_interval = QCheckBox(self.groupBox_workaround)
        self.checkBox_workaround_sleep_interval.setObjectName(u"checkBox_workaround_sleep_interval")

        self.gridLayout_18.addWidget(self.checkBox_workaround_sleep_interval, 1, 1, 1, 1)

        self.spinBox_workaround_sleep_interval_min = QSpinBox(self.groupBox_workaround)
        self.spinBox_workaround_sleep_interval_min.setObjectName(u"spinBox_workaround_sleep_interval_min")
        self.spinBox_workaround_sleep_interval_min.setMaximum(999)
        self.spinBox_workaround_sleep_interval_min.setSingleStep(1)

        self.gridLayout_18.addWidget(self.spinBox_workaround_sleep_interval_min, 1, 2, 1, 1)

        self.spinBox_workaround_sleep_interval_max = QSpinBox(self.groupBox_workaround)
        self.spinBox_workaround_sleep_interval_max.setObjectName(u"spinBox_workaround_sleep_interval_max")
        self.spinBox_workaround_sleep_interval_max.setMaximum(999)
        self.spinBox_workaround_sleep_interval_max.setSingleStep(1)

        self.gridLayout_18.addWidget(self.spinBox_workaround_sleep_interval_max, 1, 3, 1, 1)

        self.spinBox_workaround_sleep_requests = QSpinBox(self.groupBox_workaround)
        self.spinBox_workaround_sleep_requests.setObjectName(u"spinBox_workaround_sleep_requests")
        self.spinBox_workaround_sleep_requests.setMaximum(999)
        self.spinBox_workaround_sleep_requests.setSingleStep(1)

        self.gridLayout_18.addWidget(self.spinBox_workaround_sleep_requests, 0, 2, 1, 2)


        self.gridLayout_13.addWidget(self.groupBox_workaround, 1, 3, 1, 1)

        self.groupBox_cache = QGroupBox(self.tab_advanced)
        self.groupBox_cache.setObjectName(u"groupBox_cache")
        self.gridLayout_17 = QGridLayout(self.groupBox_cache)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.checkBox_cache_no_cache = QCheckBox(self.groupBox_cache)
        self.checkBox_cache_no_cache.setObjectName(u"checkBox_cache_no_cache")

        self.gridLayout_17.addWidget(self.checkBox_cache_no_cache, 0, 1, 1, 1)

        self.widget_cache_path = QWidget(self.groupBox_cache)
        self.widget_cache_path.setObjectName(u"widget_cache_path")
        sizePolicy3.setHeightForWidth(self.widget_cache_path.sizePolicy().hasHeightForWidth())
        self.widget_cache_path.setSizePolicy(sizePolicy3)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_cache_path)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_cache_path = QLineEdit(self.widget_cache_path)
        self.lineEdit_cache_path.setObjectName(u"lineEdit_cache_path")

        self.horizontalLayout_3.addWidget(self.lineEdit_cache_path)

        self.toolButton_cache_path = QToolButton(self.widget_cache_path)
        self.toolButton_cache_path.setObjectName(u"toolButton_cache_path")

        self.horizontalLayout_3.addWidget(self.toolButton_cache_path)


        self.gridLayout_17.addWidget(self.widget_cache_path, 2, 0, 1, 2)

        self.checkBox_cache_rm_cache = QCheckBox(self.groupBox_cache)
        self.checkBox_cache_rm_cache.setObjectName(u"checkBox_cache_rm_cache")

        self.gridLayout_17.addWidget(self.checkBox_cache_rm_cache, 1, 1, 1, 1)

        self.checkBox_cache = QCheckBox(self.groupBox_cache)
        self.checkBox_cache.setObjectName(u"checkBox_cache")

        self.gridLayout_17.addWidget(self.checkBox_cache, 0, 0, 2, 1)


        self.gridLayout_13.addWidget(self.groupBox_cache, 0, 3, 1, 1)

        self.groupBox_download = QGroupBox(self.tab_advanced)
        self.groupBox_download.setObjectName(u"groupBox_download")
        self.gridLayout_25 = QGridLayout(self.groupBox_download)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.comboBox_download_max_rate = QComboBox(self.groupBox_download)
        self.comboBox_download_max_rate.addItem("")
        self.comboBox_download_max_rate.addItem("")
        self.comboBox_download_max_rate.addItem("")
        self.comboBox_download_max_rate.addItem("")
        self.comboBox_download_max_rate.setObjectName(u"comboBox_download_max_rate")
        sizePolicy7.setHeightForWidth(self.comboBox_download_max_rate.sizePolicy().hasHeightForWidth())
        self.comboBox_download_max_rate.setSizePolicy(sizePolicy7)
        self.comboBox_download_max_rate.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_25.addWidget(self.comboBox_download_max_rate, 3, 1, 1, 1)

        self.doubleSpinBox_download_max_rate = QDoubleSpinBox(self.groupBox_download)
        self.doubleSpinBox_download_max_rate.setObjectName(u"doubleSpinBox_download_max_rate")
        sizePolicy4.setHeightForWidth(self.doubleSpinBox_download_max_rate.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_download_max_rate.setSizePolicy(sizePolicy4)
        self.doubleSpinBox_download_max_rate.setDecimals(1)
        self.doubleSpinBox_download_max_rate.setMaximum(999.000000000000000)

        self.gridLayout_25.addWidget(self.doubleSpinBox_download_max_rate, 3, 0, 1, 1)

        self.comboBox_download_min_rate = QComboBox(self.groupBox_download)
        self.comboBox_download_min_rate.addItem("")
        self.comboBox_download_min_rate.addItem("")
        self.comboBox_download_min_rate.addItem("")
        self.comboBox_download_min_rate.addItem("")
        self.comboBox_download_min_rate.setObjectName(u"comboBox_download_min_rate")
        sizePolicy7.setHeightForWidth(self.comboBox_download_min_rate.sizePolicy().hasHeightForWidth())
        self.comboBox_download_min_rate.setSizePolicy(sizePolicy7)
        self.comboBox_download_min_rate.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_25.addWidget(self.comboBox_download_min_rate, 3, 3, 1, 1)

        self.checkBox_download_min_rate = QCheckBox(self.groupBox_download)
        self.checkBox_download_min_rate.setObjectName(u"checkBox_download_min_rate")

        self.gridLayout_25.addWidget(self.checkBox_download_min_rate, 2, 2, 1, 2)

        self.doubleSpinBox_download_min_rate = QDoubleSpinBox(self.groupBox_download)
        self.doubleSpinBox_download_min_rate.setObjectName(u"doubleSpinBox_download_min_rate")
        self.doubleSpinBox_download_min_rate.setDecimals(1)
        self.doubleSpinBox_download_min_rate.setMaximum(999.000000000000000)

        self.gridLayout_25.addWidget(self.doubleSpinBox_download_min_rate, 3, 2, 1, 1)

        self.checkBox_download_max_rate = QCheckBox(self.groupBox_download)
        self.checkBox_download_max_rate.setObjectName(u"checkBox_download_max_rate")

        self.gridLayout_25.addWidget(self.checkBox_download_max_rate, 2, 0, 1, 2)

        self.checkBox_download_retry_sleep = QCheckBox(self.groupBox_download)
        self.checkBox_download_retry_sleep.setObjectName(u"checkBox_download_retry_sleep")

        self.gridLayout_25.addWidget(self.checkBox_download_retry_sleep, 4, 2, 1, 2)

        self.checkBox_download_retries = QCheckBox(self.groupBox_download)
        self.checkBox_download_retries.setObjectName(u"checkBox_download_retries")

        self.gridLayout_25.addWidget(self.checkBox_download_retries, 4, 0, 1, 2)

        self.spinBox_download_retries = QSpinBox(self.groupBox_download)
        self.spinBox_download_retries.setObjectName(u"spinBox_download_retries")

        self.gridLayout_25.addWidget(self.spinBox_download_retries, 5, 1, 1, 1)

        self.checkBox_download_retries_infinite = QCheckBox(self.groupBox_download)
        self.checkBox_download_retries_infinite.setObjectName(u"checkBox_download_retries_infinite")

        self.gridLayout_25.addWidget(self.checkBox_download_retries_infinite, 5, 0, 1, 1)

        self.line_download = QFrame(self.groupBox_download)
        self.line_download.setObjectName(u"line_download")
        self.line_download.setLineWidth(5)
        self.line_download.setFrameShape(QFrame.Shape.HLine)
        self.line_download.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_25.addWidget(self.line_download, 1, 0, 1, 4)

        self.spinBox_download_retry_sleep = QSpinBox(self.groupBox_download)
        self.spinBox_download_retry_sleep.setObjectName(u"spinBox_download_retry_sleep")

        self.gridLayout_25.addWidget(self.spinBox_download_retry_sleep, 5, 2, 1, 2)

        self.checkBox_download_keep_fragments = QCheckBox(self.groupBox_download)
        self.checkBox_download_keep_fragments.setObjectName(u"checkBox_download_keep_fragments")

        self.gridLayout_25.addWidget(self.checkBox_download_keep_fragments, 0, 0, 1, 4)


        self.gridLayout_13.addWidget(self.groupBox_download, 0, 1, 2, 1)

        self.tabWidget.addTab(self.tab_advanced, "")
        self.tab_extra_processing = QWidget()
        self.tab_extra_processing.setObjectName(u"tab_extra_processing")
        self.gridLayout_26 = QGridLayout(self.tab_extra_processing)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.groupBox_pymlsub = QGroupBox(self.tab_extra_processing)
        self.groupBox_pymlsub.setObjectName(u"groupBox_pymlsub")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.groupBox_pymlsub.sizePolicy().hasHeightForWidth())
        self.groupBox_pymlsub.setSizePolicy(sizePolicy8)
        self.gridLayout_30 = QGridLayout(self.groupBox_pymlsub)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.doubleSpinBox_pyml_min_duration = QDoubleSpinBox(self.groupBox_pymlsub)
        self.doubleSpinBox_pyml_min_duration.setObjectName(u"doubleSpinBox_pyml_min_duration")
        self.doubleSpinBox_pyml_min_duration.setMaximum(1.000000000000000)
        self.doubleSpinBox_pyml_min_duration.setSingleStep(0.010000000000000)
        self.doubleSpinBox_pyml_min_duration.setValue(0.350000000000000)

        self.gridLayout_30.addWidget(self.doubleSpinBox_pyml_min_duration, 0, 2, 1, 1)

        self.checkBox_pyml_min_duartion = QCheckBox(self.groupBox_pymlsub)
        self.checkBox_pyml_min_duartion.setObjectName(u"checkBox_pyml_min_duartion")

        self.gridLayout_30.addWidget(self.checkBox_pyml_min_duartion, 0, 1, 1, 1)

        self.checkBox_pyml_brute_force = QCheckBox(self.groupBox_pymlsub)
        self.checkBox_pyml_brute_force.setObjectName(u"checkBox_pyml_brute_force")

        self.gridLayout_30.addWidget(self.checkBox_pyml_brute_force, 0, 0, 1, 1)

        self.comboBox_pyml_format = QComboBox(self.groupBox_pymlsub)
        self.comboBox_pyml_format.addItem("")
        self.comboBox_pyml_format.addItem("")
        self.comboBox_pyml_format.addItem("")
        self.comboBox_pyml_format.addItem("")
        self.comboBox_pyml_format.setObjectName(u"comboBox_pyml_format")

        self.gridLayout_30.addWidget(self.comboBox_pyml_format, 1, 2, 1, 1)

        self.checkBox_pyml_format = QCheckBox(self.groupBox_pymlsub)
        self.checkBox_pyml_format.setObjectName(u"checkBox_pyml_format")

        self.gridLayout_30.addWidget(self.checkBox_pyml_format, 1, 0, 1, 2)

        self.doubleSpinBox_pyml_loop_duration_max = QDoubleSpinBox(self.groupBox_pymlsub)
        self.doubleSpinBox_pyml_loop_duration_max.setObjectName(u"doubleSpinBox_pyml_loop_duration_max")
        self.doubleSpinBox_pyml_loop_duration_max.setDecimals(3)
        self.doubleSpinBox_pyml_loop_duration_max.setMaximum(9999.000000000000000)

        self.gridLayout_30.addWidget(self.doubleSpinBox_pyml_loop_duration_max, 1, 4, 1, 1)

        self.doubleSpinBox_pyml_loop_duration_min = QDoubleSpinBox(self.groupBox_pymlsub)
        self.doubleSpinBox_pyml_loop_duration_min.setObjectName(u"doubleSpinBox_pyml_loop_duration_min")
        self.doubleSpinBox_pyml_loop_duration_min.setDecimals(3)
        self.doubleSpinBox_pyml_loop_duration_min.setMaximum(9999.000000000000000)

        self.gridLayout_30.addWidget(self.doubleSpinBox_pyml_loop_duration_min, 0, 4, 1, 1)

        self.checkBox_pyml_loop_duration = QCheckBox(self.groupBox_pymlsub)
        self.checkBox_pyml_loop_duration.setObjectName(u"checkBox_pyml_loop_duration")

        self.gridLayout_30.addWidget(self.checkBox_pyml_loop_duration, 0, 3, 2, 1)


        self.gridLayout_26.addWidget(self.groupBox_pymlsub, 1, 0, 1, 1)

        self.groupBox_ffmpeg = QGroupBox(self.tab_extra_processing)
        self.groupBox_ffmpeg.setObjectName(u"groupBox_ffmpeg")
        self.gridLayout_27 = QGridLayout(self.groupBox_ffmpeg)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.checkBox_ffmpeg = QCheckBox(self.groupBox_ffmpeg)
        self.checkBox_ffmpeg.setObjectName(u"checkBox_ffmpeg")

        self.gridLayout_27.addWidget(self.checkBox_ffmpeg, 0, 0, 1, 1)

        self.label_ffmpeg_help_right = QLabel(self.groupBox_ffmpeg)
        self.label_ffmpeg_help_right.setObjectName(u"label_ffmpeg_help_right")
        sizePolicy1.setHeightForWidth(self.label_ffmpeg_help_right.sizePolicy().hasHeightForWidth())
        self.label_ffmpeg_help_right.setSizePolicy(sizePolicy1)
        self.label_ffmpeg_help_right.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_ffmpeg_help_right.setOpenExternalLinks(True)

        self.gridLayout_27.addWidget(self.label_ffmpeg_help_right, 0, 1, 2, 1)

        self.label_ffmpeg_help_left = QLabel(self.groupBox_ffmpeg)
        self.label_ffmpeg_help_left.setObjectName(u"label_ffmpeg_help_left")
        self.label_ffmpeg_help_left.setTextFormat(Qt.AutoText)

        self.gridLayout_27.addWidget(self.label_ffmpeg_help_left, 1, 0, 2, 1)

        self.plainTextEdit_ffmpeg_arguments = QPlainTextEdit(self.groupBox_ffmpeg)
        self.plainTextEdit_ffmpeg_arguments.setObjectName(u"plainTextEdit_ffmpeg_arguments")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.plainTextEdit_ffmpeg_arguments.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_ffmpeg_arguments.setSizePolicy(sizePolicy9)
        self.plainTextEdit_ffmpeg_arguments.setMinimumSize(QSize(0, 30))
        self.plainTextEdit_ffmpeg_arguments.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_27.addWidget(self.plainTextEdit_ffmpeg_arguments, 3, 0, 1, 2)

        self.lineEdit_ffmpeg_output_container = QLineEdit(self.groupBox_ffmpeg)
        self.lineEdit_ffmpeg_output_container.setObjectName(u"lineEdit_ffmpeg_output_container")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.lineEdit_ffmpeg_output_container.sizePolicy().hasHeightForWidth())
        self.lineEdit_ffmpeg_output_container.setSizePolicy(sizePolicy10)

        self.gridLayout_27.addWidget(self.lineEdit_ffmpeg_output_container, 2, 1, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_ffmpeg, 0, 0, 1, 1)

        self.groupBox_pymlmain = QGroupBox(self.tab_extra_processing)
        self.groupBox_pymlmain.setObjectName(u"groupBox_pymlmain")
        self.gridLayout_29 = QGridLayout(self.groupBox_pymlmain)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.checkBox_pyml_export_format = QCheckBox(self.groupBox_pymlmain)
        self.checkBox_pyml_export_format.setObjectName(u"checkBox_pyml_export_format")

        self.gridLayout_29.addWidget(self.checkBox_pyml_export_format, 5, 0, 1, 1)

        self.radioButton_pyml_tag = QRadioButton(self.groupBox_pymlmain)
        self.radioButton_pyml_tag.setObjectName(u"radioButton_pyml_tag")

        self.gridLayout_29.addWidget(self.radioButton_pyml_tag, 3, 2, 1, 2)

        self.checkBox_pyml_export_topN = QCheckBox(self.groupBox_pymlmain)
        self.checkBox_pyml_export_topN.setObjectName(u"checkBox_pyml_export_topN")

        self.gridLayout_29.addWidget(self.checkBox_pyml_export_topN, 4, 0, 1, 1)

        self.spinBox_pyml_export_topN = QSpinBox(self.groupBox_pymlmain)
        self.spinBox_pyml_export_topN.setObjectName(u"spinBox_pyml_export_topN")
        self.spinBox_pyml_export_topN.setMinimum(-1)
        self.spinBox_pyml_export_topN.setMaximum(999)
        self.spinBox_pyml_export_topN.setValue(1)

        self.gridLayout_29.addWidget(self.spinBox_pyml_export_topN, 4, 1, 1, 1)

        self.checkBox_pyml_tag_override = QCheckBox(self.groupBox_pymlmain)
        self.checkBox_pyml_tag_override.setObjectName(u"checkBox_pyml_tag_override")

        self.gridLayout_29.addWidget(self.checkBox_pyml_tag_override, 4, 2, 1, 2)

        self.comboBox_pyml_export_format = QComboBox(self.groupBox_pymlmain)
        self.comboBox_pyml_export_format.addItem("")
        self.comboBox_pyml_export_format.addItem("")
        self.comboBox_pyml_export_format.addItem("")
        self.comboBox_pyml_export_format.setObjectName(u"comboBox_pyml_export_format")

        self.gridLayout_29.addWidget(self.comboBox_pyml_export_format, 5, 1, 1, 1)

        self.lineEdit_pyml_tag_start = QLineEdit(self.groupBox_pymlmain)
        self.lineEdit_pyml_tag_start.setObjectName(u"lineEdit_pyml_tag_start")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Minimum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.lineEdit_pyml_tag_start.sizePolicy().hasHeightForWidth())
        self.lineEdit_pyml_tag_start.setSizePolicy(sizePolicy11)
        self.lineEdit_pyml_tag_start.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_29.addWidget(self.lineEdit_pyml_tag_start, 5, 2, 1, 1)

        self.lineEdit_pyml_tag_end = QLineEdit(self.groupBox_pymlmain)
        self.lineEdit_pyml_tag_end.setObjectName(u"lineEdit_pyml_tag_end")
        sizePolicy10.setHeightForWidth(self.lineEdit_pyml_tag_end.sizePolicy().hasHeightForWidth())
        self.lineEdit_pyml_tag_end.setSizePolicy(sizePolicy10)

        self.gridLayout_29.addWidget(self.lineEdit_pyml_tag_end, 5, 3, 1, 1)

        self.label_pyml_help_right = QLabel(self.groupBox_pymlmain)
        self.label_pyml_help_right.setObjectName(u"label_pyml_help_right")

        self.gridLayout_29.addWidget(self.label_pyml_help_right, 2, 2, 1, 2)

        self.checkBox_pyml = QCheckBox(self.groupBox_pymlmain)
        self.checkBox_pyml.setObjectName(u"checkBox_pyml")

        self.gridLayout_29.addWidget(self.checkBox_pyml, 0, 0, 1, 4)

        self.label_pyml_extend_length = QLabel(self.groupBox_pymlmain)
        self.label_pyml_extend_length.setObjectName(u"label_pyml_extend_length")
        sizePolicy3.setHeightForWidth(self.label_pyml_extend_length.sizePolicy().hasHeightForWidth())
        self.label_pyml_extend_length.setSizePolicy(sizePolicy3)

        self.gridLayout_29.addWidget(self.label_pyml_extend_length, 7, 0, 1, 1)

        self.doubleSpinBox_pyml_extend_length = QDoubleSpinBox(self.groupBox_pymlmain)
        self.doubleSpinBox_pyml_extend_length.setObjectName(u"doubleSpinBox_pyml_extend_length")
        self.doubleSpinBox_pyml_extend_length.setMaximum(9999.000000000000000)
        self.doubleSpinBox_pyml_extend_length.setValue(3600.000000000000000)

        self.gridLayout_29.addWidget(self.doubleSpinBox_pyml_extend_length, 7, 1, 1, 1)

        self.label_pyml_help_left = QLabel(self.groupBox_pymlmain)
        self.label_pyml_help_left.setObjectName(u"label_pyml_help_left")
        self.label_pyml_help_left.setTextFormat(Qt.AutoText)
        self.label_pyml_help_left.setOpenExternalLinks(True)

        self.gridLayout_29.addWidget(self.label_pyml_help_left, 2, 0, 1, 2)

        self.label_pyml_extend_fade = QLabel(self.groupBox_pymlmain)
        self.label_pyml_extend_fade.setObjectName(u"label_pyml_extend_fade")
        sizePolicy3.setHeightForWidth(self.label_pyml_extend_fade.sizePolicy().hasHeightForWidth())
        self.label_pyml_extend_fade.setSizePolicy(sizePolicy3)

        self.gridLayout_29.addWidget(self.label_pyml_extend_fade, 8, 0, 1, 1)

        self.doubleSpinBox_pyml_extend_fade = QDoubleSpinBox(self.groupBox_pymlmain)
        self.doubleSpinBox_pyml_extend_fade.setObjectName(u"doubleSpinBox_pyml_extend_fade")
        self.doubleSpinBox_pyml_extend_fade.setMaximum(9999.000000000000000)
        self.doubleSpinBox_pyml_extend_fade.setSingleStep(0.100000000000000)
        self.doubleSpinBox_pyml_extend_fade.setValue(5.000000000000000)

        self.gridLayout_29.addWidget(self.doubleSpinBox_pyml_extend_fade, 8, 1, 1, 1)

        self.radioButton_split = QRadioButton(self.groupBox_pymlmain)
        self.radioButton_split.setObjectName(u"radioButton_split")

        self.gridLayout_29.addWidget(self.radioButton_split, 6, 2, 1, 2)

        self.label_pyml_split_help = QLabel(self.groupBox_pymlmain)
        self.label_pyml_split_help.setObjectName(u"label_pyml_split_help")
        self.label_pyml_split_help.setTextFormat(Qt.AutoText)
        self.label_pyml_split_help.setOpenExternalLinks(True)

        self.gridLayout_29.addWidget(self.label_pyml_split_help, 7, 2, 2, 2)

        self.radioButton_pyml_export = QRadioButton(self.groupBox_pymlmain)
        self.radioButton_pyml_export.setObjectName(u"radioButton_pyml_export")
        self.radioButton_pyml_export.setChecked(True)

        self.gridLayout_29.addWidget(self.radioButton_pyml_export, 3, 0, 1, 2)

        self.radioButton_pyml_extend = QRadioButton(self.groupBox_pymlmain)
        self.radioButton_pyml_extend.setObjectName(u"radioButton_pyml_extend")

        self.gridLayout_29.addWidget(self.radioButton_pyml_extend, 6, 0, 1, 2)


        self.gridLayout_26.addWidget(self.groupBox_pymlmain, 0, 1, 2, 1)

        self.tabWidget.addTab(self.tab_extra_processing, "")
        self.tab_behavior = QWidget()
        self.tab_behavior.setObjectName(u"tab_behavior")
        self.gridLayout_31 = QGridLayout(self.tab_behavior)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.groupBox_afk = QGroupBox(self.tab_behavior)
        self.groupBox_afk.setObjectName(u"groupBox_afk")
        self.gridLayout_32 = QGridLayout(self.groupBox_afk)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_afk_running = QLabel(self.groupBox_afk)
        self.label_afk_running.setObjectName(u"label_afk_running")

        self.gridLayout_32.addWidget(self.label_afk_running, 0, 0, 1, 1)

        self.radioButton_afk_close = QRadioButton(self.groupBox_afk)
        self.radioButton_afk_close.setObjectName(u"radioButton_afk_close")

        self.gridLayout_32.addWidget(self.radioButton_afk_close, 6, 0, 1, 1)

        self.label_afk_done = QLabel(self.groupBox_afk)
        self.label_afk_done.setObjectName(u"label_afk_done")

        self.gridLayout_32.addWidget(self.label_afk_done, 2, 0, 1, 1)

        self.radioButton_afk_nothing = QRadioButton(self.groupBox_afk)
        self.radioButton_afk_nothing.setObjectName(u"radioButton_afk_nothing")
        self.radioButton_afk_nothing.setChecked(True)

        self.gridLayout_32.addWidget(self.radioButton_afk_nothing, 3, 0, 1, 1)

        self.radioButton_afk_restart = QRadioButton(self.groupBox_afk)
        self.radioButton_afk_restart.setObjectName(u"radioButton_afk_restart")

        self.gridLayout_32.addWidget(self.radioButton_afk_restart, 5, 0, 1, 1)

        self.radioButton_afk_shutdown = QRadioButton(self.groupBox_afk)
        self.radioButton_afk_shutdown.setObjectName(u"radioButton_afk_shutdown")

        self.gridLayout_32.addWidget(self.radioButton_afk_shutdown, 4, 0, 1, 1)

        self.checkBox_afk_keep_awake = QCheckBox(self.groupBox_afk)
        self.checkBox_afk_keep_awake.setObjectName(u"checkBox_afk_keep_awake")

        self.gridLayout_32.addWidget(self.checkBox_afk_keep_awake, 1, 0, 1, 1)

        self.radioButton_afk_command = QRadioButton(self.groupBox_afk)
        self.radioButton_afk_command.setObjectName(u"radioButton_afk_command")

        self.gridLayout_32.addWidget(self.radioButton_afk_command, 7, 0, 1, 1)

        self.lineEdit_afk_command = QLineEdit(self.groupBox_afk)
        self.lineEdit_afk_command.setObjectName(u"lineEdit_afk_command")

        self.gridLayout_32.addWidget(self.lineEdit_afk_command, 8, 0, 1, 1)


        self.gridLayout_31.addWidget(self.groupBox_afk, 0, 0, 1, 1)

        self.groupBox_worker = QGroupBox(self.tab_behavior)
        self.groupBox_worker.setObjectName(u"groupBox_worker")
        self.groupBox_worker.setEnabled(True)
        self.groupBox_worker.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_6 = QGridLayout(self.groupBox_worker)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_worker_ytdlp = QLabel(self.groupBox_worker)
        self.label_worker_ytdlp.setObjectName(u"label_worker_ytdlp")

        self.gridLayout_6.addWidget(self.label_worker_ytdlp, 1, 0, 1, 1)

        self.spinBox_worker_ytdlp = QSpinBox(self.groupBox_worker)
        self.spinBox_worker_ytdlp.setObjectName(u"spinBox_worker_ytdlp")
        self.spinBox_worker_ytdlp.setEnabled(False)
        self.spinBox_worker_ytdlp.setMinimum(1)
        self.spinBox_worker_ytdlp.setMaximum(16)

        self.gridLayout_6.addWidget(self.spinBox_worker_ytdlp, 1, 1, 1, 1)

        self.label_worker_exproc = QLabel(self.groupBox_worker)
        self.label_worker_exproc.setObjectName(u"label_worker_exproc")

        self.gridLayout_6.addWidget(self.label_worker_exproc, 2, 0, 1, 1)

        self.spinBox_worker_exproc = QSpinBox(self.groupBox_worker)
        self.spinBox_worker_exproc.setObjectName(u"spinBox_worker_exproc")
        self.spinBox_worker_exproc.setEnabled(False)
        self.spinBox_worker_exproc.setMinimum(1)
        self.spinBox_worker_exproc.setMaximum(16)

        self.gridLayout_6.addWidget(self.spinBox_worker_exproc, 2, 1, 1, 1)

        self.label_worker_help = QLabel(self.groupBox_worker)
        self.label_worker_help.setObjectName(u"label_worker_help")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.label_worker_help.sizePolicy().hasHeightForWidth())
        self.label_worker_help.setSizePolicy(sizePolicy12)
        self.label_worker_help.setTextFormat(Qt.AutoText)

        self.gridLayout_6.addWidget(self.label_worker_help, 0, 0, 1, 2)


        self.gridLayout_31.addWidget(self.groupBox_worker, 0, 1, 1, 1, Qt.AlignTop)

        self.tabWidget.addTab(self.tab_behavior, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.groupBox_status = QGroupBox(self.centralwidget)
        self.groupBox_status.setObjectName(u"groupBox_status")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_status)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.treeView_status = QTreeView(self.groupBox_status)
        self.treeView_status.setObjectName(u"treeView_status")

        self.verticalLayout_2.addWidget(self.treeView_status)


        self.verticalLayout.addWidget(self.groupBox_status)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 918, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menu_About = QMenu(self.menubar)
        self.menu_About.setObjectName(u"menu_About")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.menuFile.addAction(self.action_Exit)
        self.menu_About.addAction(self.action_About_shiny_adventure)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"shiny-adventure", None))
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"&Exit", None))
        self.action_About_shiny_adventure.setText(QCoreApplication.translate("MainWindow", u"&About shiny-adventure...", None))
        self.groupBox_quality.setTitle(QCoreApplication.translate("MainWindow", u"Quality", None))
        self.radioButton_quality_best.setText(QCoreApplication.translate("MainWindow", u"Best", None))
        self.radioButton_quality_at_most.setText(QCoreApplication.translate("MainWindow", u"At most", None))
        self.radioButton_quality_at_least.setText(QCoreApplication.translate("MainWindow", u"At least", None))
        self.comboBox_quality.setItemText(0, QCoreApplication.translate("MainWindow", u"1080p", None))
        self.comboBox_quality.setItemText(1, QCoreApplication.translate("MainWindow", u"720p", None))
        self.comboBox_quality.setItemText(2, QCoreApplication.translate("MainWindow", u"480p", None))
        self.comboBox_quality.setItemText(3, QCoreApplication.translate("MainWindow", u"360p", None))
        self.comboBox_quality.setItemText(4, QCoreApplication.translate("MainWindow", u"240p", None))
        self.comboBox_quality.setItemText(5, QCoreApplication.translate("MainWindow", u"144p", None))
        self.comboBox_quality.setItemText(6, QCoreApplication.translate("MainWindow", u"1440p", None))
        self.comboBox_quality.setItemText(7, QCoreApplication.translate("MainWindow", u"2160p", None))
        self.comboBox_quality.setItemText(8, QCoreApplication.translate("MainWindow", u"4320p", None))

        self.radioButton_quality_worst.setText(QCoreApplication.translate("MainWindow", u"Worst", None))
        self.groupBox_arguments.setTitle(QCoreApplication.translate("MainWindow", u"Arguments", None))
        self.lineEdit_argument_link.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://www.youtube.com/watch?v=dQw4w9WgXcQ", None))
        self.label_argument_link.setText(QCoreApplication.translate("MainWindow", u"Link", None))
        self.label_argument_path.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.pushButton_argument_link_multiple.setText(QCoreApplication.translate("MainWindow", u"Multiple...", None))
        self.lineEdit_argument_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\Users\\Public\\Videos", None))
        self.label_argument_ytdlp_args.setText(QCoreApplication.translate("MainWindow", u"yt-dlp\n"
"args", None))
        self.toolButton_argument_link_add.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
        self.lineEdit_argument_ytdlp_args.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--add-headers FIELD:VALUE --username USERNAME --password PASSWORD --twofactor TWOFACTOR", None))
        self.lineEdit_argument_filename.setPlaceholderText(QCoreApplication.translate("MainWindow", u"%(title)s [%(id)s]", None))
        self.label_argument_filename.setText(QCoreApplication.translate("MainWindow", u"Filename", None))
        self.toolButton_argument_path_revert.setText(QCoreApplication.translate("MainWindow", u"\u21ba", None))
        self.pushButton_argument_path_browse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.label_argument_ytdlp_conf.setText(QCoreApplication.translate("MainWindow", u"yt-dlp\n"
"conf file", None))
        self.lineEdit_argument_ytdlp_conf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"./yt-dlp.conf", None))
        self.pushButton_argument_ytdlp_conf_browse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.checkBox_argument_ytdlp_conf.setText("")
        self.label_argument_filename_help.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#output-template\"><span style=\" text-decoration: underline; color:#0000ff;\">Output template</span></a></p></body></html>", None))
        self.label_argument_ytdlp_args_help.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#usage-and-options\"><span style=\" text-decoration: underline; color:#0000ff;\">Usage &amp; options</span></a></p></body></html>", None))
        self.groupBox_stream.setTitle(QCoreApplication.translate("MainWindow", u"Stream", None))
        self.radioButton_stream_both.setText(QCoreApplication.translate("MainWindow", u"Video && Audio", None))
        self.radioButton_stream_audio.setText(QCoreApplication.translate("MainWindow", u"Audio only", None))
        self.groupBox_format.setTitle(QCoreApplication.translate("MainWindow", u"Format", None))
        self.label_format_video.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.comboBox_format_video.setItemText(0, QCoreApplication.translate("MainWindow", u"bestvideo", None))
        self.comboBox_format_video.setItemText(1, QCoreApplication.translate("MainWindow", u"3gp", None))
        self.comboBox_format_video.setItemText(2, QCoreApplication.translate("MainWindow", u"flv", None))
        self.comboBox_format_video.setItemText(3, QCoreApplication.translate("MainWindow", u"mp4", None))
        self.comboBox_format_video.setItemText(4, QCoreApplication.translate("MainWindow", u"webm", None))

        self.comboBox_format_audio.setItemText(0, QCoreApplication.translate("MainWindow", u"bestaudio", None))
        self.comboBox_format_audio.setItemText(1, QCoreApplication.translate("MainWindow", u"aac", None))
        self.comboBox_format_audio.setItemText(2, QCoreApplication.translate("MainWindow", u"m4a", None))
        self.comboBox_format_audio.setItemText(3, QCoreApplication.translate("MainWindow", u"ogg", None))
        self.comboBox_format_audio.setItemText(4, QCoreApplication.translate("MainWindow", u"wav", None))

        self.label_format_audio.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.checkBox_format_prefer.setText(QCoreApplication.translate("MainWindow", u"Prefer video formats\n"
"with free containers\n"
"over non-free", None))
        self.groupBox_info.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
        self.toolButton_ytdlp_help.setText(QCoreApplication.translate("MainWindow", u"yt-dlp --help", None))
        self.toolButton_ytdlp_version.setText(QCoreApplication.translate("MainWindow", u"yt-dlp --version", None))
        self.label_ytdlp_github.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/yt-dlp/yt-dlp\"><span style=\" text-decoration: underline; color:#0000ff;\">yt-dlp's GitHub</span></a></p></body></html>", None))
        self.groupBox_commands.setTitle(QCoreApplication.translate("MainWindow", u"Commands", None))
        self.pushButton_commands_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_commands_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_commands_remove.setText(QCoreApplication.translate("MainWindow", u"Remove selected", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), QCoreApplication.translate("MainWindow", u"General", None))
        self.groupBox_ppspices.setTitle(QCoreApplication.translate("MainWindow", u"Post-processing for embeds", None))
        self.checkBox_ppspices_no_post_overwrites.setText(QCoreApplication.translate("MainWindow", u"Do not overwrite\n"
"post-processed files", None))
        self.checkBox_ppspices_keep_video.setText(QCoreApplication.translate("MainWindow", u"Keep the intermediate\n"
"video file on disk after\n"
"post-processing", None))
        self.checkBox_ppspices_remux.setText(QCoreApplication.translate("MainWindow", u"Remux", None))
        self.checkBox_ppspices_recode.setText(QCoreApplication.translate("MainWindow", u"Recode", None))
        self.label_ppspices_remux_recode_help.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#post-processing-options\"><span style=\" text-decoration: underline; color:#0000ff;\">Read remux and recode Post-Processing Options</span></a></p></body></html>", None))
        self.groupBox_thumbnail.setTitle(QCoreApplication.translate("MainWindow", u"Thumbnail", None))
        self.checkBox_thumbnail_write.setText(QCoreApplication.translate("MainWindow", u"Write thumbnail", None))
        self.comboBox_thumbnail_convert_format.setItemText(0, QCoreApplication.translate("MainWindow", u"jpg", None))
        self.comboBox_thumbnail_convert_format.setItemText(1, QCoreApplication.translate("MainWindow", u"png", None))
        self.comboBox_thumbnail_convert_format.setItemText(2, QCoreApplication.translate("MainWindow", u"webp", None))

        self.checkBox_thumbnail_convert_format.setText(QCoreApplication.translate("MainWindow", u"Convert format", None))
        self.checkBox_thumbnail_embed.setText(QCoreApplication.translate("MainWindow", u"Embed as cover art", None))
        self.checkBox_thumbnail_write_all_formats.setText(QCoreApplication.translate("MainWindow", u"Write all formats", None))
        self.groupBox_subtitle.setTitle(QCoreApplication.translate("MainWindow", u"Subtitle", None))
        self.label_subtitle_language.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Languages<br/><a href=\"https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#subtitle-options\"><span style=\" text-decoration: underline; color:#0000ff;\">Read rules</span></a></p></body></html>", None))
        self.checkBox_subtitle_write.setText(QCoreApplication.translate("MainWindow", u"Write subtitles", None))
        self.checkBox_subtitle_convert_format.setText(QCoreApplication.translate("MainWindow", u"Convert format", None))
        self.comboBox_subtitle_convert_format.setItemText(0, QCoreApplication.translate("MainWindow", u"srt", None))
        self.comboBox_subtitle_convert_format.setItemText(1, QCoreApplication.translate("MainWindow", u"ass", None))
        self.comboBox_subtitle_convert_format.setItemText(2, QCoreApplication.translate("MainWindow", u"vtt", None))
        self.comboBox_subtitle_convert_format.setItemText(3, QCoreApplication.translate("MainWindow", u"lrc", None))

        self.checkBox_subtitle_format.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.comboBox_subtitle_format.setItemText(0, QCoreApplication.translate("MainWindow", u"srt", None))
        self.comboBox_subtitle_format.setItemText(1, QCoreApplication.translate("MainWindow", u"ass", None))
        self.comboBox_subtitle_format.setItemText(2, QCoreApplication.translate("MainWindow", u"vtt", None))
        self.comboBox_subtitle_format.setItemText(3, QCoreApplication.translate("MainWindow", u"lrc", None))

        self.radioButton_subtitle_language_all.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.radioButton_subtitle_language_rules.setText(QCoreApplication.translate("MainWindow", u"Use rules", None))
        self.checkBox_subtitle_autosub.setText(QCoreApplication.translate("MainWindow", u"Write auto-sub", None))
        self.checkBox_subtitle_embed.setText(QCoreApplication.translate("MainWindow", u"Embed subtitles", None))
        self.groupBox_metadata.setTitle(QCoreApplication.translate("MainWindow", u"Meatdata", None))
        self.checkBox_metadata_chapter.setText(QCoreApplication.translate("MainWindow", u"Embed chapters", None))
        self.checkBox_metadata_info_json.setText(QCoreApplication.translate("MainWindow", u"Embed info.json", None))
        self.checkBox_metadata_embed.setText(QCoreApplication.translate("MainWindow", u"Embed metadata", None))
        self.checkBox_metadata_xattrs.setText(QCoreApplication.translate("MainWindow", u"Write xattrs", None))
        self.groupBox_spicecmd.setTitle(QCoreApplication.translate("MainWindow", u"Commands", None))
        self.toolButton_spicecmd_list_formats.setText(QCoreApplication.translate("MainWindow", u"Run\n"
"--list-formats", None))
        self.toolButton_spicecmd_list_subs.setText(QCoreApplication.translate("MainWindow", u"Run\n"
"--list-subs", None))
        self.toolButton_spicecmd_list_thumbnails.setText(QCoreApplication.translate("MainWindow", u"Run\n"
"--list-thumbnails", None))
        self.toolButton_spicecmd_list_extractors.setText(QCoreApplication.translate("MainWindow", u"Run\n"
"--list-extractors", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_spices), QCoreApplication.translate("MainWindow", u"Spices", None))
        self.groupBox_returnytdislikes.setTitle(QCoreApplication.translate("MainWindow", u"Return Youtube Dislikes", None))
        self.checkBox_returnytdislikes.setText(QCoreApplication.translate("MainWindow", u"Add a Youtube Dislike count to Youtube video metadata", None))
        self.label_returnytdislikes_help.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>&#128712; Uses <a href=\"https://github.com/pukkandan/yt-dlp-ReturnYoutubeDislike\"><span style=\" text-decoration: underline; color:#0000ff;\">yt-dlp-ReturnYoutubeDislike plugin</span></a>. Then use <span style=\" font-weight:600;\">%(dislike_count)s<br/></span>Updated info fields: like_count, dislike_count, average_rating, view_count<br/>The original values of those fields and the response from the API are saved<br/>under <span style=\" font-weight:600;\">RYD</span> key in the info dict</p></body></html>", None))
        self.groupBox_dontlock.setTitle(QCoreApplication.translate("MainWindow", u"Don't lock", None))
        self.checkBox_dontlock.setText(QCoreApplication.translate("MainWindow", u"Keep awake during yt-dlp's execution", None))
        self.label_dontlock_help.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>&#128712; Uses <a href=\"https://github.com/Grub4K/yt-dont-lock-p\"><span style=\" text-decoration: underline; color:#0000ff;\">yt-dont-lock-p plugin<br/></span></a>Only applies to yt-dlp's execution</p><p>&#128712; Doesn't apply to <span style=\" text-decoration: underline;\">Extra processing</span><br/>Use <span style=\" text-decoration: underline;\">Behavior</span> for that</p></body></html>", None))
        self.groupBox_internetshortcut.setTitle(QCoreApplication.translate("MainWindow", u"Internet shortcut", None))
        self.checkBox_internetshortcut_windows.setText(QCoreApplication.translate("MainWindow", u".url Windows", None))
        self.checkBox_internetshortcut_mac.setText(QCoreApplication.translate("MainWindow", u".webloc macOS", None))
        self.checkBox_internetshortcut_platform.setText(QCoreApplication.translate("MainWindow", u"Current platform", None))
        self.checkBox_internetshortcut_linux.setText(QCoreApplication.translate("MainWindow", u".desktop Linux", None))
        self.groupBox_dearrow.setTitle(QCoreApplication.translate("MainWindow", u"DeArrow", None))
        self.checkBox_dearrow_title.setText(QCoreApplication.translate("MainWindow", u"Replace title", None))
        self.checkBox_dearrow_thumbnail.setText(QCoreApplication.translate("MainWindow", u"Download thumbnail", None))
        self.label_dearrow_title_help.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>&#128712; Uses <a href=\"https://github.com/QuantumWarpCode/yt-dlp-dearrow\"><span style=\" text-decoration: underline; color:#0000ff;\">yt-dlp-dearrow plugin</span></a>, replaces <span style=\" font-weight:600;\">%(title)s<br/></span>Access original with <span style=\" font-weight:600;\">%(original_title)s</span></p></body></html>", None))
        self.label_dearrow_thumbnail_help.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>&#128712; Manually download an additional thumbnail<br/>an image (webp) from <a href=\"https://wiki.sponsor.ajay.app/w/API_Docs/DeArrow#GET_/api/v1/getThumbnail\"><span style=\" text-decoration: underline; color:#0000ff;\">DeArrow's API</span></a></p></body></html>", None))
        self.groupBox_sponsorblock.setTitle(QCoreApplication.translate("MainWindow", u"SponsorBlock", None))
        self.radioButton_sponsorblock_remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.radioButton_sponsorblock_disable.setText(QCoreApplication.translate("MainWindow", u"Disable", None))
        self.radioButton_sponsorblock_mark.setText(QCoreApplication.translate("MainWindow", u"Mark", None))
        self.checkBox_sponsorblock_default.setText(QCoreApplication.translate("MainWindow", u"default", None))
        self.checkBox_sponsorblock_chapter.setText(QCoreApplication.translate("MainWindow", u"chapter", None))
        self.checkBox_sponsorblock_all.setText(QCoreApplication.translate("MainWindow", u"all", None))
        self.checkBox_sponsorblock_sponsor.setText(QCoreApplication.translate("MainWindow", u"sponsor", None))
        self.checkBox_sponsorblock_intro.setText(QCoreApplication.translate("MainWindow", u"intro", None))
        self.checkBox_sponsorblock_outro.setText(QCoreApplication.translate("MainWindow", u"outro", None))
        self.checkBox_sponsorblock_selfpromo.setText(QCoreApplication.translate("MainWindow", u"selfpromo", None))
        self.checkBox_sponsorblock_preview.setText(QCoreApplication.translate("MainWindow", u"preview", None))
        self.checkBox_sponsorblock_filler.setText(QCoreApplication.translate("MainWindow", u"filler", None))
        self.checkBox_sponsorblock_interaction.setText(QCoreApplication.translate("MainWindow", u"interaction", None))
        self.checkBox_sponsorblock_music_offtopic.setText(QCoreApplication.translate("MainWindow", u"music_offtopic", None))
        self.checkBox_sponsorblock_poi_highlight.setText(QCoreApplication.translate("MainWindow", u"poi_highlight", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_miscellaneous), QCoreApplication.translate("MainWindow", u"Miscellaneous", None))
        self.groupBox_cookies.setTitle(QCoreApplication.translate("MainWindow", u"Cookies", None))
        self.label_cookies_profile.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_cookies_container.setText(QCoreApplication.translate("MainWindow", u"Container", None))
        self.checkBox_cookies.setText(QCoreApplication.translate("MainWindow", u"Read and dump cookie jar in", None))
        self.toolButton_cookies_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.comboBox_cookies_keyring.setItemText(0, QCoreApplication.translate("MainWindow", u"deselected (windows)", None))
        self.comboBox_cookies_keyring.setItemText(1, QCoreApplication.translate("MainWindow", u"gnomekeyring", None))
        self.comboBox_cookies_keyring.setItemText(2, QCoreApplication.translate("MainWindow", u"basictext", None))
        self.comboBox_cookies_keyring.setItemText(3, QCoreApplication.translate("MainWindow", u"kwallet", None))
        self.comboBox_cookies_keyring.setItemText(4, QCoreApplication.translate("MainWindow", u"kwallet5", None))
        self.comboBox_cookies_keyring.setItemText(5, QCoreApplication.translate("MainWindow", u"kwallet6", None))

        self.label_cookies_keyring.setText(QCoreApplication.translate("MainWindow", u"Keyring", None))
        self.checkBox_cookies_browser.setText(QCoreApplication.translate("MainWindow", u"Read from browser", None))
        self.comboBox_cookies_browser.setItemText(0, QCoreApplication.translate("MainWindow", u"chrome", None))
        self.comboBox_cookies_browser.setItemText(1, QCoreApplication.translate("MainWindow", u"firefox", None))
        self.comboBox_cookies_browser.setItemText(2, QCoreApplication.translate("MainWindow", u"edge", None))
        self.comboBox_cookies_browser.setItemText(3, QCoreApplication.translate("MainWindow", u"brave", None))
        self.comboBox_cookies_browser.setItemText(4, QCoreApplication.translate("MainWindow", u"safari", None))
        self.comboBox_cookies_browser.setItemText(5, QCoreApplication.translate("MainWindow", u"chromium", None))
        self.comboBox_cookies_browser.setItemText(6, QCoreApplication.translate("MainWindow", u"vivaldi", None))
        self.comboBox_cookies_browser.setItemText(7, QCoreApplication.translate("MainWindow", u"whale", None))

        self.groupBox_filesystem.setTitle(QCoreApplication.translate("MainWindow", u"Filesystem", None))
        self.checkBox_filesystem_write_comments.setText(QCoreApplication.translate("MainWindow", u"Retrieve video comments\n"
"to be placed in the infojson", None))
        self.checkBox_filesystem_no_part.setText(QCoreApplication.translate("MainWindow", u"Do not use .part files -\n"
"write directly into output file", None))
        self.checkBox_filesystem_no_mtme.setText(QCoreApplication.translate("MainWindow", u"Do not use the Last-modified\n"
"header to set the file\n"
"modification time", None))
        self.checkBox_filesystem_write_description.setText(QCoreApplication.translate("MainWindow", u"Write video description to a\n"
".description file", None))
        self.checkBox_filesystem_windows_filenames.setText(QCoreApplication.translate("MainWindow", u"Force filenames to be\n"
"Windows-compatible", None))
        self.checkBox_filesystem_restrict_filenames.setText(QCoreApplication.translate("MainWindow", u"Restrict filenames to only\n"
"ASCII characters, and\n"
"avoid \"&&\" and spaces", None))
        self.checkBox_filesystem_no_continue.setText(QCoreApplication.translate("MainWindow", u"Do not resume partially\n"
"downloaded fragments", None))
        self.checkBox_filesystem_no_overwrites.setText(QCoreApplication.translate("MainWindow", u"Do not overwrite any files", None))
        self.checkBox_filesystem_force_overwrites.setText(QCoreApplication.translate("MainWindow", u"Force overwrite all\n"
"video and metadata files", None))
        self.checkBox_filesystem_trim_filenames.setText(QCoreApplication.translate("MainWindow", u"Limit the filename length\n"
"(excluding extension) to", None))
        self.checkBox_filesystem_write_infojson.setText(QCoreApplication.translate("MainWindow", u"Write video metadata to a\n"
".info.json file", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_filesystem), QCoreApplication.translate("MainWindow", u"Filesystem", None))
        self.groupBox_simulation.setTitle(QCoreApplication.translate("MainWindow", u"Simulation", None))
        self.checkBox_simulation_no_simulate.setText(QCoreApplication.translate("MainWindow", u"No simulation (Download\n"
"the video even if\n"
"printing/listing options\n"
"are used)", None))
        self.checkBox_simulation_skip_download.setText(QCoreApplication.translate("MainWindow", u"Do not download the video\n"
"but write all related files", None))
        self.checkBox_simulation_ignore_error.setText(QCoreApplication.translate("MainWindow", u"Ignore \"No video formats\"", None))
        self.checkBox_simulation_write_archive.setText(QCoreApplication.translate("MainWindow", u"Force write archive", None))
        self.checkBox_simulation_simulate.setText(QCoreApplication.translate("MainWindow", u"Force simulation (Do not\n"
"download the video and\n"
"do not write any files)", None))
        self.groupBox_workaround.setTitle(QCoreApplication.translate("MainWindow", u"Workarounds", None))
        self.checkBox_workaround_legacy.setText(QCoreApplication.translate("MainWindow", u"HTTPS without SRFC 5746\n"
"secure renegotiation", None))
        self.checkBox_workaround_sleep_requests.setText(QCoreApplication.translate("MainWindow", u"Sleep between requests", None))
        self.checkBox_workaround_no_certificates.setText(QCoreApplication.translate("MainWindow", u"No HTTPS certificate\n"
"validation", None))
        self.checkBox_workaround_sleep_interval.setText(QCoreApplication.translate("MainWindow", u"Sleep each download", None))
#if QT_CONFIG(tooltip)
        self.spinBox_workaround_sleep_interval_min.setToolTip(QCoreApplication.translate("MainWindow", u"minimum in seconds", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_workaround_sleep_interval_min.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
#if QT_CONFIG(tooltip)
        self.spinBox_workaround_sleep_interval_max.setToolTip(QCoreApplication.translate("MainWindow", u"maximum in seconds", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_workaround_sleep_interval_max.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
#if QT_CONFIG(tooltip)
        self.spinBox_workaround_sleep_requests.setToolTip(QCoreApplication.translate("MainWindow", u"in seconds", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_workaround_sleep_requests.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
        self.groupBox_cache.setTitle(QCoreApplication.translate("MainWindow", u"Cache", None))
        self.checkBox_cache_no_cache.setText(QCoreApplication.translate("MainWindow", u"Disable filesystem caching", None))
        self.toolButton_cache_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBox_cache_rm_cache.setText(QCoreApplication.translate("MainWindow", u"Delete all filesystem cache", None))
        self.checkBox_cache.setText(QCoreApplication.translate("MainWindow", u"Set cache dir where yt-dlp\n"
"can store downloaded\n"
"information permanently", None))
        self.groupBox_download.setTitle(QCoreApplication.translate("MainWindow", u"Download", None))
        self.comboBox_download_max_rate.setItemText(0, QCoreApplication.translate("MainWindow", u"B", None))
        self.comboBox_download_max_rate.setItemText(1, QCoreApplication.translate("MainWindow", u"K", None))
        self.comboBox_download_max_rate.setItemText(2, QCoreApplication.translate("MainWindow", u"M", None))
        self.comboBox_download_max_rate.setItemText(3, QCoreApplication.translate("MainWindow", u"G", None))

        self.comboBox_download_min_rate.setItemText(0, QCoreApplication.translate("MainWindow", u"B", None))
        self.comboBox_download_min_rate.setItemText(1, QCoreApplication.translate("MainWindow", u"K", None))
        self.comboBox_download_min_rate.setItemText(2, QCoreApplication.translate("MainWindow", u"M", None))
        self.comboBox_download_min_rate.setItemText(3, QCoreApplication.translate("MainWindow", u"G", None))

        self.checkBox_download_min_rate.setText(QCoreApplication.translate("MainWindow", u"Assumed\n"
"throttled rate", None))
        self.checkBox_download_max_rate.setText(QCoreApplication.translate("MainWindow", u"Maximum\n"
"download rate", None))
        self.checkBox_download_retry_sleep.setText(QCoreApplication.translate("MainWindow", u"Retry sleep", None))
        self.checkBox_download_retries.setText(QCoreApplication.translate("MainWindow", u"Retries (infinite\n"
"OR count)", None))
        self.checkBox_download_retries_infinite.setText(QCoreApplication.translate("MainWindow", u"infinite", None))
#if QT_CONFIG(tooltip)
        self.spinBox_download_retry_sleep.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.spinBox_download_retry_sleep.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
        self.checkBox_download_keep_fragments.setText(QCoreApplication.translate("MainWindow", u"Keep fragments after download", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_advanced), QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.groupBox_pymlsub.setTitle(QCoreApplication.translate("MainWindow", u"PyMusicLooper (loop detection general settings)", None))
        self.doubleSpinBox_pyml_min_duration.setSuffix(QCoreApplication.translate("MainWindow", u"x", None))
        self.checkBox_pyml_min_duartion.setText(QCoreApplication.translate("MainWindow", u"Min duration\n"
"multiplier", None))
        self.checkBox_pyml_brute_force.setText(QCoreApplication.translate("MainWindow", u"Brute force", None))
        self.comboBox_pyml_format.setItemText(0, QCoreApplication.translate("MainWindow", u"WAV", None))
        self.comboBox_pyml_format.setItemText(1, QCoreApplication.translate("MainWindow", u"FLAC", None))
        self.comboBox_pyml_format.setItemText(2, QCoreApplication.translate("MainWindow", u"OGG", None))
        self.comboBox_pyml_format.setItemText(3, QCoreApplication.translate("MainWindow", u"MP3", None))

        self.checkBox_pyml_format.setText(QCoreApplication.translate("MainWindow", u"Override split or extend\n"
"output format", None))
#if QT_CONFIG(tooltip)
        self.doubleSpinBox_pyml_loop_duration_max.setToolTip(QCoreApplication.translate("MainWindow", u"Max", None))
#endif // QT_CONFIG(tooltip)
        self.doubleSpinBox_pyml_loop_duration_max.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
#if QT_CONFIG(tooltip)
        self.doubleSpinBox_pyml_loop_duration_min.setToolTip(QCoreApplication.translate("MainWindow", u"Min", None))
#endif // QT_CONFIG(tooltip)
        self.doubleSpinBox_pyml_loop_duration_min.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
        self.checkBox_pyml_loop_duration.setText(QCoreApplication.translate("MainWindow", u"Loop\n"
"durations", None))
        self.groupBox_ffmpeg.setTitle(QCoreApplication.translate("MainWindow", u"FFmpeg", None))
        self.checkBox_ffmpeg.setText(QCoreApplication.translate("MainWindow", u"Run a pass of ffmpeg for each yt-dlpprocessed video", None))
        self.label_ffmpeg_help_right.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://ffmpeg.org/documentation.html\"><span style=\" text-decoration: underline; color:#0000ff;\">FFmpeg's documentation</span></a></p><p>Output container</p></body></html>", None))
        self.label_ffmpeg_help_left.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Input and ouput params are already provided as follows:<br/>&gt; ffmpeg <span style=\" font-weight:600;\">-i %(_filename)s </span>[...]<br/><span style=\" font-weight:600;\">%(_filename)s</span>_ffmpeg.<span style=\" font-weight:600;\">[Output container]</span></p></body></html>", None))
        self.plainTextEdit_ffmpeg_arguments.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-filter:v scale=720:-1 -c:a copy", None))
        self.groupBox_pymlmain.setTitle(QCoreApplication.translate("MainWindow", u"PyMusicLooper (export settings)", None))
        self.checkBox_pyml_export_format.setText(QCoreApplication.translate("MainWindow", u"Format exports as", None))
        self.radioButton_pyml_tag.setText(QCoreApplication.translate("MainWindow", u"Tag the input file", None))
        self.checkBox_pyml_export_topN.setText(QCoreApplication.translate("MainWindow", u"Top N loop points", None))
        self.checkBox_pyml_tag_override.setText(QCoreApplication.translate("MainWindow", u"Override tag names", None))
        self.comboBox_pyml_export_format.setItemText(0, QCoreApplication.translate("MainWindow", u"SAMPLES", None))
        self.comboBox_pyml_export_format.setItemText(1, QCoreApplication.translate("MainWindow", u"SECONDS", None))
        self.comboBox_pyml_export_format.setItemText(2, QCoreApplication.translate("MainWindow", u"TIME (mm:ss.sss)", None))

        self.lineEdit_pyml_tag_start.setText(QCoreApplication.translate("MainWindow", u"LOOP_START", None))
        self.lineEdit_pyml_tag_end.setText(QCoreApplication.translate("MainWindow", u"LOOP_END", None))
        self.label_pyml_help_right.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Interactive mode is not supported<br/>Only export commands is used</span></p></body></html>", None))
        self.checkBox_pyml.setText(QCoreApplication.translate("MainWindow", u"Run a pass of pymusiclooper for each yt-dlp processed video", None))
        self.label_pyml_extend_length.setText(QCoreApplication.translate("MainWindow", u"Extended length", None))
        self.doubleSpinBox_pyml_extend_length.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_pyml_help_left.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/arkrow/PyMusicLooper/blob/master/CLI_README.md\"><span style=\" text-decoration: underline; color:#0000ff;\">Read PyMusicLopper's documentzation</span></a>.<br/>Input audio is already provided</p></body></html>", None))
        self.label_pyml_extend_fade.setText(QCoreApplication.translate("MainWindow", u"Fade out duration", None))
        self.doubleSpinBox_pyml_extend_fade.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
        self.radioButton_split.setText(QCoreApplication.translate("MainWindow", u"Split the input file", None))
        self.label_pyml_split_help.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>&#128712; Split the input audio into intro,<br/><span style=\" font-weight:600;\">loop </span>and outro sections<br/>&#128712; Play the <span style=\" font-weight:600;\">loop</span> section with<br/><a href=\"https://en.wikipedia.org/wiki/Gapless_playback\"><span style=\" text-decoration: underline; color:#0000ff;\">gapless playback</span></a> for immediate effect</p></body></html>", None))
        self.radioButton_pyml_export.setText(QCoreApplication.translate("MainWindow", u"Export to text file", None))
        self.radioButton_pyml_extend.setText(QCoreApplication.translate("MainWindow", u"Extends the input file", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_extra_processing), QCoreApplication.translate("MainWindow", u"Extra processing", None))
        self.groupBox_afk.setTitle(QCoreApplication.translate("MainWindow", u"AFK", None))
        self.label_afk_running.setText(QCoreApplication.translate("MainWindow", u"While running", None))
        self.radioButton_afk_close.setText(QCoreApplication.translate("MainWindow", u"Close this application", None))
        self.label_afk_done.setText(QCoreApplication.translate("MainWindow", u"When done", None))
        self.radioButton_afk_nothing.setText(QCoreApplication.translate("MainWindow", u"Keep PC running", None))
        self.radioButton_afk_restart.setText(QCoreApplication.translate("MainWindow", u"Restart PC", None))
        self.radioButton_afk_shutdown.setText(QCoreApplication.translate("MainWindow", u"Turn off PC", None))
        self.checkBox_afk_keep_awake.setText(QCoreApplication.translate("MainWindow", u"Keep PC awake", None))
        self.radioButton_afk_command.setText(QCoreApplication.translate("MainWindow", u"Run command", None))
        self.lineEdit_afk_command.setPlaceholderText(QCoreApplication.translate("MainWindow", u"curl -i -H \"Accept: application/json\" -H \"Content-Type:application/json\" -X POST --data \"{\"content\": \"shiny-adventure\"}\" discord-webhook-link", None))
        self.groupBox_worker.setTitle(QCoreApplication.translate("MainWindow", u"Workers", None))
        self.label_worker_ytdlp.setText(QCoreApplication.translate("MainWindow", u"yt-dlp workers", None))
        self.label_worker_exproc.setText(QCoreApplication.translate("MainWindow", u"Extra processing workers", None))
        self.label_worker_help.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>&#128712; Not implemented</p><p>Note to self: multi-producer<br/>multi-consumer pattern</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_behavior), QCoreApplication.translate("MainWindow", u"Behavior", None))
        self.groupBox_status.setTitle(QCoreApplication.translate("MainWindow", u"Status", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_About.setTitle(QCoreApplication.translate("MainWindow", u"&About", None))
    # retranslateUi

