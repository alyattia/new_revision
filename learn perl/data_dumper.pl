#!/usr/bin/env perl

# we use the "use" or "require" to ipmort modules
use strict;
use warnings;
# the data dumper module should be already installed
# data dumper is used to debug our code instead of using print
use Data::Dumper;


my $x = 1;
my $a = "hello world";

print Dumper($x, $a);



1;
