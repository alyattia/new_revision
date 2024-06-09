#!/usr/bin/env perl

# logical operations

use strict;
use warnings;
use Data::Dumper;
# that feature automatically adds a new line at the end of anything we are printing
use feature qw/ say /;


# that's called a turnery expression
say 1 ? "yes" : "no";
# checks equality
say 1==0 ? "yes" : "no";
# checks not equality
say 1 != 0 ? "yes" : "no";
# comaprisen
say 1 > 0 ? "yes" : "no";
say 1 >= 0 ? "yes" : "no";
# returns -1 0 1 according to the comparison
say 1 <=> 2;


# string logics
# checks equality
say "a" eq "b" ? "yes" : "no";
# checks not equality
say "a" ne "b" ? "yes" : "no";
# comparison
say "a" lt "b" ? "yes" : "no"; # less than
say "a" le "b" ? "yes" : "no"; # less than or euals
say "a" gt "b" ? "yes" : "no"; # greater than
say "a" ge "b" ? "yes" : "no"; # greater than or equals


# compined logics
say 1 > 0 && 2 > 1 ? "yes" : "no";
say 1 > 0 || 2 > 1 ? "yes" : "no";
say 1 > 0 && (2 > 1 || 0 < 1) ? "yes" : "no";

say "-" x 40;

# conditions
my $test2 = 0 if 2>1;
my $var = -1;
if ($var > 0) {
  say "$var is a positive number";
}elsif ($var == 0) {
  say "$var is zero"
}else {
  say "$var is a negative number";
}

# unless is like if but opposite
# so it is like if not true
# use it when you want to make an if not condition
unless ($var > 0) {
  say "$var is a negative number";  
}


1;
