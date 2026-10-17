
import tkinter as tk
from tkinter import ttk

from robot import Robot


class RobotGUI:
    def _init_(self, root):
        self.root = root
        self.root.title("RoboMove - Student Robotics")
        self.root.geometry("760x650")
        self.root.minsize(620, 580)

        self.robot = Robot(grid_size=9)
        self.cell_size = 48
        self.padding = 20

        self.status = tk.StringVar()
        self.message = tk.StringVar(value="Robot is ready!")

        self.build_interface()
        self.draw_grid()
        