import numpy as np
import asyncio
from pyppeteer import launch
import time
from PIL import Image
import io

async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()
    # await page.goto('http://192.168.14.147:8000/')
    await page.goto('http://unsting-relay.netlify.com')
    asyncio.sleep(3)

    while(True):
        initial = time.time()
        img = await page.screenshot()
        # img = await page.screenshot()
        # img = Image.frombytes('RGB', (640, 480), img)
        image = Image.open(io.BytesIO(img)).convert('RGB')
        print(type(image))
        img = np.array(image)
        print("array ", img.shape)

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
