#!/bin/sh
read ter;
read tab;
cmd=`date`
for var in ter
do
gnome-terminal -t "rock" --tab -e "$cmd"
done


