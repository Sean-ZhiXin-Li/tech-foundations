from controller import Robot

TIME_STEP = 64
MAX_SPEED = 6.28

FRONT = [7, 0]      # front-most pair
LEFT_ARC = [6, 5]   # front-left arc
RIGHT_ARC = [1, 2]  # front-right arc

OBSTACLE_THR = 80.0 # tune 60~120 depending on world/lighting
PRINT_DEBUG = True

def enable_ir(robot):
    sensors = []
    for i in range(8):
        s = robot.getDevice(f'ps{i}')
        s.enable(TIME_STEP)
        sensors.append(s)
    return sensors

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def main():
    robot = Robot()

    left = robot.getDevice('left wheel motor')
    right = robot.getDevice('right wheel motor')
    left.setPosition(float('inf'))
    right.setPosition(float('inf'))
    left.setVelocity(0.0)
    right.setVelocity(0.0)

    sensors = enable_ir(robot)
    base = 0.80 * MAX_SPEED
    turn = 0.70 * MAX_SPEED

    while robot.step(TIME_STEP) != -1:
        vals = [s.getValue() for s in sensors]
        if PRINT_DEBUG:
            print("IR:", " ".join(f"{v:6.1f}" for v in vals))

        front = sum(vals[i] for i in FRONT) / len(FRONT)
        leftv = sum(vals[i] for i in LEFT_ARC) / len(LEFT_ARC)
        rightv = sum(vals[i] for i in RIGHT_ARC) / len(RIGHT_ARC)

        if front > OBSTACLE_THR:
            if leftv > rightv:
                lw, rw = +turn, -turn     # turn right in place
            else:
                lw, rw = -turn, +turn     # turn left in place
        elif leftv > OBSTACLE_THR:
            lw, rw = +turn, +0.2 * turn   # slight right
        elif rightv > OBSTACLE_THR:
            lw, rw = +0.2 * turn, +turn   # slight left
        else:
            lw, rw = base, base

        left.setVelocity(clamp(lw, -MAX_SPEED, +MAX_SPEED))
        right.setVelocity(clamp(rw, -MAX_SPEED, +MAX_SPEED))

if __name__ == "__main__":
    main()
