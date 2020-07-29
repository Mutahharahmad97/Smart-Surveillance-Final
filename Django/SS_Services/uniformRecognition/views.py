from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import numpy as np
import urllib
import json
import cv2
import pickle
import os
from pathlib import Path
from django.conf import settings
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import keras.backend.tensorflow_backend as tb

model_Path = Path(settings.BASE_DIR + "/Models/fashion.model")
picke_path = Path(settings.BASE_DIR + '/Models/mlb.pickle')

#OPEN MODELS FOR UNIFORM RECOGNITION
model = load_model(model_Path)
#OPEN MODELS FOR UNIFORM RECOGNITION
# mlb = pickle.loads(open(picke_path, "rb").read())

with open(picke_path, 'rb') as pickle_read:
    mlb = pickle.load(pickle_read)

@csrf_exempt
def detect_UR(request):
    if request.method == 'POST':
        label = ""
        position = []
        
        if request.FILES.get("image", None) is not None:
            frame = request.FILES["image"]
            frame = frame.read()
            frame = np.asarray(bytearray(frame), dtype="uint8")
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
            
            image = cv2.resize(frame, (96, 96))
            image = image.astype("float") / 255.0
            image = img_to_array(image)
            image = np.expand_dims(image, axis=0)

            tb._SYMBOLIC_SCOPE.value = True
            proba = model.predict(image)[0]
            idxs = np.argsort(proba)[::-1][:2]

            for (i, j) in enumerate(idxs):
                label += "{}: {:.2f}%".format(mlb.classes_[j], proba[j] * 100) + ","
                position.append(i * 30)
            
        label = label.split(',')
        return JsonResponse({'color' : label[0], 'type': label[1], 'position': position})
