def max_overlap(s, t):
    '''
    >>> max_overlap('bugs', 'bunny')
    'bu'
    >>> max_overlap('winter', 'winner')
    'win'
    >>> max_overlap('hand', 'made')
    ''
    >>> max_overlap('x', 'x')
    'x'
    '''
    
    last = min(len(s),len(t))
    i = 0
    while i < last and s[i] == t[i]:
        i = i + 1
    return s[0:i]
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
