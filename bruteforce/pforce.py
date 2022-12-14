import hashlib
import time
import multiprocessing
import math
import sys


class Process(multiprocessing.Process):
    def __init__(self, id):
        super(Process, self).__init__()
        self.id = id

    def run(self):
        time.sleep(1)
        print("Process ID: {}".format(self.id))


num_hash = input("Hash: ")
digit = int(input("Number of digits to check: "))
digit_pow = 10 ** (digit)
interval = 0

# Determines whether all processes end
done = False


def func(x):
    upper = x + digit_pow / 10
    global done
    while x <= upper and not done:
        if hashlib.sha256(str.encode(str(x))).hexdigest() == num_hash:
            done = True
            return x
        x = x + 1
    return 0


if __name__ == '__main__':
    start = time.time()
    pool = multiprocessing.Pool()
    pool = multiprocessing.Pool(10)

    inputs = []
    for i in range(10):
        inputs.append(interval)
        interval = interval + int(digit_pow / 10)
    outputs = []

    val = None
    print("\nProcessing... ", end='')
    for result in pool.map(func, inputs):
        outputs.append(result)
        if result != 0:
            val = result

    end = time.time()
    net = round(end - start, 2)

    if val is None:
        print("Number wasn't found in range. ")
    else:
        print("Complete.", end='')
        time.sleep(1)
        print("\n\nHash value cracked in " + str(net) + " seconds: " + "'" + str(val) + "'" + "\nHash/sec" " = " + str(
            f'{math.trunc(int(val) / (end - start)):,}'))
