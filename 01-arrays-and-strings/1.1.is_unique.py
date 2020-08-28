def is_unique(s: str) -> bool:
    a = []
    
    for c in s:
        if c in d: return False
        else: d.append(c)

    return True
