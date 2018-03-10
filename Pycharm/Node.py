from Link import Link
from NodeData import NodeData


class Node:

    unique_id = 0
    nodes = []

    def __init__(self):
        self.nodes.append(NodeData())
        self.id = self.unique_id
        self.unique_id += 1

    def set_position(self, pos):
        self.nodes[id].set_position(pos)

    def get_position(self):
        return self.nodes[id].get_position()

    def add_connection(self, con):
        self.nodes[id].add_connection(con)

    def get_destinations(self):
        dests = []
        for con in self.nodes[id].get_connections():
            dests.append(con.end_node())
        return dests

    def get_connection_to(self, val):
        for con in self.nodes[id].get_connections():
            if con.end_node() == val:
                return con
        return Link()

    def clear_connections(self):
        self.nodes[id].clear_connections()
