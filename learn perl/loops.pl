#!/usr/bin/env perl

# Loops

use strict;
use warnings;
use Data::Dumper;
use feature qw/ say /;

# while loop
my $var = 0;
while ($var < 3) {
  say "while loop> $var";
  $var++;
}
say "-" x 40;

# for loop
for (my $var2 = 0; $var2 < 3; $var2++) {
  say "for loop> $var2";
}
say "-" x 40;

# for each loop
# also in the foreach any changes you do on the item it actually do it in the original loop
my $list = ["ali", "obad", "roby"];
foreach my $item ($list->@*) {
  say "for each> $item";
  $item = $item . " overrided";
}

# keywords in arrays:
#> next: like continue in py and js
#used as follows > next if $item == "value";
#> last: like break
#used as follows > last if $item == "value";
#> redo: used to restart the current iteration
#used as follows > redo if $item == "value";
#> goto: use it if you are naming loops
# Loop1:
# foreach my $item ($list->@*) {
#   goto Loop2 if $item ==2;
#   say "hello from loop: $item";
#   Loop2:
#   foreach my $nested_item ($list->@*) {
#     say "hi nested $nested_item";
#   };
# }


say "-" x 40;
print Dumper($list);



1;
