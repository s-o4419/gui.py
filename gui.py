
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
        
        def build_interface(self):
            title = ttk.Label(
            self.root,
            text="RoboMove Simulator",
            font=("Arial", 20, "bold")
            )
            title.pack(pady=10)

            self.canvas = tk.Canvas(
                self.root,
                width=self.cell_size * 9,
                height=self.cell_size * 9,
                bg="white",
                highlightthickness=1,
                highlightbackround="#cccccc"
            )                 
            self.canvas.pack(padx=10, pady=5)

            controls = ttk.Frame(self.root)
            controls.pack(pady=10)

            ttk.Button(
                controls, text="⬆️ Forward",
                command=self.forward
            ).grid(row=0, column=1, padx=5, pady=4)

            ttk.Button(
                controls, text="⬅️ Turn Left",
                command=self.turn_left
            ).grid(row=1, column=0, padx=5, pady=4)
                                                      
            
