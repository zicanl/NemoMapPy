from Graph import Graph
from collections import defaultdict


class GraphProcessor:
    """
        A Class to read a graph from a file.
        File should be formatted:
            'first#ofEdge1 second#ofEdge1
            first#ofEdge2 second#ofEdge2 . . .'

        Methods
        -------
        loadGraph
            reads edges from a text file and stores the values in a 2D list
        """

    def __init__(self):
        pass

    def loadGraph(self, fileName, directed):
        """
        loadGraph: reads edges from a text file and stores the values in a 2D list
        :param graphType: string that identify the input file type 'int' or 'str'
        :param directed: boolean value that identify if the graph is directed
        :param fileName:string The name f the file containing the graph edges
        :return: Graph - A graph containing the edges from the file
        """
        # if graphType == "int":
        # edgeList = []
        # with open(fileName) as myFile:
        #     for line in myFile:
        #         if "#" not in line:  # catch comments
        #             pair = [int(i) for i in line.split()]  # read in as integers
        #             if pair[0] != pair[1]:
        #                 """
        #                 edgeList is a 2D list with each index of edgeList
        #                 containing exactly one edge. edgeList[index][0] is the
        #                 first number in a pair, edgeList[index][1] is the seccond
        #                 """
        #                 edgeList.append(pair)
        #
        # newGraph = Graph(edgeList, None, directed)
        # return newGraph

        mappings = defaultdict(str)
        edgeList = []
        with open(fileName) as myFile:
            for line in myFile:
                if "#" not in line:  # catch comments
                    pair = line.split()
                    if len(pair) == 2:
                        for node in pair:
                            if node not in mappings:
                                mappings[len(mappings.keys()) // 2] = node
                                mappings[node] = str(len(mappings.keys()) // 2)
                        if pair[0] != pair[1]:
                            edge = [int(mappings[pair[0]]), int(mappings[pair[1]])]
                            edgeList.append(edge)
        newGraph = Graph(edgeList, mappings, directed)
        return newGraph
