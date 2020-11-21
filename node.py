# 4-dimensions node that represents a 3D point (w = scale) 
class Node3D():
    def __init__(self, px = 0., py = 0., pz = 0., pw = 1.):
        self.x = float(px)
        self.y = float(py)
        self.z = float(pz)
        self.w = float(pw)

    def __repr__(self):
        node_as_string = "(%s\n %s\n %s\n %s)" % (self.x, self.y, self.z, self.w)
        return node_as_string


# 3-dimensions node that represents a 2D point (w = scale) 
class Node2D():
    def __init__(self, px = 0., py = 0., pw = 1.):
        self.x = float(px)
        self.y = float(py)
        self.w = float(pw)

    def __repr__(self):
        node_as_string = "(%s\n %s\n %s)" % (self.x, self.y, self.w)
        return node_as_string


# 4-dimensions NAMED node that represents a 3D point (w = scale)
class NamedNode3D(Node3D):
    def __init__(self, px = 0., py = 0., pz = 0., pw = 1., pname = None):
        super().__init__(px, py, pz, pw)
        self.name = pname

    def __repr__(self):
        node_as_string = "%s : \n(%s\n %s\n %s\n %s)" % (self.name, self.x, self.y, self.z, self.w)
        return node_as_string


# 3-dimensions NAMED node that represents a 2D point (w = scale)
class NamedNode2D(Node2D):
    def __init__(self, px = 0., py = 0., pw = 1., pname = None):
        super().__init__(px, py, pw)
        self.name = pname

    def __repr__(self):
        node_as_string = "%s : \n(%s\n %s\n %s)" % (self.name, self.x, self.y, self.w)
        return node_as_string
