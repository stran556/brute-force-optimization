# brute-force-optimization

Experimenting with speedup optimization for brute-forcing a hashed number.

## sforce.py
Utilizes 100% serial processing to crack the value of a hash. Results for 1000000, 10000000, 100000000, and 1000000000: 

![](https://github.com/stran556/brute-force-optimization/blob/main/serial_results.png)


## pforce.py
Utilizes 6% serial and 94% parallel processing to crack the value of a hash. Due to the nature of how parallel processing divides up the number space, using any hash value divisible by 10^x will be cracked instantly. Instead, the upperbound is represented by any number with 9 as its digits. Results for the worst-case of previous numbers 999999, 9999999, 99999999, 999999999: 

![](https://github.com/stran556/brute-force-optimization/blob/main/parallel_results.png)

