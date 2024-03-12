#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && !isNaN(w) && !isNaN(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    let Myvar = 0;
    Myvar = this.height;
    this.height = this.width;
    this.width = Myvar;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
