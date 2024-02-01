/* Conditionals */
/* 

if (condition) {
    // sentences
}

if (condition) {
    // sentences
} else {
    // sentences
}


if (condition) {
    // sentences
} else if (condition) {
    // sentences
} else if (condition) {
    // sentences
} else {
    // sentences
}

switch(valor){
    case condition: // sentences
        break;
    default: // sentences
        break;
}

*/

let a = 10;
let b = 20;
let c = 15;

if (a > b){
    console.log("A es mayor que B")
}


if (a > b) {
    console.log("A es mayor que B")
} else {
    console.log("B es mayor que A")
}

if (a > b && a > c){
    console.log("El mayor es A")
} else if (b > c){
    console.log("El mayor es B")
} else {
    console.log("El mayor es C")
}