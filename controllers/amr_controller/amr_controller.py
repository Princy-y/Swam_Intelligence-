from controller import Robot

# Initialize the robot instance
robot = Robot()

# Get the simulation time step (typically 32 ms)
timestep = int(robot.getBasicTimeStep())

# Connect to the Pioneer 3-DX motors
left_motor = robot.getDevice('left wheel')
right_motor = robot.getDevice('right wheel')

# Set motors to velocity control mode (infinity position)
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set a forward driving speed (rad/s)
SPEED = 3.0
left_motor.setVelocity(SPEED)
right_motor.setVelocity(SPEED)

print("[SUCCESS] Controller connected! Robot is driving forward...")

# Main simulation loop
while robot.step(timestep) != -1:
    pass