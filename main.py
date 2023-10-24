import time
import psutil


def testCalSpeed():
    test_l = [i for i in range(1, 100000001)]
    time_start = time.perf_counter()
    
    Amount = 0
    
    for num in test_l:
        Amount += num
    time_end = time.perf_counter()
    
    print(f"Added 100,000,000 numbers within {time_end - time_start:0.4f} seconds")
    print("CPU Usage: {:.2}%".format(psutil.cpu_percent(interval=time_end - time_start)))
    return Amount

if __name__ == "__main__":
    testCalSpeed()