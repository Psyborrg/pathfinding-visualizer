# File where the implementation of Dijkstras will take place in python
import time

# How does dijkstras work?
# Need to get from one node to another, find shortest path
# has a stack of nodes that need to be visited, starting node has a dist of zero and all others begin with infinity
# Pops nodes off the stack one by one in order of lowest distance, when they get popped off: get the distance for every adjacent node
# The node that gets popped off moves to the "visited" heap
# continue until you reach the finish node

visitedNodes = []
nodesToVisit = []
# Stole this number from java to use as our "infinity"
bigNumber = 2147483647

def initializeDijkstras(grid, startX, startY, finishX, finishY):

    print("Initializing board for Dijkstras")

    for i,row in enumerate(grid):
        for j,column in enumerate(row):

            node = grid[i][j]

            # Add the index of the node node to the nodesToVisit list
            # The index is separated by a comma
            nodesToVisit.append(node)

            # If the start node, set distance to 0
            if i == startX and j == startY:
                node.distance = 0
                node.isStart = True
                node.prevNode = node # Start node has a prevNode of itself
                node.widget['bg'] = 'green'
            
            # If its the finish Node, set the isFinish field to true
            elif i == finishX and j == finishY:
                node.distance = bigNumber
                node.isFinish = True
                node.prevNode = None
                node.widget['bg'] = 'brown'
            
            else:
                # Distance for non-start nodes begins at the max value
                node.distance = bigNumber
                node.prevNode = None
                #add check for passable terrain
                if node.isPassable:
                    node.widget['bg'] = 'grey'
                else:
                    node.widget['bg'] = 'black'            

# Actual method for the dijkstras algorithm, to be done recursively 
def dijkstrasRecursion(grid, root):

    # Sort the list of nodes to visit by their distance
    nodesToVisit.sort(key=sortByDistance)
    # Pop the visited node off the stack
    currNode = nodesToVisit.pop(0)
    # Add the node to the list of visited Nodes
    visitedNodes.append(currNode)

    # Base case, did we just pop the finish Node?
    if currNode.isFinish == True:
        # Do the backtracking to find the solution path
        backtrack(currNode)
        return


    # If there is no path, one of the infinite distance nodes will be popped
    # Just return and display that there is no path
    elif currNode.distance == bigNumber:
        print("There is no path!")
        return


    # If not the finish node:
    # update the distances for all of the adjacent nodes, call this again
    else:
        # Directions that a node can travel in this version, no diagonals
        moves = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # For each direction, try editing the distance for that node
        for move in moves:
            newRow = currNode.row + move[0]
            newCol = currNode.col + move[1]

            # If the new row or column is outside the bounds, skip it
            if newRow < 0 or newRow >= len(grid):
                continue
            if newCol < 0 or newCol >= len(grid[currNode.row]):
                continue
            
            # Get the adjacent Node and its new Distance
            adjNode = grid[newRow][newCol]
            newDist = currNode.distance + adjNode.weight

            # If the adjacent node is a wall, dont update it
            if adjNode.isPassable == False:
                continue

            # If this is a better path than before, update the distance and previous Node
            if adjNode.prevNode == None or adjNode.distance > newDist:
                adjNode.distance = currNode.distance + adjNode.weight
                adjNode.prevNode = currNode
            
        # Change the color of the newly visited Node
        currNode.widget['bg'] = 'red'
        root.update()
        time.sleep(.1)

        dijkstrasRecursion(grid, root)


def backtrack(node):
    node.widget['bg'] = 'yellow'

    if node.prevNode == node:
        print("reached the begining")
        return
    else:
        backtrack(node.prevNode)


def sortByDistance(node):
    return node.distance






















# def initializeDijkstras(grid, startX, startY, finishX, finishY):
#     for i,row in enumerate(grid):
#         for j,column in enumerate(row):
#             nodesToVisit.append(grid[i][j])
#             grid[i][j].distance = float('inf')
#             grid[i][j].prevNode = None
#             grid[i][j].distance = float('inf')
    
#     # Initialize the current Node
#     grid[startX][startY].isStart = True
#     global currNode
#     currNode = grid[startX][startY]

#     # Initialize the finish Node
#     grid[finishX][finishY].isFinish = True


# def dijkstras(grid, frame):
#     global currNode

#     # Sort the list of nodes to visit by their distance
#     nodesToVisit.sort(key=sortByDistance)
#     # Pop the visited node off the stack
#     currNode = nodesToVisit.pop(0)
#     # Add the node to the list of visited Nodes
#     visitedNodes.append(currNode)

#     # Get the adjacent Node distances
#     moves = [
#         (1, 1),
#         (1, -1),
#         (-1, 1),
#         (-1, -1)
#     ]

#     # For each direction, try editing the distance for that node
#     for move in moves:
#         try:
#             # Get the adjacent Node and its new Distance
#             adjNode = grid[currNode.row + move[0], currNode.col + move[1]]
#             newDist = currNode.distance + adjNode.weight

#             # If this is a better path than before, update the distance and previous Node
#             if adjNode.prevNode == None or adjNode.distance > newDist:
#                 adjNode.distance = currNode.distance + adjNode.weight
#                 adjNode.prevNode = currNode
#         except:
#             continue

#     # Change the color of the newly visited Node
#     currNode.widget['bg'] = 'red'
   

# def sortByDistance(node):
#     return node.distance

