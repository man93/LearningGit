#!/bin/bash
gnome-terminal --tab -e "bash -c '{ cd /home/manjul/programs; vi test.cpp; }';bash" --tab -e "bash -c 'cal';bash" --tab -e "bash -c 'date';bash" --tab -e "bash -c 'who';bash" --tab -e "bash -c 'ping 127.0.0.1';bash" --tab -e "bash -c 'netstat';bash" --tab -e "bash -c '{ date; cal; }';bash"
