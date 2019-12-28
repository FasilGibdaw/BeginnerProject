import cmath
# quadratic root solver developed by Fasil Tesema @ longyearbyen, Norway January 29 2019


def quad_root(a, b, c):
    det = b**2 - 4*a*c #determinat of the quadratic equation 
    if det == 0:
        r1 = -b/(2*a)
        r2 = r1
        print 'roots are equal'  # , '\n', r1
    elif det > 0:
        r1 = (-b+cmath.sqrt(det))/(2*a)
        r2 = (-b-cmath.sqrt(det))/(2*a)
        print 'roots are real'  # , '\n', r1, r2
    else:
        r1 = (-b+cmath.sqrt(det))/(2*a)
        r2 = (-b-cmath.sqrt(det))/(2*a)
        print 'roots are imaginary'  # , '\n', r1, r2
    return r1, r2


if __name__ == '__main__':
    print("roots are:", quad_root(1, 2, 3))

#r1, r2 = quad_root((1, 5, 9))
#print r1, r2
