def string_compression(s: str) -> str:
    store = [[s[0], 1]]

    j = 0
    for i in range(len(s)):
        if store[j][0] == s[i]:
            store[j][1] += 1
        else:
            j += 1
            store.append([s[i], 1])

    out = ""
    for i in range(len(store)):
        out += store[i][0] + str(store[i][1])

    return out if len(out) < len(s) else s
    
print(string_compression("aabcccccaaa"))
print(string_compression("abcaaa"))

# O(len(s)+len(store)) time, O(len(store)) space