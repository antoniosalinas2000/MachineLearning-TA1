from obj_converter import Obj

if __name__ == '__main__':
    obj = Obj.read("models/obj/Rick.obj")
    stl = obj.to_stl()

    print("")
    print("")
    print("OBJ File:", obj)
    print("STL File:", stl)

    stl.write("models/stl/stlRick.stl")