import os
from FileInput import FileInput
from GraphMaker import GraphMaker
from Renderer import Renderer

# run program
# print("Hello world.")
this_dir = os.path.dirname(os.path.realpath(__file__))
FileInput.do_file_input(this_dir, 4)
GraphMaker.build_nodes()
GraphMaker.build_connections()
# for n in GraphMaker.nodes:
#     print(str(n))

# n = Node()
# n.set_position((1, 2))
# print(str(n))
# n2 = Node()
# n2.set_position((4, 3))
# print(str(n2))

# Solver.initialise_solver(GraphMaker.nodes)
# Solver.generate_path()
#
# Solver.initialise_solver(GraphMaker.nodes)

Renderer.render_graph()
