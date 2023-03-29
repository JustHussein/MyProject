var http = require('http');
var dt = require('./madules/mytime');
var fs = require('fs')

http.createServer(function (req, res) {
    fs.readFile('E:/MyProject/responsive/index.html',function(err,data){
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        return res.end();

    });
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('write method return'+dt.myDateTime()+'\n');
    res.end('The time is: '+dt.myDateTime()); 
}).listen(8080);