import numpy as np
import asyncio
from pyppeteer import launch
import time
from PIL import Image
import io
from darkflow.net.build import TFNet
import cv2

options = {
    "model": "config/tiny-yolo-voc.cfg",
    "load": "config/tiny-yolo-voc.weights",
    "labels" : "config/labels.txt"
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
    cv2.imwrite('before.jpg', img)
    for annot in annots:
        x, y, x2, y2 = annot['tl'] + annot['br']
        cv2.rectangle(img, (x, y), (x2, y2), (0,255,0), 2)
    # cv2.imshow('sample', img)
    cv2.imwrite('after.jpg', img)

async def main():
    browser = await launch({'executablePath': '/usr/bin/google-chrome-stable'})
    page = await browser.newPage()
    await page.goto('http://unsting-relay.netlify.com')

    while(True):
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

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
