def isUniqueCharacterString(s):
    temp = {}
    for i in s:
        if i in temp:
            return False
        else:
            temp[i] = True

    return True

s = 'test'
x = isUniqueCharacterString(s)
print(s,'=',x)
