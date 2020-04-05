
import Rhino
import scriptcontext
import System.Guid
from cube import Cube

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
    mesh = Rhino.Geometry.Mesh()

    for cube in sub_cubes:

        for vertice in cube.vertices:
            mesh.Verticies.AddVertice

        for face in cube.faceVertices:
            mesh.Faces.AddFace(face)

    
    mesh.Normals.ComputeNormals()
    mesh.Compact()
    if scriptcontext.doc.Objects.AddMesh(mesh)!=System.Guid.Empty:
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure

if __name__=="__main__":
    cube = gen_cube(1,(0,0,0),3)
    





