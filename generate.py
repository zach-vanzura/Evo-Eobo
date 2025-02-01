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
    pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3", type="revolute", position=[0, 0.5, 0.5])
    pyrosim.Send_Cube(name="Link3", pos=[0, 0.5, 0], size=[length, width, height])
    pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4", type="revolute", position=[0, 1, 0])
    pyrosim.Send_Cube(name="Link4", pos=[x_child, 0.5, 0], size=[length, width, height])
    pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5", type="revolute", position=[0, 0.5, -0.5])
    pyrosim.Send_Cube(name="Link5", pos=[0, 0, -0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6", type="revolute", position=[0, 0, -1])
    pyrosim.Send_Cube(name="Link6", pos=[0, 0, -0.5], size=[length, width, height])






    pyrosim.End()


create_world()
create_robot()
