
import Rhino
import rhinoscriptsyntax as rs
import scriptcontext
import System.Guid

class Cube():

    def __init__(self,origin,length):

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
        origins.append((x+(l*2/3),y,z))
        origins.append((x+(l*1/3),y,z))
        origins.append((x,y+(l*2/3),z))
        origins.append((x,y +(l*1/3),z))
        origins.append((x,y,z+(l*2/3)))
        origins.append((x,y,z+(l*1/3)))
        origins.append((x+(l*2/3),y,z+(l*2/3)))
        origins.append((x,y+(l*2/3),z+(l*2/3)))
        origins.append((x+(l*1/3),y,z+(l*2/3)))
        origins.append((x,y+(l*1/3),z+(l*2/3)))
        origins.append((x+(l*2/3),y+(l*1/3),z+(l*2/3)))
        origins.append((x+(l*2/3),y,z+(l*1/3)))
        origins.append((x+(l*2/3),y+(l*1/3),z))
        origins.append((x+(l*2/3),y+(l*2/3),z))
        origins.append((x+(l*2/3),y+(l*2/3),z+(l*2/3)))
        origins.append((x+(l*1/3),y+(l*2/3),z+(l*2/3)))
        origins.append((x+(l*1/3),y+(l*2/3),z))
        origins.append((x,y+(l*2/3),z+(l*1/3)))
        origins.append((x+(l*2/3),y+(l*2/3),z+(l*1/3)))

        # Create cubes with origins
        for o in origins:
            child_cubes.append(Cube(o,l/3))

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
    cube = Cube(origin, length)
    sub_cubes = cube.get_children()

    for level in xrange(depth):
        for sub_cube in sub_cubes:
            sub_cube.divide()   
            
        sub_cubes = cube.get_children()
        
    # Create a rhino mesh
    #mesh = Rhino.Geometry.Mesh()
        
    for sub_cube in sub_cubes:
        #sub_mesh = Rhino.Geometry.Mesh()
        vertices = []
        for vertex in sub_cube.vertices:
            #sub_mesh.Vertices.Add(vertex[0],vertex[1],vertex[2])
            vertices.append(vertex)
        
        faces = []
        for face in sub_cube.faceVertices:
            #sub_mesh.Faces.AddFace(face[0],face[1],face[2],face[3])
            faces.append(face)
            
        rs.AddMesh(vertices, faces)
            
        #origin = sub_cube.origin
        #sub_mesh.Translate(origin[0],origin[1],origin[2])
                
        #mesh.Append(sub_mesh)
        #rs.MessageBox ("Hello World")

    
    #mesh.Normals.ComputeNormals()
    #mesh.Compact()
            
    #if scriptcontext.doc.Objects.AddMesh(mesh)!=System.Guid.Empty:
    #    scriptcontext.doc.Views.Redraw()
    #    return Rhino.Commands.Result.Success
    #return Rhino.Commands.Result.Failure
        
        

if __name__=="__main__":
    cube = gen_cube(5,(0.,0.,0.),10)
    
    





