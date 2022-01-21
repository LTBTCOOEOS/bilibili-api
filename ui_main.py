import threading, time, os, json, sys
from PySide6.QtCore import QObject, QThread, Signal, Slot, QFile
from PySide6.QtWidgets import QWidgetItem, QListWidget, QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget, \
    QLabel, QWidgetItem, QListWidgetItem, QComboBox
from ui_mainwindow import Ui_Widget

class MainForm(Ui_Widget):
    def __init__(self):
        super(Ui_Widget, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("LTB_PYTHON")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec())
