#!/bin/bash
#set -x
if [ $# -eq 0 ];
  #no key specified
	then echo "error 1";
fi
	#key exists!
if [ -e /opt/tmpfs/$1 ];
#this has an unintended potential side effect
# i think stating a file in tmpfs may bounce it off swap
# if that should be where it lie. I may put this check after
# the next one if this side effect is both present and not desired.
	then
	if [ ${#2} -eq 0 ];
		#no value!
		then echo "error 100";

		else echo $2 > /opt/tmpfs/$1;
	fi;

	# Key does not exist
	else echo "error 11";
fi
