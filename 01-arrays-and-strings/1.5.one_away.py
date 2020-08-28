def one_away(s1: str, s2: str) -> bool:
	if abs(len(s1) - len(s2)) > 1: return False
	
	i, j, diff = 0, 0, 0
	
	while diff < 2 and i < len(s1) and j < len(s2):
		if s1[i] != s2[j]:
			diff += 1
			if s1[i+1] == s2[j]: i += 1
			elif s1[i] == s2[j+1]: j += 1
		
		i += 1
		j += 1
		
	return diff < 2
