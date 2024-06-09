#!/usr/bin/env perl

# Regular expression

use strict;
use warnings;
use feature qw/ say /;

use Data::Dumper;

my $test = "cat"; # /cat/
my $test2 = "cat/"; # /cat\//
my $test3 = "cat/"; # /cat\// or m{cat/}

if ($test3 =~ m{cat/}) {
  say "Regex matches";
}else {
  say "does not match";
}






1;
