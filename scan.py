#!/usr/bin/env python3

import serial
import time
import pygame.camera
import pygame.image

serial_port = '/dev/ttyACM3'
baudrate = 115200

pygame.camera.init()
cameras = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cameras[0])
webcam.start()
time.sleep(5)

ser = serial.Serial(serial_port, baudrate)
print(ser.name)
ser.write(b'G91')
count = 0
for x in range(24):
    img = webcam.get_image()
    pygame.image.save(img, 'image{0:0>3}.jpg'.format(count))
    ser.write(b'y0.212\n')
    count += 1
    time.sleep(1)
ser.close()
webcam.stop()
print('finito, merda')
