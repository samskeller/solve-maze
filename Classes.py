# Classes.py
#
# Contains all of our classes for the solveMaze.py file. 

class Vertex:
    '''This makes the vertex class that's used in the adjacency list in our graph.
    It has a list of all of its neighbors (in their tuple form) and has a visited
    value as well as a previous'''

    def __init__(self, row, col):
        '''Sets up the intial vertex with a row and a column, a previous of none, and
        a visited value of false'''
        self.adj = []
        self.prev = None
        self.row = row
        self.col = col
        self.visited = False
    
    def getRow(self):
        '''Returns the row of the vertex'''
        return self.row
        
    def getCol(self):
        '''Returns the column of the vertex'''
        return self.col
    
    def addNeighbor(self,nbr):
        '''Adds a neighbor to the list of the vertex's neighbors. It adds a tuple
        of the form (row,col)'''
        self.adj.append(nbr)
    
    def setPrev(self,prev):
        '''Sets the previous of the vertex'''
        self.prev = prev
    
    def getPrev(self):
        '''Returns the previous of the vertex'''
        return self.prev
    
    def getAdj(self):
        '''Returns the list of the neighbors of our vertex'''
        return self.adj

    def setVisited(self):
        '''Sets the vertex to be visited so we won't look at it again'''
        self.visited = True
    
    def getVisited(self):
        '''Returns the visited value of the vertex'''
        return self.visited

        
class Graph(dict):
    '''This class makes a graph, inheriting from dictionary, using an adjacency list. 
    We have a buildGraph method that appends all the vertices and adds all of their
    possible neighbors to their own neighbor list.'''
    
    def __init__(self):
        '''Sets up the initial size to be 0'''
        self.size = 0
    
    def buildGraph(self,file):
        '''This method adds each of the vertices and then looks for neighbors. If
        it has neighbors with values of 0, it adds a tuple to its neighbor list of
        the form (row,col) of th neighbor. It also sets the size of the maze, to be
        used in the getSize method.'''
        col=0
        row=0
        for line in file:
            line=line.split()
            col=0
            for i in line:
                if i == '0': 
                    # If the number is a 0, we want to make a vertex out of it. If it's
                    # just a 1, we want to ignore it
                    v = Vertex(row,col)
                    # Add it to the adjacency list:
                    self[(row,col)] = v
                    # Now we go through and check for any neighbors to add to the vertex's
                    # neighbor's list:
                    if (row+1,col) in self:
                        v.addNeighbor((row+1,col))
                        temp = self[(row+1,col)]
                        temp.addNeighbor((row,col))
                    if (row,col+1) in self:
                        v.addNeighbor((row,col+1))
                        temp = self[(row,col+1)]
                        temp.addNeighbor((row,col))                   
                    if (row-1,col) in self:
                        v.addNeighbor((row-1,col))
                        temp = self[(row-1,col)]
                        temp.addNeighbor((row,col))
                    if (row,col-1) in self:
                        v.addNeighbor((row,col-1))
                        temp = self[(row,col-1)]
                        temp.addNeighbor((row,col))            
                col+=1
            self.size = col -1
            row+=1
            
    def getSize(self):
        '''Returns the size of the graph'''
        return self.size

    
class Queue(list):
    '''This class makes a queue, inheriting from list, where we can append items to
    the back of the list and pop items from the front of the list'''

    def __init__ (self):
        '''Sets the initial size of the queue to be 0'''
        self.size = 0
        list.__init__(self)
   
    def push(self,item):
        '''Pushes an item onto the end of the list and increases the size of the queue'''
        self.append(item)
        self.size+=1
        
    def newPop(self):
        '''Pops the first item out of the list and updates the size of the queue'''
        self.size-=1
        return self.pop(0)
        
    def isEmpty(self):
        '''Checks to see if the queue is empty or not'''
        if self.size == 0:
            return True
        else:
            return False
            
    def peek(self):
        '''Looks at the first item in the list without popping it off'''
        return self[0]
