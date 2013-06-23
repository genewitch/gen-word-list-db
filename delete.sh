#!/bin/bash
#set -x
if [ $# -eq 0 ];
  #no key specified
	then echo "0";
fi
	#key exists!
if [ -e /opt/tmpfs/$1 ];
# this has an unintended potential side effect
# i think "stat"ing a file in tmpfs may bounce it off swap
# if that should be where it lie. I may put this check after
# the next one if this side effect is both present and not desired.
	then
	echo $(rm /opt/tmpfs/$1);
fi
