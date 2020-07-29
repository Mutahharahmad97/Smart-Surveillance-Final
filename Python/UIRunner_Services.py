'''
THIS IS THE MAIN SCRIPT TO RUN THE USER INTERFACE

MADE BY MUTAHHAR AHMAD
'''

import sys
import cv2
from UI.MainPage import *
from UI.FaceRecognition import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from API import API
from API.ttypes import *
import numpy as np
import os
import requests
import time

class MainWindow(QtWidgets.QMainWindow):
    # EXIT THE PROGRAM
    def exit_(self):
        sys.exit()
        cv2.destroyAllWindows()
        
    def Uniform_Recognition_(self, frame):
        
        ret, image = cv2.imencode('.jpg', frame)
        
        payload = {"image": image}
        r = requests.post(UR_Service_Url, files=payload).json()

        cv2.putText(frame, r['color'], (10, r['position'][0] + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, r['type'], (10, r['position'][1] + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        color = ((r['color'].split(':'))[0])
            
        return frame,color
        
    def Face_Recognition_(self,frame):
        face_names = []
        face_titles = []
        
        ret, image = cv2.imencode('.jpg', frame)
        
        payload = {"image": image}
        r = requests.post(FR_Service_Url, files=payload).json()
        
        for(name,title,top,right,bottom,left) in r['faces']:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name+ ": " + title, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            face_names.append(name)
            face_titles.append(title)
        
        return frame,face_names,face_titles
    
    # FOR DISPLAYING THE NEXT FRAME ON THE UI AFTER PROCESSING
    def nextFrameSlot(self):
        ret, frame = self.vc.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        uniform_Recognition_Frame = frame.copy()
        
        frame,names,titles = self.Face_Recognition_(frame)
        uniform_Recognition_Frame,color = self.Uniform_Recognition_(uniform_Recognition_Frame)
        
        # message = 'alert'
        # r = requests.get(UR_Service_Url + '?message=' + message).json()
        # if(r['status'] == 'Ok'):
        #    continue
        
        for name in names:
            if not client.isOneAnEmployee(name):
                print('Unknown Employee Detected')
                continue
                
            if not client.shouldOneBeHere(name, '47'):
                print(name+ ' is at wrong zone')
                continue
                
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            
            if not client.isShiftValid(name, str(current_time)):
                print(name + ' shift is not valid')
                continue
                
            if not client.isUniformValid(name,color):
                print(name + ' uniform invalid')
                continue
            
        frame = cv2.add(frame,uniform_Recognition_Frame)
        
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(image)
        self.ui.label.setPixmap(pixmap)
        
    # OPENING THE VIDEO STREAM VIDEO
    def FRWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Face_Recognition_Window()
        self.ui.setupUi(self.window)
        self.window.show()
        
        self.vc = cv2.VideoCapture(0)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000./24)
        
    # MAIN WINDOW
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        
        self.ui = Main_Window()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.FRWindow)
        self.ui.pushButton_2.clicked.connect(self.FRWindow)
        self.ui.pushButton_3.clicked.connect(self.exit_)


# Face Recognition Service
FR_Service_Url = 'http://localhost:8000/faceRecognition/'

# Uniform Recognition Service
UR_Service_Url = 'http://localhost:8000/uniformRecognition/'

# Email Sending Service
ES_Service_Url = 'http://localhost:8000/EmailSender'

try:
  transport = TSocket.TSocket('localhost', 9090)
  transport = TTransport.TBufferedTransport(transport)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = API.Client(protocol)
  transport.open()
  
except:
    print('Couldn\'t find server at port')
    exit()
    

# RUN THE APPLICATION
app = QtWidgets.QApplication(sys.argv)
myApp = MainWindow()
myApp.show()
sys.exit(app.exec_())
