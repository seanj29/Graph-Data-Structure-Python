from Graph import *
from sys import maxsize

class Dijkstra:

    def dijkstra(graph: Graph, startNode: Node):
        
    
        unvisitedNodes: list[Node] = list(graph.getNodes())
        shortestPath = {}
        previousNodes = {}
        maxValue = maxsize
        
        # We'll use max_value to initialize the "infinity" value of the unvisited nodes
        
        for node in unvisitedNodes:
            shortestPath[node] = maxValue
            
        # However, we initialize the starting node's value with 0  
        shortestPath[startNode] = 0
        
        while unvisitedNodes:
            
            currentMinNode = None
            for node in unvisitedNodes:
                if currentMinNode == None:
                    currentMinNode = node
                elif shortestPath[node] < shortestPath[currentMinNode]:
                    currentMinNode = node

            neighbours = graph.getNeighhbours(currentMinNode)
            for neighbor in neighbours:
                tempValue = shortestPath[currentMinNode] + graph.getEdgeValue(currentMinNode, neighbor)
                if tempValue < shortestPath[neighbor]:
                    shortestPath[neighbor] = tempValue
                    # Update the best path to the curent node
                    previousNodes[neighbor] = currentMinNode
            # After visiting its neighbors, we mark the node as "visited"
            unvisitedNodes.remove(currentMinNode)
            
        return previousNodes, shortestPath

    def printPath(previousNodes: dict, shortestPath: dict, startNode: Node, targetNode: Node):
        path = []
        node = targetNode
        
        while node != startNode:
            path.append(node.data)
            node = previousNodes[node]
        
        path.append(startNode.data)

        print("We found the following best path with a value of {}".format(shortestPath[targetNode]))
        print(" -> ".join(reversed(path)))
    