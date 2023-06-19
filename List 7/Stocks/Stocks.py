def total_stock(stk1,stk2):
    '''
    >>> stock_alice = {'orange':5, 'lemon':2, 'tangerine':1}
    >>> stock_bob = {'apple':3, 'orange':6, 'tangerine':1}
    >>> stock_alice_bob = total_stock(stock_alice, stock_bob)
    >>> stock_alice_bob == {'tangerine': 2, 'orange':11, 'lemon':2, 'apple':3} 
    True
    '''
    for x in stk1:
        if x in stk2:
            #stk2.update({x:stk1.get(x)+stk2.get(x)})
            stk2[x] += stk1[x]
        else:
            #stk2.update({x:stk1.get(x)})
            stk2[x] = stk1[x]
    return stk2
