#!/usr/bin/node
const firstArgument = process.argv[2];
if (firstArgument === undefined) {
  console.log('Not a number');
} else if (isNaN(firstArgument)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(firstArgument));
}
