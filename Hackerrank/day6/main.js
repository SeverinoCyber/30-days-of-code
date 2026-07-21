function processData(input) {
    //Enter your code here
    let lineas = input.trim().split('\n');
    let T = parseInt(lineas[0]);
    for (let i = 1; i <= T; i ++){
        let S = lineas[i].trim();
        let par = "";
        let impar = "";
        
        for (let indice = 0; indice < S.length; indice++){
            if(indice % 2 === 0){
                par += S[indice];
            }else{
                impar += S[indice];
            }
        }console.log(par+" "+impar)
    }
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
