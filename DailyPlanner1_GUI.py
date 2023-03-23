# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DailyPlanner1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 504)
        MainWindow.setStyleSheet("background-color: rgb(176, 152, 65);\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 511, 61))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(242, 255, 183);\n"
"  border-radius: 25px;\n"
"font: 24pt \"Algerian\";\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(30, 110, 511, 321))
        self.calendar.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(242, 255, 183);\n"
"color: rgb(0, 0, 0);\n"
"  border-radius: 25px;\n"
"\n"
"")
        self.calendar.setObjectName("calendar")
        self.listTask = QtWidgets.QListWidget(self.centralwidget)
        self.listTask.setGeometry(QtCore.QRect(570, 150, 291, 231))
        self.listTask.setStyleSheet("background-color: rgb(242, 255, 183);\n"
"  border-radius: 10px;\n"
"")
        self.listTask.setObjectName("listTask")
        self.lblDate = QtWidgets.QLabel(self.centralwidget)
        self.lblDate.setGeometry(QtCore.QRect(580, 105, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblDate.setFont(font)
        self.lblDate.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(242, 255, 183);\n"
"color: rgb(0, 0, 0);\n"
"  border-radius: 10px;\n"
"")
        self.lblDate.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDate.setObjectName("lblDate")
        self.lblImage = QtWidgets.QLabel(self.centralwidget)
        self.lblImage.setGeometry(QtCore.QRect(630, -20, 161, 121))
        self.lblImage.setText("")
        self.lblImage.setPixmap(QtGui.QPixmap("images/353600404c3228d8577957d01f06a101_1.gif"))
        self.lblImage.setScaledContents(True)
        self.lblImage.setObjectName("lblImage")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(570, 390, 295, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAddTask = QtWidgets.QPushButton(self.layoutWidget)
        self.btnAddTask.setStyleSheet("background-color: rgb(242, 255, 183);\n"
"\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"")
        self.btnAddTask.setObjectName("btnAddTask")
        self.horizontalLayout.addWidget(self.btnAddTask)
        self.btnUpdateTask = QtWidgets.QPushButton(self.layoutWidget)
        self.btnUpdateTask.setStyleSheet("background-color: rgb(242, 255, 183);\n"
"\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"")
        self.btnUpdateTask.setObjectName("btnUpdateTask")
        self.horizontalLayout.addWidget(self.btnUpdateTask)
        self.btnDeleteTask = QtWidgets.QPushButton(self.layoutWidget)
        self.btnDeleteTask.setStyleSheet("background-color: rgb(242, 255, 183);\n"
"\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"")
        self.btnDeleteTask.setObjectName("btnDeleteTask")
        self.horizontalLayout.addWidget(self.btnDeleteTask)
        self.layoutWidget.raise_()
        self.lblImage.raise_()
        self.label.raise_()
        self.calendar.raise_()
        self.listTask.raise_()
        self.lblDate.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 906, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Daily Planner"))
        self.lblDate.setText(_translate("MainWindow", "Date"))
        self.btnAddTask.setToolTip(_translate("MainWindow", "<html><head/><body><p>To Add Task click the Button</p></body></html>"))
        self.btnAddTask.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.btnAddTask.setText(_translate("MainWindow", "Add Task"))
        self.btnUpdateTask.setText(_translate("MainWindow", "Update Task"))
        self.btnDeleteTask.setText(_translate("MainWindow", "Delete Task"))
