// const { JSDOM } = require('jsdom');
const puppeteer = require("puppeteer");

// const agora = require("./AgoraRTCSDK-2.3.1");
/*console.log(JSDOM);
const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
console.log(dom.window.document.querySelector("p").textContent); // "Hello world"
const {window} = dom;
const {navigator}=window;*/
// console.log(navigator);
(async () => {
    const browser = await puppeteer.launch({headless: false});
    const page = await browser.newPage();
    await page.goto('http://192.168.14.147:8000/');
    let i=0;
    setInterval(function () {
        page.screenshot({path: `example${i++}.png`});

    },3000);

})();
/*console.log(navigator);
console.log(agora);*/
