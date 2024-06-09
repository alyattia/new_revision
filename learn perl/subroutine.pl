#!/usr/bin/env perl

# a subroutine is exactly like a function in perl

use strict;
use warnings;
use Data::Dumper;
# to use subroutines signatures in your code
use feature qw/ signatures /;


my $a = "a";

sub test2 {
  print "from sub 2 ";
  test("ali");
}

sub test {
  # all the parameters are stored in that special charectre "@_"
  my @args = @_;
  my $name = $args[0] || "no name";
  print "Hallo $name\n";
}

sub plus {
  my @args = @_;
  # return $args[0] + $args[1];
  # will automatically return the result var
  my $result = $args[0] + $args[1];
}

# using subroutines signatures
sub signatures( $name = "no name" ) {
  print "hallo $name!\n";
}
# hash args
sub hash_args( %inputs ) {
  print Dumper \%inputs;
}
# many args
sub many_args( @inputs ) {
  print Dumper \@inputs;
}

test(test2);
print plus(5, 6) . "\n";
signatures("Rehab");
hash_args(a => 1, b => 2);
many_args(1, 2, 3);

1;
