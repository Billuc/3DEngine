# 4x4 transform Matrix (3D)
class Matrix():
    def __init__(self, 
                    pxx = 0., pxy = 0., pxz = 0., pxw = 0.,
                    pyx = 0., pyy = 0., pyz = 0., pyw = 0.,
                    pzx = 0., pzy = 0., pzz = 0., pzw = 0.,
                    pwx = 0., pwy = 0., pwz = 0., pww = 1.):
        self.xx = float(pxx)
        self.xy = float(pxy)
        self.xz = float(pxz)
        self.xw = float(pxw)
        
        self.yx = float(pyx)
        self.yy = float(pyy)
        self.yz = float(pyz)
        self.yw = float(pyw)

        self.zx = float(pzx)
        self.zy = float(pzy)
        self.zz = float(pzz)
        self.zw = float(pzw)

        self.wx = float(pwx)
        self.wy = float(pwy)
        self.wz = float(pwz)
        self.ww = float(pww)

    def __repr__(self):
        matrix_as_string = "["
        matrix_as_string += "%s, %s, %s, %s" % (self.xx, self.xy, self.xz, self.xw)
        matrix_as_string += "\n"

        matrix_as_string += " %s, %s, %s, %s" % (self.yx, self.yy, self.yz, self.yw)
        matrix_as_string += "\n"

        matrix_as_string += " %s, %s, %s, %s" % (self.zx, self.zy, self.zz, self.zw)
        matrix_as_string += "\n"

        matrix_as_string += " %s, %s, %s, %s" % (self.wx, self.wy, self.wz, self.ww)
        matrix_as_string += "]"

        return matrix_as_string

    # Standard matrix multiplication
    #  other_matrix : another Matrix (4x4 matrix) object
    def multiply(self, other_matrix):
        
        # Result matrix
        m = Matrix()

        m.xx = self.xx * other_matrix.xx + \
                    self.xy * other_matrix.yx + \
                    self.xz * other_matrix.zx + \
                    self.xw * other_matrix.wx
        m.xy = self.xx * other_matrix.xy + \
                    self.xy * other_matrix.yy + \
                    self.xz * other_matrix.zy + \
                    self.xw * other_matrix.wy
        m.xz = self.xx * other_matrix.xz + \
                    self.xy * other_matrix.yz + \
                    self.xz * other_matrix.zz + \
                    self.xw * other_matrix.wz
        m.xw = self.xx * other_matrix.xw + \
                    self.xy * other_matrix.yw + \
                    self.xz * other_matrix.zw + \
                    self.xw * other_matrix.ww

        m.yx = self.yx * other_matrix.xx + \
                    self.yy * other_matrix.yx + \
                    self.yz * other_matrix.zx + \
                    self.yw * other_matrix.wx
        m.yy = self.yx * other_matrix.xy + \
                    self.yy * other_matrix.yy + \
                    self.yz * other_matrix.zy + \
                    self.yw * other_matrix.wy
        m.yz = self.yx * other_matrix.xz + \
                    self.yy * other_matrix.yz + \
                    self.yz * other_matrix.zz + \
                    self.yw * other_matrix.wz
        m.yw = self.yx * other_matrix.xw + \
                    self.yy * other_matrix.yw + \
                    self.yz * other_matrix.zw + \
                    self.yw * other_matrix.ww
                    
        m.zx = self.zx * other_matrix.xx + \
                    self.zy * other_matrix.yx + \
                    self.zz * other_matrix.zx + \
                    self.zw * other_matrix.wx
        m.zy = self.zx * other_matrix.xy + \
                    self.zy * other_matrix.yy + \
                    self.zz * other_matrix.zy + \
                    self.zw * other_matrix.wy
        m.zz = self.zx * other_matrix.xz + \
                    self.zy * other_matrix.yz + \
                    self.zz * other_matrix.zz + \
                    self.zw * other_matrix.wz
        m.zw = self.zx * other_matrix.xw + \
                    self.zy * other_matrix.yw + \
                    self.zz * other_matrix.zw + \
                    self.zw * other_matrix.ww
                    
        m.wx = self.wx * other_matrix.xx + \
                    self.wy * other_matrix.yx + \
                    self.wz * other_matrix.zx + \
                    self.ww * other_matrix.wx
        m.wy = self.wx * other_matrix.xy + \
                    self.wy * other_matrix.yy + \
                    self.wz * other_matrix.zy + \
                    self.ww * other_matrix.wy
        m.wz = self.wx * other_matrix.xz + \
                    self.wy * other_matrix.yz + \
                    self.wz * other_matrix.zz + \
                    self.ww * other_matrix.wz
        m.ww = self.wx * other_matrix.xw + \
                    self.wy * other_matrix.yw + \
                    self.wz * other_matrix.zw + \
                    self.ww * other_matrix.ww

        return m

    # Multiplication of the matrix by a Vector (Node3D)
    #  node : a Node3D (4 dim vector) object
    def multiply_by_node(self, node):
        from node import Node3D

        # Result vector
        n = Node3D()
        
        n.x = self.xx * node.x + \
                self.xy * node.y + \
                self.xz * node.z + \
                self.xw * node.w

        n.y = self.yx * node.x + \
                self.yy * node.y + \
                self.yz * node.z + \
                self.yw * node.w
                    
        n.z = self.zx * node.x + \
                self.zy * node.y + \
                self.zz * node.z + \
                self.zw * node.w
                    
        n.w = self.wx * node.x + \
                self.wy * node.y + \
                self.wz * node.z + \
                self.ww * node.w

        return n

# /!\ UNUSED /!\
# Function that creates a Matrix from a table (length : 16)
#  table : array of length 16 that contains the elements of the matrix   
def matrix_from_table(table):
    if len(table) == 16:
        return Matrix(
            float(table[0]), float(table[1]), float(table[2]), float(table[3]),
            float(table[4]), float(table[5]), float(table[6]), float(table[7]),
            float(table[8]), float(table[9]), float(table[10]), float(table[11]),
            float(table[12]), float(table[13]), float(table[14]), float(table[15]))
    else:
        raise BaseException("Table size should be 16")
