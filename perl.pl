# Usage:
# $ perl perl.pl - 5 > is_even.pl
#                ^ This is NOT the negative sign
#
# Now run the generated script:
# $ perl is_even.pl
# 0

use strict;
use warnings;

use Scalar::Util qw(looks_like_number);

if ( $#ARGV < 1 ) {
    die "Please enter a number to generate the is_even program.\n";
}

my $num = $ARGV[1];

if ( not looks_like_number($num) or $num != int $num ) {
    die "Please enter a valid number to generate the is_even program.\n";
}

$num = int $num;

sub printing {
    my $n = shift;
    print "if ( \$number == $n ) {\n";
    my $bool = ($n % 2 == 0) ? 1 : 0;
    print "    print \"$bool\\n\";\n}\n";
}

print "my \$number = $num;\n\n";

if ( $num < 0 ) {
    for (my $i = 0; $i >= $num; $i--) {
        printing ($i);
    }
    exit;
}

for (my $i = 0; $i <= $num; $i++) {
    printing ($i);
}

