#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";

    
    // Declare second integer, double, and String variables.
    int entero;
    double flotante;
    string cadena;
    // Read and save an integer, double, and String to your variables.
    // Note: If you have trouble reading the entire string, please go back and review the Tutorial closely.
    cin >> entero;
    cin >> flotante;
    cin.ignore();
    getline(cin, cadena);
    // Print the sum of both integer variables on a new line.
    int result = entero + i;
    cout << result << endl;
    // Print the sum of the double variables on a new line.
    double result1 = flotante + d;
    cout << fixed << setprecision(1) << result1 << endl;
    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    string result2 = s + cadena;
    cout << result2 << endl;

    return 0;