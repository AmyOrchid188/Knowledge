#!/usr/bin/awk -f
# interest2 - compute compound interest
# input: amout rate years
# output: compound value at the end of each year

{ for (i=1;i <= $3;i++){
    printf( "\t%.2f\n", $1 * (1+$2) ^i )
}
}
