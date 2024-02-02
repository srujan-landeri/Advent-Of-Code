time = list(map(int, "7  15   30".split()))
distance = list(map(int, "9  40  200".split()))


def get(time, distance):
    ways = 0
    for i in range(time + 1):
        speed = i
        remaing_time = time - i
        distanceCovered = speed * remaing_time
        if distanceCovered > distance:
            ways += 1
    return ways
ways = 1

for i in range(len(time)):
    ways *= (get(time[i], distance[i]))

print(ways)