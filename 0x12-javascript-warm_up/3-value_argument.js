#!/usr/bin/node
const numberOfArguments = process.argv.length - 2;
if (numberOfArguments === 0) {
  console.log('No argument');
} else {
  const firstArgument = process.argv[2];
  console.log(firstArgument);
}
