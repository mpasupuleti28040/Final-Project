# Optimized implementation

import random
import time
from collections import Counter

# Generate a large list of random integers
data = [random.randint(0, 1000) for _ in range(1000000)]

def count_frequencies_optimized(data):
    return Counter(data)

# Measure execution time
start_time = time.time()
freq_optimized = count_frequencies_optimized(data)
end_time = time.time()
print(f"Optimized Implementation Time: {end_time - start_time:.4f} seconds")