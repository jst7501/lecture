var request = require("request");

const url = "http://127.0.0.1";

async function post(url) {
  return new Promise(function (resolve, reject) {
    request(
      {
        url: url,
        method: "post",
        headers: { "content-type": "apllication/json" },
        body: JSON.stringify({ client: hi }),
      },
      function (err, res, resbody) {
        if (err) {
          reject(err);
        } else {
          console.log("post :", res.statusCode);
          resolve(resbody);
        }
      }
    );
  });
}
async function get(url) {
  return new Promise(function (resolve, reject) {
    request(url, function (err, res, resbody) {
      if (err) {
        reject(err);
      } else {
        console.log("GET :", res.statusCode);
        resolve(resbody);
      }
    });
  });
}
async function main() {
  ret = await get(url);
  console.log(ret);
  ret = await post(url);
  console.log(ret);
}
main();
