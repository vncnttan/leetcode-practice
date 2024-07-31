def minHeightShelves(books, shelfWidth):
    """
    :type books: List[List[int]]
    :type shelfWidth: int
    :rtype: int
    """
    n = len(books)
    dp = [float('inf')] * (n + 2)
    dp[0] = 0

    for i in range(1, n+1):
        width = height = 0

        for j in range(i-1, -1, -1):
            width += books[j][0]
            if width > shelfWidth:
                break

            height = max(height, books[j][1])
            dp[i] = min(dp[i], dp[j] + height)
            # print(f"\t{dp[:10]}")

        # print(dp[:10])
    return dp[n]

books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth = 4
res = minHeightShelves(books, 4)
print(res)