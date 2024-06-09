#!/usr/bin/env perl

# a refrence is point in memory that points to another data structure
# it allows you to make nested hashes or arrays
# i think it is a data type

use strict;
use warnings;
use Data::Dumper;

my %hash = (a => 1, b =>2);
my @array = qw/one tow/;
my $scalar = 19;

my $arr_ref = \@array;

# if you want to add somethign to that array for example
# push $arr_ref, "three"; #that will give you an error bec you should de refrence the ref before manpulating the array
push $arr_ref->@*, "three";


# you can also construct refrences the same way you construct a hash or array
my $ref_arr = [1, 2, 3];
my $ref_hash = {name => "ali", age => 19};

# you can nest hashes in refs
my $nested_hash = {
  name => "Rehab",
  age => 45,
  fav_colors => ["blue", "pink", "red"],
  children => [
    {name => "Ali", age => 19},
    {name => "Obad", age => 17},
  ]
};


# that is the refrence location of that data type
print \%hash . "\n"; #> HASH(0xa000531f0)
print Dumper(@array);
print "------------------------\n";

# now we will debug the refrences using dupper and it gives us a normal array
print Dumper(\@array); #> ["one","two","three]
print Dumper(\%hash);
print "------------------------\n";

# refrences like hashes and arrays
print $ref_arr . "\n"; #> ARRAY(0xa00048b58)
print Dumper($ref_arr);
print Dumper($ref_hash);
# to access an element inside the hash for example you have to firstly derefrence the hash
print Dumper( $ref_hash->{name} ); #> $VAR1 = 'ali';
print Dumper( $ref_arr->[1] ); #> $VAR1 = 2;
# to dereference the reference
print Dumper( $ref_hash->%* );
print Dumper( @{$ref_arr } );
# print nested hash
print Dumper( $nested_hash );
print Dumper( $nested_hash->{children}->[0]->{'name'} );
# to know the data structure you are working with
print Dumper( ref($nested_hash->{children}) ); #> $VAR1 = 'HASH';




1;
