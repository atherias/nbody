# Taken from:
# The Computer Language Benchmarks Game
# https://salsa.debian.org/benchmarksgame-team/benchmarksgame/
#
# originally by Kevin Carson
# modified by Tupteq, Fredrik Johansson, and Daniel Nanz
# modified by Maciej Fijalkowski
# 2to3
# modified by Andriy Misyura
# slightly modified by bmmeijers
# modified by Adele Therias

import sys
import time
from math import sqrt, pi as PI

#create a list of all possible combinations of items from a list
def combinations(l):
    result = []
    for x in range(len(l) - 1):
        ls = l[x + 1 :]
        for y in ls:
            result.append((l[x][0], l[x][1], l[x][2], y[0], y[1], y[2]))
    return result


SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

'''Dictionary of key-value pairs
key = name of body
value = tuple that includes:
    (1) list - starting coordinates (x, y, z)
    (2) list - velocity in each direction (x, y, z)
    (3) float - mass of the body as a function of solar mass'''

BODIES = {
    "sun": ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS),
    "jupiter": (
        [4.84143144246472090e00, -1.16032004402742839e00, -1.03622044471123109e-01],
        [
            1.66007664274403694e-03 * DAYS_PER_YEAR,
            7.69901118419740425e-03 * DAYS_PER_YEAR,
            -6.90460016972063023e-05 * DAYS_PER_YEAR,
        ],
        9.54791938424326609e-04 * SOLAR_MASS,
    ),
    "saturn": (
        [8.34336671824457987e00, 4.12479856412430479e00, -4.03523417114321381e-01],
        [
            -2.76742510726862411e-03 * DAYS_PER_YEAR,
            4.99852801234917238e-03 * DAYS_PER_YEAR,
            2.30417297573763929e-05 * DAYS_PER_YEAR,
        ],
        2.85885980666130812e-04 * SOLAR_MASS,
    ),
    "uranus": (
        [1.28943695621391310e01, -1.51111514016986312e01, -2.23307578892655734e-01],
        [
            2.96460137564761618e-03 * DAYS_PER_YEAR,
            2.37847173959480950e-03 * DAYS_PER_YEAR,
            -2.96589568540237556e-05 * DAYS_PER_YEAR,
        ],
        4.36624404335156298e-05 * SOLAR_MASS,
    ),
    "neptune": (
        [1.53796971148509165e01, -2.59193146099879641e01, 1.79258772950371181e-01],
        [
            2.68067772490389322e-03 * DAYS_PER_YEAR,
            1.62824170038242295e-03 * DAYS_PER_YEAR,
            -9.51592254519715870e-05 * DAYS_PER_YEAR,
        ],
        5.15138902046611451e-05 * SOLAR_MASS,
    ),
}

#create tuple that includes all values for each body (coordinates, velocity in each direction, mass)
SYSTEM = tuple(BODIES.values())

#create tuple of lists that each contains one possible combination of two bodies
PAIRS = tuple(combinations(SYSTEM))


def advance(dt, n, bodies=SYSTEM, pairs=PAIRS):

    # iterate over each step in number of iterations (e.g. 1-5000)
    for i in range(n):
        #iterate over values for each pair of bodies (e.g. saturn and uranus, saturn and jupiter etc)
        for ([x1, y1, z1], v1, m1, [x2, y2, z2], v2, m2) in pairs:

            #calculate distance between bodies in pair
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            dist = sqrt(dx * dx + dy * dy + dz * dz)

            #update velocities in each direction for each body in pair
            mag = dt / (dist * dist * dist)
            b1m = m1 * mag
            b2m = m2 * mag
            v1[0] -= dx * b2m
            v1[1] -= dy * b2m
            v1[2] -= dz * b2m
            v2[2] += dz * b1m
            v2[1] += dy * b1m
            v2[0] += dx * b1m

        # iterate over bodies and update positions based on velocities
        for (r, [vx, vy, vz], m) in bodies:
            r[0] += dt * vx
            r[1] += dt * vy
            r[2] += dt * vz

        #write resulting coordinates to csv file

        def body_name(BODIES, m):
            for body, mass in iter(dict.items(BODIES)):
                if m == mass[2]:
                    return body

        # for (r, [vx, vy, vz], m) in bodies:
        #     fh.write('{0};{1};{2};{3}\n'.format(body_name(BODIES,m),r[0],r[1],r[2]))


def report_energy(bodies=SYSTEM, pairs=PAIRS, e=0.0):
    #iterate over each pair of bodies (e.g. saturn and uranus, saturn and jupiter etc)
    for ((x1, y1, z1), v1, m1, (x2, y2, z2), v2, m2) in pairs:
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        #determine energy / force(?) based on distance of bodies from each other
        e -= (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5)

    #iterate over all bodies and modify energy / force(?) based on all velocities
    for (r, [vx, vy, vz], m) in bodies:
        e += m * (vx * vx + vy * vy + vz * vz) / 2.0
    print("Energy: %.9f" % e)


def offset_momentum(ref, bodies=SYSTEM, px=0.0, py=0.0, pz=0.0):
    #iterate over all bodies, calculate momentum offset based on velocity in each direction and mass, update velocity values
    for (r, [vx, vy, vz], m) in bodies:
        px -= vx * m
        py -= vy * m
        pz -= vz * m

    #set values for body as new ref
    (r, v, m) = ref
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m


def main(n, ref="sun"):
    offset_momentum(BODIES[ref])
    report_energy()
    advance(0.01, n)
    report_energy()

if __name__ == "__main__":
    start_time = time.time()
    if len(sys.argv) >= 2:
        # fh = open("nbody.csv","w")
        # fh.write("body; x; y; z\n")
        # fh.close()
        # fh = open("nbody.csv", "a")
        main(int(sys.argv[1]))
        print("Run time is %s seconds" % (time.time() - start_time))
        sys.exit(0)
    else:
        print(f"This is {sys.argv[0]}")
        print("Call this program with an integer as program argument")
        print("(to set the number of iterations for the n-body simulation).")
        sys.exit(1)
