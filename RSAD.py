import sys

def ExtendedGcd(a, b) :
    if a == 0 :
        return (b, 0, 1)
    else :
        gcd, x, y = ExtendedGcd( b % a, a )
        return gcd, y - int( b / a ) * x, x

def GeneralPrivateKey(e, N) :
    gcd, d, y = ExtendedGcd( e, N )
    if d < 0 :
        d += N
    return d

def Decrypt(cipher, p, q) :
    e = 65537
    n = p * q
    N = ( p - 1 ) * ( q - 1 )
    plain = []

    d = GeneralPrivateKey(e, N)

    for c in cipher :
        m = pow(c, d, n)
        plain.append(chr(m))
    
    return ''.join(plain)

if __name__ == '__main__' :
    p = ' p of RSAE.py '
    q = ' q of RSAE.py '
    cipher = ' cipher of RSAE.py'
    result = Decrypt(cipher, p, q)
    print(str(result))
