import binascii
import redis   #easy_install redis / pip install redis --user

#minwlength=5
maxwlength=7
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
#	If you want caps too switch the next two lines
#	if ((check >= 65) and (check <=90)) or ((check >= 97) and (check <=122)):
	if ((check >= 97) and (check <=122)):
		return str(check)
	else:
		return -1


# check redis:
print checkdict("ASJKDH")
print checkdict("abroad")
print "should read:\n False\n True\n redis test complete"

with open("/home/genewitch/sts/r", 'rb') as f:
	while True:
		bytte = f.read(1)

		if bytte == '' :
			f.close()
			break

		if ( checkascii(bytte) == -1 ):
			charsrejected = charsrejected + 1

		else:
			charsaccepted = charsaccepted + 1

			if wloopvar > maxwlength - 1 :
				if checkdict( wordy ):
					wordsaccepted = wordsaccepted + 1
					print( wordy )
					wordy=""
					wloopvar = 0
				else:
					wordsrejected = wordsrejected + 1
					#print ( wordy ) # debug, forgot the next two lines
					wloopvar = 0
					wordy = ""

			else:
				wordy = wordy + bytte
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
