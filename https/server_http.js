var express = require("express"),
  http = require("http");
app = express();
bodyParser = require("body-parser");
var server = http.createServer(app);
server.listen(80);
app.use(express.static(__dirname + "/web"));
app.use(bodyParser.json());
app.get("/", function (req, res) {
  console.log("앙 서버 오픈띠");
  res.send("Hi, Client, I am a server");
});
app.post("/", (req, res) => {
  console.log("[Server] POST : " + JSON.stringify(req.body));
  res.send(`post value is : ` + req.body.Client + `안녕하세요`);
});

var io = require("socket.io")(server);
var roomName;
io.on("connection", function (socket) {
  console.log("connect");
  var instanceId = socket.id;
  socket.on("joinRoom", function (data) {
    console.log(data);
    socket.join(data.roomName);
    roomName = data.roomName;
  });
  socket.on("reqMsg", function (data) {
    console.log(data);
    io.sockets
      .in(roomName)
      .emit("recMsg", { comment: instanceId + " : " + data.comment + "\n" });
  });
});
