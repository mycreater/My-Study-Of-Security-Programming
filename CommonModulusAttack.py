def ExtendedGcd(a, b) :
    if a == 0 :
        return ( b, 0, 1 )
    else :
        gcd, x, y = ExtendedGcd( b % a, a)
        return ( gcd, y - int( b / a ) * x, x )

def Decrypt(c1, c2, e1, e2, N) :
    _, s1, s2 = ExtendedGcd(e1, e2)

    if s1 < 0 :
        _, c1, _ = ExtendedGcd(c1, N)
    elif s2 < 0 :
        _, c2, _ = ExtendedGcd(c2, N)

    m1 = pow( c1, abs(s1), N )
    m2 = pow( c2, abs(s2), N )

    m = ( m1 * m2 ) % N

    return chr(m)

if __name__ == '__main__' :
    m = ord('H')
    e1, e2 = 65537, 10007
    p, q = 'p', 'q'
    N = p * q
    c1 = pow( m, e1, N )
    c2 = pow( m, e2, N )

    result = Decrypt(c1, c2, e1, e2, N)
    print(str(result))