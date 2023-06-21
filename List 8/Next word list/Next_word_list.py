def next_word_list(w, f):
	'''
	>>> next_word_list('red', ['red','yellow','red','black','grey','red'])
	['yellow', 'black']
	>>> next_word_list('big', ['small','big'])
	[]
	>>> next_word_list('big' , ['big','small'])
	['small']
	>>> next_word_list('blue', ['green'])
	[]
	>>> next_word_list('blue', [])
	[]
	>>> next_word_list('red', ['red','red','red'])
	['red', 'red']
	'''
	result = []
	for i in range(len(f) - 1):
		if f[i] == w:
			result.append(f[i + 1])
	return result




if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
