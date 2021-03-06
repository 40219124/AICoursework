class NodeData:

    def __init__(self):
        self.location = (0, 0)
        self.connections = []  # List of links

    def __str__(self):
        return "Node[loc:" + str(self.location) + ",cons:" + str(len(self.connections)) + "]"

    def set_position(self, pos):
        self.location = pos

    def get_position(self):
        return self.location

    def add_connection(self, con):
        self.connections.append(con)

    def get_connections(self):
        return self.connections

    def clear_connections(self):
        self.connections.clear()
