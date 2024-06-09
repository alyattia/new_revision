#!/usr/bin/env perl

# scopes of variables

use strict;
use warnings;
use feature qw/ say /;

use Data::Dumper;


# map
my @list = (0..3);
my @new_list = map{
  # ($_) is the current item
  $_+= 10;
} @list;
print Dumper (\@new_list);
say "-" x 40;

# grep // it like compares
# it is like the filter in js
my @list2 = qw/ali obad mama/;
my @new_list2 = grep {
  $_ eq "ali";
} @list2;
print Dumper (\@new_list2);
say "-" x 40;


# split // genau so wie die split in JS
# the m/_/ is a patern that says split every "_"
my @parts = split m/_/, "ali_mama_obad";
print Dumper (\@parts);

# join // genau so wie die join in JS
my @parts2 = qw/a l i/;
my @new_parts2 = join "", @parts2;
print Dumper (\@new_parts2);
say "-" x 40;


# get the legnth of string
my $test = "cat";
my $size = length $test;
say "the length of the string is $size";

# random number and integer a value
my $rand_num = int( rand(10) );# between 0 and 10
say "the random number is $rand_num";

# stop the excution of code for the given seconds
say "hello before sleeping";
sleep 2;
say "hello after sleeping";
say "-" x 40;


#substring is like slicing in python
my $sub_string = substr( "abdullah", 0, 5);# like [:5] in python
say $sub_string;


# get the time 
say (time);






1;
