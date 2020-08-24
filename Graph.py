from collections import defaultdict


class Graph:
    """
    A Class to represent a network

    Attributes
    ----------
    edgeList:List[List[int]] contains all unique edges in the graph
    vertexList:Dict[int, List[int] contains all unique vertex in the graph

    Methods
    -------
    addEdge: add a edge and its corresponding vertices to the graph

    getNumberofVertices: returns the number of vertices in the graph

    getNumberofEdges: return the number of edges in the graph

    tryEdge: test if sn edge is is the graph

    getNeighbors: get list of neighbors for requested vertex

    getNodesSortedByDegree: left list of verteces that have at least x amount of connected nodes

    getEdgeList: return the 2d edge list

    getVertexList: return the dictionary vertex list

    getDegreeSequence: degree sequence of all vertices in descending order

    getOutDegree: get out degree of a vertex

    """

    def __init__(self, inputEdgeList=None, mappings=None, directed=False):
        """
        Constructor: create a graph by updating self.edgeList and self.vertexList
            :param inputEdgeList:List[List[int]] - Contains list of edges to be used to create a graph
            :Result: edgeList and vertexList are created and filled to represent
                    the graph
        """
        if mappings is None:
            mappings = []
        if inputEdgeList is None:
            inputEdgeList = []
        self.edgeList = []
        self.vertexList = defaultdict(list)
        self.mappings = mappings
        self.directed = directed
        self.fromNode = defaultdict(list)
        self.toNode = defaultdict(list)

        "Handle Edges"
        for source, target in inputEdgeList:
            self.edgeList.append([source, target])
            self.vertexList[source].append(target)
            self.vertexList[target].append(source)
            if self.directed:
                self.fromNode[source].append(target)
                self.toNode[target].append(source)

    def addEdge(self, edge):
        """
        addEdge: add a edge and its corresponding vertices to the graph
        :param edge:List[int] - the edge to be added
        :return: Boolean: true if edge is added. false if edge is not added
        """
        if self.directed:
            if edge not in self.edgeList and edge[0] != edge[1]:
                self.edgeList.append(edge)
                self.vertexList[edge[0]].append(edge[1])
                self.vertexList[edge[1]].append(edge[0])
                self.fromNode[edge[0]].append(edge[1])
                self.toNode[edge[1]].append(edge[0])
        else:
            if edge not in self.edgeList and [edge[1], edge[0]] not in self.edgeList and edge[0] != edge[1]:
                self.edgeList.append(edge)
                self.vertexList[edge[0]].append(edge[1])
                self.vertexList[edge[1]].append(edge[0])


    def getNumberofVertices(self):
        """
        "return: the number of vertexs in graph
        """
        return len(self.vertexList)

    def getNumberofEdges(self):
        """
        :return: the number of edges in graph
        """
        return len(self.edgeList)

    def getNodesSortedByDegree(self, degreeCutOff):
        """
        GetNodesSortedByDegree: get a list of vertices sorted by their degree sequence
        :param degreeCutOff:int - the threshold of out degree that we want to check
        :return: List[int]: list of nodes IDs sorted by out degree in ascending order
        """
        nodeSortedByDegree = []  # <vertexID>
        for vertex in self.vertexList:
            if len(self.vertexList[vertex]) >= degreeCutOff:
                nodeSortedByDegree.append(vertex)
        nodeSortedByDegree.sort(key=lambda x: len(self.vertexList[x]))
        return nodeSortedByDegree

    def tryGetEdge(self, edge):
        """
        tryGetEdge: check if an edge exist in the graph
        :param edge:List[int] - the edge we are trying to find
        :return: boolean - true if edge exist, false otherwise
        """

        if edge in self.edgeList or [edge[1], edge[0]] in self.edgeList:
            return True
        return False

    def getNeighbors(self, source):
        """
        getNeighbors: return the neighbors of the source
        :param source:int - the vertex we are finding the neighbors of
        :return: List[int] - list containing the neighbors of source
        """
        return sorted((self.vertexList.get(source, -1)))

    def getDegreeSequence(self):
        """
        get degree sequence of all vertices in descending order
        :return: List[int] - degree sequence of all vertices in descending order
        """
        return sorted([len(self.vertexList[vertex]) for vertex in self.vertexList],
                      reverse=True)

    def getEdgeList(self):
        """
        :return: LIst[List[int]] - the 2d list of edges
        """
        return self.edgeList

    def getVertexList(self):
        """
        :return: Dict[int, List[int]] - the dictionary containing the vertex list
        """
        return self.vertexList

    def getOutDegree(self, source):
        """
        get out degree of a vertex
        :param source:int - vertex whose degree you want to find
        :return: int - number of degree of the vertex if exists, -1 if doesn't exist
        """
        if source in self.vertexList:
            return len(self.vertexList[int(source)])
        else:
            return -1

    def getDirected(self):
        """
        :return: Boolean - the type of this graph, directed (True) or undirected (False)
        """
        return self.directed

    def getFrom(self):
        """
        :return: Dict[List[int]] - return dictionary of vertex of from nodes
        """
        return self.fromNode

    def getTo(self):
        """
        :return: Dict[List[int]] - return dictionary of vertex of in nodes
        """
        return self.toNode

    def getFromToCount(self):
        """
        :return: return the count of from and to for each vertex (For Directed Graph only)
        """
        return [(len(self.fromNode[vertex]), len(self.toNode[vertex])) for vertex in self.vertexList]

    """
       *   Testing methods
       *   mostly returns dicts and prints out data
       """
    def testGetters(self):
        print("Number of Vertices: %d" % self.getNumberofVertices())
        print("Number of Edges: %d" % self.getNumberofEdges())

    def testGetNodesSortedByDegree(self, num):
        return self.getNodesSortedByDegree(num)