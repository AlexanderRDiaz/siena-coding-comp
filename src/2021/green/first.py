def getForce(mass: int, acceleration: int) -> int:
    return mass * acceleration


if __name__ == '__main__':
    mass, acceleration = int(input()), int(input())
    print(getForce(mass, acceleration))
