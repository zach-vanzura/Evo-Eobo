import pyrosim.pyrosim as pyrosim

length, width, height = 1, 1, 1
x, y, z = 0, 0, 0.5

x_root, y_root, z_root = 0, 0, 0.5
x_child, y_child, z_child = 0, 0, 0.5


def create_world():

    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-3, 3, z], size=[length, width, height])
    pyrosim.End()


def create_robot():

    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link0", pos=[x_root, y_root, z_root], size=[length, width, height])
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0, 0, 1])
    pyrosim.Send_Cube(name="Link1", pos=[x_child, y_child, z_child], size=[length, width, height])
    pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[0, 0, 1])
    pyrosim.Send_Cube(name="Link2", pos=[x_child, y_child, z_child], size=[length, width, height])

    pyrosim.End()


create_world()
create_robot()
