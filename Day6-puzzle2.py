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

print(get(46689866, 358105418071080))