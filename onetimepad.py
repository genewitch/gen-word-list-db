import binascii

minwlength=5
maxwlength=7
wlength=0
wloopvar=0

charsrejected=0
charsaccepted=0
wordy=""

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

with open("/home/genewitch/sts/r", 'rb') as f:
        while True:
                bytte = f.read(1)

                if (checkascii(bytte) == -1):
                        charsrejected = charsrejected + 1

                else:
                        charsaccepted = charsaccepted + 1

                        if wloopvar > maxwlength - 1 :
                                print( wordy )
                                wordy=""
                                wloopvar = 0

                        else:
                                wordy = wordy + bytte
                                wloopvar = wloopvar + 1
