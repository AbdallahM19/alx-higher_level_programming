#!/usr/bin/node

const fs = require('fs');

const file = [process.argv[2], process.argv[3], process.argv[4]];
if (fs.existsSync(file[0]) && fs.statSync(file[0]).isFile && fs.existsSync(file[1]) && fs.statSync(file[1]).isFile && file[2] !== undefined) {
  const fileMe = [fs.readFileSync(file[0]), fs.readFileSync(file[1])];
  const fileC = fs.createWriteStream(file[2]);
  fileC.write(fileMe[0]);
  fileC.write(fileMe[1]);
  fileC.end();
}
