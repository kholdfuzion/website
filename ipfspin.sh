#!/bin/sh

#check for something passed as arg1, hope its a CID hash...
if [ -z "$1" ]; then
    echo "No CID supplied"
    exit 1
fi

#yay there was an argument, lets let user know what we are doing as if they didn't know
echo pinning $1

#do ipfs1
echo ipfs1 start
ssh ipfs@192.168.1.106 "ipfs pin add $1"
echo ipfs1 end

#do ipfs2
echo ipfs2 start
ssh ipfs@192.168.1.170 "ipfs pin add $1"
echo ipfs2 end

#do ipfs3
echo ipfs3 start
ssh ipfs@192.168.1.141 "ipfs pin add $1"
echo ipfs3 end

