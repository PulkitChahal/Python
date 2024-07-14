// -> Loops

// for loop:-
// for(init, conditions, incre, decrement)

// for (let i = 0; i < 5; i++) {
// console.log(i);
// }

// for (let i = 0; i < 5; i++) {
// console.log(`${i}`);
// }

// let mobile = [
//   "Mobile1",
//   "Mobile2",
//   "Mobile3",
//   "Mobile4",
//   "Mobile5",
//   "Mobile6",
//   "Mobile7",
//   "Mobile8",
// ];
// for (let i = 0; i < mobile.length; i++) {
//   console.log(mobile[i]);
// }

// let mobile = ["Mobile1", "Mobile2", "Mobile3", "Mobile4", "Mobile5"];
// let phone = [];
// for (let i = 0; i < mobile.length; i++) {
//   phone.push(mobile[i].toUpperCase());
// }
// console.log(phone);

// while loop:-

// let i = 0;
// while (i <= 5) {
//   console.log(i);
//   i++;
// }

// do while loop:-

// let i = 0;
// do {
//   console.log(i);
//   i++;
// } while (i < 6);

// for of:- Array

// let tech = [
//   "HTML",
//   "CSS",
//   "Tailwind",
//   "JavaScript",
//   "ReactJs",
//   "NodeJs",
//   "Express",
//   "MongoDB",
// ];
// for (let tech_need of tech) {
// console.log(tech_need);
// }

// let mobile = ["Mobile1", "Mobile2", "Mobile3", "Mobile4", "Mobile5"];
// for (let i = 0; i < mobile.length; i++) {
//   if (mobile[i] == "Mobile3") {
// break;
//   }
//   console.log(mobile[i]);
// }

// for (let i = 0; i < mobile.length; i++) {
//   if (mobile[i] == "Mobile3") {
// continue;
//   }
//   console.log(mobile[i]);
// }

// -> Object
// {key:value}

// let userDetails = {
//   firstName: "Pulkit",
//   lastName: "Chahal",
//   companyName: "iNeuron",
//   loginCount: "25",
//   role: "student",
//   login: true,
// };
// console.log(userDetails);
// console.log(userDetails.firstName);
// console.log(userDetails.lastName);
// console.log(userDetails["firstName"]); // This is Not Good practice

// -> Object on Hold
// -> Functions

// function squar(num) {
//   console.log(num * num);
// }
// squar(2);

// function areaOfCircle(r) {
//   let area = Math.PI * r * r;
//   return area;
// }
// let result = areaOfCircle(7);
// console.log(result);

// function sumOfAll() {
// console.log(arguments);
// let sum = 0;
// for (let i = 0; i< arguments.length; i++){
// sum += arguments[i];
// }
// return sum;
// }
// console.log(sumOfAll(10, 20, 30, 40, 50, 60));

// Arrow Function:-

// let sumOfAll = (x, y) => {
//   console.log(x, y);
// };
// sumOfAll(10, 20);

// let sumOfAll = (x, y) => {
//   let sum = x + y;
//   return sum;
// };
// console.log(sumOfAll(10, 20));

// let xyz = function () {};

// -> Object Begins

// let userDetailCourse = {
//   firstName: "Pulkit",
//   lastName: "Chahal",
//   role: "student",
//   loginCount: 25,
//   googleLogin: true,
//   courseList: [],
//   buyCourse: function (courseName) {
// this.courseList.push(courseName);
//   },
//   getCourseCount: function () {
// return `${this.firstName} is having a course count of ${this.courseList}`;
//   },
// };
// console.log(userDetailCourse);
// userDetailCourse.buyCourse("Pro Frontend Dev");
// userDetailCourse.buyCourse("Pro Frontend Dev V2");
// console.log(userDetailCourse.getCourseCount());
