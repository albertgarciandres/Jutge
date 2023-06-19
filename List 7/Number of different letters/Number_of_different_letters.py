def num_dif_letters_list(f:list):
    '''
    >>> num_dif_letters_list(['alea', 'iacta', 'est'])
    [3, 4, 3]
    >>> num_dif_letters_list(['', 'z', 'zz', 'zzz', 'zzzz'])
    [0, 1, 1, 1, 1]
    >>> num_dif_letters_list([])
    []
    >>> num_dif_letters_list(['atalaya', 'orinoco', 'pasas', 'elixir'])
    [4, 5, 3, 5]
    '''
    
    letters = []
    for i in f:
        letters.append(len(set(i)))
    return letters


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
