from node import *
from matrix import Matrix
from math import cos, sin, pi, tan, atan

# Object corresponding to a set of points and data to transform them
class Viewer():
    def __init__(self, p_width, p_height, p_v_fov = pi/2, p_radius = 10):
        # Width and height of display
        self.width = float(p_width)
        self.height = float(p_height)

        # Fields of view (vertical and horizontal)
        self.v_fov = float(p_v_fov)
        self.h_fov = 2 * atan( tan(self.v_fov / 2) * p_width / p_height )

        # Distance between the origin and the "camera"
        self.radius = float(p_radius)

        # The transformation matrix (rotations)
        #  The zz element is -1 because the vertical axis on displays is towards the bottom
        self.transformation_matrix = Matrix(
                                        1,0,0,0,
                                        0,1,0,0,
                                        0,0,-1,0,
                                        0,0,0,1
                                    )

        # Arrays containing the original nodes, their transformed and projected nodes
        self.nodes = []
        self.transformed_nodes = []
        self.nodes_2d = []

    # Method to add a new node
    def add_node(self, node):
        self.nodes.append(node)

    # Method that transforms and projects the nodes
    def calc_nodes_2d(self):
        self.transformed_nodes = []
        self.nodes_2d = []

        # Looping through all the nodes
        for n in self.nodes:
            # Calculating the transformed node by multiplying the transform matrix by the node
            tranformed = self.transformation_matrix.multiply_by_node(n)
            # Unnecessary
            self.transformed_nodes.append(tranformed)

            # Calculating the intersection of the screen plan and the line passing through the camera and the transformed node
            #  Plan's equation : x = 0 (the constant doesn't really matter as long as it is lower than self.radius; 0 is just convenient)
            #  Line's equation : (x,y,z) = (camera pos) + t * ((transformed node) - (camera pos))
            #   Camera position = (self.radius, 0, 0)

            # To avoid dividing by 0
            #  Basically, if the transformed node is at the same x as the camera, we won't add the node
            if (tranformed.x / tranformed.w) == self.radius:
                t = 0
            else:
                # Solving
                t = - self.radius / ( (tranformed.x / tranformed.w) - self.radius )

            # If we are in front of the camera, the node is added
            if t > 0:
                # Calculating the relative coordinates on the screen
                y = ( t * tranformed.y / tranformed.w ) / ( 2 * self.radius * tan(self.h_fov / 2.) ) + 1 / 2. 
                z = ( t * tranformed.z / tranformed.w ) / ( 2 * self.radius * tan(self.v_fov / 2.) ) + 1 / 2.

                distance = ( (tranformed.x / tranformed.w) - self.radius )**2 + (tranformed.y / tranformed.w)**2 + (tranformed.z / tranformed.w)**2
                distance = distance**(1/2.)
                
                # Creating the projected node (with absolute coordinates)
                #  We add the distance to camera in the z coordinate
                node_2d = Node3D(self.width * y, self.height * z, distance, 1)

                # Adding the node
                self.nodes_2d.append(node_2d)

    # Rotating the view horizontally (around the z-axis)
    # Updating the transform matrix
    def rotate_horizontally(self, angle, isRadians = True):
        # If the angle is in degrees, we convert it to radians
        if not isRadians:
            angle = angle * pi / 180

        # Updating the transform matrix (rotating it by multiplicating by the rotation matrix)
        self.transformation_matrix = get_rot_z_matrix(angle).multiply(self.transformation_matrix)
        
    # Rotating the view vertically (around the y-axis)
    # Updating the transform matrix
    def rotate_vertically(self, angle, isRadians = False):
        # If the angle is in degrees, we convert it to radians
        if not isRadians:
            angle = angle * pi / 180

        # Updating the transform matrix (rotating it by multiplicating by the rotation matrix)
        self.transformation_matrix = get_rot_y_matrix(angle).multiply(self.transformation_matrix)

    # Rotating the camera horizontally (around the z-axis)
    # Updating the transform matrix
    def rotate_camera_horizontally(self, angle, isRadians = True):
        # If the angle is in degrees, we convert it to radians
        if not isRadians:
            angle = angle * pi / 180

        # Updating the transform matrix
        self.transformation_matrix = get_translate_x_matrix(-self.radius).multiply(self.transformation_matrix)
        self.transformation_matrix = get_rot_z_matrix(angle).multiply(self.transformation_matrix)
        self.transformation_matrix = get_translate_x_matrix(self.radius).multiply(self.transformation_matrix)
        
    # Rotating the camera vertically (around the y-axis)
    # Updating the transform matrix
    def rotate_camera_vertically(self, angle, isRadians = False):
        # If the angle is in degrees, we convert it to radians
        if not isRadians:
            angle = angle * pi / 180

        # Updating the transform matrix
        self.transformation_matrix = get_translate_x_matrix(-self.radius).multiply(self.transformation_matrix)
        self.transformation_matrix = get_rot_y_matrix(angle).multiply(self.transformation_matrix)
        self.transformation_matrix = get_translate_x_matrix(self.radius).multiply(self.transformation_matrix)

    # Translating the view horizontally (y-axis)
    # Updating the transform matrix
    def translate_horizontally(self, distance):
        # Updating the transform matrix (translating it by multiplicating by the translation matrix)
        self.transformation_matrix = get_translate_y_matrix(distance).multiply(self.transformation_matrix)
        
    # Translating the view vertically (z-axis)
    # Updating the transform matrix
    def translate_vertically(self, distance):
        # Updating the transform matrix (translating it by multiplicating by the translation matrix)
        self.transformation_matrix = get_translate_z_matrix(distance).multiply(self.transformation_matrix)

    # Zooming out by increasing the distance between the camera and the origin
    def increase_radius(self, delta):
        self.radius += delta

    # Zooming out by increasing the distance between the camera and the origin
    def decrease_radius(self, delta):
        if self.radius - delta <= 1:
            self.radius = 1
        else:
            self.radius -= delta

    # Updating width and height and horizontal field of view
    # Used when resize
    def update_dimensions(self, p_width, p_height):
        self.width = float(p_width)
        self.height = float(p_height)
        self.h_fov = 2 * atan( tan(self.v_fov / 2) * p_width / p_height )

    # Returns to the original view by resetting the transform matrix
    def reset_transform_matrix(self):
        self.transformation_matrix = Matrix(
                                        1,0,0,0,
                                        0,1,0,0,
                                        0,0,-1,0,
                                        0,0,0,1
                                    )


# Function to get the transform matrix of a rotation around the x-axis
def get_rot_x_matrix(angle):
    return Matrix(
        1, 0, 0, 0,
        0, cos(angle), -sin(angle), 0,
        0, sin(angle), cos(angle), 0,
        0, 0, 0, 1
    )

# Function to get the transform matrix of a rotation around the y-axis
def get_rot_y_matrix(angle):
    return Matrix(
        cos(angle), 0, sin(angle), 0,
        0, 1, 0, 0,
        -sin(angle), 0, cos(angle), 0,
        0, 0, 0, 1
    )

# Function to get the transform matrix of a rotation around the z-axis
def get_rot_z_matrix(angle):
    return Matrix(
        cos(angle), -sin(angle), 0, 0,
        sin(angle), cos(angle), 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1
    )

# Function to get the transform matrix of a rotation around the x-axis
def get_translate_x_matrix(distance):
    return Matrix(
        1, 0, 0, distance,
        0, 1, 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1
    )

# Function to get the transform matrix of a rotation around the y-axis
def get_translate_y_matrix(distance):
    return Matrix(
        1, 0, 0, 0,
        0, 1, 0, distance,
        0, 0, 1, 0,
        0, 0, 0, 1
    )

# Function to get the transform matrix of a rotation around the z-axis
def get_translate_z_matrix(distance):
    return Matrix(
        1, 0, 0, 0,
        0, 1, 0, 0,
        0, 0, 1, distance,
        0, 0, 0, 1
    )