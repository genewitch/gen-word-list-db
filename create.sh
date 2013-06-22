#!/bin/bash
set +x
if [ $# -eq 0 ];

	#no key specified
	then echo "error 1";

	#key exists!
	elif [ -e /opt/tmpfs/$1 ];
	then echo "error 10";
	else
		if [ ${#2} -eq 0 ];
			#no value, call self with "0" as the parameter
			then ./$0 $1 "0";
		else echo $2 > /opt/tmpfs/$1;
		fi
fi
