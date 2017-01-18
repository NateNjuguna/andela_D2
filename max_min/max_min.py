def find_max_min(l):
	l.sort();
	return [l[0]] if l[0] is l[(len(l)-1)] else [l[0], l[(len(l)-1)]]
