'''
VIDEO STREAM OUTPUT PANEL
'''


from PyQt5 import QtCore, QtGui, QtWidgets


class Face_Recognition_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 849)
        MainWindow.setStyleSheet("background: #004D40")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 571, 511))
        self.label.setText("")
        self.label.setObjectName("label")

        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(110, 550, 81, 31))
        # self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n""color:white;\n""")
        # self.label_2.setObjectName("label_2")

        # self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(460, 600, 81, 31))
        # self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n""color:white;\n""")
        # self.label_3.setObjectName("label_3")

        # self.label_4 = QtWidgets.QLabel(self.centralwidget)
        # self.label_4.setGeometry(QtCore.QRect(460, 550, 81, 31))
        # self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n""color:white;\n""")
        # self.label_4.setObjectName("label_4")

        # self.label_5 = QtWidgets.QLabel(self.centralwidget)
        # self.label_5.setGeometry(QtCore.QRect(110, 650, 81, 31))
        # self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n""color:white;\n""")
        # self.label_5.setObjectName("label_5")

        # self.label_6 = QtWidgets.QLabel(self.centralwidget)
        # self.label_6.setGeometry(QtCore.QRect(110, 600, 81, 31))
        # self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n""color:white;\n""")
        # self.label_6.setObjectName("label_6")

        # self.label_7 = QtWidgets.QLabel(self.centralwidget)
        # self.label_7.setGeometry(QtCore.QRect(460, 650, 81, 31))
        # self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n""color:white;\n""")
        # self.label_7.setObjectName("label_7")

        # self.label_8 = QtWidgets.QLabel(self.centralwidget)
        # self.label_8.setGeometry(QtCore.QRect(110, 700, 81, 31))
        # self.label_8.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n""color:white;\n""")
        # self.label_8.setObjectName("label_8")

        # self.label_9 = QtWidgets.QLabel(self.centralwidget)
        # self.label_9.setGeometry(QtCore.QRect(460, 750, 81, 31))
        # self.label_9.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n""color:white;\n""")
        # self.label_9.setObjectName("label_9")

        # self.label_10 = QtWidgets.QLabel(self.centralwidget)
        # self.label_10.setGeometry(QtCore.QRect(110, 750, 81, 31))
        # self.label_10.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n""color:white;\n""")
        # self.label_10.setObjectName("label_10")

        # self.label_11 = QtWidgets.QLabel(self.centralwidget)
        # self.label_11.setGeometry(QtCore.QRect(460, 700, 81, 31))
        # self.label_11.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n""color:white;\n""")
        # self.label_11.setObjectName("label_11")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 26))
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
        # self.label_2.setText(_translate("MainWindow", "Employee"))
        # self.label_3.setText(_translate("MainWindow", "jaskld"))
        # self.label_4.setText(_translate("MainWindow", "Employee Name"))
        # self.label_5.setText(_translate("MainWindow", "jaskld"))
        # self.label_6.setText(_translate("MainWindow", "jaskld"))
        # self.label_7.setText(_translate("MainWindow", "jaskld"))
        # self.label_8.setText(_translate("MainWindow", "jaskld"))
        # self.label_9.setText(_translate("MainWindow", "jaskld"))
        # self.label_10.setText(_translate("MainWindow", "jaskld"))
        # self.label_11.setText(_translate("MainWindow", "jaskld"))
