import time

def CubicTime(n):
    start = time.time()
    for _ in range(n):
        for _ in range(n):
            for _ in range(n):
                pass
    end = time.time()
    print(f"Time taken for n = {n}: {end - start} seconds")

CubicTime(10)
CubicTime(100)
CubicTime(1000)

# OUTPUT

# Time taken for n = 10: 1.621246337890625e-05 seconds
# Time taken for n = 100: 0.004198789596557617 seconds
# Time taken for n = 1000: 7.888701438903809 seconds
