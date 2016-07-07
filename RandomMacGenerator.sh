#!/bin/sh
# generate a random mac address for the qemu nic
printf 'DE:AD:BE:EF:%02X:%02X\n' $((RANDOM%256)) $((RANDOM%256))
MACADDR="52:54:00:$(dd if=/dev/urandom bs=512 count=1 2>/dev/null | md5sum | sed 's/^\(..\)\(..\)\(..\).*$/\1:\2:\3/')"; echo $MACADDR
