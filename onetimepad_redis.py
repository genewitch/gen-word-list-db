import binascii
import redis

#minwlength=5
maxwlength=4
wlength=0
wloopvar=0

charsrejected=0
charsaccepted=0
wordsrejected=0
wordsaccepted=0
wordy=""

r = redis.StrictRedis(host='localhost', port=6379, db=0)
key="work"

def checkdict(word):
        return r.sismember(key, word)

def hexint(b):
        return int(binascii.hexlify(b), 16)

def checkascii(char):
        check = hexint(char)
#       If you want caps too switch the next two lines
#       if ((check >= 65) and (check <=90)) or ((check >= 97) and (check <=122)):
        if ((check >= 97) and (check <=122)):
                return str(check)
        else:
                return -1

# i use `time python ../arbitraryrandom.py > /tmp/rnd/rdrand.out` and there's
# `ln -s /tmp/rnd/rdrand.out ~/sts/r` because sts is a PITA to use without a short
# generator filename. change whatever you want.

with open("/home/genewitch/sts/r", 'rb') as f:
        while True:
                bytte = f.read(1)
                if bytte == '' :
                        f.close()
                        break
                cab = checkascii(bytte)
                if (cab == -1):
                        charsrejected = charsrejected + 1

                else:
                        charsaccepted = charsaccepted + 1

                        if wloopvar > maxwlength - 1 :
                                if checkdict(wordy):
                                        wordsaccepted = wordsaccepted + 1
                                        print( wordy )
                                        wordy=""
                                        wloopvar = 0
                                else:
                                        wordsrejected = wordsrejected + 1

                        else:
                                wordy = wordy + cab
                                wloopvar = wloopvar + 1

print "wordsrejected"
print wordsrejected
print "wordsaccepted"
print wordsaccepted
print
print "charsaccepted"
print charsaccepted
print "charsrejected"
print charsrejected
print "-------------------------------"
print
