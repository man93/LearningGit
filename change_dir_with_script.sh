#!/bin/bash
#you can read path from user
# read var
#you can also give path as command line argument
#var=$1
var=/proc
function myprog() {
cd $var
}
myprog
