'''
A simple Program for grabing video from basler camera and converting it to opencv img.
Tested on Basler acA1300-200uc (USB3, linux 64bit , python 3.5)
'''
from pypylon import pylon
import cv2
import time
import sys

# conecting to the first available camera
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

# Grabing Continusely (video) with minimal delay
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
converter = pylon.ImageFormatConverter()

# converting to opencv bgr format
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

try:
    if sys.argv[1] == 's':
        showWindow = True
    else:
        showWindow = False
except:
    showWindow = False

qtdframes = 0
startTime = time.perf_counter()

while camera.IsGrabbing():
    
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        qtdframes += 1
        # Access the image data
        image = converter.Convert(grabResult)
        img = image.GetArray()
        
        if showWindow:
            cv2.namedWindow('title', cv2.WINDOW_NORMAL)
            cv2.imshow('title', img)
            k = cv2.waitKey(1)
            if k == 27:
                break

        if qtdframes > 30:
            print(f'Frame Rate: { round(qtdframes / (time.perf_counter() - startTime), 1)} fps')
            startTime = time.perf_counter()
            qtdframes = 0
    
    grabResult.Release()
    
# Releasing the resource    
camera.StopGrabbing()

cv2.destroyAllWindows()