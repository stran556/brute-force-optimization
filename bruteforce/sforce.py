import hashlib
import time
import math

# single thread
num_hash = input("Hash: ")
digit = int(input("Number of digits to check: "))
digit_pow = 10 ** (digit)

counter = 0
val = 0
start = time.time()
while counter <= digit_pow:
    str_c = str(counter)
    if hashlib.sha256(str.encode(str_c)).hexdigest() == num_hash:
        val = counter
        break
    counter = counter + 1;
end = time.time()

net = round(end - start, 2)
print("Hash value = " + str(f'{counter:,}'))
print("Time = " + str(net) + " sec \nHash/sec = " + str(f'{math.trunc(int(val) / (end - start)):,}'))
