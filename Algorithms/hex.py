import math

lat = 12.9939455
lon = 77.66040169999997
r = 0.0012

if __name__ == "__main__":

    x = [0 for _ in range(6)]
    y = [0 for _ in range(6)]
    c = r * math.cos(math.radians(30)) - 0.00042
    s = r * math.sin(math.radians(60))

    x[0], y[0] = lat + r, lon
    x[1], y[1] = lat - c, lon + s
    x[2], y[2] = lat - c, lon - s
    x[3], y[3] = lat - r, lon
    x[4], y[4] = lat + c, lon - s
    x[5], y[5] = lat + c, lon + s

    for i in range(6):
        print(str(x[i]) + "," + str(y[i]) + ",a")
    print(str(lat) + "," + str(lon) + ",abc")
