#!/usr/bin/env perl

# the list is the data you assign to the array (the array is the actuall variable)

use strict;
use warnings;
use Data::Dumper;

# the array in perl is consisting of variables actually (more specific list of variables)
my @my_arr = (1, "ali", 1.4);
# if you have only a string array that's easier
my @string_arr = qw/one tow three array/;

print Dumper(@my_arr);
print "------------------------\n";
print Dumper(@string_arr);


# overriding and indexing
$string_arr[-1] = "overrieded";
# overriding a value more than the array's length that will make all variables before that
# index "undef" which is undefined
$string_arr[7] = "hahaa";

print "------------------------\n";
print Dumper("index 1 is @string_arr[0]");
# its like array[:3] in python
print Dumper(@string_arr[0 .. 3]);
print Dumper(@string_arr);
print "------------------------\n";


# getting the size of the array
# since you're defining a list to a scaler it takes the length of the list
my $size = @string_arr;
my $last_index = $#string_arr;

print Dumper("the length of the array is $size");
print Dumper("the last index is $last_index");
print "------------------------\n";


# Array methods and add ons

my @nums_arr = (1 .. 10);
# add el at the end of the list
push @nums_arr, 11;
# remove el fromt he end of the arr
pop @nums_arr;
# remove the first el of the list
shift @nums_arr;
# add el at the beginning of the list
unshift @nums_arr, 0;
# sorting STRINGS...
my @un_sorted = qw/b a c/;
@un_sorted = sort @un_sorted;
# sorting NUMERICAL VALUES...
my @un_sorted_nums = (4, 2, 1, 3);
@un_sorted_nums = sort @un_sorted_nums; # that's wrong bec it will sorted it as strings
# you should define a function to achieve that task
# the $a here is the first el you recieve and $b is the next item in the iteration
@un_sorted_nums = sort { $a <=> $b } @un_sorted_nums;

print Dumper(@nums_arr);
print Dumper(@un_sorted);
print Dumper(@un_sorted_nums);
print "------------------------\n";

1;
