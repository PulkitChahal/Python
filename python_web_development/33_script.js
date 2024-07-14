// -> Primitive - when variables hold single value
// 7
// 2.5
// Datatype: Number;

// "pulkit", 'pulkit'
// Datatype: String;

// true
// false
// Name: George Boole
// Datatype: Boolean;

// null
// undefined
// Datatype: Empty Values;

// -> Non-Primitive - when variables hold multiple values
// [1, 2, 3, 4, 5]
// [1, 2, 'Anurag', true, false, null]
// Datatype: Array

// Object
// {key:value}
// {fname:'pulkit', lname:'chahal'}

// -> Variables

// var username = "Pulkit";
// let lastname = "Chahal";
// const companyname = "iNeuron";
// let number = 25;

// console.log(username);

// console.log(typeof lastname);

// console.log("Name is " + username + " Number is " + number);

// interpolation / Template Literal / Template Strings

// console.log(`
// My Name is ${username}
// My Number is ${number}
// `);

// console.log(username.length);
// console.log(username[3]);

// -> Operator
// arithmetic OP
// +, -, *, /, %, **

// console.log(5 + 3); // addition
// console.log('5' + 5); // addition
// console.log(5 - 3); // subtraction

// comparison OP
// ==, ===

// let one = 1;
// let two = '1';
// console.log(one == two); // true -> matches only value
// console.log(one === two); // false -> matches value and its type also

// logical OP
// &&(and) ||(or)

// ternary OP

// -> Conditions

// Mini app => Rating App
// let rating = 4;
// if (rating == 5) {
//   console.log("5 stars");
// } else if (rating == 4) {
//   console.log("4 stars");
// } else {
//   console.log("We will improve");
// }

// ternary Conditions (oper)

// condition ? exp(true) : exp(false);

// let login = true;
// login ? console.log('Logout') : console.log('Login First');

// let result = rating = 5 ? console.log('5 stars') : console.log('4 stars');

// truthy Value , Falsy Value

// truthy Value -> if statement is true
// falsy Value -> if statement is false


// -> Math Object

const pulkit = Math.PI
console.log(pulkit)
console.log(Math.random()); // 0 - 0.999999
console.log(Math.floor(Math.random() * 50));
