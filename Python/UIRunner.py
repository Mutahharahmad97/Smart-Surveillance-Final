'''
THIS IS THE MAIN SCRIPT TO RUN THE USER INTERFACE

MADE BY MUTAHHAR AHMAD
'''

from face_recognition import face_recognition
import sys
import cv2
import pickle
from UI.MainPage import *
from UI.FaceRecognition import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from API import API
from API.ttypes import *
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import imutils
import os
import time

class MainWindow(QtWidgets.QMainWindow):
    # EXIT THE PROGRAM
    def exit_(self):
        sys.exit()
        cv2.destroyAllWindows()
        
    def Uniform_Recognition_(self, frame):
        image = cv2.resize(frame, (96, 96))
        image = image.astype("float") / 255.0
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        
        proba = model.predict(image)[0]
        idxs = np.argsort(proba)[::-1][:2]
        
        for (i, j) in enumerate(idxs):
            label = "{}: {:.2f}%".format(mlb.classes_[j], proba[j] * 100)
            cv2.putText(frame, label, (10, (i * 30) + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
        return frame
        
    def Face_Recognition_(self,frame):
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        face_titles = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(knownFE, face_encoding)
            name = "Unknown"
            title = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = knownN[first_match_index]
                title = knownT[first_match_index]

            face_names.append(name)
            face_titles.append(title)
        
        for (top, right, bottom, left), name,title in zip(face_locations, face_names, face_titles):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name+ ": " + title, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
        return frame,face_names,face_titles
    
    # FOR DISPLAYING THE NEXT FRAME ON THE UI AFTER PROCESSING
    def nextFrameSlot(self):
        ret, frame = self.vc.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        uniform_Recognition_Frame = frame.copy()
        
        frame,names,titles = self.Face_Recognition_(frame)
        uniform_Recognition_Frame = self.Uniform_Recognition_(uniform_Recognition_Frame)
        
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
                
            if not client.isUniformValid(name,'blue'):
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


# OPEN THE FACE RECOGNITION PICKLE FILE
with open('Models/encodings.pickle', 'rb') as pickle_read:
    data = pickle.load(pickle_read)

# ENCODINGS AND NAMES FROM PICKLE FILE
knownFE = data['encodings']
knownN = data['names']
knownT = data['titles']

#OPEN MODELS FOR UNIFORM RECOGNITION
model = load_model(r"Models/fashion.model")
#OPEN MODELS FOR UNIFORM RECOGNITION
mlb = pickle.loads(open(r"Models/mlb.pickle", "rb").read())

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
