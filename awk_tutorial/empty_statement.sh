#!/usr/bin/awk -f
# learn empty statement. A semicolon by itself denotes the empty statement.
  BEGIN { FS = "\t" }
        { for (i=1;i<=NF&&$i!="";i++)
              ;
            if (i<=NF)
             print
        }
