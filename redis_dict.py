import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
key="work"

#   put your own dict file in, this one is on some systems:
with open("/usr/share/dict/cracklib-small", 'rb') as f:
        for line in f:
                r.sadd(key, line.strip()) #gets rid of \n in values and adds to redis set
f.close()
