#!/usr/bin/env perl

# error handling

use strict;
use warnings;
use Data::Dumper;
# import the scopes2 file
require './scopes2.pl';
use feature qw/ state /;


# we use the our keyword to be able to export variables and so
# and this syntax is for importing vars
our ($scope2_var);

# the feature state tells perl that this vari should be intialized once (only once) in the memory
sub state_test {
  # this var will be intialized once and the state will keep tracking of the var's value
  state $state_var = 1;
  $state_var += 1;
  print '>>>>' . $state_var . "\n";
}


# print Dumper $var1;
print "$scope2_var\n";


state_test();
state_test();
state_test();





1;
