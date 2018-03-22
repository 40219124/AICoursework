from FileInput import FileInput
from Node import Node
from GraphMaker import GraphMaker
from Solver import Solver
from tkinter import *
import tkinter as tk

# run program
print("Hello world.")

fi = FileInput.do_file_input()
GraphMaker.build_nodes()
GraphMaker.build_connections()
for n in GraphMaker.nodes:
    print(str(n))

# n = Node()
# n.set_position((1, 2))
# print(str(n))
# n2 = Node()
# n2.set_position((4, 3))
# print(str(n2))

Solver.initialise_solver(GraphMaker.nodes)
Solver.generate_path()
