def max2freq(numbers):
    '''
    >>> print(max2freq([ 40, 30, 40, 32, 41, 10, 41, 31, 31, 40, 41, 40, 41, 30, 32, 32, 30, 31, 11 ]))
    ([40, 41], [30, 31, 32])
    >>> max2freq([ 20, 20, 10, 30, 30, 21, 21, 30 ])
    ([30], [20, 21])
    '''
    freq = {}
    for x in numbers:
        if x not in freq:
            freq[x] = 1
        else:
            freq[x] += 1

    n = 0
    m = 0
    for x in freq:
        if freq[x] > n:
            m = n
            n = freq[x]
        elif freq[x] != n and freq[x] > m:
            m = freq[x]

    listatop = []
    listasec = []
    for x in freq:
        if freq[x] == n:
            listatop.append(x)
        elif freq[x] == m:
            listasec.append(x)
    return sorted(listatop), sorted(listasec)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
