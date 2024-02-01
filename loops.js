 /* Loops o Ciclos */
 /* 
 
 for(counter; condition; increment){
    sentences
 }

 for (indice in collection){
    sentences
 }

 for (value in collection){
    sentences
 }

 while (condition){
    sentences
 }

 do {
    sentences
 } while (condition)
 
 
 */

 for(let i = 1;  i <= 10; i++){
    console.log(i)
 }

 let nombres = ["Hugo", "Paco", "Luis"]
 for(let indice = 0; indice < nombres.length; indice++){
    console.log(nombres[indice])
 }

 for(let indice in nombres){
    console.log(indice) // 0 1 2 
    console.log(nombres[indice])
 }

 for(let nombre of nombres){
    console.log(nombre) // Hugo Paco Luis
 }

 let i = 1;
 while(i <= 10){
    console.log(i)
    i++
 }

 let indice = 0;
 while(indice < nombres.length){
    console.log(nombres[indice])
    indice++
 }

 i = 1;
 do {
    console.log(i);
    i++
 } while (i <= 10)