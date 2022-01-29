import asyncio
import threading, time, os, json, sys
from copy import deepcopy

from PySide6.QtCore import QObject, QThread, Signal, Slot, QFile
from PySide6.QtWidgets import QWidgetItem, QListWidget, QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget, \
    QLabel, QWidgetItem, QListWidgetItem, QComboBox
from selenium import webdriver
from selenium.webdriver.common.by import By
from bilibili_api import live, sync
from bilibili_api.user import User
from LTB_Config import LTB_Config
from ui_mainwindow import Ui_Widget

spacer = ":"


class MainForm(Ui_Widget):
    room_id = 737562
    room = live.LiveDanmaku(room_id)
    start_button_pressed = False

    def __init__(self):
        super(Ui_Widget, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("LTB_PYTHON")

        # connect all buttons
        self.ui.button_addRoom.clicked.connect(self.button_addRoom)
        self.ui.button_updatePort.clicked.connect(self.button_updatePort)
        self.ui.button_SelectRoom.clicked.connect(self.button_SelectRoom)
        self.ui.button_startButton.clicked.connect(self.button_StartButton)

        # new rooms can be added here for now
        self.ui.listWidget_roomList.addItem("互殴1房" + spacer + "737562")
        self.ui.listWidget_roomList.addItem("互殴2房" + spacer + "23982147")
        self.ui.listWidget_roomList.addItem("修勾夜店" + spacer + "3645373")

    def button_addRoom(self):
        # not to be supported in this session
        print("not to be supported in this session")

    def button_SelectRoom(self):
        room_id_text = self.ui.listWidget_roomList.selectedItems()[0].text()
        room_id_start_index = room_id_text.find(":") + 1
        room_id = int(room_id_text[room_id_start_index:])
        print(room_id)
        self.room_id = room_id

    def button_updatePort(self):
        print("implement me ")

    def button_StartButton(self):
        print("start button")
        self.start_button_pressed = True
        # self.room = live.LiveDanmaku(self.room_id)
        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)
        # tasks = [self.room.connect()]
        # loop.run_until_complete(asyncio.wait(tasks))
        my_room_thread = threading.Thread(target=self.room_thread)
        my_room_thread.daemon = True
        my_room_thread.start()
        print("end of function")
        print(self.start_button_pressed)

    def room_thread(self):
        self.room = live.LiveDanmaku(self.room_id)
        sync(self.room.connect())


@MainForm.room.on('ALL')
async def All_msg(self, event):
    print(event)


async def qt_ui():
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec())



if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = [qt_ui()]
    loop.run_until_complete(asyncio.wait(tasks))
    # app = QApplication(sys.argv)
    # window = MainForm()
    # window.show()
    # sys.exit(app.exec())
