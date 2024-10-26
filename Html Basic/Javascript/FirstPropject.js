Age = 24
console.log(Age)
let age = 24;
age = 23
console.log(age)

const pi = 3.14;
console.log(pi)
let X = BigInt("123")
let y = 9.5
let z = true
let a = null
let b
let c = Symbol("Hello")

const student ={
    Name: "Asad Amin",
    Age: 25,
    CGPA: 2.9,
    isPass: true
};
student["Age"] = student["Age"] + 5
console.log(student["Age"])

const product ={
    Title: "Ball Pen",
    Rating: 5,
    Offer: 5,
    Price: 300
}
console.log(product)

//Comments In JavaScript
/* Multiple Lines Of Comments
In JavaScript*/

// Arithmatic Operators in JavaScript

let d = 6
let e = 2
//Plus
console.log("d + e =", d + e)
//Minus
console.log("d - e =", d - e)
//Divide
console.log("d / e =", d / e)
//Multiply
console.log("d * e =", d * e)
// Reminder
console.log("d % e =", d % e)
//Power of any number
console.log("e ** d =", e ** d)
//Increment and decrement
d++
e--
console.log("d + e =", d + e)

d += 4
console.log("d + e = ", d + e)

d -= 4
console.log("d - e = ", d - e)

console.log("d == e", d == e)

console.log("d != e", d != e)

console.log("d === e", d === e)

console.log("d !== e", d !== e)

//Logical Operators

let f = 5
let g = 6
let cond1 = f < g;
let cond2 = f != 5;
console.log("Cond1 && Cond2 =", cond1 && cond2);
console.log("Cond1 || Cond2 =", cond1 || cond2);
console.log("!(f == g)", !(f == g));

// Conditional Statements

let A = 16;
/*
if (A >= 18) {
    console.log("You Can Vote")
}
if (A < 18) {
    console.log("You Cannot Vote")
}

*/
if (A > 18) {
    console.log("You Can Vote")
}else {
    console.log("You Cannot Vote")
}

// Check Even And Odd

let num = 5
if (num % 2 ===0) {
    console.log(num, " is even")
} else { 
    console.log(num, " is odd")
}
