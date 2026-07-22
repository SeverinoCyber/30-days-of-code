using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static void Main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        int N = Convert.ToInt32(Console.ReadLine());
        Dictionary<string, string> mapa = new Dictionary<string, string>();
        
        for(int i = 0;i< N;i++){
            string[] input = Console.ReadLine().Split(' ');
            string name = input[0];
            string phone = input[1];
            
            mapa[name] = phone;
        }
        string buscar;
        while ((buscar = Console.ReadLine()) != null){
            if (buscar =="")continue;
            
            if (mapa.ContainsKey(buscar)){
                Console.WriteLine(buscar+"="+mapa[buscar]);
            }else{
                Console.WriteLine("Not found");
            }
        }
            }
        }
    