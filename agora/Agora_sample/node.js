const http = require('http');

http.createServer(function (req, res) {
  res.write('d610c4a86c774d1890e33db32592447c'); //write a response to the client
  res.end(); //end the response
}).listen(8080); //the server object listens on port 8080

