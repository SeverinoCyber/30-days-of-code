unction processData(input) {
    //Enter your code here
    let lineas = input.trim().split('\n');
    
    let N = parseInt(lineas[0].trim());
    let mapa = {};

    for (let i = 1; i <= N; i++) {
        let [name, phone] = lineas[i].trim().split(' ');
        mapa[name] = phone;
    }

    for (let i = N + 1; i < lineas.length; i++) {
        let search = lineas[i].trim();
        
        if (search === "") continue;

        if (mapa.hasOwnProperty(search)) {

            console.log(search + "=" + mapa[search]);
        } else {
            
            console.log("Not found");
        }
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
