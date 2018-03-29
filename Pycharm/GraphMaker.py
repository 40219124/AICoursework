from FileInput import FileInput
from Node import Node
from Link import Link


class GraphMaker:

    nodes = []

    @staticmethod
    def build_nodes():
        nodes = []
        nums = FileInput.numbers.copy()
        nums = nums[1:nums[0] * 2 + 1]
        while len(nums) > 0:
            n = Node()
            n.set_position((nums.pop(0), nums.pop(0)))
            nodes.append(n)
            # print(str(n))
        GraphMaker.nodes = nodes.copy()

    @staticmethod
    def build_connections():
        count = FileInput.count
        nums = FileInput.numbers.copy()
        cons = nums[FileInput.count * 2 + 1:]
        for f in range(count):
            for t in range(count):
                if cons[count * t + f] == 1:
                    link = Link()
                    link.set_ends(f, t)
                    link.set_length(GraphMaker.calculate_link_length(
                        Node.nodes[f].get_position(), Node.nodes[t].get_position()))
                    GraphMaker.nodes[f].add_connection(link)

    @staticmethod
    def calculate_link_length(s, e):
        return ((e[0] - s[0])**2 + (e[1] - s[1])**2)**(1/2.0)
