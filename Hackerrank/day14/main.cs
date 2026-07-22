ing System;
using System.Linq;

class Difference {
    private int[] elements;
    public int maximumDifference;

	// Add your code here
    public Difference(int[] elements)
    
    {
        this.elements = elements;
    }
    public void computeDifference(){
        int min = elements[0];
        int max = elements[0];

        foreach (int num in elements)
        {
            if (num < min) min = num;
            if (num > max) max = num;
        }

        maximumDifference = Math.Abs(max - min);
    }
        

} // End of Difference Class

class Solution {
    static void Main(string[] args) {
        Convert.ToInt32(Console.ReadLine());
        
        int[] a = Console.ReadLine().Split(' ').Select(x=>Convert.ToInt32(x)).ToArray();
        
        Difference d = new Difference(a);
        
        d.computeDifference();
        
        Console.Write(d.maximumDifference);
    }
}