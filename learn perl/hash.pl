#!/usr/bin/env perl

# a hash is like a dictionary in py or an obj in js

use strict;
use warnings;
use Data::Dumper;


# the hash is like a list of variables 1 key 2 value and so on
my %person = (
  name => "Ali",
  age => 19,
  money => 1.68,
  money => 0, # the last key will override all the others with same names
  '1_%' => "special characters", # to add special characters to the keys make ''
);
# overriding
$person{name} = "Obad";

# merge hashes
my %person2 = (
  %person,
  name => "Rehab",
  "not_exist" => undef,
);

# array of keys and values
my @keys_arr = keys %person2;
my @vals_arr = values %person2;
# get the size of the hash
my $size = @keys_arr;
# check if key exists
my $is_exist = exists $person2{"not_exist"} ? 'yes' : 'no';
# delete item from the hash
delete $person2{"not_exist"};

print Dumper(%person);
print "------------------------\n";
print Dumper( $person{name} );
print "------------------------\n";
print Dumper(%person2);
print "------------------------\n";
print Dumper(@keys_arr);
print Dumper(@vals_arr);
print Dumper($size);
print Dumper($is_exist);
print "------------------------\n";


1;
