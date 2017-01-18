
def words(string):
	l = string.replace('\t', ' ').replace('\n', ' ').split(' ')
	result = {}
	for w in l:
		try:
			w = int(w)
		except Exception:
			pass 
		if w is '':
			continue
		if result.get(w, None) is None:
			result[w] = 1
		else:
			result[w] = result[w] + 1
	return result
