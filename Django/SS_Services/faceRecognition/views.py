from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import numpy as np
import urllib
import json
import cv2
import pickle
import os
from pathlib import Path
from . import face_recognition
from django.conf import settings

model = Path(settings.BASE_DIR + '/Models/encodings.pickle')
pickle_model = open(model, 'rb')
data = pickle.load(pickle_model)
# ENCODINGS AND NAMES FROM PICKLE FILE
knownFE = data['encodings']
knownN = data['names']
knownT = data['titles']


@csrf_exempt
def detect(request):        
    face_data = {'success' : False}
    rects = []
    
    if request.method == 'POST':
        if request.FILES.get("image", None) is not None:
            frame = request.FILES["image"]
            frame = frame.read()
            frame = np.asarray(bytearray(frame), dtype="uint8")
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            face_titles = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(knownFE, face_encoding)
                name = "Unknown"
                title = 'unknown'

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
                rects.append([name,title,top,right,bottom,left])
                
            face_data.update({"faces": rects, "success" : True})
    
    return JsonResponse(face_data)
