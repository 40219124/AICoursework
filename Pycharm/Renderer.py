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
    canvas = -1
    selected = -1

    def __init__(self):
        if not Solver.ready:
            Solver.initialise_solver()
        min_x = 9999999
        max_x = -9999999
        min_y = 9999999
        max_y = -9999999
        for i in range(len(Solver.solver_nodes)):
            # Make the new render node
            rn = RenderNode()
            rn.id = i
            rn.loc = Solver.solver_nodes[i].get_node().get_position()
            # To calculate screen details
            if rn.loc[0] < min_x:
                min_x = rn.loc[0]
            if rn.loc[0] > max_x:
                max_x = rn.loc[0]
            if rn.loc[1] < min_y:
                min_y = rn.loc[1]
            if rn.loc[1] > max_y:
                max_y = rn.loc[1]
            Renderer.render_nodes.append(rn)
        # Save screen details
        Renderer.min_x = 1 - min_x
        Renderer.min_y = 1 - min_y
        Renderer.width = max_x - min_x + 2
        Renderer.height = max_y - min_y + 2
        # Start node
        Renderer.render_nodes[0].start = True
        Renderer.render_nodes[0].selected = True
        Renderer.render_nodes[0].visited = True
        Renderer.render_nodes[0].examined = True
        Renderer.selected = 0
        # Goal node
        Renderer.render_nodes[len(Renderer.render_nodes) - 1].goal = True

        # Window set up
        Renderer.window.title("Hey!")
        Renderer.window.geometry(str(Renderer.width * Renderer.scale + 100) + "x" +
                                 str(Renderer.height * Renderer.scale + 100))
        # Button frame set up
        bottomframe = Frame(Renderer.window)
        bottomframe.pack(side=BOTTOM)
        # Button for all
        all_button = Button(bottomframe, text="All", fg="black", command=Renderer.do_all)
        all_button.pack(side=TOP)
        # Button for stepping
        step_button = Button(bottomframe, text="Step", fg="black", command=Renderer.do_step)
        step_button.pack(side=BOTTOM)
        # Canvas set up
        Renderer.canvas = Canvas(Renderer.window, width=Renderer.width * Renderer.scale,
                                 height=Renderer.height * Renderer.scale)
        Renderer.canvas.pack(side=TOP)
        # Draw on canvas
        for node in Renderer.render_nodes:
            for link in node.get_solver_node().get_node().get_links():
                Renderer.draw_links(Renderer.canvas, link)
        for node in Renderer.render_nodes:
            Renderer.draw_node(Renderer.canvas, node)

        # Main loop
        Renderer.window.mainloop()

    @staticmethod
    def do_all():
        while not Solver.solved:
            Renderer.do_step()
        # Renderer.do_step()

    @staticmethod
    def do_step():
        Solver.generate_by_step()
        if Renderer.selected != -1:
            Renderer.render_nodes[Renderer.selected].selected = False
            Renderer.selected = -1
        if not Solver.solved:
            if len(Renderer.inspected) > 0:
                sel = Renderer.inspected.pop(0)
                Renderer.selected = sel
                Renderer.render_nodes[sel].visited = True
                Renderer.render_nodes[sel].selected = True
            queue = Solver.visit_queue
            new_inspects = []
            for pair in queue:
                new_inspects.append(pair[0])
                if pair[0] not in Renderer.inspected:
                    Renderer.render_nodes[pair[0]].examined = True
                    Renderer.inspected.append(pair[0])
            Renderer.inspected = new_inspects
        else:
            Renderer.render_nodes[len(Renderer.render_nodes) - 1].visited = True
            Renderer.render_nodes[len(Renderer.render_nodes) - 1].selected = True
            for node_id in Solver.get_path():
                Renderer.render_nodes[node_id].selected = True
        for node in Renderer.render_nodes:
            Renderer.draw_node(Renderer.canvas, node)

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
            if render_node.selected:
                canvas.itemconfig(render_node.oval, fill="#66ff66")
            else:
                canvas.itemconfig(render_node.oval, fill="#2eb82e")
        if render_node.goal:
            if render_node.selected:
                canvas.itemconfig(render_node.oval, fill="#ff3311")
            else:
                canvas.itemconfig(render_node.oval, fill="#cc0000")

    @staticmethod
    def draw_links(canvas, link):
        start = list(Solver.solver_nodes[link.start].get_node().get_position())
        start[0] = (start[0] + Renderer.min_x) * Renderer.scale
        start[1] = (Renderer.height - (start[1] + Renderer.min_y)) * Renderer.scale
        end = list(Solver.solver_nodes[link.end].get_node().get_position())
        end[0] = (end[0] + Renderer.min_x) * Renderer.scale
        end[1] = (Renderer.height - (end[1] + Renderer.min_y)) * Renderer.scale
        start, end = Renderer.arrow_reduction(start, end)

        canvas.create_line(start[0], start[1], end[0], end[1], arrow=LAST)

    @staticmethod
    def arrow_reduction(start, end):
        direction = [end[0] - start[0], end[1] - start[1]]
        direction = Renderer.normalise(direction)
        start = [start[0] + direction[0] * 5, start[1] + direction[1] * 5]
        end = [end[0] - direction[0] * 5, end[1] - direction[1] * 5]
        return start, end

    @staticmethod
    def normalise(vec):
        length = (vec[0] ** 2 + vec[1] ** 2)**(1/2)
        return [vec[0]/length, vec[1]/length]
