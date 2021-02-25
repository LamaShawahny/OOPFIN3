import json
import sys
from typing import List
import GraphInterface
from nodedata import nodedata
from edgedata import edgedata
from DiGraph import DiGraph


class GraphAlgo:
    # this class is represent a directed weighted graph with a basic methods complex methods
    def __init__(self,graph):
        self.myGraph = DiGraph()
        self.nill = -1
        self.sizeofarr1 = 0
        self.prev = {}
        self.destination = {}
        self.init(graph)

    def init(self,graph):
        self.MyGraph=graph
        for i in graph.get_all_v():
            x = i.getkey()
            if self.sizeofarr1 < x:
                self.sizeofarr1 = x
        self.sizeofarr = self.sizeofarr1

    def get_graph(self) -> GraphInterface:  # this method return the graph
        return self.MyGraph

    def shortest_path(self, id1: int, id2: int) -> (float, list):  # this method return the a list that contains the shortest path and its dest
        myls = []
        if self.MyGraph.getnode(id1) is None or self.MyGraph.getnode(id2) is None:
            return -1, myls
        if id1 == id2:  # if the two nodes are the same return 0 and list contain id1 node
            myls.append(self.MyGraph.getnode(id1))
            return 0, myls
        if self.MyGraph.getnode(id1) is None or self.MyGraph.getnode(id2) is None:  # if one of the nodes ar'nt exist return -1
            return -1, None
        if self.findtheminpath(id1, id2) is None:  # if there is no path return -1
            return -1, None
        myls = self.findtheminpath(id1, id2)
        np = []
        for n1 in myls:
            if n1 is not None:
                np.append(n1)
        x = self.destination[id2]
        if x == sys.maxsize:
            x = -1
        return x, np


    def findtheminpath(self, id1: int, id2: int) -> list:  # algorithm I find the psodocode in the internet
     # the method find the shortest path between the src and the dest
        a = 0
        q = {}
        listofnodes = []
        arraydic = []
        self.resetarr()
        for n in self.MyGraph.get_all_v():
            q[n.getkey()] = n
        self.destination[id1] = 0
        while len(q) != 0:
            index = self.getmin(q,self.destination)
            u = self.MyGraph.getnode(index)
            if u is None:
                break
            q.pop(index)
            for e1 in self.MyGraph.all_out_edges_of_node(u.getkey()):
                if e1.get_dist() in q.keys():
                    a = self.destination[index]+e1.get_weight()
                    if a < self.destination[e1.get_dist()]:
                        self.destination[e1.get_dist()] = a
                        self.prev[e1.get_dist()] = u.getkey()
        u2 = self.MyGraph.getnode(id2)
        j = 0
        if self.prev[u2.getkey()] != -1 or u2.getkey() == id1:
            while u2 is not None:
                arraydic.append(u2.getkey())
                j = j+1
                u2 = self.MyGraph.getnode(self.prev[u2.getkey()])
        if j == 1:
         return None
        j = j-1
        while j > 0:
            listofnodes.append(arraydic[j])
            j = j-1
        if len(listofnodes) > 0:
            listofnodes.append(id2)
        return listofnodes


    def resetarr(self):  # this method set the prev array values to -1 and the destination to sys. maxsize
        for x in range(0, self.sizeofarr+1):
            self.prev[x]= self.nill
            self.destination[x] =sys.maxsize
        return

    def getmin(self, q,d):  # this method return the the index of the min node
        index = 0
        min = sys.maxsize
        for i, item in enumerate(d):
            if item <= min and i in q:
                min = item
                index = i
        return index

    def load_from_json(self, file_name: str) -> bool:

        self.MyGraph = DiGraph()
        try:
            with open(file_name, 'r') as file:
                jGraph = json.load(file)
                # Insert ALl Nodes Into The Graph
                Nodes = jGraph.get("Nodes")
                for node in Nodes:
                    # Check If There Is Pos Also
                    if len(node) > 1:
                        self.MyGraph.add_node(node_id=node["id"], pos=node["pos"])
                    else:
                        self.MyGraph.add_node(node["id"])
                # Insert ALl Edges Into The Graph
                Edges = jGraph.get("Edges")
                for edge in Edges:
                    self.MyGraph.add_edge(id1=edge["src"], id2=edge["dest"], weight=edge["w"])
            return True

        except IOError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:

        try:
            with open(file_name, 'w') as file:
                Nodes = []
                Edges = []
                for k, v in self.MyGraph.get_all_v().items():
                    # Check If There Is Pos Also
                    if v.pos is not None:
                        print(v.pos)
                        Nodes.append({"id": k, "pos": v.pos})
                    else:
                        Nodes.append({"id": k})
                    dest = self.MyGraph.all_out_edges_of_node(k)
                    if len(dest) > 0:
                        for d, w in dest.items():
                            Edges.append({
                                "src": k,
                                "w": w,
                                "dest": d
                            })
                save = {"Nodes": Nodes, "Edges": Edges}
                json.dump(save, default=self.encoder, indent=4, fp=file)

            return True

        except IOError as e:
            print(e)
            return False

        raise NotImplementedError

    def connected_component(self, id1: int) -> list:  # this method return all the connected components of the id1
        visited = []
        for n1 in self.MyGraph.get_all_v():
            if self.shortest_path(id1, n1.getkey()) != (-1, []):
                visited.append(n1.getkey())
        return visited

    def connected_components(self) -> List[list]:  # this method return list of lists that contains all the graph nodes and its connected components
        ls = []
        for n in self.MyGraph.get_all_v():
            lst = self.connected_component(n.getkey())
            ls.append(lst)
        return ls

    def helpm(self, q) -> bool:
        flag = True
        for i in q.keys():
            if q[i] != -5000:
                flag = False
        return flag

    def plot_graph(self) -> None:
        return