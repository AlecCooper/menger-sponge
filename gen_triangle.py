import rhinoscriptsyntax as rs

class Triangle():

    def __init__(self,origin,length):

        self.length = length
        self.origin = origin

        # Add vertices
        vertices = []
        vertices.append(origin) #0
        vertices.append((origin[0]+length,origin[1],origin[2])) #1
        vertices.append((origin[0],origin[1]+length,origin[2])) #2
        vertices.append((origin[0]+length,origin[1]+length,origin[2])) #3
        vertices.append((origin[0]+length/2,origin[1]+length/2,origin[2]+length)) #4

        # Add faceVertices
        faceVertices = []
        faceVertices.append([0,1,2,3])
        faceVertices.append([0,1,4])
        faceVertices.append([0,2,4])
        faceVertices.append([2,3,4])
        faceVertices.append([1,3,4])

        # Verticies and Faces
        self.faceVertices = faceVertices
        self.vertices = vertices

        # Child cubes
        self.child_cubes = None

    # Divide into child cubes
    def divide(self):

        child_cubes = []
        l = self.length
        origin = self.origin

        x = origin[0]
        y = origin[1]
        z = origin[2]

        # Create list of new cube origins
        origins = []
        origins.append((x,y,z))
        origins.append((x + l/2, y, z))
        origins.append((x,y + l/2, z))
        origins.append((x + l/2,y + l/2, z))
        origins.append((x + l/4,y + l/4, z+l/2))
        

        # Create cubes with origins
        for o in origins:
            child_cubes.append(Triangle(o,l/2))

        self.child_cubes = child_cubes


    def get_children(self):

        if not self.child_cubes == None:
            cubes = []
            for cube in self.child_cubes:
                cubes += cube.get_children()

            return cubes
            
        else:
            return [self]
        

# Generate a list of the sub cubes of a menger sponge
def gen_cube(depth, origin, length):

    # define our initial cube
    cube = Triangle(origin, length)
    sub_cubes = cube.get_children()

    for level in xrange(depth):
        for sub_cube in sub_cubes:
            sub_cube.divide()   
            
        sub_cubes = cube.get_children()
        
    # Create a mesh for each subcube
    for sub_cube in sub_cubes:
        
        vertices = []
        for vertex in sub_cube.vertices:
            
            vertices.append(vertex)
        
        faces = []
        for face in sub_cube.faceVertices:
            faces.append(face)
            
        rs.AddMesh(vertices, faces)
            


if __name__=="__main__":
    length = rs.GetReal("Side length of cube:")
    depth = rs.GetInteger("Number of iterations:")
    origin = rs.GetPoint("Set the origin:")
    cube = gen_cube(depth-1,origin,length)
    
    





