from Node import Node
from GraphMaker import GraphMaker


class SolverNode:

    def __init__(self):
        self.visited_from = -1
        self.visited = False
        self.shortest_dist = -1
        self.id = -1
        self.goal = False

    def set_node(self, id_no):
        self.id = id_no

    def previous(self):
        return self.visited_from

    def visited(self):
        return self.visited

    def get_node(self):
        return GraphMaker.nodes[self.id]


class Solver:

    solver_nodes = []
    visited_count = 0

    @staticmethod
    def initialise_solver(nodes):
        Solver.solver_nodes.clear()
        for i in range(len(nodes)):
            sn = SolverNode()
            sn.set_node(i)
            Solver.solver_nodes.append(sn)
        Solver.solver_nodes[0].shortest_dist = 0
        Solver.solver_nodes[len(nodes) - 1].goal = True

    @staticmethod
    def generate_path():
        if len(Solver.solver_nodes) == 0:
            Solver.initialise_solver(GraphMaker.nodes)
        if len(Solver.solver_nodes) == 0:
            print("No nodes. Aborting pathfinding.")
            return
        print("Search results:")
        Solver.search(0)
        print(Solver.visited_count)
        print(Solver.path(len(Solver.solver_nodes)-1))

    @staticmethod
    def search(this_id):
        this_node = Solver.solver_nodes[this_id]
        if this_node.goal:
            return
        Solver.visited_count += 1
        this_node.visited = True
        dests = Solver.order_closest_neighbours(this_id)
        for d in dests:
            weight = this_node.get_node().get_connection_to(d).length()
            test_val = this_node.shortest_dist + weight
            if Solver.solver_nodes[d].shortest_dist == -1 \
                    or test_val < Solver.solver_nodes[d].shortest_dist:
                Solver.solver_nodes[d].shortest_dist = test_val
                Solver.solver_nodes[d].visited_from = this_id
                Solver.search(d)

    @staticmethod
    def order_closest_neighbours(root):
        cons = GraphMaker.nodes[root].get_destinations()
        for c in cons:
            if Solver.solver_nodes[c].visited:
                cons.remove(c)
        dests = []
        while len(cons) > 0:
            shortest = 9999999
            short_id = -1
            for i in range(len(cons)):
                test_len = GraphMaker.nodes[root].get_connection_to(cons[i]).length()
                if test_len < shortest:
                    shortest = test_len
                    short_id = i
            dests.append(cons[short_id])
            cons.pop(short_id)
        return dests

    @staticmethod
    def path(goal):
        nodes = []
        flag = True
        current_id = goal
        if Solver.solver_nodes[current_id].previous() == -1:
            return "No valid solution found."
        while flag:
            if current_id == -1:
                flag = False
            else:
                nodes.insert(0, current_id)
                current_id = Solver.solver_nodes[current_id].previous()
        return nodes
