def min_Max(m):
    '''
    >>> min_Max([[1,2,3],[3,1,2],[2,3,1]])
    [[1, 3], [1, 3], [1, 3]]
    >>> min_Max([[100]])
    [[100, 100]]
    >>> min_Max([[2,2],[2,2]])
    [[2, 2], [2, 2]]
    >>> min_Max([[17, 4],[1,1]])
    [[4, 17], [1, 4]]
    >>> min_Max([[5, 1, 2, 1, -2],[1,21,-1,-2,8],[2,3,1,6,6],[1,2,3,4,5]])
    [[-2, 5], [-2, 21], [1, 3], [1, 6]]
    '''
    mx = []
    for l in range(len(m)):
        # it will compute the minimum value of each row
        
        min_row = min(m[l])
        col_m = []

        # extracts elements of a column i
        for k in range(len(m)): 
            col_m.append(m[k][l])

        # it will compute the maximum value of each column
        max_col = max(col_m)       
        mx.append([min_row,max_col])

    return(mx)

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
	
