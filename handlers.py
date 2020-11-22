class RotationHandler():
    def __init__(self, parent, viewer, d_angle):
        self.parent = parent
        self.viewer = viewer
        self.angle_increment = d_angle


    def rotate_left(self, event):
        self.viewer.rotate_horizontally(-self.angle_increment, False)
        self.parent.draw()

    def rotate_right(self, event):
        self.viewer.rotate_horizontally(self.angle_increment, False)
        self.parent.draw()

    def rotate_up(self, event):
        self.viewer.rotate_vertically(self.angle_increment, False)
        self.parent.draw()
        
    def rotate_down(self, event):
        self.viewer.rotate_vertically(-self.angle_increment, False)
        self.parent.draw()


    def rotate_camera_left(self, event):
        self.viewer.rotate_camera_horizontally(-self.angle_increment, False)
        self.parent.draw()

    def rotate_camera_right(self, event):
        self.viewer.rotate_camera_horizontally(self.angle_increment, False)
        self.parent.draw()

    def rotate_camera_up(self, event):
        self.viewer.rotate_camera_vertically(self.angle_increment, False)
        self.parent.draw()
        
    def rotate_camera_down(self, event):
        self.viewer.rotate_camera_vertically(-self.angle_increment, False)
        self.parent.draw()

class MovementHandler():
    def __init__(self, parent, viewer, d_distance):
        self.parent = parent
        self.viewer = viewer
        self.distance_increment = d_distance

    def move_left(self, event):
        self.viewer.translate_horizontally(-self.distance_increment)
        self.parent.draw()

    def move_right(self, event):
        self.viewer.translate_horizontally(self.distance_increment)
        self.parent.draw()

    def move_up(self, event):
        self.viewer.translate_vertically(-self.distance_increment)
        self.parent.draw()
        
    def move_down(self, event):
        self.viewer.translate_vertically(self.distance_increment)
        self.parent.draw()

class ZoomHandler():
    def __init__(self, parent, viewer, d_radius):
        self.parent = parent
        self.viewer = viewer
        self.radius_increment = d_radius

    def zoom_in(self, event):
        self.viewer.decrease_radius(self.radius_increment)
        self.parent.draw()

    def zoom_out(self, event):
        self.viewer.increase_radius(self.radius_increment)
        self.parent.draw()

    def zoom(self, event):
        if event.delta > 0:
            self.zoom_in(event)
        else:
            self.zoom_out(event)

class ResizeHandler():
    def __init__(self, parent, viewer):
        self.parent = parent
        self.viewer = viewer

    def resize(self, event):
        w,h = event.width - 4, event.height - 4

        self.viewer.update_dimensions(w, h)
        self.parent.canvas.config(width=w, height=h)
        self.parent.draw()