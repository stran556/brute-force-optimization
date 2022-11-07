# brute-force-optimization

Experimenting with speedup optimization for brute-forcing a hashed number.

## sforce.py
Utilizes 100% serial processing to crack the value of a hash. Results for 1000000, 10000000, 100000000, and 1000000000: 

![](https://github.com/stran556/brute-force-optimization/blob/main/serial_results.png)

##pforce.py
Utilizes 6% serial and 94% parallel processing to crack the value of a hash. Results for the worst-case of previous numbers: 

![](https://github.com/stran556/brute-force-optimization/blob/main/parallel_results.png)

