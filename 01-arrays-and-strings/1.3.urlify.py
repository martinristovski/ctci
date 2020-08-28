def urlify(s: str, l: int) -> str:
	return s[0:l].replace(" ", "%20")

print(urlify("Mr John Smith           ", 13))
