#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Coded By Kuduxaaa

import cv2
import os

SHOW_IMAGE = True;

img = cv2.imread('guido.jpg')
for images in os.scandir('images/'):
	image_name = 'images/' + str(images.name)
	readed_image = cv2.imread(image_name)

	if img.shape == readed_image.shape:
		difference = cv2.subtract(img, readed_image)
		b, g, r = cv2.split(difference)

		if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
			print(f'[+] Image Found: {image_name}')
			if SHOW_IMAGE:
				cv2.imshow('image', readed_image)
				cv2.waitKey(0)
			break
	else:
		print(f'[-] {image_name} Not Match!')