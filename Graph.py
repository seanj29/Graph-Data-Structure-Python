from typing import Iterator

type EdgeType = Edge
type NodeType = Node
        


class Node:
    def __init__(self, data, connectedEdges: Iterator[EdgeType] = []):
        self.data = data
        self.connectedEdges = connectedEdges
        
    def __eq__(self, other: NodeType):
        if other:
            return self.data == other.data and self.connectedEdges == other.connectedEdges
        else:
            False
    
    def __hash__(self):
        return hash(self.data)
    
    def __str__(self):
        return str(self.data)
    
    def appendEdge(self, edge: EdgeType):
        self.connectedEdges.append(edge)
        
    def removeEdge(self, edge: EdgeType):
        self.connectedEdges.append(edge)
        
    
        
        

class Edge:
    def __init__(self, originNode: Node, endNode: Node, data = None):
        self.data = data
        self.originNode = originNode
        self.endNode = endNode
        self.path: tuple = (originNode, endNode)
        
    def __eq__(self, other: EdgeType):
       if (self.originNode == other.originNode and self.endNode == other.endNode):
          return True
       elif (self.originNode == other.endNode and self.endNode == other.endNode):
          return True  
      
       return False 
           
    
    def __str__(self):
        return f"Edge from {self.originNode} to {self.endNode} with weight {self.data}"
    
    def isConnectingNodes(self, Node1: Node, Node2: Node):
        
        if (Node1 == self.originNode and Node2 == self.endNode) or (Node1 == self.endNode and Node2 == self.originNode):
            return True
        else:
            return False
    
        
        

class Graph:
    def __init__(self, nodeList: Iterator[Node] = [], edgeList: Iterator[Edge] = []):
        self.nodeList = nodeList
        self.edgeList = edgeList
        self.paths: list[tuple] = []
        
        for edge in edgeList:
            reverse = edge.path[::-1]     
            self.paths.append(edge.path)
            self.paths.append(reverse)
            
    def getNodes(self):
        return self.nodeList
    
    def isAdjacentTo(self, fromNode: Node, toNode: Node) -> bool:
        for edge in fromNode.connectedEdges:
            if edge.isConnectingNodes(fromNode, toNode):
                return True
        return False
    
    def getNeighhbours(self, inputNode: Node) -> list[Node]:
        neighbours = []
        for node in self.nodeList:
            if self.isAdjacentTo(inputNode, node):
                neighbours.append(node)
        return neighbours
    
    def addNode(self, Node: Node) -> Node:
        self.nodeList.append(Node)
        return Node

    def removeNode(self, Node: Node) -> Node:
        
        if Node in self.nodeList:
            self.nodeList.remove(Node)
            
        for edge in Node.connectedEdges:
            self.removeEdge(edge.originNode, edge.endNode)
                
        return Node
    
    def addEdge(self, Node1: Node, Node2: Node, value) -> Edge:
        
        Edgetemp = Edge(Node1, Node2, value)        
        if self.isAdjacentTo(Node1, Node2) == False:
            
            self.edgeList.append(Edgetemp)
            
            Node1.appendEdge(Edgetemp)
            Node2.appendEdge(Edgetemp)
            
            self.paths.append(Edgetemp.path)
            self.paths.append(Edgetemp.path[::-1])
            return Edgetemp
        else:
            existingEdge = Edge(Node1, Node2)
            return existingEdge
            
    def removeEdge(self, Node1: Node, Node2: Node) -> Edge:
        
        Edgetemp = Edge(Node1, Node2)
        
        if self.isAdjacentTo(Node1, Node2):
            
            self.edgeList.remove(Edgetemp)
            
            Node1.removeEdge(Edgetemp)
            Node2.removeEdge(Edgetemp)
        
            self.paths.remove(Edgetemp.path)
            self.paths.remove(Edgetemp.path[::-1])
             
        return Edgetemp
            
    def getNodeValue(self, Node: Node):
        return Node.data
    def setNodeValue(self, Node: Node, value) -> Node:
        
        Node.data = value
        return Node
    
    def getEdgeValue(self, Node1: Node, Node2: Node):
        
                 
        for edge in self.edgeList:
            if edge.isConnectingNodes(Node1, Node2):
                return edge.data
        else:
            
            return None
            
    
    def setEdgeValue(self, Node1: Node, Node2: Node, value):
        
        if self.getEdgeValue(Node1, Node2) is not None:
            return self.getEdgeValue(Node1, Node2)
        
        if self.isAdjacentTo(Node1, Node2):
            for edge in Node1.connectedEdges:
                if edge in Node2.connectedEdges:   
                    edge.data = value
            
    
        
    
   
        
        
        
        
        

    


g1 = Graph()




