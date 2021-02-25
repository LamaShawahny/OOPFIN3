class nodedata:  # this class is represent the nodes of the graph with a basic methods
    def __init__(self, key, pos):
        self.weight=0
        self.key=key
        self.ni={}
        self.inedge=[]
        self.pos=pos
        self.tag=0
        self.outedes=[]

    def setpos(self,pos):
        self.pos=pos

    def gettag(self):
        return self.tag

    def settag(self,tag):
        self.tag=tag

    def getpos(self):
        return self.pos

    def getweight(self):  # this method return the node weight
        return self.weight

    def getkey(self):  # this method return the key value
        return self.key

    def getinedges(self):  # return the list that contains the edeges that our node key is the dest
        return self.inedge

    def setweight(self, weight):  # this method set the node weight
        self.weight = weight

    def getmyhash(self):  # return a hashmap that contains the edges between our node and is't neighbors
        return self.ni

    def getmyedeges(self):  # return the edges that our node is the src in them
        return self.ni.values()