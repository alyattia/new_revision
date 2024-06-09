# pm stands for perl module
package Dog;

use strict;
use warnings;

# when creating an instance of that class you will call that function
sub new {
  # those are like the attributes and the class attr is automatically the package name which is here "Dog"
  my ($class, $type, $height, $weight, $color, $name) = @_; 
  my $self = {
    type => $type,
    height => $height,
    weight => $weight,
    color => $color,
    name => $name,
  };

  # that simply says that this self belongs to that class
  bless $self, $class;

  return $self;
}

# make the getters function to get the class attributes
sub get_type {
  # that is the self
  # $VAR1 = bless( {
  #                'height' => 50,
  #                'name' => 'eyad',
  #                'color' => 'blue',
  #                'type' => 'labrador',
  #                'weight' => 70
  #              }, 'Dog' );
  # shift is getting the first el in the array
  my $self = shift @_;
  return $self->{type};
}
sub get_name {
  # shift is getting the first el in the array
  my $self = shift @_;
  return $self->{name};
}
sub get_color {
  # shift is getting the first el in the array
  my $self = shift @_;
  return $self->{color};
}
sub get_height {
  # shift is getting the first el in the array
  my $self = shift @_;
  return $self->{height};
}
sub get_weight {
  # shift is getting the first el in the array
  my $self = shift @_;
  return $self->{weight};
}

# setters
sub set_type {
  my ($self, $type) = @_;
  $self->{type} = $type;
  # return 1;
}

#the destroy runs at the end anyways
sub DESTROY {
  print 'bye bye everyone!\n';
}


1;
