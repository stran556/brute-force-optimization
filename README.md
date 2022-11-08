# brute-force-optimization

Experimenting with speedup optimization for brute-forcing a hashed number.

## sforce.py
Utilizes 100% serial processing to crack the value of a hash. Results for 1000000, 10000000, 100000000, and 1000000000: 

![](https://github.com/stran556/brute-force-optimization/blob/main/serial_results.png)


## pforce.py
Utilizes *6% serial and 94% parallel processing*** to crack the value of a hash. Due to the nature of how parallel processing divides up the number space, using any hash value divisible by 10<sup>number of digits</sup> will be cracked instantly. Instead, the upperbound is represented by any number with 9 as its digits. 

Results for the worst-case of previous numbers 999999, 9999999, 99999999, 999999999: 

![](https://github.com/stran556/brute-force-optimization/blob/main/parallel_results.png)

** The speedup from using a single processor to using 10 processors is approximately x6.5, calculated from dividing the time needed to crack a hash with serial processing by the time to crack a hash with parallel processing. Ex: Nine-digit number 999,999,999 will be cracked with s-proc in 580 seconds and will be cracked with p-proc in 89 seconds -> 580/89 = 6.517

Using Amdahl's law- a formula that calculates the theoretical speedup of executing a task with improved resources, the percentage of the system operating in parallel (P) can be calculated using the known values Speedup = 6.5 and N(# parallel processors) = 10. P = 0.94, implying S(1-P) = 0.6.
