from Link import Link
from NodeData import NodeData


class Node:

    unique_id = 0
    nodes = []  # list of node data

    def __init__(self):
        self.nodes.append(NodeData())
        self.id = Node.unique_id
        Node.unique_id += 1

    def __str__(self):
        return "ID:" + str(self.id + 1) + ", " + str(self.nodes[self.id])

    def set_position(self, pos):
        self.nodes[self.id].set_position(pos)

    def get_position(self):
        return self.nodes[self.id].get_position()

    def add_connection(self, con):
        self.nodes[self.id].add_connection(con)

    def get_destinations(self):
        dests = []
        for con in self.nodes[self.id].get_connections():
            dests.append(con.end_node())
        return dests

    def get_connection_to(self, val):
        for con in self.nodes[self.id].get_connections():
            if con.end_node() == val:
                return con
        return Link()

    def clear_connections(self):
        self.nodes[self.id].clear_connections()