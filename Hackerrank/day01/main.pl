$i = 4;
$d = 4.0;
$s = 'HackerRank ';
# Declare second integer, double, and String variables.
my $entero = <STDIN>;
my $flotante = <STDIN>;
my $cadena = <STDIN>;
# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.
my $result = $entero + $i;
print "$result\n";
# Print the sum of the double variables on a new line.
my $result1 = $flotante + $d;
printf ("%.1f\n", $result1);
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
my $result2 = $s . $cadena;
print $result2;
