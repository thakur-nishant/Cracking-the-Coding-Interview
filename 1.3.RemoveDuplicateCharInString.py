def removeDuplicateChar(x):
    rr = list()
    for i in x:
        if not rr.__contains__(i):
            rr.append(i)
    return "".join(rr)


s = "aaaeaaabcddfsfewbebrwrwweabcd"
print(removeDuplicateChar(s))
