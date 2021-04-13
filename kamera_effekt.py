import picamera
import pygame
import numpy as np
import cv2
import sys
A=["negative","gpen","emboss","solarize","colorswap","cartoon","washedout","posterise"]
s=0
try:
    camera=picamera.PiCamera()  
except picamera.PiCameraError:
    print("Error")
    sys.exit()

camera.resolution = (240, 320)
camera.image_effect = '{}'.format(A[s])
print(A[s])
s+=1
pygame.init()
while True:
    camera.capture('foo.jpg', use_video_port=True)
    img1=cv2.imread('foo.jpg')
    cv2.imshow('Ekran',img1)
    key=cv2.waitKey(1)&0xFF
    if key==ord("0"):
        camera.image_effect = '{}'.format(A[s])
        s+=1
    if s==8:
        s=0
                    
    if key==ord("q"):
        pygame.quit()
        cv2.destroyAllWindows()
        camera.close()
        sys.exit()
                    
    img = pygame.image.load('foo.jpg')
    screen = pygame.display.set_mode((240,320))
    if img:
        screen.blit(img,((240 - img.get_width() ) / 2,(320 - img.get_height()) / 2))
    pygame.display.update()
