# to allow permission to file as excutable otherwise it will tell you permission denied.
# to check that run > ls -la learn.pl
#!/usr/bin/env perl

# those lines allows you to write robust and less error code
# it gives you warning and so on
use strict;
use warnings;

# declaring a variable (scaler)
my $test = "test var";
my $my_num = 1;
my $my_dec = 2.5;

# you use "" as f"" in python
my $concatinated = "$test again";

print $my_dec + $my_num;
print "\n hello world\n";
print $test . " + concatination\n";
print "$test again\n";

# you can concatenate numbers with strings // it is smart enough and will convert the num to string
print "concatination of number $my_num and string $test\n";


# to send like a true when the script is executed successfully
1;

