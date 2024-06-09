#!/usr/bin/env perl

# use vs require: use is used in using a module at compile time while require is requiring
# a module at runtime

use strict;
use warnings;
use Data::Dumper; # "Data/Dumper.pm"

# firstly the use is used before anyother code is executed if you wrote the code before it
# so the use is used in the BEGIN section (compile time)

# actually when you use the "use" statement it maces as follows
# use Data::Dumper
BEGIN {
  require "Data/Dumper.pm";
}




1;
