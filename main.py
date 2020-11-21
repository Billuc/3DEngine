import tkinter as tk
from tkinter import IntVar
from tkinter import simpledialog
from viewer import Viewer
from node import NamedNode3D

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)

        self.viewer = Viewer(600,400,p_radius=2)

        center = NamedNode3D(0,0,0, pname="center")
        x_axis = NamedNode3D(1,0,0, pname="x_axis")
        y_axis = NamedNode3D(0,1,0, pname="y_axis")
        z_axis = NamedNode3D(0,0,1, pname="z_axis")
        self.viewer.add_node(center)
        self.viewer.add_node(x_axis)
        self.viewer.add_node(y_axis)
        self.viewer.add_node(z_axis)

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
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(side="left", fill="both")

        #Canvas where we draw the dots
        self.canvas = tk.Canvas(self.main_frame, bg="#d0d0d0", height=400, width=600)
        self.canvas.pack(side="top", fill="both", expand=True)

        #Frame displaying the dots and buttons to add more
        self.right_frame = tk.Frame(self, bg="#ffffc5")
        self.right_frame.pack(side="right", fill="y")

        self.create_button = tk.Button(self.right_frame, bg="#00ff00", padx=5, pady=2, text="Create a node", command=self.create_node)
        self.create_button.pack(side="top", pady=(10,0))

        self.nodes_frame = tk.Frame(self.right_frame)
        self.nodes_frame.pack(side="top", fill="both", pady=10)

        self.scroll_bar = tk.Scrollbar(self.nodes_frame)
        self.scroll_bar.pack(side="right", fill="y")

        self.list_of_nodes = tk.Listbox(self.nodes_frame, yscrollcommand = self.scroll_bar.set)
        self.list_of_nodes.pack(side="left", fill="both")

        self.scroll_bar.config(command=self.list_of_nodes.yview)

        #Mode selection frame
        self.bottom_frame = tk.Frame(self.main_frame, bg="#ffffc5")
        self.bottom_frame.pack(side="bottom", fill="x")

        self.mode_label = tk.Label(self.bottom_frame, padx=7, pady=5, text="Movement Mode selection", bg="#08aaff")
        self.mode_label.pack(side="left", fill="y", padx=10)

        self.radio_rotating = tk.Radiobutton(self.bottom_frame, text="Rotating", variable=self.movement_mode, value=1, bg="#ffffc5")
        self.radio_rotating.pack(side="left")
        self.radio_rotating.select()
        
        self.radio_moving = tk.Radiobutton(self.bottom_frame, text="Moving", variable=self.movement_mode, value=2, bg="#ffffc5")
        self.radio_moving.pack(side="left")

        self.mode_label = tk.Label(self.bottom_frame, padx=7, pady=5, text="Player Mode selection", bg="#08aaff")
        self.mode_label.pack(side="left", fill="y", padx=10)

        self.radio_origin = tk.Radiobutton(self.bottom_frame, text="Origin centered", variable=self.player_mode, value=1, bg="#ffffc5")
        self.radio_origin.pack(side="left")
        self.radio_origin.select()
        
        self.radio_player = tk.Radiobutton(self.bottom_frame, text="Player centered", variable=self.player_mode, value=2, bg="#ffffc5")
        self.radio_player.pack(side="left")

        self.reset_button = tk.Button(self.bottom_frame, bg="red", padx=5, pady=2, text="Reset", command=self.reset_viewers)
        self.reset_button.pack(side="right", padx=10)


    def rotate_left(self):
        self.viewer.rotate_horizontally(-self.angle_increment, False)
        self.draw()

    def rotate_right(self):
        self.viewer.rotate_horizontally(self.angle_increment, False)
        self.draw()

    def rotate_up(self):
        self.viewer.rotate_vertically(self.angle_increment, False)
        self.draw()
        
    def rotate_down(self):
        self.viewer.rotate_vertically(-self.angle_increment, False)
        self.draw()

    def move_left(self):
        self.viewer.translate_horizontally(-self.distance_increment)
        self.draw()

    def move_right(self):
        self.viewer.translate_horizontally(self.distance_increment)
        self.draw()

    def move_up(self):
        self.viewer.translate_vertically(-self.distance_increment)
        self.draw()
        
    def move_down(self):
        self.viewer.translate_vertically(self.distance_increment)
        self.draw()

    def rotate_camera_left(self):
        self.viewer.rotate_camera_horizontally(-self.angle_increment, False)
        self.draw()

    def rotate_camera_right(self):
        self.viewer.rotate_camera_horizontally(self.angle_increment, False)
        self.draw()

    def rotate_camera_up(self):
        self.viewer.rotate_camera_vertically(self.angle_increment, False)
        self.draw()
        
    def rotate_camera_down(self):
        self.viewer.rotate_camera_vertically(-self.angle_increment, False)
        self.draw()

    def zoom_in(self):
        self.viewer.decrease_radius(self.radius_increment)
        self.draw()

    def zoom_out(self):
        self.viewer.increase_radius(self.radius_increment)
        self.draw()

    def zoom(self, event):
        if event.delta > 0:
            self.zoom_in()
        else:
            self.zoom_out()

    def resize(self, event):
        w,h = event.width - 4, event.height - 4

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
        self.viewer.reset_transform_matrix()

        self.draw()

    def create_node(self):
        x = simpledialog.askfloat("X", "Rentrez la valeur de X")
        y = simpledialog.askfloat("Y", "Rentrez la valeur de Y")
        z = simpledialog.askfloat("Z", "Rentrez la valeur de Z")
        name = simpledialog.askstring("Nom du point", "Rentrez un nom pour le point")

        if x is None or y is None or z is None or name is None:
            raise BaseException("Missing field ! All fields have to be filled.")
        else:
            new_node = NamedNode3D(x, y, z, pname=name)
            self.viewer.add_node(new_node)
            self.list_of_nodes.insert("end", new_node)

            self.draw()

    def draw(self):
        self.canvas.delete("all")

        """# Central point
        self.canvas.create_oval(
                    int(self.canvas.cget("width")) / 2. - self.node_radius,
                    int(self.canvas.cget("height")) / 2. - self.node_radius,
                    int(self.canvas.cget("width")) / 2. + self.node_radius,
                    int(self.canvas.cget("height")) / 2. + self.node_radius,
                    fill="#00ff00"
                )"""

        self.viewer.calc_nodes_2d()
        self.draw_axes()

        for n in self.viewer.nodes_2d:
            displayed_radius = self.node_radius * n.w / n.z 

            fill_color = "red"
            if n.name in ("center", "x_axis", "y_axis", "z_axis"):
                fill_color = "blue"

            self.canvas.create_oval(
                n.x / n.w - displayed_radius,
                n.y / n.w - displayed_radius,
                n.x / n.w + displayed_radius,
                n.y / n.w + displayed_radius,
                fill=fill_color
            )

    def draw_axes(self):
        calc_center = self.viewer.find("center")
        calc_x = self.viewer.find("x_axis")
        calc_y = self.viewer.find("y_axis")
        calc_z = self.viewer.find("z_axis")  

        self.draw_axis(calc_center, calc_x)    
        self.draw_axis(calc_center, calc_y)    
        self.draw_axis(calc_center, calc_z)    

    
    def draw_axis(self, point_a, point_b):
        if point_a is not None and point_b is not None:
            self.canvas.create_line(
                    point_a.x / point_a.w, 
                    point_a.y / point_a.w,
                    point_b.x / point_b.w,
                    point_b.y / point_b.w,
                    fill="black"
                )



root = tk.Tk()
root.title("3D Engine")
app = Application(master=root)
app.mainloop()