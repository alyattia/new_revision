#!/usr/bin/env perl

# special variables

use strict;
use warnings;
use feature qw/ say /;

use Data::Dumper;


#> @ARGV 
#gives you the current args given to your script
# type "perl special_variables.pl ali" when you run the script and ["ali"] is the arg
say Dumper \@ARGV;


#> $$ 
# that is the process id of the script
say Dumper $$;


#> $]
# that is the perl version that excutes the script
say Dumper $];  


#> @INC
# the pathes to modules in our computer
say Dumper \@INC;  


#> %ENV
# those are the environment variables (decualt system variables)
# say Dumper \%ENV;  


#> __FILE__ and __LINE__ and __PACKAGE__
# print the our file's name line number and the package
say __FILE__;  
say __LINE__;  
say __PACKAGE__;  



1;
