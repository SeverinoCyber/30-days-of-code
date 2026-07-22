using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static void Main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        int T = Convert.ToInt32(Console.ReadLine());
        for(int i = 1;i <= T;i++){
            string S = Console.ReadLine();
            string par = "";
            string impar = "";
            
            for(int l = 0;l < S.Length; l++){
                if(l %2 ==0){
                    par += S[l];
                }else{
                    impar += S[l];
                }
            }
            Console.WriteLine(par+" "+impar);
        }
    }
}
