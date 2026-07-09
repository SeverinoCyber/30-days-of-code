#!/usr/bin/perl

use strict;
use warnings;

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

sub solve {
    # Write your code here
    my ($meal_cost, $tip_percent, $tax_percent) = @_;
    my $prop = $meal_cost * ($tip_percent / 100.0);
    my $imp = $meal_cost * ($tax_percent / 100.0);
    
    my $total_cost = $meal_cost + $prop + $imp;
    my $redondear = int($total_cost + 0.5);
    print "$redondear\n";

}

my $meal_cost = ltrim(rtrim(my $meal_cost_temp = <STDIN>));

my $tip_percent = ltrim(rtrim(my $tip_percent_temp = <STDIN>));

my $tax_percent = ltrim(rtrim(my $tax_percent_temp = <STDIN>));

solve $meal_cost, $tip_percent, $tax_percent;

sub ltrim {
    my $str = shift;

    $str =~ s/^\s+//;

    return $str;
}

sub rtrim {
    my $str = shift;

    $str =~ s/\s+$//;

    return $str;
}
