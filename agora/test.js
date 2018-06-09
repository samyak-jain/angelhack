const { JSDOM } = require('jsdom');

const dom = new JSDOM('', {
	url: "http://localhost:8000/",
	pretendToBeVisual: true
})

function test() {
console.log(dom.window.document)
console.log(dom.window.document.getElementById("video"));
}

setTimeout(() => {
	test();
}, 3000)

