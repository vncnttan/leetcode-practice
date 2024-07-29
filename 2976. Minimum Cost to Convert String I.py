def minimumCost(source, target, original, changed, cost):
    minCost = 0

    dist = [[float('inf') for _ in range(26)] for _ in range(26)]
    for i in range(len(cost)):
        dist[ord(original[i]) - ord('a')][ord(changed[i]) - ord('a')] = cost[i]

    for i in range(26):
        dist[i][i] = 0
    
    for k in range(26):
        for i in range(26):
            for j in range(26):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


    for (s, t) in zip(source, target):
        if s != t:
            minCost += dist[ord(s) - ord('a')][ord(t) - ord('a')]
    return minCost

source = "abcd"
target = "acbe"
original = ["a"]
changed = ["e"]
cost = [10000]

min_cost = minimumCost(source, target, original, changed, cost)
print(min_cost)