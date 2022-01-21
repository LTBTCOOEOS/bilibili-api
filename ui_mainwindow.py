# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget, QMainWindow)

class Ui_Widget(QMainWindow):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(621, 361)
        self.verticalLayoutWidget = QWidget(Widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(320, 10, 251, 181))
        self.verticalLayout_checkBoxGroup = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_checkBoxGroup.setObjectName(u"verticalLayout_checkBoxGroup")
        self.verticalLayout_checkBoxGroup.setContentsMargins(0, 0, 0, 0)
        self.static_checkBoxGroupName = QLabel(self.verticalLayoutWidget)
        self.static_checkBoxGroupName.setObjectName(u"static_checkBoxGroupName")
        self.static_checkBoxGroupName.setEnabled(True)
        font = QFont()
        font.setPointSize(22)
        self.static_checkBoxGroupName.setFont(font)
        self.static_checkBoxGroupName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_checkBoxGroup.addWidget(self.static_checkBoxGroupName)

        self.checkBox_enableTop3BossData = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_enableTop3BossData.setObjectName(u"checkBox_enableTop3BossData")
        font1 = QFont()
        font1.setPointSize(20)
        self.checkBox_enableTop3BossData.setFont(font1)
        self.checkBox_enableTop3BossData.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_enableTop3BossData.setIconSize(QSize(20, 20))

        self.verticalLayout_checkBoxGroup.addWidget(self.checkBox_enableTop3BossData)

        self.checkBox_enableNormalData = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_enableNormalData.setObjectName(u"checkBox_enableNormalData")
        self.checkBox_enableNormalData.setFont(font1)
        self.checkBox_enableNormalData.setIconSize(QSize(20, 20))

        self.verticalLayout_checkBoxGroup.addWidget(self.checkBox_enableNormalData)

        self.checkBox_enableFaces = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_enableFaces.setObjectName(u"checkBox_enableFaces")
        self.checkBox_enableFaces.setFont(font1)
        self.checkBox_enableFaces.setIconSize(QSize(20, 20))

        self.verticalLayout_checkBoxGroup.addWidget(self.checkBox_enableFaces)

        self.checkBox_enableFaces_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_enableFaces_2.setObjectName(u"checkBox_enableFaces_2")
        self.checkBox_enableFaces_2.setFont(font1)
        self.checkBox_enableFaces_2.setIconSize(QSize(20, 20))

        self.verticalLayout_checkBoxGroup.addWidget(self.checkBox_enableFaces_2)

        self.button_startButton = QPushButton(Widget)
        self.button_startButton.setObjectName(u"button_startButton")
        self.button_startButton.setGeometry(QRect(320, 290, 251, 51))
        self.lineEdit_roomID = QLineEdit(Widget)
        self.lineEdit_roomID.setObjectName(u"lineEdit_roomID")
        self.lineEdit_roomID.setGeometry(QRect(20, 50, 81, 31))
        self.horizontalLayoutWidget = QWidget(Widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 90, 251, 31))
        self.horizontalLayout_currentRoom = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_currentRoom.setObjectName(u"horizontalLayout_currentRoom")
        self.horizontalLayout_currentRoom.setContentsMargins(0, 0, 0, 0)
        self.static_CurrentRoom = QLabel(self.horizontalLayoutWidget)
        self.static_CurrentRoom.setObjectName(u"static_CurrentRoom")

        self.horizontalLayout_currentRoom.addWidget(self.static_CurrentRoom)

        self.label_CurrentRoom = QLabel(self.horizontalLayoutWidget)
        self.label_CurrentRoom.setObjectName(u"label_CurrentRoom")

        self.horizontalLayout_currentRoom.addWidget(self.label_CurrentRoom)

        self.lineEdit_port = QLineEdit(Widget)
        self.lineEdit_port.setObjectName(u"lineEdit_port")
        self.lineEdit_port.setGeometry(QRect(320, 250, 111, 31))
        self.horizontalLayoutWidget_2 = QWidget(Widget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(320, 210, 251, 31))
        self.horizontalLayout_currentPort = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_currentPort.setObjectName(u"horizontalLayout_currentPort")
        self.horizontalLayout_currentPort.setContentsMargins(0, 0, 0, 0)
        self.static_CurrentPort = QLabel(self.horizontalLayoutWidget_2)
        self.static_CurrentPort.setObjectName(u"static_CurrentPort")

        self.horizontalLayout_currentPort.addWidget(self.static_CurrentPort)

        self.label_CurrentPort = QLabel(self.horizontalLayoutWidget_2)
        self.label_CurrentPort.setObjectName(u"label_CurrentPort")

        self.horizontalLayout_currentPort.addWidget(self.label_CurrentPort)

        self.button_SelectRoom = QPushButton(Widget)
        self.button_SelectRoom.setObjectName(u"button_SelectRoom")
        self.button_SelectRoom.setGeometry(QRect(20, 310, 241, 31))
        self.button_updatePort = QPushButton(Widget)
        self.button_updatePort.setObjectName(u"button_updatePort")
        self.button_updatePort.setGeometry(QRect(440, 250, 131, 31))
        self.listWidget_roomList = QListWidget(Widget)
        self.listWidget_roomList.setObjectName(u"listWidget_roomList")
        self.listWidget_roomList.setGeometry(QRect(20, 130, 261, 171))
        self.lineEdit_roomName = QLineEdit(Widget)
        self.lineEdit_roomName.setObjectName(u"lineEdit_roomName")
        self.lineEdit_roomName.setGeometry(QRect(110, 50, 81, 31))
        self.button_addRoom = QPushButton(Widget)
        self.button_addRoom.setObjectName(u"button_addRoom")
        self.button_addRoom.setGeometry(QRect(200, 50, 71, 31))
        self.horizontalLayoutWidget_3 = QWidget(Widget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(20, 10, 181, 31))
        self.horizontalLayout_Static_room = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_Static_room.setObjectName(u"horizontalLayout_Static_room")
        self.horizontalLayout_Static_room.setContentsMargins(0, 0, 0, 0)
        self.static_roomID = QLabel(self.horizontalLayoutWidget_3)
        self.static_roomID.setObjectName(u"static_roomID")

        self.horizontalLayout_Static_room.addWidget(self.static_roomID)

        self.static_roomName = QLabel(self.horizontalLayoutWidget_3)
        self.static_roomName.setObjectName(u"static_roomName")

        self.horizontalLayout_Static_room.addWidget(self.static_roomName)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.static_checkBoxGroupName.setText(QCoreApplication.translate("Widget", u"Enabled functions", None))
        self.checkBox_enableTop3BossData.setText(QCoreApplication.translate("Widget", u"enableTop3BossData", None))
        self.checkBox_enableNormalData.setText(QCoreApplication.translate("Widget", u"enableNormalData", None))
        self.checkBox_enableFaces.setText(QCoreApplication.translate("Widget", u"enableFaces", None))
        self.checkBox_enableFaces_2.setText(QCoreApplication.translate("Widget", u"enablePresistData", None))
        self.button_startButton.setText(QCoreApplication.translate("Widget", u"StartButton", None))
        self.lineEdit_roomID.setText("")
        self.static_CurrentRoom.setText(QCoreApplication.translate("Widget", u"CurrentRoom", None))
        self.label_CurrentRoom.setText(QCoreApplication.translate("Widget", u"6", None))
        self.static_CurrentPort.setText(QCoreApplication.translate("Widget", u"CurrentPort", None))
        self.label_CurrentPort.setText(QCoreApplication.translate("Widget", u"60000", None))
        self.button_SelectRoom.setText(QCoreApplication.translate("Widget", u"SelectRoom", None))
        self.button_updatePort.setText(QCoreApplication.translate("Widget", u"updatePort", None))
        self.button_addRoom.setText(QCoreApplication.translate("Widget", u"addRoom", None))
        self.static_roomID.setText(QCoreApplication.translate("Widget", u"roomID", None))
        self.static_roomName.setText(QCoreApplication.translate("Widget", u"roomName", None))
    # retranslateUi
