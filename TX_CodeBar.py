# No Windows, se a biblioteca pyzbar estiver com erro na hora de importar
# pode ser necessário instalar o Visual C++
# https://www.microsoft.com/en-US/download/details.aspx?id=40784

# import the necessary packages
from pyzbar import pyzbar
import argparse
import cv2
from multiprocessing import Queue, current_process
import time

def searchForImages(imgQ, exitQ):

    while True:
        if exitQ.get():
            print(f'{current_process().name} finalizado')
            break

        if imgQ.not_empty():
            
            print("Gray values of first row: ", imgQ.get()[0])
            print()
        else:
            print('Nenhuma imagem na fila')

        print('nada ainda')
        time.sleep(1)







def SearchForCodeBars(image, show_Window=False):

    barcodes = pyzbar.decode(image)

    # loop over the detected barcodes
    for barcode in barcodes:

        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # print the barcode type and data to the terminal
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

        if show_Window:
            # extract the bounding box location of the barcode and draw the
            # bounding box surrounding the barcode on the image
            (x, y, w, h) = barcode.rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # the barcode data is a bytes object so if we want to draw it on
            # our output image we need to convert it to a string first

            # draw the barcode data and barcode type on the image
            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 255), 2)

    if show_Window:
        # show the output image
        cv2.imshow("Image", image)
        cv2.waitKey(0)

    return barcodeData

if __name__ == '__main__':

    # load the input image
    image = cv2.imread('teste 2.png')
    # find the barcodes in the image and decode each of the barcodes

    SearchForCodeBars(image, show_Window=True)
