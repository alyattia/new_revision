#!/usr/bin/env perl

# scopes of variables

use strict;
use warnings;
use Data::Dumper;


# the die keyword stops the program from excuting anything below it
# die "(I typed that). died";

my $test = "world";


# use the key word eval to define an exepction
eval {
  die "error";
  $test = "that should throw an error";
};


# use the warn keyword to just give a warning and don't stop the excution
warn "my  warning";



print "hello $test \n";


1;
