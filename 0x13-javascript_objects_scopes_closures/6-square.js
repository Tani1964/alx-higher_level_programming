#!/usr/bin/node

const SupSquare = require('./5-square');

class Square extends SupSquare {
  charPrint (c) {
    if (!c) { c = 'X'; }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;\n
