'''
MAIN PAGE UI
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor

buttonStyle = '''
                QPushButton{
                        border-radius: 35px;
                        background: #00897B;
                        color: white;
                        font-size: 18px
                }
                
                QPushButton:hover{
                        background: #4DB6AC;
                }
                '''

class Main_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(495, 497)
        MainWindow.setStyleSheet("background: #004D40")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 130, 241, 71))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(buttonStyle)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 220, 241, 71))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(buttonStyle)
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 310, 241, 71))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(buttonStyle)
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 391, 61))
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n""color: #E0F2F1;\n""background: transparent")
        self.label.setObjectName("label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome"))
        self.pushButton.setText(_translate("MainWindow", "Face Recognition"))
        self.pushButton_2.setText(_translate("MainWindow", "Activity Recognition"))
        self.label.setText(_translate("MainWindow", "Welcome Mutahhar Ahmad"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit"))
