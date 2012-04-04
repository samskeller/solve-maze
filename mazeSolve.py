# Written by Sam Keller, Justin Norden, and Alex Evangelides on June 2nd, 2011
#
# mazeSolve.py
#
# This program solves a maze, given by the user as a file of 0s for open cells and 1s
# for walls, using a graph that is set up with an adjacency list. The adjacency list
# is a list of vertices, which have their own class. Each vertex has a list of tuples
# that is the list of neighbors that are also open cells. Each vertex also has a visited
# value, which is changed during the solveMaze process. We also have a graph class that
# inherits from a dictionary, where the keys are the tuples containing the row and 
# column information, and the values are the vertices themselves. We also make a queue
# class to be used when solving the maze. We assume that the starting point of the maze
# is the top left corner and the ending point is the bottom right corner. If the maze
# is unsolvable, we return a statement saying it can't be solved. Otherwise, we return
# a list of tuples that show the path through the maze.
       
from Classes import *
        
def solveMaze(graph):
    '''This function makes a queue from our queue class, and using the graph called,
    starts at the beginning of the maze at (0,0) and finds the shortest path through
    the maze using breadth first search (BFS). We used the algorithm described in class.'''
    Q=Queue()
    size = graph.getSize()
    start=graph[(0,0)]
    start.setVisited()
    Q.push(start)
    while not Q.isEmpty():
        # This while loop will run until we've found the end of the list or until
        # the algorithm has figured out that there's no possible path
        cur=Q.newPop()
        for neighbor in cur.getAdj():
            # Check each neighbor of our current spot. If it has been visited, ignore it,
            # if it hasn't, set it to visited and add it to the queue so it can be checked
            # for a potential path to the end of the maze
            if not graph[neighbor].getVisited():
                graph[neighbor].setVisited()
                Q.push(graph[neighbor])
                graph[neighbor].setPrev(cur)
    end=graph[(size,size)]
    path=[]
    while end.getPrev() != None:
        # Now, go back through and append each previous item to the list called path.
        # Starting with the last item, the previous of each spot is necessarily part
        # of our path, so we simply step through them to find our path
        path.append((end.getRow(),end.getCol()))
        end=end.getPrev()
    if path != []:
        # If the path is not empty, we must have a valid solution to the maze. We
        # then append the last item to the list, the starting point, and return the list
        path.append((0,0))
        return path
    else:
        # If our algorithm returned an empty list, there must not be a valid solution.
        return 'Sorry, this maze is unsolvable.'
    

def main():
    '''Our main function. Reads a file with a bunch of 1s and 0s, representing the maze,
    makes a graph, builds the graph out of htis file and then looks for a solution using
    our solveMaze function'''
    filename = raw_input("Please enter a file name to be used: ")
    file = open(filename,'r')
    myGraph = Graph()
    myGraph.buildGraph(file)
    solution = solveMaze(myGraph)
    print "The solution, in reverse order: ", solution
    
main()