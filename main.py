import time


def timer(x, y, z):
    x = x * 60
    y = y + x
    y = y * 60
    z = z + y

    for i in range(1, z+1):
        print(z, "seconds left")
        z = z - 1
        time.sleep(1)


jk = int(input("Hours"))
yu = int(input("Minutes"))
zm = int(input("Seconds"))

timer(jk, yu, zm)
