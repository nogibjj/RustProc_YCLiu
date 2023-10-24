import time
import psutil


def testCalSpeed():
    test_l = [i for i in range(1, 100000001)]
    time_start = time.perf_counter()
    
    Amount = 0
    
    for num in test_l:
        Amount += num
    time_end = time.perf_counter()
    time_dif = time_end - time_start
    print(f"Added 100,000,000 numbers within {time_dif} s")
    print("CPU Usage: {:.2}%".format(psutil.cpu_percent(interval=time_dif)))
    return Amount

if __name__ == "__main__":
    testCalSpeed()