using System;
using System.Collections.Generic;
using System.IO;

class Solution {
    static void Main(String[] args) {
        int i = 4;
        double d = 4.0;
        string s = "HackerRank ";

        
        // Declare second integer, double, and String variables.
        int entero;
        double flotante;
        string cadena;
        // Read and save an integer, double, and String to your variables.
        entero = int.Parse(Console.ReadLine());
        flotante = double.Parse(Console.ReadLine());
        cadena = Console.ReadLine();
        // Print the sum of both integer variables on a new line.
        Console.WriteLine(entero + i);
        // Print the sum of the double variables on a new line.
        double result1 = flotante + d; 
        Console.WriteLine($"{result1:F1}");
        // Concatenate and print the String variables on a new line
        // The 's' variable above should be printed first.
        string result = $"{s}{cadena}";
        Console.WriteLine(result);

    }
}