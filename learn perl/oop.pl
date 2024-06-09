#!/usr/bin/env perl

# Object oriented programming with perl using the built-in perl and the mouse module

use strict;
use warnings;
use feature qw/ say /;

# this BEGIN statement must work before those uses
BEGIN {
  # adds the folder where the Dog module is located to tell perl where he can search for that module and find it
  push @INC, "Z:\\programing\\learn perl"
}

use Data::Dumper;
# importing our module or class or package
use Dog;


# the new is the method we created in our package file see the package
my $Dog = Dog->new("labrador", 50, 70, "blue", "eyad");

say $Dog;
say $Dog->get_weight;
$Dog->set_type("chiwawa");
say $Dog->get_type; 





1;
