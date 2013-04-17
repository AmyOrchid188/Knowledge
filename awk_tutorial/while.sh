#!/usr/bin/awk -f
# interest1 - compute compound interest
# input: amount rate yesrs
# output: compounded value at the end of each year
{ i = 1
 print $3
  while( i <= $3 ) { 
        printf(" \t %.2f\n",$1 * ( 1 + $2 ) ^ i )
        i = i + 1       
}
}
