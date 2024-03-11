#!/usr/bin/node

const argc = parseInt(process.argv[2]);
if (!isNaN(argc)) {
  if (argc > 0) {
    for (let index = 0; index < argc; index++) {
      console.log('X'.repeat(argc));
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
