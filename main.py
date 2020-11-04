import tkinter as tk
from tkinter import IntVar
from viewer import Viewer
from node import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)

        self.axles_viewer = Viewer(600,400,p_radius=2)
        self.axles_viewer.add_node(Node3D(0,0,0))

        self.axles_viewer.add_node(Node3D(1,0,0))
        self.axles_viewer.add_node(Node3D(0,1,0))
        self.axles_viewer.add_node(Node3D(0,0,1))

        self.viewer = Viewer(600,400,p_radius=2)
        self.node_radius = 4
        self.angle_increment = 1
        self.distance_increment = 0.1
        self.radius_increment = 0.5

        # Movement Mode : rotation (1) or moving (2)
        self.movement_mode = IntVar()
        # Player Mode : origin-centered (1) or player-centered (2)
        self.player_mode = IntVar()

        self.create_widgets()
        self.init_keypress()
        self.draw()

    def init_keypress(self):
        self.master.bind('<Left>', self.handle_arrows)
        self.master.bind('<Right>', self.handle_arrows)
        self.master.bind('<Up>', self.handle_arrows)
        self.master.bind('<Down>', self.handle_arrows)
        
        self.canvas.bind('<MouseWheel>', self.zoom)

        self.canvas.bind('<Configure>', self.resize)

        self.master.bind('<space>', self.change_movement_mode)
        self.master.bind('<Shift_L>', self.change_player_mode)

    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg="#d0d0d0", height=400, width=600)
        self.canvas.pack(side="left", fill="both", expand=True)


        self.add_node_frame = tk.Frame(self, bg="#ffffc5")
        self.add_node_frame.pack(side="right", fill="y")

        self.add_frame_label = tk.Label(self.add_node_frame, padx=7, pady=5, text="New Node", bg="#08aaff")
        self.add_frame_label.pack(side="top", fill="x")
        
        self.x_label = tk.Label(self.add_node_frame, padx=3, text="X", bg="#ffffc5")
        self.x_label.pack(side="top", pady=(5,0))

        self.x_entry = tk.Entry(self.add_node_frame)
        self.x_entry.pack(side="top", padx=3)

        self.y_label = tk.Label(self.add_node_frame, padx=3, text="Y", bg="#ffffc5")
        self.y_label.pack(side="top", pady=(10,0))

        self.y_entry = tk.Entry(self.add_node_frame)
        self.y_entry.pack(side="top", padx=3)

        self.z_label = tk.Label(self.add_node_frame, padx=3, text="Z", bg="#ffffc5")
        self.z_label.pack(side="top", pady=(10,0))

        self.z_entry = tk.Entry(self.add_node_frame)
        self.z_entry.pack(side="top", padx=3)

        self.create_button = tk.Button(self.add_node_frame, bg="#00ff00", padx=5, pady=2, text="Create", command=self.create_node)
        self.create_button.pack(side="top", pady=(10,0))
        
        self.reset_button = tk.Button(self.add_node_frame, bg="red", padx=5, pady=2, text="Reset", command=self.reset_viewers)
        self.reset_button.pack(side="bottom", pady=10)

        self.mode_label = tk.Label(self.add_node_frame, padx=7, pady=5, text="Movement Mode selection", bg="#08aaff")
        self.mode_label.pack(side="top", fill="x", pady=10)

        self.radio_rotating = tk.Radiobutton(self.add_node_frame, text="Rotating", variable=self.movement_mode, value=1, bg="#ffffc5")
        self.radio_rotating.pack(side="top")
        self.radio_rotating.select()
        
        self.radio_moving = tk.Radiobutton(self.add_node_frame, text="Moving", variable=self.movement_mode, value=2, bg="#ffffc5")
        self.radio_moving.pack(side="top")

        self.mode_label = tk.Label(self.add_node_frame, padx=7, pady=5, text="Player Mode selection", bg="#08aaff")
        self.mode_label.pack(side="top", fill="x", pady=10)

        self.radio_origin = tk.Radiobutton(self.add_node_frame, text="Origin centered", variable=self.player_mode, value=1, bg="#ffffc5")
        self.radio_origin.pack(side="top")
        self.radio_origin.select()
        
        self.radio_player = tk.Radiobutton(self.add_node_frame, text="Player centered", variable=self.player_mode, value=2, bg="#ffffc5")
        self.radio_player.pack(side="top")


    def rotate_left(self):
        self.axles_viewer.rotate_horizontally(-self.angle_increment, False)
        self.viewer.rotate_horizontally(-self.angle_increment, False)
        self.draw()

    def rotate_right(self):
        self.axles_viewer.rotate_horizontally(self.angle_increment, False)
        self.viewer.rotate_horizontally(self.angle_increment, False)
        self.draw()

    def rotate_up(self):
        self.axles_viewer.rotate_vertically(self.angle_increment, False)
        self.viewer.rotate_vertically(self.angle_increment, False)
        self.draw()
        
    def rotate_down(self):
        self.axles_viewer.rotate_vertically(-self.angle_increment, False)
        self.viewer.rotate_vertically(-self.angle_increment, False)
        self.draw()

    def move_left(self):
        self.axles_viewer.translate_horizontally(-self.distance_increment)
        self.viewer.translate_horizontally(-self.distance_increment)
        self.draw()

    def move_right(self):
        self.axles_viewer.translate_horizontally(self.distance_increment)
        self.viewer.translate_horizontally(self.distance_increment)
        self.draw()

    def move_up(self):
        self.axles_viewer.translate_vertically(-self.distance_increment)
        self.viewer.translate_vertically(-self.distance_increment)
        self.draw()
        
    def move_down(self):
        self.axles_viewer.translate_vertically(self.distance_increment)
        self.viewer.translate_vertically(self.distance_increment)
        self.draw()

    def rotate_camera_left(self):
        self.axles_viewer.rotate_camera_horizontally(-self.angle_increment, False)
        self.viewer.rotate_camera_horizontally(-self.angle_increment, False)
        self.draw()

    def rotate_camera_right(self):
        self.axles_viewer.rotate_camera_horizontally(self.angle_increment, False)
        self.viewer.rotate_camera_horizontally(self.angle_increment, False)
        self.draw()

    def rotate_camera_up(self):
        self.axles_viewer.rotate_camera_vertically(self.angle_increment, False)
        self.viewer.rotate_camera_vertically(self.angle_increment, False)
        self.draw()
        
    def rotate_camera_down(self):
        self.axles_viewer.rotate_camera_vertically(-self.angle_increment, False)
        self.viewer.rotate_camera_vertically(-self.angle_increment, False)
        self.draw()

    def zoom_in(self):
        self.axles_viewer.decrease_radius(self.radius_increment)
        self.viewer.decrease_radius(self.radius_increment)
        self.draw()

    def zoom_out(self):
        self.axles_viewer.increase_radius(self.radius_increment)
        self.viewer.increase_radius(self.radius_increment)
        self.draw()

    def zoom(self, event):
        if event.delta > 0:
            self.zoom_in()
        else:
            self.zoom_out()

    def resize(self, event):
        w,h = event.width - 4, event.height - 4

        self.axles_viewer.update_dimensions(w, h)
        self.viewer.update_dimensions(w, h)

        self.canvas.config(width=w, height=h)

        self.draw()

    def handle_arrows(self, event):
        key = event.keysym
        
        if self.player_mode.get() == 1:
            if self.movement_mode.get() == 1:
                if key == "Left":
                    self.rotate_left()
                elif key == "Right":
                    self.rotate_right()
                elif key == "Up":
                    self.rotate_up()
                elif key == "Down":
                    self.rotate_down()
            elif self.movement_mode.get() == 2:
                if key == "Left":
                    self.move_left()
                elif key == "Right":
                    self.move_right()
                elif key == "Up":
                    self.move_up()
                elif key == "Down":
                    self.move_down()
        elif self.player_mode.get() == 2:
            if self.movement_mode.get() == 1:
                if key == "Left":
                    self.rotate_camera_left()
                elif key == "Right":
                    self.rotate_camera_right()
                elif key == "Up":
                    self.rotate_camera_up()
                elif key == "Down":
                    self.rotate_camera_down()
            elif self.movement_mode.get() == 2:
                if key == "Left":
                    self.move_right()
                elif key == "Right":
                    self.move_left()
                elif key == "Up":
                    self.move_down()
                elif key == "Down":
                    self.move_up()

    def change_movement_mode(self, event):
        if self.movement_mode.get() == 1:
            self.radio_moving.select()
        else:
            self.radio_rotating.select()

    def change_player_mode(self, event):
        if self.player_mode.get() == 1:
            self.radio_player.select()
        else:
            self.radio_origin.select()

    def reset_viewers(self):
        self.axles_viewer.reset_transform_matrix()
        self.viewer.reset_transform_matrix()

        self.draw()

    def create_node(self):
        x = float(self.x_entry.get())
        y = float(self.y_entry.get())
        z = float(self.z_entry.get())

        new_node = Node3D(x, y, z)
        self.viewer.add_node(new_node)

        self.draw()

        self.x_entry.delete(0, 'end')
        self.y_entry.delete(0, 'end')
        self.z_entry.delete(0, 'end')

    def draw(self):
        self.canvas.delete("all")

        # Central point
        self.canvas.create_oval(
                    int(self.canvas.cget("width")) / 2. - self.node_radius,
                    int(self.canvas.cget("height")) / 2. - self.node_radius,
                    int(self.canvas.cget("width")) / 2. + self.node_radius,
                    int(self.canvas.cget("height")) / 2. + self.node_radius,
                    fill="#00ff00"
                )

        self.draw_axles()

        self.viewer.calc_nodes_2d()

        for n in self.viewer.nodes_2d:
            displayed_radius = self.node_radius * self.viewer.radius / (n.z / n.w)

            self.canvas.create_oval(
                n.x / n.w - displayed_radius,
                n.y / n.w - displayed_radius,
                n.x / n.w + displayed_radius,
                n.y / n.w + displayed_radius,
                fill="red"
            )

    def draw_axles(self):
        self.axles_viewer.calc_nodes_2d()
        
        if len(self.axles_viewer.nodes_2d) > 0:
            center = self.axles_viewer.nodes_2d[0]

            for n in self.axles_viewer.nodes_2d:
                self.canvas.create_line(
                    center.x / center.w, 
                    center.y / center.w,
                    n.x / n.w,
                    n.y / n.w,
                    fill="black"
                )

            for n in self.axles_viewer.nodes_2d:
                displayed_radius = self.node_radius * self.axles_viewer.radius / (n.z / n.w)

                self.canvas.create_oval(
                    n.x / n.w - displayed_radius,
                    n.y / n.w - displayed_radius,
                    n.x / n.w + displayed_radius,
                    n.y / n.w + displayed_radius,
                    fill="blue"
                )



root = tk.Tk()
app = Application(master=root)
app.mainloop()