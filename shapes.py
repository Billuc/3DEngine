from node import NamedNode3D

class Shape():
    def __init__(self, pname = None):
        self.nodes = []
        self.name = pname

    def __repr__(self):
        return "%s (Shape) : %s" % (self.name, self.nodes)

    def add_node(self, node):
        self.nodes.append(node)

    def replace_node(self, index, node):
        if len(self.nodes) > index:
            self.nodes[index] = node
        else:
            raise IndexError("Index out of bounds")


class Triangle(Shape):
    def __init__(self, node_a, node_b, node_c, pname = None):
        super().__init__(pname)
        self.add_node(node_a)
        self.add_node(node_b)
        self.add_node(node_c)

    def __repr__(self):
        return "%s (Triangle) : %s" % (self.name, self.nodes)

    def add_node(self, node):
        if len(self.nodes) < 3:
            super().add_node(node)