from obj_converter import Wavefront

if __name__ == '__main__':
    obj = Wavefront.read("models/obj/Rick.obj")
    stl = obj.to_stl()

    print("")
    print("")
    print("OBJ File:", obj)
    print("STL File:", stl)

    stl.write("models/stl/stlRick.stl")