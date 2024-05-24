# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
        MainWindow.resize(873, 600)
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
        self.radioButton_3 = QRadioButton(self.groupBox_quality)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setChecked(True)

        self.gridLayout_4.addWidget(self.radioButton_3, 0, 0, 1, 1)

        self.radioButton_5 = QRadioButton(self.groupBox_quality)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout_4.addWidget(self.radioButton_5, 2, 0, 1, 1)

        self.radioButton_6 = QRadioButton(self.groupBox_quality)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout_4.addWidget(self.radioButton_6, 3, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.groupBox_quality)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_4.addWidget(self.comboBox_3, 2, 1, 2, 1)

        self.radioButton_4 = QRadioButton(self.groupBox_quality)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout_4.addWidget(self.radioButton_4, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_quality, 0, 2, 1, 1)

        self.groupBox_arguments = QGroupBox(self.tab_general)
        self.groupBox_arguments.setObjectName(u"groupBox_arguments")
        self.gridLayout = QGridLayout(self.groupBox_arguments)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.groupBox_arguments)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)

        self.label = QLabel(self.groupBox_arguments)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_arguments)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox_arguments)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox_arguments)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox_arguments)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.toolButton = QToolButton(self.groupBox_arguments)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.toolButton, 0, 4, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox_arguments)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 4, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox_arguments)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 2, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_arguments)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.toolButton_7 = QToolButton(self.groupBox_arguments)
        self.toolButton_7.setObjectName(u"toolButton_7")
        sizePolicy1.setHeightForWidth(self.toolButton_7.sizePolicy().hasHeightForWidth())
        self.toolButton_7.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.toolButton_7, 1, 4, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_arguments)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 3, 1, 1)

        self.label_15 = QLabel(self.groupBox_arguments)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 3, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.groupBox_arguments)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout.addWidget(self.lineEdit_10, 3, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox_arguments)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 3, 3, 1, 1)

        self.checkBox_62 = QCheckBox(self.groupBox_arguments)
        self.checkBox_62.setObjectName(u"checkBox_62")

        self.gridLayout.addWidget(self.checkBox_62, 3, 4, 1, 1)

        self.label_17 = QLabel(self.groupBox_arguments)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setTextFormat(Qt.RichText)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_17, 2, 3, 1, 2)

        self.label_18 = QLabel(self.groupBox_arguments)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setTextFormat(Qt.RichText)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_18, 4, 3, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox_arguments, 0, 0, 2, 1)

        self.groupBox_stream = QGroupBox(self.tab_general)
        self.groupBox_stream.setObjectName(u"groupBox_stream")
        self.gridLayout_2 = QGridLayout(self.groupBox_stream)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton = QRadioButton(self.groupBox_stream)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.gridLayout_2.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.groupBox_stream)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_2.addWidget(self.radioButton_2, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_stream, 0, 1, 1, 1)

        self.groupBox_format = QGroupBox(self.tab_general)
        self.groupBox_format.setObjectName(u"groupBox_format")
        self.gridLayout_5 = QGridLayout(self.groupBox_format)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_5 = QLabel(self.groupBox_format)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.groupBox_format)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_5.addWidget(self.comboBox, 0, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox_format)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_5.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_format)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.label_6, 1, 0, 1, 1)

        self.checkBox_32 = QCheckBox(self.groupBox_format)
        self.checkBox_32.setObjectName(u"checkBox_32")

        self.gridLayout_5.addWidget(self.checkBox_32, 0, 2, 2, 1)


        self.gridLayout_3.addWidget(self.groupBox_format, 1, 1, 1, 2)

        self.groupBox_info = QGroupBox(self.tab_general)
        self.groupBox_info.setObjectName(u"groupBox_info")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_info)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toolButton_2 = QToolButton(self.groupBox_info)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy1.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.toolButton_2)

        self.toolButton_3 = QToolButton(self.groupBox_info)
        self.toolButton_3.setObjectName(u"toolButton_3")
        sizePolicy1.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.toolButton_3)

        self.label_28 = QLabel(self.groupBox_info)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setTextFormat(Qt.RichText)

        self.horizontalLayout_4.addWidget(self.label_28)


        self.gridLayout_3.addWidget(self.groupBox_info, 2, 1, 1, 3)

        self.groupBox_commands = QGroupBox(self.tab_general)
        self.groupBox_commands.setObjectName(u"groupBox_commands")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_commands)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_3 = QPushButton(self.groupBox_commands)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_5.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox_commands)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_5.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.groupBox_commands)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_5.addWidget(self.pushButton_5)


        self.gridLayout_3.addWidget(self.groupBox_commands, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_general, "")
        self.tab_spices = QWidget()
        self.tab_spices.setObjectName(u"tab_spices")
        self.gridLayout_7 = QGridLayout(self.tab_spices)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_18 = QGroupBox(self.tab_spices)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_18.setFlat(False)
        self.gridLayout_20 = QGridLayout(self.groupBox_18)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.checkBox_45 = QCheckBox(self.groupBox_18)
        self.checkBox_45.setObjectName(u"checkBox_45")

        self.gridLayout_20.addWidget(self.checkBox_45, 0, 1, 1, 1)

        self.checkBox_44 = QCheckBox(self.groupBox_18)
        self.checkBox_44.setObjectName(u"checkBox_44")

        self.gridLayout_20.addWidget(self.checkBox_44, 0, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.groupBox_18)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_20.addWidget(self.lineEdit_12, 5, 1, 1, 1)

        self.lineEdit_11 = QLineEdit(self.groupBox_18)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_20.addWidget(self.lineEdit_11, 5, 0, 1, 1)

        self.checkBox_71 = QCheckBox(self.groupBox_18)
        self.checkBox_71.setObjectName(u"checkBox_71")

        self.gridLayout_20.addWidget(self.checkBox_71, 4, 0, 1, 1)

        self.checkBox_70 = QCheckBox(self.groupBox_18)
        self.checkBox_70.setObjectName(u"checkBox_70")

        self.gridLayout_20.addWidget(self.checkBox_70, 4, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_18)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setTextFormat(Qt.RichText)

        self.gridLayout_20.addWidget(self.label_19, 6, 0, 1, 2)


        self.gridLayout_7.addWidget(self.groupBox_18, 1, 2, 2, 1)

        self.groupBox_9 = QGroupBox(self.tab_spices)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy2.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy2)
        self.gridLayout_9 = QGridLayout(self.groupBox_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.checkBox = QCheckBox(self.groupBox_9)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_9.addWidget(self.checkBox, 0, 0, 1, 1)

        self.comboBox_6 = QComboBox(self.groupBox_9)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout_9.addWidget(self.comboBox_6, 3, 1, 1, 1)

        self.checkBox_34 = QCheckBox(self.groupBox_9)
        self.checkBox_34.setObjectName(u"checkBox_34")

        self.gridLayout_9.addWidget(self.checkBox_34, 3, 0, 1, 1)

        self.checkBox_33 = QCheckBox(self.groupBox_9)
        self.checkBox_33.setObjectName(u"checkBox_33")

        self.gridLayout_9.addWidget(self.checkBox_33, 4, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox_9)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_9.addWidget(self.checkBox_2, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_9, 1, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.tab_spices)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy2.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy2)
        self.gridLayout_8 = QGridLayout(self.groupBox_10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_7 = QLabel(self.groupBox_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setTextFormat(Qt.RichText)

        self.gridLayout_8.addWidget(self.label_7, 2, 0, 2, 1)

        self.checkBox_35 = QCheckBox(self.groupBox_10)
        self.checkBox_35.setObjectName(u"checkBox_35")

        self.gridLayout_8.addWidget(self.checkBox_35, 0, 0, 1, 1)

        self.checkBox_36 = QCheckBox(self.groupBox_10)
        self.checkBox_36.setObjectName(u"checkBox_36")

        self.gridLayout_8.addWidget(self.checkBox_36, 6, 0, 1, 1)

        self.comboBox_7 = QComboBox(self.groupBox_10)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.gridLayout_8.addWidget(self.comboBox_7, 6, 1, 1, 1)

        self.checkBox_38 = QCheckBox(self.groupBox_10)
        self.checkBox_38.setObjectName(u"checkBox_38")

        self.gridLayout_8.addWidget(self.checkBox_38, 5, 0, 1, 1)

        self.comboBox_8 = QComboBox(self.groupBox_10)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.gridLayout_8.addWidget(self.comboBox_8, 5, 1, 1, 1)

        self.radioButton_7 = QRadioButton(self.groupBox_10)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.gridLayout_8.addWidget(self.radioButton_7, 2, 1, 1, 1)

        self.radioButton_8 = QRadioButton(self.groupBox_10)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.gridLayout_8.addWidget(self.radioButton_8, 3, 1, 1, 1)

        self.checkBox_37 = QCheckBox(self.groupBox_10)
        self.checkBox_37.setObjectName(u"checkBox_37")

        self.gridLayout_8.addWidget(self.checkBox_37, 1, 0, 1, 1)

        self.checkBox_39 = QCheckBox(self.groupBox_10)
        self.checkBox_39.setObjectName(u"checkBox_39")

        self.gridLayout_8.addWidget(self.checkBox_39, 1, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox_10)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_8.addWidget(self.lineEdit_5, 4, 0, 1, 2)


        self.gridLayout_7.addWidget(self.groupBox_10, 1, 1, 3, 1)

        self.groupBox_17 = QGroupBox(self.tab_spices)
        self.groupBox_17.setObjectName(u"groupBox_17")
        sizePolicy1.setHeightForWidth(self.groupBox_17.sizePolicy().hasHeightForWidth())
        self.groupBox_17.setSizePolicy(sizePolicy1)
        self.gridLayout_19 = QGridLayout(self.groupBox_17)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.checkBox_41 = QCheckBox(self.groupBox_17)
        self.checkBox_41.setObjectName(u"checkBox_41")

        self.gridLayout_19.addWidget(self.checkBox_41, 1, 0, 1, 1)

        self.checkBox_42 = QCheckBox(self.groupBox_17)
        self.checkBox_42.setObjectName(u"checkBox_42")

        self.gridLayout_19.addWidget(self.checkBox_42, 2, 0, 1, 1)

        self.checkBox_40 = QCheckBox(self.groupBox_17)
        self.checkBox_40.setObjectName(u"checkBox_40")

        self.gridLayout_19.addWidget(self.checkBox_40, 0, 0, 1, 1)

        self.checkBox_43 = QCheckBox(self.groupBox_17)
        self.checkBox_43.setObjectName(u"checkBox_43")

        self.gridLayout_19.addWidget(self.checkBox_43, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_17, 2, 0, 2, 1)

        self.groupBox_24 = QGroupBox(self.tab_spices)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.gridLayout_28 = QGridLayout(self.groupBox_24)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.toolButton_10 = QToolButton(self.groupBox_24)
        self.toolButton_10.setObjectName(u"toolButton_10")
        sizePolicy1.setHeightForWidth(self.toolButton_10.sizePolicy().hasHeightForWidth())
        self.toolButton_10.setSizePolicy(sizePolicy1)

        self.gridLayout_28.addWidget(self.toolButton_10, 0, 2, 1, 1)

        self.toolButton_9 = QToolButton(self.groupBox_24)
        self.toolButton_9.setObjectName(u"toolButton_9")
        sizePolicy1.setHeightForWidth(self.toolButton_9.sizePolicy().hasHeightForWidth())
        self.toolButton_9.setSizePolicy(sizePolicy1)

        self.gridLayout_28.addWidget(self.toolButton_9, 0, 1, 1, 1)

        self.toolButton_8 = QToolButton(self.groupBox_24)
        self.toolButton_8.setObjectName(u"toolButton_8")
        sizePolicy1.setHeightForWidth(self.toolButton_8.sizePolicy().hasHeightForWidth())
        self.toolButton_8.setSizePolicy(sizePolicy1)

        self.gridLayout_28.addWidget(self.toolButton_8, 0, 0, 1, 1)

        self.toolButton_11 = QToolButton(self.groupBox_24)
        self.toolButton_11.setObjectName(u"toolButton_11")
        sizePolicy1.setHeightForWidth(self.toolButton_11.sizePolicy().hasHeightForWidth())
        self.toolButton_11.setSizePolicy(sizePolicy1)

        self.gridLayout_28.addWidget(self.toolButton_11, 0, 3, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_24, 3, 2, 1, 1)

        self.tabWidget.addTab(self.tab_spices, "")
        self.tab_miscellaneous = QWidget()
        self.tab_miscellaneous.setObjectName(u"tab_miscellaneous")
        self.gridLayout_10 = QGridLayout(self.tab_miscellaneous)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.groupBox_7 = QGroupBox(self.tab_miscellaneous)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_21 = QGridLayout(self.groupBox_7)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.checkBox_46 = QCheckBox(self.groupBox_7)
        self.checkBox_46.setObjectName(u"checkBox_46")

        self.gridLayout_21.addWidget(self.checkBox_46, 0, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setTextFormat(Qt.RichText)

        self.gridLayout_21.addWidget(self.label_13, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_7, 0, 2, 1, 1)

        self.groupBox_20 = QGroupBox(self.tab_miscellaneous)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.gridLayout_23 = QGridLayout(self.groupBox_20)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.checkBox_49 = QCheckBox(self.groupBox_20)
        self.checkBox_49.setObjectName(u"checkBox_49")

        self.gridLayout_23.addWidget(self.checkBox_49, 0, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_20)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setTextFormat(Qt.RichText)

        self.gridLayout_23.addWidget(self.label_14, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_20, 0, 1, 1, 1)

        self.groupBox_8 = QGroupBox(self.tab_miscellaneous)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_11 = QGridLayout(self.groupBox_8)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.checkBox_4 = QCheckBox(self.groupBox_8)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_11.addWidget(self.checkBox_4, 1, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.groupBox_8)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_11.addWidget(self.checkBox_5, 2, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox_8)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_11.addWidget(self.checkBox_3, 0, 0, 1, 1)

        self.checkBox_6 = QCheckBox(self.groupBox_8)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_11.addWidget(self.checkBox_6, 3, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_8, 0, 0, 1, 1)

        self.groupBox_19 = QGroupBox(self.tab_miscellaneous)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.gridLayout_22 = QGridLayout(self.groupBox_19)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.checkBox_47 = QCheckBox(self.groupBox_19)
        self.checkBox_47.setObjectName(u"checkBox_47")

        self.gridLayout_22.addWidget(self.checkBox_47, 0, 0, 1, 1)

        self.checkBox_48 = QCheckBox(self.groupBox_19)
        self.checkBox_48.setObjectName(u"checkBox_48")

        self.gridLayout_22.addWidget(self.checkBox_48, 1, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_19)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setTextFormat(Qt.RichText)

        self.gridLayout_22.addWidget(self.label_11, 0, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_19)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setTextFormat(Qt.RichText)

        self.gridLayout_22.addWidget(self.label_12, 1, 1, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_19, 1, 2, 1, 1)

        self.groupBox_21 = QGroupBox(self.tab_miscellaneous)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.gridLayout_24 = QGridLayout(self.groupBox_21)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.radioButton_10 = QRadioButton(self.groupBox_21)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.gridLayout_24.addWidget(self.radioButton_10, 1, 0, 1, 1)

        self.radioButton_9 = QRadioButton(self.groupBox_21)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setChecked(True)

        self.gridLayout_24.addWidget(self.radioButton_9, 0, 0, 1, 1)

        self.radioButton_11 = QRadioButton(self.groupBox_21)
        self.radioButton_11.setObjectName(u"radioButton_11")

        self.gridLayout_24.addWidget(self.radioButton_11, 2, 0, 1, 1)

        self.checkBox_50 = QCheckBox(self.groupBox_21)
        self.checkBox_50.setObjectName(u"checkBox_50")

        self.gridLayout_24.addWidget(self.checkBox_50, 0, 2, 1, 1)

        self.checkBox_52 = QCheckBox(self.groupBox_21)
        self.checkBox_52.setObjectName(u"checkBox_52")

        self.gridLayout_24.addWidget(self.checkBox_52, 0, 4, 1, 1)

        self.checkBox_51 = QCheckBox(self.groupBox_21)
        self.checkBox_51.setObjectName(u"checkBox_51")

        self.gridLayout_24.addWidget(self.checkBox_51, 0, 3, 1, 1)

        self.line = QFrame(self.groupBox_21)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(5)
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_24.addWidget(self.line, 0, 1, 3, 1)

        self.checkBox_53 = QCheckBox(self.groupBox_21)
        self.checkBox_53.setObjectName(u"checkBox_53")

        self.gridLayout_24.addWidget(self.checkBox_53, 0, 5, 1, 1)

        self.checkBox_54 = QCheckBox(self.groupBox_21)
        self.checkBox_54.setObjectName(u"checkBox_54")

        self.gridLayout_24.addWidget(self.checkBox_54, 1, 2, 1, 1)

        self.checkBox_55 = QCheckBox(self.groupBox_21)
        self.checkBox_55.setObjectName(u"checkBox_55")

        self.gridLayout_24.addWidget(self.checkBox_55, 1, 3, 1, 1)

        self.checkBox_56 = QCheckBox(self.groupBox_21)
        self.checkBox_56.setObjectName(u"checkBox_56")

        self.gridLayout_24.addWidget(self.checkBox_56, 1, 4, 1, 1)

        self.checkBox_57 = QCheckBox(self.groupBox_21)
        self.checkBox_57.setObjectName(u"checkBox_57")

        self.gridLayout_24.addWidget(self.checkBox_57, 1, 5, 1, 1)

        self.checkBox_58 = QCheckBox(self.groupBox_21)
        self.checkBox_58.setObjectName(u"checkBox_58")

        self.gridLayout_24.addWidget(self.checkBox_58, 2, 2, 1, 1)

        self.checkBox_59 = QCheckBox(self.groupBox_21)
        self.checkBox_59.setObjectName(u"checkBox_59")

        self.gridLayout_24.addWidget(self.checkBox_59, 2, 3, 1, 1)

        self.checkBox_60 = QCheckBox(self.groupBox_21)
        self.checkBox_60.setObjectName(u"checkBox_60")

        self.gridLayout_24.addWidget(self.checkBox_60, 2, 4, 1, 1)

        self.checkBox_61 = QCheckBox(self.groupBox_21)
        self.checkBox_61.setObjectName(u"checkBox_61")

        self.gridLayout_24.addWidget(self.checkBox_61, 2, 5, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_21, 1, 0, 1, 2)

        self.tabWidget.addTab(self.tab_miscellaneous, "")
        self.tab_filesystem = QWidget()
        self.tab_filesystem.setObjectName(u"tab_filesystem")
        self.gridLayout_12 = QGridLayout(self.tab_filesystem)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.groupBox_11 = QGroupBox(self.tab_filesystem)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy1.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy1)
        self.groupBox_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_16 = QGridLayout(self.groupBox_11)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_10 = QLabel(self.groupBox_11)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_10, 3, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_8, 3, 2, 1, 1)

        self.checkBox_7 = QCheckBox(self.groupBox_11)
        self.checkBox_7.setObjectName(u"checkBox_7")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy4)

        self.gridLayout_16.addWidget(self.checkBox_7, 0, 0, 1, 3)

        self.lineEdit_8 = QLineEdit(self.groupBox_11)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy5)
        self.lineEdit_8.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_16.addWidget(self.lineEdit_8, 4, 2, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox_11)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy5.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy5)
        self.lineEdit_7.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_16.addWidget(self.lineEdit_7, 4, 1, 1, 1)

        self.widget = QWidget(self.groupBox_11)
        self.widget.setObjectName(u"widget")
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_6 = QLineEdit(self.widget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout.addWidget(self.lineEdit_6)

        self.toolButton_5 = QToolButton(self.widget)
        self.toolButton_5.setObjectName(u"toolButton_5")

        self.horizontalLayout.addWidget(self.toolButton_5)


        self.gridLayout_16.addWidget(self.widget, 1, 0, 1, 3)

        self.comboBox_5 = QComboBox(self.groupBox_11)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy6)
        self.comboBox_5.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_16.addWidget(self.comboBox_5, 4, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_11)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_9, 3, 0, 1, 1)

        self.widget_2 = QWidget(self.groupBox_11)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy4.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy4)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_8 = QCheckBox(self.widget_2)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.horizontalLayout_2.addWidget(self.checkBox_8)

        self.comboBox_4 = QComboBox(self.widget_2)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy4.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.comboBox_4)


        self.gridLayout_16.addWidget(self.widget_2, 2, 0, 1, 3)


        self.gridLayout_12.addWidget(self.groupBox_11, 0, 2, 1, 1)

        self.groupBox_12 = QGroupBox(self.tab_filesystem)
        self.groupBox_12.setObjectName(u"groupBox_12")
        sizePolicy2.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy2)
        self.groupBox_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_14 = QGridLayout(self.groupBox_12)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.checkBox_22 = QCheckBox(self.groupBox_12)
        self.checkBox_22.setObjectName(u"checkBox_22")
        sizePolicy3.setHeightForWidth(self.checkBox_22.sizePolicy().hasHeightForWidth())
        self.checkBox_22.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_22, 5, 2, 1, 1)

        self.checkBox_18 = QCheckBox(self.groupBox_12)
        self.checkBox_18.setObjectName(u"checkBox_18")
        sizePolicy3.setHeightForWidth(self.checkBox_18.sizePolicy().hasHeightForWidth())
        self.checkBox_18.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_18, 2, 1, 1, 1)

        self.checkBox_19 = QCheckBox(self.groupBox_12)
        self.checkBox_19.setObjectName(u"checkBox_19")
        sizePolicy3.setHeightForWidth(self.checkBox_19.sizePolicy().hasHeightForWidth())
        self.checkBox_19.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_19, 1, 2, 1, 1)

        self.checkBox_20 = QCheckBox(self.groupBox_12)
        self.checkBox_20.setObjectName(u"checkBox_20")
        sizePolicy3.setHeightForWidth(self.checkBox_20.sizePolicy().hasHeightForWidth())
        self.checkBox_20.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_20, 2, 2, 1, 1)

        self.checkBox_13 = QCheckBox(self.groupBox_12)
        self.checkBox_13.setObjectName(u"checkBox_13")
        sizePolicy3.setHeightForWidth(self.checkBox_13.sizePolicy().hasHeightForWidth())
        self.checkBox_13.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_13, 2, 0, 1, 1)

        self.checkBox_12 = QCheckBox(self.groupBox_12)
        self.checkBox_12.setObjectName(u"checkBox_12")
        sizePolicy3.setHeightForWidth(self.checkBox_12.sizePolicy().hasHeightForWidth())
        self.checkBox_12.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_12, 1, 0, 1, 1)

        self.checkBox_17 = QCheckBox(self.groupBox_12)
        self.checkBox_17.setObjectName(u"checkBox_17")
        sizePolicy3.setHeightForWidth(self.checkBox_17.sizePolicy().hasHeightForWidth())
        self.checkBox_17.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_17, 1, 1, 1, 1)

        self.checkBox_15 = QCheckBox(self.groupBox_12)
        self.checkBox_15.setObjectName(u"checkBox_15")
        sizePolicy3.setHeightForWidth(self.checkBox_15.sizePolicy().hasHeightForWidth())
        self.checkBox_15.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_15, 3, 0, 1, 1)

        self.checkBox_16 = QCheckBox(self.groupBox_12)
        self.checkBox_16.setObjectName(u"checkBox_16")
        sizePolicy3.setHeightForWidth(self.checkBox_16.sizePolicy().hasHeightForWidth())
        self.checkBox_16.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_16, 3, 1, 1, 1)

        self.checkBox_14 = QCheckBox(self.groupBox_12)
        self.checkBox_14.setObjectName(u"checkBox_14")
        sizePolicy3.setHeightForWidth(self.checkBox_14.sizePolicy().hasHeightForWidth())
        self.checkBox_14.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_14, 5, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox_12)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy7)
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(9999)
        self.spinBox.setSingleStep(10)

        self.gridLayout_14.addWidget(self.spinBox, 5, 1, 1, 1)

        self.checkBox_21 = QCheckBox(self.groupBox_12)
        self.checkBox_21.setObjectName(u"checkBox_21")
        sizePolicy3.setHeightForWidth(self.checkBox_21.sizePolicy().hasHeightForWidth())
        self.checkBox_21.setSizePolicy(sizePolicy3)

        self.gridLayout_14.addWidget(self.checkBox_21, 3, 2, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_12, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_filesystem, "")
        self.tab_advanced = QWidget()
        self.tab_advanced.setObjectName(u"tab_advanced")
        self.gridLayout_13 = QGridLayout(self.tab_advanced)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.groupBox_13 = QGroupBox(self.tab_advanced)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_15 = QGridLayout(self.groupBox_13)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.checkBox_23 = QCheckBox(self.groupBox_13)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.gridLayout_15.addWidget(self.checkBox_23, 1, 0, 1, 1)

        self.checkBox_24 = QCheckBox(self.groupBox_13)
        self.checkBox_24.setObjectName(u"checkBox_24")

        self.gridLayout_15.addWidget(self.checkBox_24, 6, 0, 1, 2)

        self.checkBox_25 = QCheckBox(self.groupBox_13)
        self.checkBox_25.setObjectName(u"checkBox_25")

        self.gridLayout_15.addWidget(self.checkBox_25, 5, 0, 1, 2)

        self.checkBox_26 = QCheckBox(self.groupBox_13)
        self.checkBox_26.setObjectName(u"checkBox_26")

        self.gridLayout_15.addWidget(self.checkBox_26, 7, 0, 1, 1)

        self.checkBox_27 = QCheckBox(self.groupBox_13)
        self.checkBox_27.setObjectName(u"checkBox_27")

        self.gridLayout_15.addWidget(self.checkBox_27, 2, 0, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_13, 0, 0, 2, 1)

        self.groupBox_16 = QGroupBox(self.tab_advanced)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_18 = QGridLayout(self.groupBox_16)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.checkBox_28 = QCheckBox(self.groupBox_16)
        self.checkBox_28.setObjectName(u"checkBox_28")

        self.gridLayout_18.addWidget(self.checkBox_28, 0, 0, 1, 1)

        self.checkBox_30 = QCheckBox(self.groupBox_16)
        self.checkBox_30.setObjectName(u"checkBox_30")

        self.gridLayout_18.addWidget(self.checkBox_30, 0, 1, 1, 1)

        self.checkBox_29 = QCheckBox(self.groupBox_16)
        self.checkBox_29.setObjectName(u"checkBox_29")

        self.gridLayout_18.addWidget(self.checkBox_29, 1, 0, 1, 1)

        self.checkBox_31 = QCheckBox(self.groupBox_16)
        self.checkBox_31.setObjectName(u"checkBox_31")

        self.gridLayout_18.addWidget(self.checkBox_31, 1, 1, 1, 1)

        self.spinBox_3 = QSpinBox(self.groupBox_16)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(9999)
        self.spinBox_3.setSingleStep(100)

        self.gridLayout_18.addWidget(self.spinBox_3, 1, 2, 1, 1)

        self.spinBox_4 = QSpinBox(self.groupBox_16)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMaximum(9999)
        self.spinBox_4.setSingleStep(100)

        self.gridLayout_18.addWidget(self.spinBox_4, 1, 3, 1, 1)

        self.spinBox_2 = QSpinBox(self.groupBox_16)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(9999)
        self.spinBox_2.setSingleStep(100)

        self.gridLayout_18.addWidget(self.spinBox_2, 0, 2, 1, 2)


        self.gridLayout_13.addWidget(self.groupBox_16, 1, 3, 1, 1)

        self.groupBox_14 = QGroupBox(self.tab_advanced)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_17 = QGridLayout(self.groupBox_14)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.checkBox_10 = QCheckBox(self.groupBox_14)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout_17.addWidget(self.checkBox_10, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.groupBox_14)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy3.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy3)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_9 = QLineEdit(self.widget_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_3.addWidget(self.lineEdit_9)

        self.toolButton_6 = QToolButton(self.widget_3)
        self.toolButton_6.setObjectName(u"toolButton_6")

        self.horizontalLayout_3.addWidget(self.toolButton_6)


        self.gridLayout_17.addWidget(self.widget_3, 2, 0, 1, 2)

        self.checkBox_11 = QCheckBox(self.groupBox_14)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.gridLayout_17.addWidget(self.checkBox_11, 1, 1, 1, 1)

        self.checkBox_9 = QCheckBox(self.groupBox_14)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout_17.addWidget(self.checkBox_9, 0, 0, 2, 1)


        self.gridLayout_13.addWidget(self.groupBox_14, 0, 3, 1, 1)

        self.groupBox_15 = QGroupBox(self.tab_advanced)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_25 = QGridLayout(self.groupBox_15)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.comboBox_9 = QComboBox(self.groupBox_15)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        sizePolicy7.setHeightForWidth(self.comboBox_9.sizePolicy().hasHeightForWidth())
        self.comboBox_9.setSizePolicy(sizePolicy7)
        self.comboBox_9.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_25.addWidget(self.comboBox_9, 3, 1, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox_15)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        sizePolicy4.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy4)
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMaximum(999.000000000000000)

        self.gridLayout_25.addWidget(self.doubleSpinBox, 3, 0, 1, 1)

        self.comboBox_10 = QComboBox(self.groupBox_15)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")
        sizePolicy7.setHeightForWidth(self.comboBox_10.sizePolicy().hasHeightForWidth())
        self.comboBox_10.setSizePolicy(sizePolicy7)
        self.comboBox_10.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_25.addWidget(self.comboBox_10, 3, 3, 1, 1)

        self.checkBox_64 = QCheckBox(self.groupBox_15)
        self.checkBox_64.setObjectName(u"checkBox_64")

        self.gridLayout_25.addWidget(self.checkBox_64, 2, 2, 1, 2)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox_15)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setDecimals(1)
        self.doubleSpinBox_2.setMaximum(999.000000000000000)

        self.gridLayout_25.addWidget(self.doubleSpinBox_2, 3, 2, 1, 1)

        self.checkBox_63 = QCheckBox(self.groupBox_15)
        self.checkBox_63.setObjectName(u"checkBox_63")

        self.gridLayout_25.addWidget(self.checkBox_63, 2, 0, 1, 2)

        self.checkBox_67 = QCheckBox(self.groupBox_15)
        self.checkBox_67.setObjectName(u"checkBox_67")

        self.gridLayout_25.addWidget(self.checkBox_67, 4, 2, 1, 2)

        self.checkBox_65 = QCheckBox(self.groupBox_15)
        self.checkBox_65.setObjectName(u"checkBox_65")

        self.gridLayout_25.addWidget(self.checkBox_65, 4, 0, 1, 2)

        self.spinBox_5 = QSpinBox(self.groupBox_15)
        self.spinBox_5.setObjectName(u"spinBox_5")

        self.gridLayout_25.addWidget(self.spinBox_5, 5, 1, 1, 1)

        self.checkBox_66 = QCheckBox(self.groupBox_15)
        self.checkBox_66.setObjectName(u"checkBox_66")

        self.gridLayout_25.addWidget(self.checkBox_66, 5, 0, 1, 1)

        self.line_2 = QFrame(self.groupBox_15)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_25.addWidget(self.line_2, 1, 0, 1, 4)

        self.spinBox_6 = QSpinBox(self.groupBox_15)
        self.spinBox_6.setObjectName(u"spinBox_6")

        self.gridLayout_25.addWidget(self.spinBox_6, 5, 2, 1, 2)

        self.checkBox_68 = QCheckBox(self.groupBox_15)
        self.checkBox_68.setObjectName(u"checkBox_68")

        self.gridLayout_25.addWidget(self.checkBox_68, 0, 0, 1, 4)


        self.gridLayout_13.addWidget(self.groupBox_15, 0, 1, 2, 1)

        self.tabWidget.addTab(self.tab_advanced, "")
        self.tab_extra_processing = QWidget()
        self.tab_extra_processing.setObjectName(u"tab_extra_processing")
        self.gridLayout_26 = QGridLayout(self.tab_extra_processing)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.groupBox_25 = QGroupBox(self.tab_extra_processing)
        self.groupBox_25.setObjectName(u"groupBox_25")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.groupBox_25.sizePolicy().hasHeightForWidth())
        self.groupBox_25.setSizePolicy(sizePolicy8)
        self.gridLayout_30 = QGridLayout(self.groupBox_25)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.doubleSpinBox_3 = QDoubleSpinBox(self.groupBox_25)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setMaximum(1.000000000000000)
        self.doubleSpinBox_3.setSingleStep(0.010000000000000)
        self.doubleSpinBox_3.setValue(0.350000000000000)

        self.gridLayout_30.addWidget(self.doubleSpinBox_3, 0, 2, 1, 1)

        self.checkBox_75 = QCheckBox(self.groupBox_25)
        self.checkBox_75.setObjectName(u"checkBox_75")

        self.gridLayout_30.addWidget(self.checkBox_75, 0, 1, 1, 1)

        self.checkBox_78 = QCheckBox(self.groupBox_25)
        self.checkBox_78.setObjectName(u"checkBox_78")

        self.gridLayout_30.addWidget(self.checkBox_78, 0, 0, 1, 1)

        self.comboBox_12 = QComboBox(self.groupBox_25)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")

        self.gridLayout_30.addWidget(self.comboBox_12, 1, 2, 1, 1)

        self.checkBox_79 = QCheckBox(self.groupBox_25)
        self.checkBox_79.setObjectName(u"checkBox_79")

        self.gridLayout_30.addWidget(self.checkBox_79, 1, 0, 1, 2)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.groupBox_25)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setDecimals(3)
        self.doubleSpinBox_5.setMaximum(9999.000000000000000)

        self.gridLayout_30.addWidget(self.doubleSpinBox_5, 1, 4, 1, 1)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.groupBox_25)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setDecimals(3)
        self.doubleSpinBox_4.setMaximum(9999.000000000000000)

        self.gridLayout_30.addWidget(self.doubleSpinBox_4, 0, 4, 1, 1)

        self.checkBox_76 = QCheckBox(self.groupBox_25)
        self.checkBox_76.setObjectName(u"checkBox_76")

        self.gridLayout_30.addWidget(self.checkBox_76, 0, 3, 2, 1)


        self.gridLayout_26.addWidget(self.groupBox_25, 1, 0, 1, 1)

        self.groupBox_22 = QGroupBox(self.tab_extra_processing)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.gridLayout_27 = QGridLayout(self.groupBox_22)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.checkBox_69 = QCheckBox(self.groupBox_22)
        self.checkBox_69.setObjectName(u"checkBox_69")

        self.gridLayout_27.addWidget(self.checkBox_69, 0, 0, 1, 1)

        self.label_21 = QLabel(self.groupBox_22)
        self.label_21.setObjectName(u"label_21")
        sizePolicy1.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy1)
        self.label_21.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_27.addWidget(self.label_21, 0, 1, 2, 1)

        self.label_16 = QLabel(self.groupBox_22)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setTextFormat(Qt.RichText)

        self.gridLayout_27.addWidget(self.label_16, 1, 0, 2, 1)

        self.plainTextEdit = QPlainTextEdit(self.groupBox_22)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy9)
        self.plainTextEdit.setMinimumSize(QSize(0, 30))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_27.addWidget(self.plainTextEdit, 3, 0, 1, 2)

        self.lineEdit_13 = QLineEdit(self.groupBox_22)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy10)

        self.gridLayout_27.addWidget(self.lineEdit_13, 2, 1, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_22, 0, 0, 1, 1)

        self.groupBox_23 = QGroupBox(self.tab_extra_processing)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.gridLayout_29 = QGridLayout(self.groupBox_23)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.checkBox_74 = QCheckBox(self.groupBox_23)
        self.checkBox_74.setObjectName(u"checkBox_74")

        self.gridLayout_29.addWidget(self.checkBox_74, 5, 0, 1, 1)

        self.radioButton_14 = QRadioButton(self.groupBox_23)
        self.radioButton_14.setObjectName(u"radioButton_14")

        self.gridLayout_29.addWidget(self.radioButton_14, 3, 2, 1, 2)

        self.checkBox_73 = QCheckBox(self.groupBox_23)
        self.checkBox_73.setObjectName(u"checkBox_73")

        self.gridLayout_29.addWidget(self.checkBox_73, 4, 0, 1, 1)

        self.spinBox_7 = QSpinBox(self.groupBox_23)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setMinimum(-1)
        self.spinBox_7.setMaximum(999)
        self.spinBox_7.setValue(1)

        self.gridLayout_29.addWidget(self.spinBox_7, 4, 1, 1, 1)

        self.checkBox_77 = QCheckBox(self.groupBox_23)
        self.checkBox_77.setObjectName(u"checkBox_77")

        self.gridLayout_29.addWidget(self.checkBox_77, 4, 2, 1, 2)

        self.comboBox_11 = QComboBox(self.groupBox_23)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")

        self.gridLayout_29.addWidget(self.comboBox_11, 5, 1, 1, 1)

        self.lineEdit_14 = QLineEdit(self.groupBox_23)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Minimum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.lineEdit_14.sizePolicy().hasHeightForWidth())
        self.lineEdit_14.setSizePolicy(sizePolicy11)
        self.lineEdit_14.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_29.addWidget(self.lineEdit_14, 5, 2, 1, 1)

        self.lineEdit_15 = QLineEdit(self.groupBox_23)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        sizePolicy10.setHeightForWidth(self.lineEdit_15.sizePolicy().hasHeightForWidth())
        self.lineEdit_15.setSizePolicy(sizePolicy10)

        self.gridLayout_29.addWidget(self.lineEdit_15, 5, 3, 1, 1)

        self.label_20 = QLabel(self.groupBox_23)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_29.addWidget(self.label_20, 2, 2, 1, 2)

        self.checkBox_72 = QCheckBox(self.groupBox_23)
        self.checkBox_72.setObjectName(u"checkBox_72")

        self.gridLayout_29.addWidget(self.checkBox_72, 0, 0, 1, 4)

        self.label_23 = QLabel(self.groupBox_23)
        self.label_23.setObjectName(u"label_23")
        sizePolicy3.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy3)

        self.gridLayout_29.addWidget(self.label_23, 7, 0, 1, 1)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.groupBox_23)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setMaximum(9999.000000000000000)
        self.doubleSpinBox_6.setValue(3600.000000000000000)

        self.gridLayout_29.addWidget(self.doubleSpinBox_6, 7, 1, 1, 1)

        self.label_22 = QLabel(self.groupBox_23)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setTextFormat(Qt.RichText)

        self.gridLayout_29.addWidget(self.label_22, 2, 0, 1, 2)

        self.label_24 = QLabel(self.groupBox_23)
        self.label_24.setObjectName(u"label_24")
        sizePolicy3.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy3)

        self.gridLayout_29.addWidget(self.label_24, 8, 0, 1, 1)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.groupBox_23)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")
        self.doubleSpinBox_7.setMaximum(9999.000000000000000)
        self.doubleSpinBox_7.setSingleStep(0.100000000000000)
        self.doubleSpinBox_7.setValue(5.000000000000000)

        self.gridLayout_29.addWidget(self.doubleSpinBox_7, 8, 1, 1, 1)

        self.radioButton_13 = QRadioButton(self.groupBox_23)
        self.radioButton_13.setObjectName(u"radioButton_13")

        self.gridLayout_29.addWidget(self.radioButton_13, 6, 2, 1, 2)

        self.label_25 = QLabel(self.groupBox_23)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setTextFormat(Qt.RichText)

        self.gridLayout_29.addWidget(self.label_25, 7, 2, 2, 2)

        self.radioButton_12 = QRadioButton(self.groupBox_23)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setChecked(True)

        self.gridLayout_29.addWidget(self.radioButton_12, 3, 0, 1, 2)

        self.radioButton_15 = QRadioButton(self.groupBox_23)
        self.radioButton_15.setObjectName(u"radioButton_15")

        self.gridLayout_29.addWidget(self.radioButton_15, 6, 0, 1, 2)


        self.gridLayout_26.addWidget(self.groupBox_23, 0, 1, 2, 1)

        self.tabWidget.addTab(self.tab_extra_processing, "")
        self.tab_behavior = QWidget()
        self.tab_behavior.setObjectName(u"tab_behavior")
        self.gridLayout_31 = QGridLayout(self.tab_behavior)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.groupBox_26 = QGroupBox(self.tab_behavior)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.gridLayout_32 = QGridLayout(self.groupBox_26)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_26 = QLabel(self.groupBox_26)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_32.addWidget(self.label_26, 0, 0, 1, 1)

        self.radioButton_21 = QRadioButton(self.groupBox_26)
        self.radioButton_21.setObjectName(u"radioButton_21")

        self.gridLayout_32.addWidget(self.radioButton_21, 6, 0, 1, 1)

        self.label_27 = QLabel(self.groupBox_26)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_32.addWidget(self.label_27, 2, 0, 1, 1)

        self.radioButton_16 = QRadioButton(self.groupBox_26)
        self.radioButton_16.setObjectName(u"radioButton_16")
        self.radioButton_16.setChecked(True)

        self.gridLayout_32.addWidget(self.radioButton_16, 3, 0, 1, 1)

        self.radioButton_18 = QRadioButton(self.groupBox_26)
        self.radioButton_18.setObjectName(u"radioButton_18")

        self.gridLayout_32.addWidget(self.radioButton_18, 5, 0, 1, 1)

        self.radioButton_17 = QRadioButton(self.groupBox_26)
        self.radioButton_17.setObjectName(u"radioButton_17")

        self.gridLayout_32.addWidget(self.radioButton_17, 4, 0, 1, 1)

        self.checkBox_80 = QCheckBox(self.groupBox_26)
        self.checkBox_80.setObjectName(u"checkBox_80")

        self.gridLayout_32.addWidget(self.checkBox_80, 1, 0, 1, 1)

        self.radioButton_19 = QRadioButton(self.groupBox_26)
        self.radioButton_19.setObjectName(u"radioButton_19")

        self.gridLayout_32.addWidget(self.radioButton_19, 7, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.groupBox_26)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_32.addWidget(self.lineEdit_16, 8, 0, 1, 1)


        self.gridLayout_31.addWidget(self.groupBox_26, 0, 0, 1, 1)

        self.groupBox_28 = QGroupBox(self.tab_behavior)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.groupBox_28.setEnabled(False)
        self.groupBox_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_6 = QGridLayout(self.groupBox_28)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_30 = QLabel(self.groupBox_28)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_6.addWidget(self.label_30, 1, 0, 1, 1)

        self.spinBox_8 = QSpinBox(self.groupBox_28)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setMinimum(1)
        self.spinBox_8.setMaximum(16)

        self.gridLayout_6.addWidget(self.spinBox_8, 1, 1, 1, 1)

        self.label_31 = QLabel(self.groupBox_28)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_6.addWidget(self.label_31, 2, 0, 1, 1)

        self.spinBox_9 = QSpinBox(self.groupBox_28)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setMinimum(1)
        self.spinBox_9.setMaximum(16)

        self.gridLayout_6.addWidget(self.spinBox_9, 2, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_28)
        self.label_29.setObjectName(u"label_29")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy12)
        self.label_29.setTextFormat(Qt.RichText)

        self.gridLayout_6.addWidget(self.label_29, 0, 0, 1, 2)


        self.gridLayout_31.addWidget(self.groupBox_28, 0, 1, 1, 1, Qt.AlignTop)

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
        self.menubar.setGeometry(QRect(0, 0, 873, 21))
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"&Exit", None))
        self.action_About_shiny_adventure.setText(QCoreApplication.translate("MainWindow", u"&About shiny-adventure...", None))
        self.groupBox_quality.setTitle(QCoreApplication.translate("MainWindow", u"Quality", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Best", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"At most", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"At least", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"1080p", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"720p", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"480p", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"360p", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"240p", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"144p", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"1440p", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"2160p", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("MainWindow", u"4320p", None))

        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Worst", None))
        self.groupBox_arguments.setTitle(QCoreApplication.translate("MainWindow", u"Arguments", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://www.youtube.com/watch?v=dQw4w9WgXcQ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Link", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Multiple...", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\Users\\Public\\Videos", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"yt-dlp\n"
"args", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--add-headers FIELD:VALUE --username USERNAME --password PASSWORD --twofactor TWOFACTOR", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"%(title)s [%(id)s]", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Filename", None))
        self.toolButton_7.setText(QCoreApplication.translate("MainWindow", u"\u21ba", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"yt-dlp\n"
"conf file", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"./yt-dlp.conf", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.checkBox_62.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#output-template\"><span style=\" text-decoration: underline; color:#0000ff;\">Output template</span></a></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#usage-and-options\"><span style=\" text-decoration: underline; color:#0000ff;\">Usage &amp; options</span></a></p></body></html>", None))
        self.groupBox_stream.setTitle(QCoreApplication.translate("MainWindow", u"Stream", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Video && Audio", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Audio only", None))
        self.groupBox_format.setTitle(QCoreApplication.translate("MainWindow", u"Format", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"bestvideo", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"3gp", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"flv", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"mp4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"webm", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"bestaudio", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"aac", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"m4a", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"ogg", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"wav", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.checkBox_32.setText(QCoreApplication.translate("MainWindow", u"Prefer video formats\n"
"with free containers\n"
"over non-free", None))
        self.groupBox_info.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"yt-dlp --help", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"yt-dlp --version", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/yt-dlp/yt-dlp\"><span style=\" text-decoration: underline; color:#0000ff;\">yt-dlp's GitHub</span></a></p></body></html>", None))
        self.groupBox_commands.setTitle(QCoreApplication.translate("MainWindow", u"Commands", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Remove selected", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), QCoreApplication.translate("MainWindow", u"General", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"Post-processing for embeds", None))
        self.checkBox_45.setText(QCoreApplication.translate("MainWindow", u"Do not overwrite\n"
"post-processed files", None))
        self.checkBox_44.setText(QCoreApplication.translate("MainWindow", u"Keep the intermediate\n"
"video file on disk after\n"
"post-processing", None))
        self.checkBox_71.setText(QCoreApplication.translate("MainWindow", u"Remux", None))
        self.checkBox_70.setText(QCoreApplication.translate("MainWindow", u"Recode", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#post-processing-options\"><span style=\" text-decoration: underline; color:#0000ff;\">Read remux and recode Post-Processing Options</span></a></p></body></html>", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Thumbnail", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Write thumbnail", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"jpg", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"png", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"webp", None))

        self.checkBox_34.setText(QCoreApplication.translate("MainWindow", u"Convert format", None))
        self.checkBox_33.setText(QCoreApplication.translate("MainWindow", u"Embed as cover art", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Write all formats", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Subtitle", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Languages<br/><a href=\"https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#subtitle-options\"><span style=\" text-decoration: underline; color:#0000ff;\">Read rules</span></a></p></body></html>", None))
        self.checkBox_35.setText(QCoreApplication.translate("MainWindow", u"Write subtitles", None))
        self.checkBox_36.setText(QCoreApplication.translate("MainWindow", u"Convert format", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"srt", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"ass", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("MainWindow", u"vtt", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("MainWindow", u"lrc", None))

        self.checkBox_38.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"srt", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"ass", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("MainWindow", u"vtt", None))
        self.comboBox_8.setItemText(3, QCoreApplication.translate("MainWindow", u"lrc", None))

        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.checkBox_37.setText(QCoreApplication.translate("MainWindow", u"Write auto-sub", None))
        self.checkBox_39.setText(QCoreApplication.translate("MainWindow", u"Embed subtitles", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Meatdata", None))
        self.checkBox_41.setText(QCoreApplication.translate("MainWindow", u"Embed chapters", None))
        self.checkBox_42.setText(QCoreApplication.translate("MainWindow", u"Embed info.json", None))
        self.checkBox_40.setText(QCoreApplication.translate("MainWindow", u"Embed metadata", None))
        self.checkBox_43.setText(QCoreApplication.translate("MainWindow", u"Write xattrs", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"Commands", None))
        self.toolButton_10.setText(QCoreApplication.translate("MainWindow", u"Run\n"
"--list-formats", None))
        self.toolButton_9.setText(QCoreApplication.translate("MainWindow", u"Run\n"
"--list-subs", None))
        self.toolButton_8.setText(QCoreApplication.translate("MainWindow", u"Run\n"
"--list-thumbnails", None))
        self.toolButton_11.setText(QCoreApplication.translate("MainWindow", u"Run\n"
"--list-extractors", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_spices), QCoreApplication.translate("MainWindow", u"Spices", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Return Youtube Dislikes", None))
        self.checkBox_46.setText(QCoreApplication.translate("MainWindow", u"Add a Youtube Dislike count to Youtube video metadata", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\ud83d\udec8 Uses <a href=\"https://github.com/pukkandan/yt-dlp-ReturnYoutubeDislike\"><span style=\" text-decoration: underline; color:#0000ff;\">yt-dlp-ReturnYoutubeDislike plugin</span></a>. Then use <span style=\" font-weight:600;\">%(dislike_count)s<br/></span>Updated info fields: like_count, dislike_count, average_rating, view_count<br/>The original values of those fields and the response from the API are saved<br/>under <span style=\" font-weight:600;\">RYD</span> key in the info dict</p></body></html>", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Don't lock", None))
        self.checkBox_49.setText(QCoreApplication.translate("MainWindow", u"Keep awake during yt-dlp's execution", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\ud83d\udec8 Uses <a href=\"https://github.com/Grub4K/yt-dont-lock-p\"><span style=\" text-decoration: underline; color:#0000ff;\">yt-dont-lock-p plugin<br/></span></a>Only applies to yt-dlp's execution</p><p>\ud83d\udec8 Doesn't apply to <span style=\" text-decoration: underline;\">Extra processing</span><br/>Use <span style=\" text-decoration: underline;\">Behavior</span> for that</p></body></html>", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Internet shortcut", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u".url Windows", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u".webloc macOS", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Current platform", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u".desktop Linux", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"DeArrow", None))
        self.checkBox_47.setText(QCoreApplication.translate("MainWindow", u"Replace title", None))
        self.checkBox_48.setText(QCoreApplication.translate("MainWindow", u"Download thumbnail", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\ud83d\udec8 Uses <a href=\"https://github.com/QuantumWarpCode/yt-dlp-dearrow\"><span style=\" text-decoration: underline; color:#0000ff;\">yt-dlp-dearrow plugin</span></a>, replaces <span style=\" font-weight:600;\">%(title)s<br/></span>Access original with <span style=\" font-weight:600;\">%(original_title)s</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\ud83d\udec8 Manually download an additional thumbnail<br/>an image (webp) from <a href=\"https://wiki.sponsor.ajay.app/w/API_Docs/DeArrow#GET_/api/v1/getThumbnail\"><span style=\" text-decoration: underline; color:#0000ff;\">DeArrow's API</span></a></p></body></html>", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"SponsorBlock", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"Disable", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"Mark", None))
        self.checkBox_50.setText(QCoreApplication.translate("MainWindow", u"default", None))
        self.checkBox_52.setText(QCoreApplication.translate("MainWindow", u"chapter", None))
        self.checkBox_51.setText(QCoreApplication.translate("MainWindow", u"all", None))
        self.checkBox_53.setText(QCoreApplication.translate("MainWindow", u"sponsor", None))
        self.checkBox_54.setText(QCoreApplication.translate("MainWindow", u"intro", None))
        self.checkBox_55.setText(QCoreApplication.translate("MainWindow", u"outro", None))
        self.checkBox_56.setText(QCoreApplication.translate("MainWindow", u"selfpromo", None))
        self.checkBox_57.setText(QCoreApplication.translate("MainWindow", u"preview", None))
        self.checkBox_58.setText(QCoreApplication.translate("MainWindow", u"filler", None))
        self.checkBox_59.setText(QCoreApplication.translate("MainWindow", u"interaction", None))
        self.checkBox_60.setText(QCoreApplication.translate("MainWindow", u"music_offtopic", None))
        self.checkBox_61.setText(QCoreApplication.translate("MainWindow", u"poi_highlight", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_miscellaneous), QCoreApplication.translate("MainWindow", u"Miscellaneous", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Cookies", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Container", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Read and dump cookie jar in", None))
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"deselected (windows)", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"gnomekeyring", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"basictext", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"kwallet", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"kwallet5", None))
        self.comboBox_5.setItemText(5, QCoreApplication.translate("MainWindow", u"kwallet6", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Keyring", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Read from browser", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"chrome", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"firefox", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"edge", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"brave", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"safari", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"chromium", None))
        self.comboBox_4.setItemText(6, QCoreApplication.translate("MainWindow", u"vivaldi", None))
        self.comboBox_4.setItemText(7, QCoreApplication.translate("MainWindow", u"whale", None))

        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Miscellaneous", None))
        self.checkBox_22.setText(QCoreApplication.translate("MainWindow", u"Retrieve video comments\n"
"to be placed in the infojson", None))
        self.checkBox_18.setText(QCoreApplication.translate("MainWindow", u"Do not use .part files -\n"
"write directly into output file", None))
        self.checkBox_19.setText(QCoreApplication.translate("MainWindow", u"Do not use the Last-modified\n"
"header to set the file\n"
"modification time", None))
        self.checkBox_20.setText(QCoreApplication.translate("MainWindow", u"Write video description to a\n"
".description file", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"Force filenames to be\n"
"Windows-compatible", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"Restrict filenames to only\n"
"ASCII characters, and\n"
"avoid \"&&\" and spaces", None))
        self.checkBox_17.setText(QCoreApplication.translate("MainWindow", u"Do not resume partially\n"
"downloaded fragments", None))
        self.checkBox_15.setText(QCoreApplication.translate("MainWindow", u"Do not overwrite any files", None))
        self.checkBox_16.setText(QCoreApplication.translate("MainWindow", u"Force overwrite all\n"
"video and metadata files", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u"Limit the filename length\n"
"(excluding extension) to", None))
        self.checkBox_21.setText(QCoreApplication.translate("MainWindow", u"Write video metadata to a\n"
".info.json file", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_filesystem), QCoreApplication.translate("MainWindow", u"Filesystem", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Simulation", None))
        self.checkBox_23.setText(QCoreApplication.translate("MainWindow", u"No simulation (Download\n"
"the video even if\n"
"printing/listing options\n"
"are used)", None))
        self.checkBox_24.setText(QCoreApplication.translate("MainWindow", u"Do not download the video\n"
"but write all related files", None))
        self.checkBox_25.setText(QCoreApplication.translate("MainWindow", u"Ignore \"No video formats\"", None))
        self.checkBox_26.setText(QCoreApplication.translate("MainWindow", u"Force write archive", None))
        self.checkBox_27.setText(QCoreApplication.translate("MainWindow", u"Force simulation (Do not\n"
"download the video and\n"
"do not write any files)", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Workarounds", None))
        self.checkBox_28.setText(QCoreApplication.translate("MainWindow", u"HTTPS without SRFC 5746\n"
"secure renegotiation", None))
        self.checkBox_30.setText(QCoreApplication.translate("MainWindow", u"Sleep between requests", None))
        self.checkBox_29.setText(QCoreApplication.translate("MainWindow", u"No HTTPS certificate\n"
"validation", None))
        self.checkBox_31.setText(QCoreApplication.translate("MainWindow", u"Sleep each download", None))
#if QT_CONFIG(tooltip)
        self.spinBox_3.setToolTip(QCoreApplication.translate("MainWindow", u"minimum in seconds", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_3.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
#if QT_CONFIG(tooltip)
        self.spinBox_4.setToolTip(QCoreApplication.translate("MainWindow", u"maximum in seconds", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_4.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
#if QT_CONFIG(tooltip)
        self.spinBox_2.setToolTip(QCoreApplication.translate("MainWindow", u"in seconds", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_2.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Cache", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"Disable filesystem caching", None))
        self.toolButton_6.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"Delete all filesystem cache", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"Set cache dir where yt-dlp\n"
"can store downloaded\n"
"information permanently", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Download", None))
        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"B", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"K", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("MainWindow", u"M", None))
        self.comboBox_9.setItemText(3, QCoreApplication.translate("MainWindow", u"G", None))

        self.comboBox_10.setItemText(0, QCoreApplication.translate("MainWindow", u"B", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("MainWindow", u"K", None))
        self.comboBox_10.setItemText(2, QCoreApplication.translate("MainWindow", u"M", None))
        self.comboBox_10.setItemText(3, QCoreApplication.translate("MainWindow", u"G", None))

        self.checkBox_64.setText(QCoreApplication.translate("MainWindow", u"Assumed\n"
"throttled rate", None))
        self.checkBox_63.setText(QCoreApplication.translate("MainWindow", u"Maximum\n"
"download rate", None))
        self.checkBox_67.setText(QCoreApplication.translate("MainWindow", u"Retry sleep", None))
        self.checkBox_65.setText(QCoreApplication.translate("MainWindow", u"Retries (infinite\n"
"OR count)", None))
        self.checkBox_66.setText(QCoreApplication.translate("MainWindow", u"infinite", None))
#if QT_CONFIG(tooltip)
        self.spinBox_6.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.spinBox_6.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
        self.checkBox_68.setText(QCoreApplication.translate("MainWindow", u"Keep fragments after download", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_advanced), QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", u"PyMusicLooper (loop detection general settings)", None))
        self.doubleSpinBox_3.setSuffix(QCoreApplication.translate("MainWindow", u"x", None))
        self.checkBox_75.setText(QCoreApplication.translate("MainWindow", u"Min duration\n"
"multiplier", None))
        self.checkBox_78.setText(QCoreApplication.translate("MainWindow", u"Brute force", None))
        self.comboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"WAV", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"FLAC", None))
        self.comboBox_12.setItemText(2, QCoreApplication.translate("MainWindow", u"OGG", None))
        self.comboBox_12.setItemText(3, QCoreApplication.translate("MainWindow", u"MP3", None))

        self.checkBox_79.setText(QCoreApplication.translate("MainWindow", u"Override split or extend\n"
"output format", None))
#if QT_CONFIG(tooltip)
        self.doubleSpinBox_5.setToolTip(QCoreApplication.translate("MainWindow", u"Max", None))
#endif // QT_CONFIG(tooltip)
        self.doubleSpinBox_5.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
#if QT_CONFIG(tooltip)
        self.doubleSpinBox_4.setToolTip(QCoreApplication.translate("MainWindow", u"Min", None))
#endif // QT_CONFIG(tooltip)
        self.doubleSpinBox_4.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
        self.checkBox_76.setText(QCoreApplication.translate("MainWindow", u"Loop\n"
"durations", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"FFmpeg", None))
        self.checkBox_69.setText(QCoreApplication.translate("MainWindow", u"Run a pass of ffmpeg for each yt-dlpprocessed video", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://ffmpeg.org/documentation.html\"><span style=\" text-decoration: underline; color:#0000ff;\">FFmpeg's documentation</span></a></p><p>Output container</p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Input and ouput params are already provided as follows:<br/>&gt; ffmpeg <span style=\" font-weight:600;\">-i %(_filename)s </span>[...]<br/><span style=\" font-weight:600;\">%(_filename)s</span>_ffmpeg.<span style=\" font-weight:600;\">[Output container]</span></p></body></html>", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-filter:v scale=720:-1 -c:a copy", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"PyMusicLooper (export settings)", None))
        self.checkBox_74.setText(QCoreApplication.translate("MainWindow", u"Format exports as", None))
        self.radioButton_14.setText(QCoreApplication.translate("MainWindow", u"Tag the input file", None))
        self.checkBox_73.setText(QCoreApplication.translate("MainWindow", u"Top N loop points", None))
        self.checkBox_77.setText(QCoreApplication.translate("MainWindow", u"Override tag names", None))
        self.comboBox_11.setItemText(0, QCoreApplication.translate("MainWindow", u"SAMPLES", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("MainWindow", u"SECONDS", None))
        self.comboBox_11.setItemText(2, QCoreApplication.translate("MainWindow", u"TIME (mm:ss.sss)", None))

        self.lineEdit_14.setText(QCoreApplication.translate("MainWindow", u"LOOP_START", None))
        self.lineEdit_15.setText(QCoreApplication.translate("MainWindow", u"LOOP_END", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Interactive mode is not supported<br/>Only export commands is used</span></p></body></html>", None))
        self.checkBox_72.setText(QCoreApplication.translate("MainWindow", u"Run a pass of pymusiclooper for each yt-dlp processed video", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Extended length", None))
        self.doubleSpinBox_6.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/arkrow/PyMusicLooper/blob/master/CLI_README.md\"><span style=\" text-decoration: underline; color:#0000ff;\">Read PyMusicLopper's documentzation</span></a>.<br/>Input audio is already provided</p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Fade out duration", None))
        self.doubleSpinBox_7.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"Split the input file", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\ud83d\udec8 Split the input audio into intro,<br/><span style=\" font-weight:600;\">loop </span>and outro sections<br/>\ud83d\udec8 Play the <span style=\" font-weight:600;\">loop</span> section with<br/><a href=\"https://en.wikipedia.org/wiki/Gapless_playback\"><span style=\" text-decoration: underline; color:#0000ff;\">gapless playback</span></a> for immediate effect</p></body></html>", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"Export to text file", None))
        self.radioButton_15.setText(QCoreApplication.translate("MainWindow", u"Extends the input file", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_extra_processing), QCoreApplication.translate("MainWindow", u"Extra processing", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("MainWindow", u"AFK", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"While running", None))
        self.radioButton_21.setText(QCoreApplication.translate("MainWindow", u"Close this application", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"When done", None))
        self.radioButton_16.setText(QCoreApplication.translate("MainWindow", u"Keep PC running", None))
        self.radioButton_18.setText(QCoreApplication.translate("MainWindow", u"Restart PC", None))
        self.radioButton_17.setText(QCoreApplication.translate("MainWindow", u"Turn off PC", None))
        self.checkBox_80.setText(QCoreApplication.translate("MainWindow", u"Keep PC awake", None))
        self.radioButton_19.setText(QCoreApplication.translate("MainWindow", u"Run command", None))
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"curl -i -H \"Accept: application/json\" -H \"Content-Type:application/json\" -X POST --data \"{\"content\": \"shiny-adventure\"}\" discord-webhook-link", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("MainWindow", u"Workers", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"yt-dlp workers", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Extra processing workers", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\ud83d\udec8 Not implemented</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_behavior), QCoreApplication.translate("MainWindow", u"Behavior", None))
        self.groupBox_status.setTitle(QCoreApplication.translate("MainWindow", u"Status", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_About.setTitle(QCoreApplication.translate("MainWindow", u"&About", None))
    # retranslateUi

