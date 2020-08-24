from Graph import Graph
import random


class RandomGraphGenerator:

    def __init__(self):
        pass

    def generate(self, inputGraph):
        randomGraph = Graph(directed=inputGraph.getDirected())
        degreeSequenceVector = inputGraph.getDegreeSequence()
        indegreeSeqVector = None
        if inputGraph.getDirected():
            degreeSequenceVector = [len(lst) for lst in inputGraph.getFrom().values()]
            indegreeSeqVector = [len(lst) for lst in inputGraph.getTo().values()]

        vertexList = []
        inVertexList = []
        " generate randomized list of vertices"

        for vertex in range(inputGraph.getNumberofVertices()):
            if vertex < len(degreeSequenceVector):
                for degree in range(degreeSequenceVector[vertex]):
                    vertexList.append(vertex)
            if inputGraph.getDirected():
                if vertex < len(indegreeSeqVector):
                    for degree in range(indegreeSeqVector[vertex]):
                        inVertexList.append(vertex)

        random.shuffle(vertexList)
        if inputGraph.getDirected():
            random.shuffle(inVertexList)
        " create edges "
        while len(vertexList) > 0:
            if inputGraph.getDirected():
                u = random.randrange(0, len(vertexList))
                v = random.randrange(0, len(inVertexList))
                edgeVertexU = vertexList[u]
                edgeVertexV = inVertexList[v]

                vertexList = vertexList[:u] + vertexList[u + 1:]
                inVertexList = inVertexList[:v] + inVertexList[v + 1:]
                randomGraph.addEdge([edgeVertexU, edgeVertexV])
            else:
                u = random.randrange(0, len(vertexList))
                v = random.randrange(0, len(vertexList))
                while v == u:
                    v = random.randrange(0, len(vertexList))
                if u > v:
                    temp = u
                    u = v
                    v = temp
                edgeVertexU = vertexList[u]
                edgeVertexV = vertexList[v]
                vertexList = vertexList[:v] + vertexList[v + 1:]
                vertexList = vertexList[:u] + vertexList[u + 1:]
                randomGraph.addEdge([edgeVertexV, edgeVertexU])

        return randomGraph
