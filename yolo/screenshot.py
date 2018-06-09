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
    print(preds)
    results = []

    for pred in preds:
        result = {}
        result['tl'] = [pred['topleft']['x'], pred['topleft']['y']]
        result['br'] = [pred['bottomright']['x'], pred['bottomright']['y']]
        results.append(result)

    return results

async def main():
    browser = await launch({'executablePath': '/usr/bin/google-chrome'})
    page = await browser.newPage()
    # await page.goto('http://192.168.14.147:8000/')
    await page.goto('http://unsting-relay.netlify.com')

    while(True):
        initial = time.time()
        await asyncio.sleep(5)
        img = await page.screenshot({'path': 'example'+str(initial)+'.png'})
        image = Image.open(io.BytesIO(img)).convert('RGB')

        print(type(image))
        img = np.array(image)
        print("array ", img.shape)
        print(get_pred(img))

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
