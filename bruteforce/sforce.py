import hashlib
import time
import math

# single thread
num = "99999999"
num_hash = hashlib.sha256(str.encode(num)).hexdigest()
print("Hash = " + num_hash)

counter = 0
start = time.time()
while True:
    str_c = str(counter)
    if hashlib.sha256(str.encode(str_c)).hexdigest() == num_hash:
        break
    counter = counter + 1;
end = time.time()

net = round(end - start, 2)
print("Hash value = " + str(f'{counter:,}'))
print("Time = " + str(net) + " sec \nHash/sec = " + str(f'{math.trunc(int(num) / (end - start)):,}'))

# multi thread
