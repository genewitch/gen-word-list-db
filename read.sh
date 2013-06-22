#!/bin/bash
set +x
if [ $# -eq 0 ];

        #no key specified
        then echo "error 1";

        # If key exists, read it
        elif [ -e /opt/tmpfs/$1 ];
        then echo $(cat /opt/tmpfs/$1);

        # Key does not exist
        else
        echo "error 11";
fi
