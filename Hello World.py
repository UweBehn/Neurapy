from neurapy.robot import Robot
import time

print("################################")
print("First LARA 8 example")
print("################################")

r = Robot()
print(r.robot_name)
print(r.dof)
print(r.platform)
print(r.payload)
print(r.kURL)
print(r.robot_urdf_path)
print(r.current_tool)
print(r.connection)
print(r.version)

r.set_mode("Automatic")
time.sleep(1)


'''
joint_property = {
    "speed": 100.0, "acceleration": 100.0,
    "target_joint": [
        [0.7740276502469322, 0.13599234975308788, 1.2223307505101257, -0.31901765024691225, 0.3242476502469122, -0.31901765024691225],
        [0.30333999999999633, -0.5334353004938217, 1.4419907505101492, -0.31901765024691225, 0.3242476502469122, -0.31901765024691225],
        [0.059259210493824405, 0.08133676975309524, 1.4419907505101492, -1.0084715804938613, -0.7008323497530976, -0.31901765024691225]
    ]
}
r.move_joint(**joint_property)

print(r.get_current_joint_angles())
print(r.get_doc("move_joint"))

# moving the robot to initial position
joint_property = {
    "speed": 100.0, "acceleration": 100.0, "safety_toggle": False, 
    "target_joint": [
        [-0.0007546, 0.2713685, 1.2664022, -0.0007550, 1.6046191, -0.0007501]
    ],  "current_joint_angles":r.robot_status("jointAngles")
}
r.move_joint(**joint_property)

linear_property = {
    "speed": 1.5, "acceleration": 1.0, 
    "target_pose": [
            [0.521504613338733,-0.0005120121635832758,0.4429621801014548,3.140838623046875,-0.0007978816283866763,3.1415627002716064],
            [0.5216067833501538,-0.21429644443731097,0.44311804388931564,3.140573024749756,-0.0008633044781163335,3.1414897441864014],
            [0.30336607796720333,-0.2139397968890111,0.44282379715713066,3.140761613845825,-0.0011759602930396795,3.1410810947418213],
            [0.3033097863631349,0.19367482201823044,0.44268805519921206,-3.1399381160736084,-0.001531908637844026,3.141218662261963],
            [0.5376223865405412,0.19093033055550618,0.44330028363322316,-3.1380574703216553,-0.0019246124429628253,3.1399550437927246],
            [0.521504613338733,-0.0005120121635832758,0.4429621801014548,3.140838623046875,-0.0007978816283866763,3.1415627002716064]
        ],   
        "current_joint_angles":r.robot_status("jointAngles")
}
r.move_linear(**linear_property)

'''

print(r.get_point("pointA"))
print(r.get_point('pointA','Cartesian'))
print(r.get_point("pointB"))
print(r.get_point('pointB','Cartesian'))

#print(r.get_doc("move_linear"))

# moving the robot to initial position "pointA"
joint_property = {
    "speed": 100.0, "acceleration": 100.0, "safety_toggle": False, 
    "target_joint": [
        r.get_point("pointA")    
    ]
}
r.move_joint(**joint_property)


# moving the robot to initial position "pointB"
joint_property = {
    "speed": 100.0, "acceleration": 100.0, "safety_toggle": False, 
    "target_joint": [
        r.get_point("pointB")    
    ]
}
r.move_joint(**joint_property)

# moving the robot to position pointB and back to pointA
linear_property = {
    "speed": 0.9, "acceleration": 0.2, 
    "target_pose": [
        r.get_point('pointA','Cartesian'),
        r.get_point('pointB','Cartesian'),
        r.get_point('pointA','Cartesian')
    ]
}
r.move_linear(**linear_property)



'''
# Move to initial position
joint_property = {
    "speed": 50.0, "acceleration": 50.0, "safety_toggle": True,
    "target_joint": [
        [0.3223498, 0.170158, 1.3894271, -0.0039065, 1.5862455, -0.0013291]
    ],  "current_joint_angles": r.robot_status("jointAngles")
}
r.move_joint(**joint_property)

circular_property = {
    "speed": 0.25, "acceleration": 0.1, 
    "target_pose": [
        [0.3744609827431085,-0.3391784988266481,0.23276604279256016,3.14119553565979,-0.00017731254047248513,-0.48800110816955566],
        [0.37116786741831503,-0.19686307684994242,0.23300456855796453,3.141423225402832,-0.00020668463548645377,-0.48725831508636475],
        [0.5190337951593321,-0.1969996948428492,0.23267853691809767,3.1414194107055664,-0.00017726201622281224,-0.48750609159469604]
    ],  "current_joint_angles": r.robot_status("jointAngles")
}
r.move_circular(**circular_property)
'''