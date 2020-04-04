import rhinoscriptsyntax as rs

class Cube(rs.Mesh):

    def __init__(self,origin,length):
        super().__init__()

        self.length = length
        self.origin = origin

        # Add vertices
        vertices = []
        vertices.append(origin) #0
        vertices.append((origin[0]+length,origin[1],origin[2])) #1
        vertices.append((origin[0],origin[1]+length,origin[2])) #2
        vertices.append((origin[0],origin[1],origin[2]+length)) #3
        vertices.append((origin[0]+length,origin[1]+length,origin[2])) #4
        vertices.append((origin[0]+length,origin[1],origin[2]+length)) #5
        vertices.append((origin[0],origin[1]+length,origin[2]+length)) #6
        vertices.append((origin[0]+length,origin[1]+length,origin[2]+length)) #7

        # Add faceVertices
        faceVertices = []
        faceVertices.append([0,2,6,3])
        faceVertices.append([0,3,5,1])
        faceVertices.append([0,1,4,2])
        faceVertices.append([1,5,7,4])
        faceVertices.append([3,5,7,6])
        faceVertices.append([2,6,7,4])

        # Child cubes
        self.child_cubes = None

    # Divide into child cubes
    def divide():

        child_cubes = []
        length = self.length/3
        origin = self.origin

        x = origin[0]
        y = origin[1]
        z = origin[2]

        # Create list of new cube origins
        origins = []
        origins.append(x,y,z)
        origins.append(x*2/3,y,z)
        origins.append(x*3,y,z)
        origins.append(x,y*2/3,z)
        origins.append(x,y*3,z)
        origins.append(x,y,z*2/3)
        origins.append(x,y,z*3)
        origins.append(x*2/3,y,z*2/3)
        origins.append(x,y*2/3,z*2/3)
        origins.append(x*3,y,z*2/3)
        origins.append(x,y*3,z*2/3)
        origins.append(x*3,y*3,z*2/3)
        origins.append(x*2/3,y,z*3)
        origins.append(x*3,y,z*3)
        origins.append(x,y*2/3,z*2/3)
        origins.append(x,y*3,z*3)
        origins.append(x*2/3,y*3,z*3)
        origins.append(x*3,y*2/3,z*3)
        origins.append(x*3,y*3,z*3)
        origins.append(x*3,y*3,z)

        # Create cubes with origins
        for o in origins:

            child_cubes.append(Cube(o,length))

        return child_cubes


    def get_children(self):

        if not self.child_cubes == None:

            cubes = []
            for cube in cubes:
                cubes.append(cube.get_children)

            return cubes

        else:
            return self












        















