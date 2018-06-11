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
from pyppeteer import launch
import time
from PIL import Image
import io
from darkflow.net.build import TFNet
import cv2
from Algorithms import conversion
from dbinit import db

options = {
    "model": "config/tiny-yolo-voc.cfg",
    "load": "config/tiny-yolo-voc.weights",
    "labels": "config/labels.txt"
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

def view(img, annots):
    # cv2.imwrite('before.jpg', img)
    for annot in annots:
        x, y, x2, y2 = annot['tl'] + annot['br']
        cv2.rectangle(img, (x, y), (x2, y2), (0, 255, 0), 2)
    cv2.imshow('sample', img)
    cv2.waitKey(1) & 0xFF
    # cv2.imwrite('after.jpg', img)

def update_locations(annots):
    gps = []
    for annot in annots:
        x, y, x2, y2 = annot['tl'] + annot['br']
        out = conversion.calc(x, y, x2, y2)
        gps.append(out)

    for i, data in enumerate(gps):
        db.collection('help').document('person'+str(i)).set(data)


async def main(execpath):
    browser = await launch({'executablePath': execpath})
    page = await browser.newPage()
    await page.goto('http://unsting-relay.netlify.com')

    frames_cnt = 0

    while(True):
        if frames_cnt == 5:
            frames_cnt += 1
            continue
        frames_cnt = 0 # skip frames

        initial = time.time()
        # img = await page.screenshot({'path': 'example'+str(initial)+'.png'})
        img = await page.screenshot()
        image = Image.open(io.BytesIO(img)).convert('RGB')

        img = np.array(image)
        img = np.roll(img, 1, axis=-1)
        print("array ", img.shape)
        pred = get_pred(img)

        if len(pred) > 0:
            img = np.roll(img, 1, axis=-1)
            view(img, pred)
            update_locations(pred)


    await browser.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--execpath',
        help='chrome executable dir',
        default='/usr/bin/google-chrome-stable'
    )
    execpath = parser.parse_args().execpath
    asyncio.get_event_loop().run_until_complete(main(execpath))

