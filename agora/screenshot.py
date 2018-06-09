import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    # await page.goto('http://192.168.14.147:8000/')
    await page.goto('https://stackoverflow.com/questions/42279675/syncronous-sleep-into-asyncio-coroutine')

    for i in range(3):
        await asyncio.sleep(5)
        await page.screenshot({'path': 'example.png'})

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
