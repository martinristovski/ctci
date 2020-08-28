def check_permutation(s1: str, s2: str) -> bool:
	for c in s1:
		if c not in s2:
			return False
		s2.replace(c,"",1)
			
		if len(s2) != 0: return False

	return True

