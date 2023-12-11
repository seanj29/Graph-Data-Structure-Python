from Dijkstra import Dijkstra
from Graph import *

nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]
classNodes: list[Node] = []


mapGraph = Graph()

for node in nodes:
    mapGraph.addNode(node)
    classNodes.append(node)
    

Reykjavik, Oslo, Moscow, London, Rome, Berlin, Belgrade, Athens = classNodes
        


mapGraph.addEdge("Reykjavik","Oslo", 5)

mapGraph.addEdge("Reykjavik", "London", 4)

mapGraph.addEdge("Oslo", "Berlin", 1)

mapGraph.addEdge("Oslo", "Moscow", 3)

mapGraph.addEdge("Moscow", "Belgrade", 5)

mapGraph.addEdge("Moscow", "Athens", 4)

mapGraph.addEdge("Athens", "Belgrade", 1)

mapGraph.addEdge("Rome", "Berlin", 2)

mapGraph.addEdge("Rome", "Athens", 2)


previousNodes, shortestPath = Dijkstra.dijkstra(mapGraph, mapGraph.getNodeByValue("Reykjavik"))

Dijkstra.printPath(previousNodes, shortestPath, mapGraph.getNodeByValue("Reykjavik"), mapGraph.getNodeByValue("Rome"))

# print(mapGraph.getEdgeValue(Rome, Berlin))


