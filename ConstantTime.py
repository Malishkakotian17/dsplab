import time

# O(1)
def ConstantTime(n): 
    start = time.time()
    def inner():
        return 0
    end = time.time()
    print(f"Time taken for n = {n}: {end - start} seconds")

ConstantTime(1000)
ConstantTime(10000)
ConstantTime(100000)

# OUTPUT

# Time taken for n = 1000: 2.384185791015625e-07 seconds
# Time taken for n = 10000: 4.76837158203125e-07 seconds
# Time taken for n = 100000: 2.384185791015625e-07 seconds
