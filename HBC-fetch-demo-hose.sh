#!/bin/bash
mvn exec:java -pl \
hbc-example \
-Dconsumer.key= \
-Dconsumer.secret= \
-Daccess.token= \
-Daccess.token.secret= \
> twitter.json

 tail -n2008 twitter.json \
|head -n2000 \
|  jq .text  \
| sed 's/\x00//g' \
|grep -v t.co \
|grep -P -v "[^\x01-\x7F]" \
| grep -v null \
>> ../twitter.text.txt
