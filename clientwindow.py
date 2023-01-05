# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import socket
import threading
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 690)
        MainWindow.setMinimumSize(QtCore.QSize(442, 690))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 441, 171))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 441, 145))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setEnabled(True)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setStyleSheet("margin-bottom:0;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("127.0.0.1")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setEnabled(True)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setMaximum(65000)
        self.spinBox.setValue(8001)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.spinBox)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.pressed.connect(lambda: self.login(self.lineEdit.text(),self.spinBox.value()))
        self.verticalLayout.addWidget(self.pushButton)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 170, 441, 521))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QtCore.QRect(0, 20, 441, 471))
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 490, 441, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.pressed.connect(lambda: self.write(self.lineEdit_2.text()))
        self.horizontalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Client Chat"))
        self.groupBox.setTitle(_translate("MainWindow", "Server Settings"))
        self.label.setText(_translate("MainWindow", "IP:"))
        self.label_2.setText(_translate("MainWindow", "PORT:"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Chat"))
        self.pushButton_2.setText(_translate("MainWindow", "Send"))

    def login(self,IP,PORT):
        self.pushButton.setEnabled = False
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Connect to a host
        nickname = "Alex"
        client.connect((IP,PORT))
        self.client = client
        recieve_thread = threading.Thread(target=self.recieve, args=(client,nickname))
        recieve_thread.start()

    def recieve(self, client, nickname):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    client.send(nickname.encode('utf-8'))
                else:
                    self.textEdit.append(message)
                    print(message)
            except:
                print('Error Occured while Connecting')
                client.close()
                break
        
    def write(self,message):
        self.client.send(message.encode('utf-8'))