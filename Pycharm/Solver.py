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

    ready = False
    solver_nodes = []
    visited_count = 0
    visit_queue = []
    solved = False
    saved_path = []

    @staticmethod
    def reset_solver():
        Solver.solver_nodes.clear()
        Solver.visited_count = 0
        Solver.visit_queue = [(0, 0)]
        Solver.solved = False
        Solver.ready = False
        Solver.saved_path.clear()

    @staticmethod
    def initialise_solver():
        nodes = GraphMaker.nodes
        Solver.reset_solver()
        for i in range(len(nodes)):
            sn = SolverNode()
            sn.set_node(i)
            Solver.solver_nodes.append(sn)
        Solver.solver_nodes[0].shortest_dist = 0
        Solver.solver_nodes[len(nodes) - 1].goal = True
        Solver.ready = True

    @staticmethod
    # Dijkstra all in one
    def generate_path():
        if not Solver.ready:
            Solver.initialise_solver()
        if len(Solver.solver_nodes) == 0:
            print("No nodes. Aborting pathfinding.")
            return
        print("Search results:")

        while not Solver.solved:
            node_id = Solver.visit_queue[0][0]
            Solver.search_from_node(node_id)
            print(Solver.visit_queue)
            queue_length = len(Solver.visit_queue)
            if queue_length == 0:
                print("Didn't find a path.")
                break

        print(str(Solver.visited_count) + " visited")
        path = Solver.get_path()
        print(path)
        coords = ""
        for n in path:
            coords += str(Solver.solver_nodes[n].get_node()) + "\n"
        print(coords)

    @staticmethod
    # Step by step method for dijkstra
    def generate_by_step():
        if not Solver.ready:
            Solver.initialise_solver()
        if not Solver.solved:
            Solver.search_from_node(Solver.visit_queue[0][0])
        else:
            print(Solver.get_path())

    @staticmethod
    # Dijkstra method of node searching
    def search_from_node(this_id):
        Solver.visit_queue.pop(0)
        this_node = Solver.solver_nodes[this_id]
        Solver.visited_count += 1
        this_node.visited = True
        if this_node.goal:
            Solver.solved = True
            return
        dests = Solver.order_closest_neighbours(this_id)
        for d in dests:
            weight = this_node.get_node().get_connection_to(d).length()
            test_val = this_node.shortest_dist + weight
            if Solver.solver_nodes[d].shortest_dist == -1 \
                    or test_val < Solver.solver_nodes[d].shortest_dist:
                if Solver.solver_nodes[d].shortest_dist != -1:
                    Solver.visit_queue.remove((d, Solver.solver_nodes[d].shortest_dist))
                Solver.solver_nodes[d].shortest_dist = test_val
                Solver.solver_nodes[d].visited_from = this_id
                Solver.visit_queue.append((d, test_val))
                Solver.visit_queue.sort(key=Solver.sort_by_second)
                # Solver.search(d)
        Solver.solved = False

    @staticmethod
    def sort_by_second(pair):
        return pair[1]

    @staticmethod
    # Dijkstra method of neighbour sorting
    def order_closest_neighbours(root):
        cons = GraphMaker.nodes[root].get_destinations()
        for c in cons:
            if Solver.solver_nodes[c].visited:
                cons.remove(c)

        pairs = []
        while len(cons) > 0:
            key = cons.pop()
            pairs.append((key, GraphMaker.nodes[root].get_connection_to(key).length()))
        pairs.sort(key=Solver.sort_by_second)

        dests = []
        while len(pairs) > 0:
            dests.append(pairs.pop(0)[0])
        # while len(cons) > 0:
        #     shortest = 9999999
        #     short_id = -1
        #     for i in range(len(cons)):
        #         test_len = GraphMaker.nodes[root].get_connection_to(cons[i]).length()
        #         if test_len < shortest:
        #             shortest = test_len
        #             short_id = i
        #     dests.append(cons[short_id])
        #     cons.pop(short_id)
        return dests

    @staticmethod
    # A star method of neighbour sorting
    def order_weighted(root):
        x = root
        x += 1
        root_node = Solver.solver_nodes[root].get_node()
        cons = root_node.get_destinations()
        for c in cons:
            if Solver.solver_nodes[c].visited:
                cons.remove(c)
        dests = []
        while len(cons) > 0:
            lowest = 9999999
            low_id = -1
            for i in range(len(cons)):
                value = root_node.get_connection_to(cons[i]).length()
                value += GraphMaker.calculate_link_length(
                    Solver.solver_nodes[cons[i]].get_node().get_position(),
                    Solver.solver_nodes[len(Solver.solver_nodes) - 1].get_node().get_position())
                if value < lowest:
                    lowest = value
                    low_id = i
            dests.insert(0, cons[low_id])
            cons.pop(low_id)
        return dests

    @staticmethod
    # return the list of nodes from start to finish
    def get_path():
        if len(Solver.saved_path) == 0:
            nodes = []
            flag = True
            current_id = len(Solver.solver_nodes) - 1
            if Solver.solver_nodes[current_id].previous() == -1:
                return "No valid solution found."
            while flag:
                if current_id == -1:
                    flag = False
                else:
                    nodes.insert(0, current_id)
                    current_id = Solver.solver_nodes[current_id].previous()
            Solver.saved_path = nodes
        return Solver.saved_path
