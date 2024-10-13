# Naive Implementation

import random
import time

# Generate a large list of random integers
data = [random.randint(0, 1000) for _ in range(1000000)]

def count_frequencies_naive(data):
    frequencies = {}
    for item in data:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies

# Measure execution time
start_time = time.time()
freq_naive = count_frequencies_naive(data)
end_time = time.time()
print(f"Naive Implementation Time: {end_time - start_time:.4f} seconds")
