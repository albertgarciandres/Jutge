def is_prime(n):
    '''
    Requires a non negative integer n.
    Returns True when n is prime 
    Returns False when n is not prime
    '''
    if  n < 2:
        return False
    d = 2
    while d*d <= n:
        if n%d == 0:
            return False
        d += 1
    return True

def has_prime_chain(f, k):
    '''
    >>> has_prime_chain([6, 2, 3, 5, 2], 3)
    -1
    >>> has_prime_chain([6, 2, 3, 5, 2], 4)
    1
    >>> has_prime_chain([1, 2, 3, 4, 5, 7, 11], 3)
    4
    >>> has_prime_chain([2, 3, 4, 5, 6, 7], 1)
    3

    '''
    counter = 0
    posi= 0
    # where p stores the position of the number in the list 
    for p, num in enumerate(f):
        prime = is_prime(num)
        
        if prime:
            counter += 1
            if counter == 1:
                posi = p
        if not prime:
            if counter == k:
                return posi
            else:
                counter = 0

    if counter == k:
        return posi 
    
    else:
        return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
