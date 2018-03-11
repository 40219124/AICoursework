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
