# Code out your function definitions here

# the offset is 0 if user forgets to input
def encode(inp, off = 0):
    ret = ""
    temp = inp.lower()
    for i in temp:
        if i == " ": 
            ret += " "
            continue
        if i.isalpha():
            ret += chr((ord(i) + off - 97) % 26 + 97)
        else: 
            ret += chr((ord(i) + off - 33) % 30 + 33)
    for i in inp: 
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": 

            ret = ret[: inp.index(i)] + ret[inp.index(i)].upper() + ret[inp.index(i) + 1:]
    return ret
    
def decode(inp, off):
    ret = ""
    temp = inp.lower()
    for i in temp:
        if i == " ": 
            ret += " "
            continue
        if i.isalpha():
            ret += chr((ord(i) - off - 97) % 26 + 97)
        else: 
            # print(i.encode())
            ret += chr((ord(i) - off - 33) % 30 + 33)
    for i in inp:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": 
            # print(ret[inp.index(i)], ret[inp.index(i)].upper())
            ret = ret[: inp.index(i)] + ret[inp.index(i)].upper() + ret[inp.index(i) + 1:]
    return ret
    
    
print(encode("Python is fun!)", 8))
print(decode(encode("Python is fun!)", 8), 8))