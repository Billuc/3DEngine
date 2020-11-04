from matrix import Matrix, matrix_from_table
from node import Node3D
from viewer import *

def test_empty_matrix():
    m = Matrix()
    print(m)

def test_matrix():
    m = Matrix(1,2,3,4,5,6,7,8,9,11,10,12,13,14,15,16)
    print(m)

def test_matrix_from_table():
    table = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    m = matrix_from_table(table)
    print(m)

def test_multiply():
    m1 = Matrix(0,-1,0,0,1,0,0,0,0,0,1,0,0,0,0,1)
    m2 = Matrix(0,0,-1,0,0,1,0,0,1,0,0,0,0,0,0,1)
    m3 = m1.multiply(m2)
    print(m3)

def test_empty_node():
    n = Node3D()
    print(n)

def test_node():
    n = Node3D(1,2,3)
    print(n)

def test_multiply_by_node():
    m = Matrix(0,-1,0,0,0,0,-1,0,1,0,0,0,0,0,0,1)
    n = Node3D(1,2,3,1)
    n_result = m.multiply_by_node(n)
    print(n_result)

def test_rotations():
    v = Viewer(1,1)
    n = Node3D(1,2,3)

    v.add_node(n)

    from math import pi
    v.rotate_vertically(-pi/2)
    v.rotate_horizontally(pi/2)

    v.calc_nodes_2d()
    print(v.transformed_nodes)

def test_viewer():
    v = Viewer(6,4)
    n = Node3D(1,2,3)

    v.add_node(n)

    v.calc_nodes_2d()
    print(v.nodes_2d)

    from math import pi
    v.rotate_vertically(-pi/2)
    v.rotate_horizontally(pi/2)

    v.calc_nodes_2d()
    print(v.nodes_2d)


test_viewer()