import sys
import math
import random

def IsPrime(n) :
    if n == 2 :
        return True
    if n % 2 == 0 :
        return False
    for i in range(3, n) :
        if math.sqrt(n) < i :
            return True
        if n % i == 0 :
            return False

def GeneralPublicKey(p, q) :
    e = 65537
    n = p * q
    return e, n

def Encrypt(text, p, q) : 
    e, n = GeneralPublicKey(p, q)
    text = list(text)
    cipher = []

    for i in text :
        c = pow(i, e, n)
        cipher.append(c)
    return cipher

if __name__ == '__main__' :
    p, q = 0, 0
    while ( p == q ) or not IsPrime(p) or not IsPrime(q) :
        p = random.randint( 10**5, 10**6 )
        q = random.randint( 10**5, 10**6 )
    
    print('p:' + str(p))
    print('q:' + str(q))
    
    f_txt = open(sys.argv[1], 'rb')
    text = f_txt.read()
    f_txt.close()

    result = Encrypt(text, p, q)
    print(str(result))
   