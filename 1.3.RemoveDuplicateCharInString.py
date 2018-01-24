def removeDuplicateChar(s):
    n = len(s)
    i=0
    dic = {}
    while n > 0:
        if s[i] in dic:
            s = s[:i] + s[i+1:]
        else:
            dic[s[i]] = 1
            i += 1
        n -= 1
    return s


s = "aaaeaaabcddfsfewbebrwrwweabcd"
print(removeDuplicateChar(s))

