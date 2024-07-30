def minimumDeletions(s):
    """
    :type s: str
    :rtype: int
    """
    # Search for ba, count berapa b yang ikut, terus tinggal ditambahin
    count_b = 0
    count_a = 0
    sLength = len(s)

    for i in range(sLength):
        if s[i] == 'a':
            count_a += 1
    
    substitutionCount = []
    for i in range(sLength):
        if s[i] == 'a':
            count_a -= 1
        
        substitutionCount.append(count_a + count_b)
        if s[i] == 'b':
            count_b += 1

    return min(substitutionCount)

s = "bba"
md = minimumDeletions(s)
print(md)