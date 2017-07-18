from rdrand import RdRandom
import sys
r = RdRandom()
i=0

#numstreams=256
#numbits=100000000
#bitsperfetch=100000

while i < 2 :
#while i < 1000 : #use with 10000 below to test
	i=i+1
	bytte = r.getrandbytes(125000000)
#	bytte = r.getrandbytes(10000) #use with while i < 1000 above to test
	sys.stdout.write(bytte)
#	binpk = format(bytte,'c')
#	print(binpk),
#	binar = format(bytte,'b')
#	print(binar)
#	print(format(r.getrandbits(8),'c')),

sys.stdout.flush()
