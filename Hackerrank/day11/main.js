'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}



function main() {

    let arr = Array(6);

    for (let i = 0; i < 6; i++) {
        arr[i] = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));
    }
    let suma_max = -100;
    for(let i = 0;i < 4; i++){
        for(let j = 0; j < 4;j++){
            let sup = arr[i][j] + arr[i][j+1] + arr[i][j+2];
            let mid = arr[i+1][j+1];
            let bot = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2];
            
            let sum_actual = sup + mid + bot;
            
            if(sum_actual > suma_max){
                suma_max = sum_actual;
            }
        }
    }
    console.log(suma_max)
    
}
