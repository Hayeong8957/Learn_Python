from queue import Queue
import random

def radix_sort(a) :
    queues = []
    for i in range(BUCKETS) :
        queues.append(Queue())

    n = len(a)
    factor = 1
    for d in range(DIGITS) :
        for i in range(n) :
            queues[(a[i] // factor) % 10].put(a[i])

        i = 0
        for b in range(BUCKETS) :
            while not queues[b].empty() :
                a[i] = queues[b].get()
                i += 1
        factor *= 10
        print("step", d+1, a)

BUCKETS = 10
DIGITS = 4
data = []
for i in range(10) :
    data.append(random.randint(1, 9999))
radix_sort(data)
print("Radix: ", data)