from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import time
import pickle
from face_recognition import face_recognition

class Ui_mainWindow(object):
    def Exit(self):
        exit()
    
    def face_Encode(self):
        name = self.textEdit.toPlainText()
        title = self.textEdit_2.toPlainText()
        encodingsBox = []
        namesBox = []
        titlesBox = []
        
        cap = cv2.VideoCapture(0)
        time.sleep(1)
        while True:
            ret, frame = cap.read()
            if ret == True:
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                boxes = face_recognition.face_locations(rgb_frame, model="hog")
                encodings = face_recognition.face_encodings(rgb_frame, boxes)
                
                for encoding in encodings:
                    encodingsBox.append(encoding)
                    namesBox.append(name)
                    titlesBox.append(title)

                cv2.imshow("Frame", frame)
                if cv2.waitKey(1) == 27 & 0xff:
                    break

        data = {'encodings': encodingsBox, 'names': namesBox, 'titles': titlesBox}
        f = open("Models/encodings.pickle", "wb")
        f.write(pickle.dumps(data))
        f.close()
        cap.release()
        cv2.destroyAllWindows()
    
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(495, 499)
        mainWindow.setStyleSheet("background-color: #004D40")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 150, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 210, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white\n"
"")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(250, 150, 211, 31))
        self.textEdit.setStyleSheet("color: white")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(250, 210, 211, 31))
        self.textEdit_2.setStyleSheet("color: white")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 280, 241, 71))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("border-radius: 35px;\n"
"background: #00897B;\n"
"color: white;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 370, 241, 71))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("\n"
"border-radius: 35px;\n"
"background: #00897B;\n"
"color: white")
        self.pushButton_3.setObjectName("pushButton_3")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        
        self.pushButton.clicked.connect(self.face_Encode)
        self.pushButton_3.clicked.connect(self.Exit)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label.setText(_translate("mainWindow", "Employee Name:"))
        self.label_4.setText(_translate("mainWindow", "Title:"))
        self.label_2.setText(_translate("mainWindow", "Welcome to Training"))
        self.pushButton.setText(_translate("mainWindow", "Proceed"))
        self.pushButton_3.setText(_translate("mainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
