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



def func(x):
    upper = x + digit_pow / 10
    while x <= upper:
        str_c = str(x)
        if hashlib.sha256(str.encode(str_c)).hexdigest() == num_hash:
            end = time.time()
            net = round(end - start, 2)
            print("\nHash value cracked: " + str(x) + " in " + str(net) + " seconds" + "\nHash/sec" " = " + str(f'{math.trunc(int(x) / (end - start)):,}'))

            print("No need to wait for the program to finish. Just terminate with ctrl + c.")
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

    for result in pool.map(func, inputs):
        outputs.append(result)
        if result != 0:
            print(result)

    print("Input: {}".format(inputs))
    print("Output: {}".format(outputs))
