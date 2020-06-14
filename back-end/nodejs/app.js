
const apiCallFromNode = require('./NodeJsCall')
const http = require('http')

http.createServer((req, res) => {
    apiCallFromNode.callApi((response) => {
        response.forEach(element => {
            console.log(element[0]);
        });
        // res.write(response);
        res.end();
    });
}).listen(3000);

console.log("service running on 3000 port....");