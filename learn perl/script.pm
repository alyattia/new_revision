# that line is called shebang line it is used to make your file executable
# to check if your file is executable type > ls -la script.pl < in the terminal
# that's the expected output "-rwxr-xr-x"
# if not then you have to change mode by typing > chmod +x script.pl
#!/usr/bin/env perl

# those are pragmas
# those both show you errors and warnings
use strict;
use warnings;


print "Hello world\n";


# data types

# vars
my $test_num = 1;
my $test_str = "ali";
my $test_decimal = 0.5;

# vars are unic
# my test_num = 2

# print $test_num + $test_decimal;
# print $test_num - $test_decimal;
# print $test_num * $test_decimal;
# print $test_num / $test_decimal;


my $string1 = "yarab";
my $string2 = " wafa2na yarab";

print $string1 . $string2;

# this is a standard to return a true value of that script
1;
