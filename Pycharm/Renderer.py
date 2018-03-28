from tkinter import *
import tkinter as tk
from Solver import Solver


class RenderNode:

    def __init__(self):
        self.id = -1
        self.loc = (-1, -1)
        self.oval = -1
        self.start = False
        self.goal = False
        self.selected = False
        self.visited = False
        self.examined = False

    def get_solver_node(self):
        return Solver.solver_nodes[self.id]

    def get_x(self):
        return self.loc[0]

    def get_y(self):
        return self.loc[1]


class Renderer:

    scale = 20
    render_nodes = []
    inspected = []
    min_x = 0
    min_y = 0
    width = 0
    height = 0
    window = Tk()

    def __init__(self):
        min_x = 9999999
        max_x = -9999999
        min_y = 9999999
        max_y = -9999999
        for i in range(len(Solver.solver_nodes)):
            rn = RenderNode()
            rn.id = i
            rn.loc = Solver.solver_nodes[i].get_node().get_position()
            if rn.loc[0] < min_x:
                min_x = rn.loc[0]
            if rn.loc[0] > max_x:
                max_x = rn.loc[0]
            if rn.loc[1] < min_y:
                min_y = rn.loc[1]
            if rn.loc[1] > max_y:
                max_y = rn.loc[1]
            Renderer.render_nodes.append(rn)
        Renderer.min_x = 1 - min_x
        Renderer.min_y = 1 - min_y
        Renderer.width = max_x - min_x + 2
        Renderer.height = max_y - min_y + 2
        Renderer.render_nodes[0].start = True
        Renderer.render_nodes[len(Renderer.render_nodes) - 1].goal = True

        Renderer.window.title("Hey!")
        Renderer.window.geometry(str(Renderer.width * Renderer.scale + 100) + "x" +
                                 str(Renderer.height * Renderer.scale + 100))

        frame = Frame(Renderer.window)
        frame.pack()

        bottomframe = Frame(Renderer.window)
        bottomframe.pack(side=BOTTOM)

        redbutton = Button(bottomframe, text="Red", fg="red")
        redbutton.pack(side=RIGHT)

        bluebutton = Button(bottomframe, text="Blue", fg="blue")
        bluebutton.pack(side=LEFT)

        greenbutton = Button(bottomframe, text="Green", fg="green")
        greenbutton.pack(side=TOP)

        blackbutton = Button(bottomframe, text="Black", fg="black", command=Renderer.do_step)
        blackbutton.pack(side=BOTTOM)

        Renderer.window.mainloop()

    @staticmethod
    def do_step():
        if len(Renderer.inspected) > 0:
            Renderer.render_nodes[Renderer.inspected[0]].visited = True
        Solver.generate_by_step()
        queue = Solver.visit_queue
        for pair in queue:
            if pair[0] not in Renderer.inspected:
                Renderer.render_nodes[pair[0]].examined = True
                Renderer.inspected.append(pair[0])
        c = Canvas(Renderer.window, width=Renderer.width * Renderer.scale, height=Renderer.height * Renderer.scale)
        c.pack(side=TOP)
        for node in Renderer.render_nodes:
            Renderer.draw_node(c, node)

    @staticmethod
    def draw_node(canvas, render_node):
        assert type(render_node) is RenderNode, "not a render node"
        if render_node.oval == -1:
            x = (render_node.loc[0] + Renderer.min_x) * Renderer.scale
            y = (Renderer.height - (render_node.loc[1] + Renderer.min_y)) * Renderer.scale
            render_node.oval = canvas.create_oval(x - 5, y - 5, x + 5, y + 5)
        if render_node.examined:
            canvas.itemconfig(render_node.oval, fill="#66c2ff")
        if render_node.visited:
            canvas.itemconfig(render_node.oval, fill="#0044cc")
        if render_node.selected:
            canvas.itemconfig(render_node.oval, fill="#ff8c1a")
        if render_node.start:
            canvas.itemconfig(render_node.oval, fill="#2eb82e")
        if render_node.goal:
            canvas.itemconfig(render_node.oval, fill="#cc0000")
