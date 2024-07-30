def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    sortedNums = sorted(citations)
    cLen = len(citations)

    if cLen == 0:
        return 0

    for h in range(cLen, 0, -1):
        if sortedNums[cLen - h] >= h:
            break

    return h
