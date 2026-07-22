'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');
let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;
process.stdin.on('data', function(inputStdin: string): void {
    inputString += inputStdin;
});

process.stdin.on('end', function(): void {
    inputLines = inputString.split('\n');
    inputString = '';
    main();
});

function readLine(): string {
    return inputLines[currentLine++];
}

function main() {
    // Enter your code here
    var i = 4
    var d = 4.0
    var s = "HackerRank "
    
    var entero
    var flotante
    var cadena
    
    entero = Number(readLine())
    flotante = Number(readLine())
    cadena = readLine()
    
    console.log(entero + i)
     var result = flotante + d 
    console.log(result.toFixed(1))
    console.log(s + cadena)
}
