import sys
import math

class Node(object):
    def __init__(self, name):
        '''We assume that name is a string'''
        self.name=name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        '''We assume that src and dest are nodes'''
        self.src=src
        self.dest=dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1.0):
        '''src and dest are nodes, and weight is float'''
        self.src=src
        self.dest=dest
        self.weight=weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName() + '->(' + str(self.weight) + ')' + self.dest.getName()


class Digraph(object):
    #nodes is a list of the nodes in the graph
    #edges is a dict mapping each node to a list of its children
    def __init__(self):
        self.nodes=[]
        self.edges={}

    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node]=[]

    def addEdge(self, edge):
        src=edge.getSource()
        dest=edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.nodes
    
    def __str__(self):
        result=''
        for src in self.nodes:
            for dest in self.edges[src]:
                result=result + src.getName() + '->' + dest.getName() + '\n'
        return result[:-1]

class Graph(Digraph):
    def addEdge(self,edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def BFS(graph, start, end):
    '''graph is a Digraf, start and end are nodes'''
    '''Returns shortiest path from start to end in graph'''
    initPath=[start]
    pathList=[initPath]
    while len(pathList) != 0:
        tmpPath=pathList.pop(0)
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                nextPath = tmpPath + [nextNode]
                pathList.append(nextPath)
    return None

def BFS_list(graph, start, end_list):
    l=[]
    for e in end_list:
        l.append(BFS(graph,start,e))
    shortiest_list = min(l, key=len)
    return shortiest_list

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways

n, l, e = [int(i) for i in input().split()]

g=Graph()
nodes=[]
exit_Nodes=[]

for i in range(n):
    nodes.append(Node(str(i)))
for n in nodes:
    g.addNode(n)



for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    g.addEdge(Edge(nodes[n1], nodes[n2]))


for i in range(e):
    ei = int(input())  # the index of a gateway node
    exit_Nodes.append(nodes[ei])


# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    shorty=BFS_list(g,nodes[si],exit_Nodes)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    
    print(shorty[0],shorty[1])

