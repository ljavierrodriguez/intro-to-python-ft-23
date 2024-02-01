/* Functions */
/* 

function functionName(args){

}

let functionName = function(args){

}

*/

function sumar(a, b){
    return a + b;
}

let restar = function(a, b){
    return a - b;
}

let numeros = [1, 2, 3]

let resultados = numeros.map(function(valor){
    return valor**2
})

function totalizar(...rest){
    return rest.reduce((total, valor) => total + valor, 0)
}

console.log(totalizar(10, 20, 30, 40, 50))