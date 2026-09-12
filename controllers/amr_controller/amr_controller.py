from controller import Robot

# ============================================================
# AMR-01 BASIC CONTROLLER
# STEP 1: WAREHOUSE CONSTRUCTION
# ============================================================

# Initialize robot
robot = Robot()

# Get Webots simulation time step
timestep = int(robot.getBasicTimeStep())

# Get Pioneer 3-DX motors
left_motor = robot.getDevice('left wheel')
right_motor = robot.getDevice('right wheel')

# Set motors to velocity control mode
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Keep robot stationary while building the warehouse
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

print("[SUCCESS] AMR-01 controller connected.")
print("[INFO] Robot is stationary - warehouse construction mode.")

# Main simulation loop
while robot.step(timestep) != -1:
    pass