class Solution:
    def checkDegreesBetweenTwoRoads(self, roads, r1, r2):
        connections = 0
        for road in roads:
            if road[0] == r1:
                if road[1] == r2:
                    connections += 1
            if road[0] == r2:
                if road[1] == r1:
                    connections += 1
        return connections

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # base case 1: no roads between vertices
        if len(roads) == 0:
            return 0

        # count edges at each vertex
        degrees = [0] * n
        for road in roads:
            for r in road:
                degrees[r] += 1

        # sort unique degrees in descending order
        uniqDegrees = sorted(list(set(degrees)), reverse=True)

        # base case 2: 1 road between 2 vertices
        if len(uniqDegrees) == 1:
            maxDeg, maxDeg2 = uniqDegrees[0], -1
        else:
            # identify highest and second highest degrees
            maxDeg, maxDeg2 = uniqDegrees[0], uniqDegrees[1]

        # count number of cities with highest and 2nd highest degrees
        highest, highest2 = [], []
        for i in range(len(degrees)):
            if degrees[i] == maxDeg:
                highest.append(i)
            if degrees[i] == maxDeg2:
                highest2.append(i)
        # print("highest: ", highest)
        # print("highest2: ", highest2)
        # print("maxDeg: ", maxDeg, " maxDeg2: ", maxDeg2)
        
        # 2 cases:
        #   case 1: if 1 with highest, check connections between highest and 2nd highest
        #   case 2: if multiple with highest, check connections between them
        lowestConnects = 1000000
        # case 1:   
        if len(highest) == 1:
            maxNode = highest[0]
            for node in highest2:
                numConnects = self.checkDegreesBetweenTwoRoads(roads, maxNode, node)
                if numConnects < lowestConnects:
                    lowestConnects = numConnects
            return maxDeg + maxDeg2 - lowestConnects
        # case 2:
        else:
            bestAnswer = -1
            for i in range(len(highest)):
                for j in range(i+1, len(highest)):
                    numConnects = self.checkDegreesBetweenTwoRoads(roads, highest[i], highest[j])
                    if maxDeg - numConnects + maxDeg > bestAnswer:
                        bestAnswer = maxDeg - numConnects + maxDeg
            return bestAnswer
