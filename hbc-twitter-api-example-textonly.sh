#!/bin/bash

#needs HBC. don't remember where i got it, i will update later.

mvn exec:java -pl \
hbc-example \
-Dconsumer.key=UyJ6RDJ0kKa4FWn67792fLCtN \
-Dconsumer.secret=fo6w2Vv8AcvpybUoooBi382pP01EaldypKhODUsasnFrxlqEk2 \
-Daccess.token=28719900-XaZ4gB2UIoxXv1BAn1e29u5k4H9vucFLV4G5GnVGZ \
-Daccess.token.secret=Z5NL78WHh7alOKbrYNoxDN5hAGtgHnV5BnzDrQSVhAGM8 \
> twitter.json

 tail -n2008 twitter.json \
|head -n2000 \
|  jq .text  \
| sed 's/\x00//g' \
|grep -v t.co \
|grep -P -v "[^\x01-\x7F]" \
| grep -v null \
>> ../twitter.text.txt
