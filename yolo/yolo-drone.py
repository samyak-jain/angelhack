'''
Module receives frames from the agora api and applies
YOLO algorithm to every frame. Script emulates a browser
in the python script on a server and parses frames off it
requirements: chrome/chromium, refer requirements.txt
                requires darkflow installed via python(refer docs)
usage: run script using python3
        CLI args: executable path of the chrome/chromium browser
                    defaults to '/usr/bin/google-chrome-stable'
                    Video will be displayed everytime a person is
                    detected by the 'openlive' app available in the repo
'''

import argparse
import numpy as np
import asyncio
import time
from PIL import Image
import io
from darkflow.net.build import TFNet
import cv2
from Algorithms import conversion
from dbinit import db

options = {
    "model": "config/tiny-yolo-voc.cfg",
    "load": "config/tiny-yolo-voc.weights"
    # "labels": "config/labels.txt"
}

tfnet = TFNet(options)

def get_pred(img):
    preds = tfnet.return_predict(img)
    results = []

    for pred in preds:
        if pred['label'] != 'person':
            continue

        result = {}
        result['tl'] = [pred['topleft']['x'], pred['topleft']['y']]
        result['br'] = [pred['bottomright']['x'], pred['bottomright']['y']]
        results.append(result)

    return results

def save(img, writer, annots):
    for annot in annots:
        x, y, x2, y2 = annot['tl'] + annot['br']
        pad = 3
        cv2.rectangle(img, (x-pad, y-pad), (x2+pad, y2+pad), (0, 0, 255), 4)

    writer.write(img)
    # cv2.imwrite('output.jpg', img)


def main():
    cap = cv2.VideoCapture('drone.mov')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 30, (1920,1080))
    cnt = 0

    print('Reading video and applying YOLO')
    while(cap.isOpened() and cnt < 10000):
        ret, frame = cap.read()

        if not ret:
            continue

        pred = get_pred(frame)
        print('\r'+str(cnt)+':'+str(len(pred)), end='')
        cnt += 1

        save(frame, out, pred)

    cap.release()
    out.release()


if __name__ == '__main__':
    main()

