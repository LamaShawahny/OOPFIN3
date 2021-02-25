# OOPFIN3
assignment 4
--------------------------------------------------------------
In this assignment, we implement a  directed graph weighted in python, 
Our code basically rely on the previous assignment .   
Our assignment contains  5 main classes and 2 testers .
in addition we compare our  code with other codes : 
1.the  code of the third  assignment  
2.The python library networks   

  PART 1:MAIN CLASSES
--------------------------------------------------------------------------------------------------------------------------------------------------------------
nodedata class :

*This class represents set of operations applicable on a node (vertex) in an (directional) weighted graph.
To implement the graph we used the  collection data structure :hashmap ,Since storing and retrieving elements from the HashMap takes constant O(1) time.
 and we also used the data structure LinkedList.

    properties :
     int key - the key of the node
     double Weight - the weight of the node
     String info -the info of rhe node
     int tag -our node tag
     neighbors- this hashmap represent the edges between our node and is't neighbors
    outedeges - list that returns  the innerdeges
    constructors:
    def _init_(self,key,loc=None)
     
     Getters and setters for the  properties in O(1)complexity...

  --------------------------------------------------------------------------------------------------------------------------------------------------------------
  class edgedata:

*this class represent an edge between two nodes

      src #the source point of the edge
      weight =weight #the destination of point the edge
      dest #the weight of the edge
      info= info #the info of the edge
      tag #the tag of the edge
constructor :
    def _init_(self, src,dest,weight,info,tag):
        
etters and setters for the  properties in O(1)complexity...

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
 GraphInterface interface  <-->DiGraph class :

 *This class represents an directional weighted graph. It supports a large number of nodes , The implementation  based on an efficient compact representation.
  To implement this class we used the  collection data structure : hashmap ,Since storing and retrieving elements from the HashMap takes constant O(1) time.
   properties :
     Graph - hashmap represents the nodes in our graph
     edgeSize;-  number of the edges in the graph
     mc; -for testing changes in the graph.
 
    def int(self)-  cunstractur

    methods:                                                 
    def v_size(self) -> int: - the number of vertices (nodes) in the graph.-O(1)
    def e_size(self) -> int: -get edges size -O(1)
    def get_all_v(self) -> dict:return a dictionary of all the nodes in the Graph, each node is represented using a pair(node_id, node_data)
    def all_in_edges_of_node(self, id1: int) -> dict:return a dictionary of all the nodes connected to (into) node_id ,each node is represented using a pair (other_node_id, weight)
   def all_out_edges_of_node(self, id1: int) -> dict:return a dictionary of all the nodes connected from node_id , each node is represented using a pair (other_node_id, weight)
    def get_mc(self) -> int: modified new version of this graph on every change in the graph state - the MC should be increased
    def add_edge(self, id1: int, id2: int, weight: float) -> bool: Adds an edge to the graph.
    def add_node(self, node_id: int, pos: tuple = None) -> bool:  Adds a node to the graph.
    def remove_node(self, node_id: int) -> bool: Removes a node from the graph.
    def remove_edge(self, node_id1: int, node_id2: int) -> bool: Removes an edge from the graph.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  GraphAlgoInterface interface  <--> GraphAlgo class 

*To implement this class we used the Dijkstra  algorithm for finding the shortest paths from source to all vertices in the given graph.
 we generate a SPT (shortest path tree) with given source as root. We maintain two sets, one set contains vertices included in shortest path tree, other set includes vertices not yet included in shortest path tree. At every step of the algorithm, we find a vertex which is in the other set (set of not yet included) and has a minimum distance from the source.


  main methods:
   def _init_(self: DiGraph1): -Init the graph on which this set of algorithms operates on.
   def get_graph(self) -> GraphInterface: -get the graph 

   def shortest_path(self, id1: int, id2: int) -> (float, list):Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
   def save_to_json(self, file_name: str) -> bool:Saves the graph in JSON format to a file
   def load_from_json(self, file_name: str) -> bool: Loads a graph from a json file.
   def connected_component(self, id1: int) -> list: Finds the Strongly Connected Component (SCC) that node id1 is a part of.
   def connected_components(self) -> List[list]: Finds all the Strongly Connected Component(SCC) in the graph.
   def plot_graph(self) -> None:  If the nodes have a position, the nodes will be placedthere.
   Otherwise, they will be placed in a random but elegant manner.

   other methods :

   def findthedis(self, ls:list) -> float:this method we use in shortest_path it return the dest between the id1 and id2
   def findtheminpath(self, id1: int, id2: int) -> list:this method find the shortest path between the src and the dest
   def resetarr(self):this method set the prev array values to -1 and the destination to sys.maxsize
   def getmin(self,lst): this method return the the index of the min node
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

sources:
https://www.youtube.com/watch?v=fS3IXV4LlGc&t=2369s
https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
youtube.com/watch?v=fNX8tKnozF0&list=PLEtZq1oDporhAPIlKhfRCpcxjpXjSeR2z
https://github.com/simon-pikalov/Ariel_OOP_2020
https://www.geeksforgeeks.org/implementing-generic-graph-in-java/
https://www.khanacademy.org/computing/computer-science/algorithms/breadth-first-search/a/breadth-first-search-and-its-uses
Python מצגת (3) איליזבת   
Asignment 3 -lama shawahny 
Aaignment 3 -shady ghanem  

