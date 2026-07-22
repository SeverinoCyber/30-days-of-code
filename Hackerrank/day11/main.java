import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;



public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        List<List<Integer>> arr = new ArrayList<>();

        for (int i = 0; i < 6; i++) {
            String[] arrRowTempItems = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

            List<Integer> arrRowItems = new ArrayList<>();

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowTempItems[j]);
                arrRowItems.add(arrItem);
            }

            arr.add(arrRowItems);
        }
        int suma_max = -100;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                int sup = arr.get(i).get(j) + arr.get(i).get(j+1) + arr.get(i).get(j+2);
                int mid = arr.get(i+1).get(j+1);
                int bot = arr.get(i+2).get(j) + arr.get(i+2).get(j+1) + arr.get(i+2).get(j+2);
                
                int suma_actual = sup + mid + bot;
                if(suma_actual > suma_max){
                    suma_max = suma_actual;
                }
            }
        }
            System.out.println(suma_max);

        bufferedReader.close();
        
        
    }
}