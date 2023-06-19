from easyinput import read

word = read(str)                                                       # WE READ THE STRING

dict = {}                                                              # WE CREATE A DICTIONARY

while word is not None:                                                # WE LOOP
	if len(word) in dict:                                              # WE CHECK IF THE LENGTH OF THE WORD IS IN THE DICT
		dict[len(word)] += [word]                                      # WE ADD THE WORD TO THE DICT WITH ITS LENGHT
	else:                                                              # 
		dict[len(word)] = [word]                                       # WE ADD THE NEW WORD WITH ITS CORRESPONDING NEW LENGTH
		
	word = read(str)                                                   # WE READ THE NEXT STRING

for i in sorted(dict):                                                 # WE CREATE A LOOP FOR THE SORTED DICT
	if len(dict[i]) <= 1:                                              # IN CASE THE LENGHT OF THE DICT IS 1 OR SMALLER
		dict.pop(i)                                                    # WE ELIMINATE THE WORDS WITH LENGTH SMALLER OR 1

found = False                                                          # WE CREATE A VARIABLE AND RETURN IT FALSE

for t in sorted(dict):                                                 # WE CREATE A LOOP FOR THE NEW SORTED DICT
	if t == max(dict) and not found:                                   # WE CHECK FOR THE MAX LENGTH OF THE DICT
		print(" ".join(dict.get(t)))                                   # WE PRINT THE WORDS WITH THAT MAX LENGHT
		found = True                                                   # WE CHANGE THE VARIABLE TO TRUE
		
if not found:                                                          # IN CASE OF THE VARIABLE STILL BEING FALSE
	print("All words have different lengths")                          # WE PRINT NO WORDS WITH DIFFERENT LENGTHS
