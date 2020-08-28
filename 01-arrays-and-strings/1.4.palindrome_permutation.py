def palindrome_permutation(s: str) -> bool:
	s = s.replace(" ","")
	
	d = {}
	for c in set(s):
		d.update({c: 0})
		
	for c in s:
		d[c] += 1
		
		if d[c] == 2:
			s = s.replace(c,"",2)
	
	return len(s) < 2

