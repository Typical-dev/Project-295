"""robo_controller_295 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Keyboard, Motion

timestep = 32
key = -1

# create the Robot instance.
robot = Robot()
keyboard = Keyboard()
keyboard.enable(timestep)

wave = Motion("../../motions/wave.motion")

def printMessages():
    print("press up to wave")

printMessages()

while robot.step(timestep) != -1:
    key = keyboard.getKey()
    
    if key == Keyboard.UP:
        wave.play()
