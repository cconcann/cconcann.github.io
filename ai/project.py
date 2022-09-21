#from operator import truediv
#from os import getresuid
from queue import PriorityQueue
from string import whitespace
#from turtle import window_height
import matplotlib
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import math
 

class node: #node class
    def __init__(self, row, col, weight): #sets the args for a node, has to include self, then the row and colummn, and the int inside
         self.row = row
         self.col = col
         self.neighbors= []
         self.weight = weight
         self.visited = 0

    def getPos(self):
        return self.row, self.col

    def getWeight(self):
        return self.weight

    def isClosed(self):
        return self.visited == 1

    def isOpen(self):
        return self.visited == 0

    def isBarrier(self):
        return self.weight == 0

    def visualizePath(self): #not sure if i need this
        pass

    def updateNeighbors(self, grid): #used to know whats around the node for expansion
        self.neighbors = [] #creates an array to store the neighbros when expanded

        if self.row < len(grid) - 1 and grid[self.row + 1][self.col] != 0: #down
            self.neighbors.append([self.row + 1, self.col])

        if self.row > 0 and grid[self.row - 1][self.col] != 0: #up
            self.neighbors.append([self.row - 1, self.col])

        if self.col > 0 and grid[self.row][self.col - 1] != 0: #left
            self.neighbors.append([self.row, self.col - 1])

        if self.col < len(grid[0]) - 1 and grid[self.row][self.col + 1] != 0: #right
            self.neighbors.append([self.row, self.col + 1])

   



#def genGrid(size, max_cost=9):
    """ Generates a grid with random values in range [0,max_cost] where 0s represent obstacle cells and 1-max_cost represent the step cost to move onto the cell from any neighbor.
 
    Parameters:
        size (int): The number of rows and columns to use
        max_cost (int): The max step cost to move onto a cell in the grid
        
    Returns:
        2D list: The randomly generated grid
    """
    
#    num_rows = size
#    num_cols = size
    
#    grid = [[0]*num_cols for i in range(0,num_rows)]
    
    # ob_cost = 0
    # ob_prob = 0.2
    
    # for i_r in range(0,num_rows):
    #         for i_c in range(0,num_cols):
                    
    #                 # Default to obstacle cost
    #                 cost = ob_cost
                    
    #                 # Chance to be an obstacle
    #                 chance = random.random()
    #                 if chance > ob_prob:
    #                         # Generate a random cost for the location
    #                         cost = random.randint(1,max_cost)
                            
    #                 grid[i_r][i_c] = cost
 
    # return grid


 
def labelTile(grid, r, c, ax, text):
    """ Puts a character onto a grid cell, and changes text color based on cell color
        
    Parameters:
        grid (2D list): The grid to visualize
        r (int): The row of the cell to label
        c (int): The column of the cell to label
        text (string): The text to put onto the grid cell
        
    Returns:
        None
    """
    if grid[r][c] <= 3:
        ax.text(c, r, text, color="white", ha='center', va='center' )
    else:
        ax.text(c, r, text, color="black", ha='center', va='center' )
 
 
 
def visualizeGrid(grid, path=False, block=False, max_cost=9):
    """ Displays the grid as a grayscale image where each cell is shaded based on the step cost to move onto it. 
            
    Parameters:
            grid (2D list): The grid to visualize
            path (2D list): The path to visualize.
            block (bool): True if pyplot.show should block program flow until the window is closed
            max_cost(int): Maximum step cost to move onto any cell in the grid
            
    Returns:
            None
    """
    tempGrid = []
 
    # Flip the values so that darker means larger cost
    for r in grid:
            row = []
            for col in r:
                    if col != 0:
                        col = (max_cost+1) - col
                    row.append(col)
            tempGrid.append(row)
            
                    
    # Create colors
    cmap = matplotlib.cm.gray
    norm = colors.Normalize(vmin=0,vmax=max_cost)
    
    # Call imshow
    fig, ax = plt.subplots()
    ax.imshow(tempGrid, interpolation="none", cmap=cmap, norm=norm)
 
    # Put a 'p' character for each path position
    for i,loc in enumerate(path):
        if i == 0:
            labelTile(tempGrid, loc[1], loc[0], ax, "S")
        elif i == len(path)-1:
            labelTile(tempGrid, loc[1], loc[0], ax, "G")
        else:
            labelTile(tempGrid, loc[1], loc[0], ax, "p")
 
    
    if len(grid) <= 20:
        # Set ticks
        tickInc = 1
    else:
        tickInc = int(len(grid) / 10)
 
    ax.set_xticks(np.arange(0, len(grid)+1, tickInc))
    ax.set_yticks(np.arange(0, len(grid[0])+1, tickInc))
    ax.set_xticklabels(np.arange(0,len(grid)+1, tickInc))
    ax.set_yticklabels(np.arange(0,len(grid[0])+1, tickInc))
 
    plt.show(block=False)

def readGrid(filename):
    """ Reads a grid from a file and returns it as a 2D list. The grid values must be separated by spaces, e.g.,
    1 1 1 1 1 
    1 0 0 0 1
    1 0 0 0 1
    1 1 1 1 1
 
    Args:
        filename (string): the filename to read from
    Return:
        list: 2D list where each cell stores the value of the grid at that location
    """
    #print('In readGrid')
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])
            #this im pretty sure is where i create the Nodes
    
    f.close()
    #print 'Exiting readGrid'
    return grid
 
 
def outputGrid(grid, start, goal, path):
    """ Writes a 2D list of integers with spaces in between each character, the starting position marked as "s", the goal position marked as "g", and intermediate points marked with "*" e.g.,
    1 1 1 1 1 
    1 s * * 1
    1 0 0 g 1
    1 1 1 1 1
 
    Args:
        grid (2D list): the grid to write
        start (list): starting position (row, column)
        goal (list): goal position (row, column)
    """
    #print('In outputGrid')
    filenameStr = 'path.txt'
 
    # Open filename
    f = open(filenameStr, 'w')
 
    # Mark the start and goal points
    grid[start[0]][start[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'
 
    # Mark intermediate points with *
    for i, p in enumerate(path):
        if i > 0 and i < len(path)-1:
            grid[p[0]][p[1]] = '*'
 
    # Write the grid to a file
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            
            # Don't add a ' ' at the end of a line
            if c < len(row)-1:
                f.write(str(col)+' ')
            else:
                f.write(str(col))
 
        # Don't add a '\n' after the last line
        if r < len(grid)-1:
            f.write("\n")
 
    # Close file
    f.close()
    #print('Exiting outputGrid')


#hueristic function  using manhatten distance.
def h(p1, p2):
    x1, y1 = p1 #this gets the x coordinates
    x2, y2 = p2 #this gets the y coordinates
    return abs(x1-x2) + abs(y1-y2) #this uses the abs math function to get the manhatten distance, is admissable because wont overestimate

def finalPath(origin_node, goal): #this is for inputting the final path
    final_path_array = []

    while goal in origin_node: #while loop to cycle through all the current nodes stored
        final_path_array.append([goal.row, goal.col])
        goal = origin_node[goal] #uses the passed origin noded to keep cycling through
    final_path_array.append([goal.row, goal.col])


    print(final_path_array)
    return final_path_array
       # goal.visualizePath() #uses the visualize path to make it visable

def getNeighborLocation(location, nodeList):
    for i_n, n in enumerate(nodeList):
        if n.row == location[0] and n.col == location[1]:
            return i_n

def algorithm(grid, start, end, nodelist): #this is the a* algo, args are the passed grid, and the start and end point as its an informed search
    count = 0 #the counter for how many open nodes
    open_list = PriorityQueue() #creates the prio Q for the open list
    
    open_list.put((0, count, start)) #starts it off with the start node
    origin_node = {} #origin node list, will be used for the path

    g_value = {}
    #g_value = {node : n for n in nodelist} #the g value, starts at inf since its uknown until we get to it
    for n in nodelist:
        g_value[n] = float("inf")
    g_value[start] = 0 #the start node is obviously 0 since we start there
   
    f_value = {node: float("inf") for n in nodelist} #f value also set to inf since we cant calculate until we get there
    f_value[start] = h(start.getPos(), end.getPos()) #f value calc for start node is just going to be the h value since g is 0
    
    closed_list = []

    #TypeError: unhashable type: 'list'
    openListHash = {start} #this list starts with just the start node


    while not open_list.empty(): #per search algos, as long a the list is not empty, it cycles through
        print("in while loop")
        current = open_list.get()[2] #want to get the most valid node being expanded and makes it current node to work with
        openListHash.remove(current) #removes it from the secondary list as we work with it
        closed_list.append(current)
        print(current.getPos())


        if current == end: #if the current node is the end, then we are done and can return the final path

            return finalPath(origin_node, current) #returns true because we found the path

        print(current.neighbors)
        for neighbor in current.neighbors: #this is to expand the nodes, using the node value neighbors defined above
            node_neighbor = nodelist[getNeighborLocation(neighbor, nodelist)]
            temporary_g_value = g_value[current] + current.getWeight() #calcs the g value by adding the current g val and the weighted value from the node

            if temporary_g_value < g_value[node_neighbor]: #this is to see if this is worth going to as the next node
                origin_node[node_neighbor] = current #adds it to the origin node list for pathing
                g_value[node_neighbor] = temporary_g_value #updates the g value for future calcs
                f_value[node_neighbor] = temporary_g_value + h(node_neighbor.getPos(), end.getPos()) #calcs the f val
            if node_neighbor not in openListHash and node_neighbor not in closed_list:  #if this node has not been stored in the hash, then add it
                count += 1 #increments the counter
                open_list.put((f_value[node_neighbor], count, node_neighbor)) #adds it to the prio Q
                openListHash.add(node_neighbor)
                node_neighbor.isOpen() #sets the node to open

        if current != start: #makes the node closed
            current.isClosed() #closes the node


    return False #no path possible

def main(filename): #defining the main function so the program just runs
    grid = readGrid(filename) #input the file name to be read and created into a grid
    start = [1,2]
    end = [4,4]
    startNode = 0
    endNode = 0
    nodes = []
   # for row in grid
        #for col in row
            #n = node(col, grid[row][col])
    for i_r, row in enumerate(grid):
        for i_c, col in enumerate(row):
            n = node(i_r, i_c, col)
            nodes.append(n)
            if i_r == start[0] and i_c == start[1]:
                startNode = n
            if i_r == end[0] and i_c == end[1]:
                endNode = n
    for n in nodes: #make the nodes?
        n.updateNeighbors(grid)
        print(n.neighbors)
    path = algorithm(grid, startNode, endNode, nodes) #run the algo
    outputGrid(grid, start, end, path) #calls the vis grid to show the path and grid, also used the output grid

main("ai\\test1.txt")




