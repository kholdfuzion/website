Title: btrfs false disk full repair
Date: 03.07.2017 07:01
Category: Articles
Tags: btrfs, general, troubleshooting, repairs, disk, full

Recently I had to rebuild my local server due to a double drive failure in a raid 5 configuration. Thankfully everything I really cared about was backed up.

After recovering everything to a working state on hardware raid 10, btrfs started telling me that I was out of space on device. `df -h` showed plenty.



Turns out tools like df lie when using btrfs. they dont take into account the metadata. Thankfully it's btrfs so a fix isn't hard:

First add a second device, I used an 8gb jumpdrive which lived at /dev/sdf.

`sudo btrfs device add /dev/sdf /`

Second run a rebalance

`sudo btrfs fi balance start -musage=0 /`

`sudo btrfs fi balance start -dusage=0 /`

`sudo btrfs fi balance start -musage=1 /`

`sudo btrfs fi balance start -dusage=1 /`

`sudo btrfs fi balance start -musage=5 /`

`sudo btrfs fi balance start -musage=10 /`

`sudo btrfs fi balance start -musage=20 /`

`sudo btrfs fi balance start -dusage=5 /`

`sudo btrfs fi balance start -dusage=10 /`

`sudo btrfs fi balance start -dusage=20 /`

`sudo btrfs fi balance start -dusage=55 /`

`sudo btrfs fi balance start -musage=55 /` 

When thats done, btrfs will likely complain if you try to remove the extra drive if you're like me and have a hardware raid showing as a single device, as the usb drive is now hosting a mirror of your cleaned metadata. If so, you will have to rebalance the metadata back to a "single drive".


`sudo btrfs balance start -mconvert=single /`

After that completes, finish up with a simple

`sudo btrfs device remove /dev/sdf /`