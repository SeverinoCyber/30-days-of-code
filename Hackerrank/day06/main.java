import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        scanner.nextLine();
        
        for(int i = 1;i <= T; i++){
            String S = scanner.nextLine();
            String par = "";
            String impar = "";
            
            for(int l = 0;l < S.length();l++){
                if(l % 2 == 0){
                    par += S.charAt(l);
                }else{
                    impar += S.charAt(l);
                
            }
            
            }
            System.out.println(par+" "+impar);
        }
        scanner.close();
    }
}