import time

i = int(input("Input Your Number Here "))
num = 1

time.sleep(1)
print("Calculating in 5 Seconds!")
print("Started!")
time.sleep(5)

while num < i:
    print(num)
    num = num + 1
    time.sleep(1)

print(i)
print("Done!")
