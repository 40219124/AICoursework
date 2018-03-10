from Node import Node


class Link:

    def __init__(self):
        self.start = 0
        self.end = 0
        self.weight = 0

    def start_node(self):
        return self.start

    def end_node(self):
        return self.end

    def length(self):
        return self.weight

    def set_start(self, s):
        self.start = s

    def set_end(self, e):
        self.end = e

    def set_length(self, l):
        self.weight = l

    def set_ends(self, s, e):
        self.start = s
        self.end = e
        self.weight = self.calculate_link_length(Node.nodes[s].get_position(), Node.nodes[e].get_position())

    @staticmethod
    def calculate_link_length(s, e):
        return ((e[0] - s[0])**2 + (e[1] - s[1])**2)**(1/2.0)
