// Example for memoize add function 
// a simple function to add something
const add = (n) => (n + 10);
add(9);
// a simple memoized function to add something
const memoizedAdd = () => {
  let cache = {};
  return (n) => {
    if (n in cache) {
      console.log('Fetching from cache');
      return cache[n];
    }
    else {
      console.log('Calculating result');
      let result = n + 10;
      cache[n] = result;
      return result;
    }
  }
}
// returned function from memoizedAdd
const newAdd = memoizedAdd();
console.log(newAdd(9)); // calculated
console.log(newAdd(9)); // cached


// Example for any functions 

// a simple pure function to get a value adding 10
const addten = (n) => (n + 10);
console.log('Simple call', addten(3));
// a simple memoize function that takes in a function
// and returns a memoized function
const memoize = (fn) => {
  let cache = {};
  return (...args) => {
    let n = args[0];  // just taking one argument here
    if (n in cache) {
      console.log('Fetching from cache');
      return cache[n];
    }
    else {
      console.log('Calculating result');
      let result = fn(n);
      cache[n] = result;
      return result;
    }
  }
}
// creating a memoized function for the 'add' pure function
const memoizeAddTenn = memoize(addten);
console.log(memoizeAddTenn(3));  // calculated
console.log(memoizeAddTenn(3));  // cached
console.log(memoizeAddTenn(4));  // calculated
console.log(memoizeAddTenn(4));  // cached


// Another alternative is to make use of some de-facto libraries such as:

//  - Lodash’s _.memoize(func, [resolver])
//  - ES7 @memoize decorators from decko


// For recursive function : 
// same memoize function from before
const memoizeFn = (fn) => {
  let cache = {};
  return (...args) => {
    let n = args[0];
    if (n in cache) {
      console.log('Fetching from cache', n);
      return cache[n];
    }
    else {
      console.log('Calculating result', n);
      let result = fn(n);
      cache[n] = result;
      return result;
    }
  }
}
const factorial = memoizeFn(
  (x) => {
    if (x === 0) {
      return 1;
    }
    else {
      return x * factorial(x - 1);
    }
  }
);
console.log(factorial(5)); // calculated
console.log(factorial(6)); // calculated for 6 and cached for 5