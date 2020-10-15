# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from Model.config import AWK_FILE_NAME, BTN_FILE_NAME

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(608, 658)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(50, 90, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(25, 90, 150, 85))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(AWK_FILE_NAME))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.btn_awk_clear = QtWidgets.QPushButton(self.groupBox)
        self.btn_awk_clear.setGeometry(QtCore.QRect(15, 40, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_awk_clear.setFont(font)
        self.btn_awk_clear.setObjectName("btn_awk_clear")
        self.btn_awk_set = QtWidgets.QPushButton(self.groupBox)
        self.btn_awk_set.setGeometry(QtCore.QRect(115, 40, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_awk_set.setFont(font)
        self.btn_awk_set.setObjectName("btn_awk_set")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(350, 90, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(25, 90, 150, 85))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(BTN_FILE_NAME))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.btn_awk_clear_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_awk_clear_2.setGeometry(QtCore.QRect(15, 40, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_awk_clear_2.setFont(font)
        self.btn_awk_clear_2.setObjectName("btn_awk_clear_2")
        self.btn_awk_set_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_awk_set_2.setGeometry(QtCore.QRect(115, 40, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_awk_set_2.setFont(font)
        self.btn_awk_set_2.setObjectName("btn_awk_set_2")
        self.btn_clear_stats = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear_stats.setGeometry(QtCore.QRect(510, 775, 75, 25))
        self.btn_clear_stats.setObjectName("btn_clear_stats")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 300, 381, 331))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cbx_stat = QtWidgets.QComboBox(self.frame)
        self.cbx_stat.setGeometry(QtCore.QRect(10, 20, 70, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_stat.sizePolicy().hasHeightForWidth())
        self.cbx_stat.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cbx_stat.setFont(font)
        self.cbx_stat.setObjectName("cbx_stat")
        self.cbx_stat.addItem("")
        self.sa_selected_stats = QtWidgets.QScrollArea(self.frame)
        self.sa_selected_stats.setGeometry(QtCore.QRect(10, 70, 250, 250))
        self.sa_selected_stats.setWidgetResizable(True)
        self.sa_selected_stats.setObjectName("sa_selected_stats")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 248, 248))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.sa_selected_stats.setWidget(self.scrollAreaWidgetContents)
        self.tdt_stat_value = QtWidgets.QTextEdit(self.frame)
        self.tdt_stat_value.setGeometry(QtCore.QRect(190, 20, 70, 30))
        self.tdt_stat_value.setObjectName("tdt_stat_value")
        self.btn_add_stat = QtWidgets.QPushButton(self.frame)
        self.btn_add_stat.setGeometry(QtCore.QRect(290, 70, 75, 25))
        self.btn_add_stat.setObjectName("btn_add_stat")
        self.cbx_sign = QtWidgets.QComboBox(self.frame)
        self.cbx_sign.setGeometry(QtCore.QRect(100, 20, 70, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_sign.sizePolicy().hasHeightForWidth())
        self.cbx_sign.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cbx_sign.setFont(font)
        self.cbx_sign.setObjectName("cbx_sign")
        self.cbx_sign.addItem("")
        self.btn_remove_stat = QtWidgets.QPushButton(self.frame)
        self.btn_remove_stat.setGeometry(QtCore.QRect(290, 115, 75, 25))
        self.btn_remove_stat.setObjectName("btn_remove_stat")
        self.btn_clear_stats_2 = QtWidgets.QPushButton(self.frame)
        self.btn_clear_stats_2.setGeometry(QtCore.QRect(290, 295, 75, 25))
        self.btn_clear_stats_2.setObjectName("btn_clear_stats_2")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(460, 390, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_start.setFont(font)
        self.btn_start.setObjectName("btn_start")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(460, 500, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_stop.setFont(font)
        self.btn_stop.setObjectName("btn_stop")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 60, 181, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Awakening Window"))
        self.btn_awk_clear.setText(_translate("MainWindow", "Clear"))
        self.btn_awk_set.setText(_translate("MainWindow", "Set"))
        self.label.setText(_translate("MainWindow", "~ FlyFF Awakening Bot ~"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Ok Button Window"))
        self.btn_awk_clear_2.setText(_translate("MainWindow", "Clear"))
        self.btn_awk_set_2.setText(_translate("MainWindow", "Set"))
        self.btn_clear_stats.setText(_translate("MainWindow", "Clear"))
        self.cbx_stat.setItemText(0, _translate("MainWindow", "Speed"))
        self.btn_add_stat.setText(_translate("MainWindow", "Add"))
        self.cbx_sign.setItemText(0, _translate("MainWindow", ">="))
        self.btn_remove_stat.setText(_translate("MainWindow", "Remove"))
        self.btn_clear_stats_2.setText(_translate("MainWindow", "Clear"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.label_4.setText(_translate("MainWindow", "by Matan ameleh"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))


