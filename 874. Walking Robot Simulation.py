import math

def robotSim(commands, obstacles):
    """
    :type commands: List[int]
    :type obstacles: List[List[int]]
    :rtype: int
    """
    currentPos = [0, 0]
    maxEuclid = math.trunc(currentPos[0] * currentPos[0] + currentPos[1] * currentPos[1])

    robotDirection = (0, 1)
    obstacleSet = set((i,j) for i,j in obstacles)

    for c in commands:
        if c > 0:
            # Move to a direction

            initialPos = currentPos
            for _ in range(c):
                if (currentPos[0] + robotDirection[0], currentPos[1] + robotDirection[1]) in obstacleSet:
                    break
                
                currentPos = (currentPos[0] + robotDirection[0], currentPos[1] + robotDirection[1])

                # currentPos = (currentPos[0] + robotDirection[0] * c, currentPos[1] + robotDirection[1] * c)
                
                # for o in obstacles:
                #     if initialPos[0] == currentPos[0] and initialPos[0] == o[0]:
                #         # If the obstacle is in the middle of the current and initial, then change it
                #         if (initialPos[1] < o[1] and o[1] <= currentPos[1]):
                #             currentPos = (o[0], o[1]-1)
                #         if  (initialPos[1] > o[1] and o[1] >= currentPos[1]):
                #             currentPos = (o[0], o[1]+1)

                #     elif initialPos[1] == currentPos[1] and initialPos[1] == o[1]:
                #         if (initialPos[0] < o[0] and o[0] <= currentPos[0]):
                #             currentPos = (o[0]-1, o[1])
                #         if (initialPos[0] > o[0] and o[0] >= currentPos[0]):
                #             currentPos = (o[0]+1, o[1])

            print("Initial Pos: ", initialPos)
            print("Current Pos: ", currentPos)
            print("Robot Direction: ", robotDirection)

            maxEuclid = max(maxEuclid, math.trunc(currentPos[0] ** 2 + currentPos[1] ** 2))
            print("Max Euclid: ", maxEuclid)
            print()

        elif c < 0:
            # Change direction
            if c == -1:
                print("Turn right")
                print()
                # Turn right 90 degrees
                if robotDirection[0] == 0:
                    robotDirection = (robotDirection[1], 0)
                elif robotDirection[1] == 0:
                    robotDirection = (0, -robotDirection[0])

            elif c == -2:
                print("Turn left")
                print()
                # Turn left 90 degrees
                if robotDirection[0] == 0:
                    robotDirection = (-robotDirection[1], 0)
                elif robotDirection[1] == 0:
                    robotDirection = (0, robotDirection[0])
    
    return maxEuclid


print(robotSim([1,2,-2,5,-1,-2,-1,8,3,-1,9,4,-2,3,2,4,3,9,2,-1,-1,-2,1,3,-2,4,1,4,-1,1,9,-1,-2,5,-1,5,5,-2,6,6,7,7,2,8,9,-1,7,4,6,9,9,9,-1,5,1,3,3,-1,5,9,7,4,8,-1,-2,1,3,2,9,3,-1,-2,8,8,7,5,-2,6,8,4,6,2,7,2,-1,7,-2,3,3,2,-2,6,9,8,1,-2,-1,1,4,7], 
               
               [[-57,-58],[-72,91],[-55,35],[-20,29],[51,70],[-61,88],[-62,99],[52,17],[-75,-32],[91,-22],[54,33],[-45,-59],[47,-48],[53,-98],[-91,83],[81,12],[-34,-90],[-79,-82],[-15,-86],[-24,66],[-35,35],[3,31],[87,93],[2,-19],[87,-93],[24,-10],[84,-53],[86,87],[-88,-18],[-51,89],[96,66],[-77,-94],[-39,-1],[89,51],[-23,-72],[27,24],[53,-80],[52,-33],[32,4],[78,-55],[-25,18],[-23,47],[79,-5],[-23,-22],[14,-25],[-11,69],[63,36],[35,-99],[-24,82],[-29,-98],[-50,-70],[72,95],[80,80],[-68,-40],[65,70],[-92,78],[-45,-63],[1,34],[81,50],[14,91],[-77,-54],[13,-88],[24,37],[-12,59],[-48,-62],[57,-22],[-8,85],[48,71],[12,1],[-20,36],[-32,-14],[39,46],[-41,75],[13,-23],[98,10],[-88,64],[50,37],[-95,-32],[46,-91],[10,79],[-11,43],[-94,98],[79,42],[51,71],[4,-30],[2,74],[4,10],[61,98],[57,98],[46,43],[-16,72],[53,-69],[54,-96],[22,0],[-7,92],[-69,80],[68,-73],[-24,-92],[-21,82],[32,-1],[-6,16],[15,-29],[70,-66],[-85,80],[50,-3],[6,13],[-30,-98],[-30,59],[-67,40],[17,72],[79,82],[89,-100],[2,79],[-95,-46],[17,68],[-46,81],[-5,-57],[7,58],[-42,68],[19,-95],[-17,-76],[81,-86],[79,78],[-82,-67],[6,0],[35,-16],[98,83],[-81,100],[-11,46],[-21,-38],[-30,-41],[86,18],[-68,6],[80,75],[-96,-44],[-19,66],[21,84],[-56,-64],[39,-15],[0,45],[-81,-54],[-66,-93],[-4,2],[-42,-67],[-15,-33],[1,-32],[-74,-24],[7,18],[-62,84],[19,61],[39,79],[60,-98],[-76,45],[58,-98],[33,26],[-74,-95],[22,30],[-68,-62],[-59,4],[-62,35],[-78,80],[-82,54],[-42,81],[56,-15],[32,-19],[34,93],[57,-100],[-1,-87],[68,-26],[18,86],[-55,-19],[-68,-99],[-9,47],[24,94],[92,97],[5,67],[97,-71],[63,-57],[-52,-14],[-86,-78],[-17,92],[-61,-83],[-84,-10],[20,13],[-68,-47],[7,28],[66,89],[-41,-17],[-14,-46],[-72,-91],[4,52],[-17,-59],[-85,-46],[-94,-23],[-48,-3],[-64,-37],[2,26],[76,88],[-8,-46],[-19,-68]]))