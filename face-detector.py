#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Coded By Kuduxaaa

import cv2

# წაიკითხოს / გახსნას ფოტო
readed_image = cv2.imread('guido.jpg') 

# ფოტოს გაშავთეთრება უკეთესი შედეგისთვის
gray_image = cv2.cvtColor(readed_image, cv2.COLOR_BGR2GRAY)

# შემოიტანოს ფაილი რომელიც დაეხმარება სახის ამოცნობაში
face_detector = cv2.CascadeClassifier('config/HFD.xml')

# სახის კოორდინატების ამოცნობა
detected_faces = face_detector.detectMultiScale(readed_image, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30)) 

# ამოცობილი სახეების თანმიმდევრობით ჩარჩოში ჩასმა
for (x, y, w, h) in detected_faces:
	cv2.rectangle(readed_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# ფოტოს ჩვენება
cv2.imshow('image', readed_image)
cv2.waitKey(0)