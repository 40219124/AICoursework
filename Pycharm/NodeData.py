class NodeData:

    def __init__(self):
        self.location = (0, 0)
        self.connections = []

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
