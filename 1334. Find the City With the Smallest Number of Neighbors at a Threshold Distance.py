n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4

def findTheCity(n, edges, distanceThreshold):
    """
    :type n: int
    :type edges: List[List[int]]
    :type distanceThreshold: int
    :rtype: int
    """
    cities_can_be_visisted = {}
    for i in range(n):
        cities_can_be_visisted[i] = {}

    def findNeighboringCity(searching, starting, m):
        for e in edges:
            # print(searching, starting, m)
            if e[0] == starting and e[2] <= m and e[1] != searching:
                cities_can_be_visisted[searching][e[1]] = True
                findNeighboringCity(searching, e[1], m - e[2])
            if e[1] == starting and e[2] <= m and e[0] != searching:
                cities_can_be_visisted[searching][e[0]] = True
                findNeighboringCity(searching, e[0], m - e[2])
        return 

    for e in edges:
        findNeighboringCity(e[0], e[0], distanceThreshold)
        findNeighboringCity(e[1], e[1], distanceThreshold)
        # print()

    min = 101
    city_min = 0
    for idx in range(n):
        # print("Length: ", len(cities_can_be_visisted[idx]))
        if (len(cities_can_be_visisted[idx]) <= min):
            min = len(cities_can_be_visisted[idx])
            city_min = idx
    
    # print(city_min)
    return city_min

findTheCity(n, edges, distanceThreshold)