import time

def testCalSpeed():
    test_l = [i for i in range(1, 1000001)]
    time_start = time.perf_counter()
    Amount = 0
    for num in test_l:
        Amount += num
    time_end = time.perf_counter()
    print(f"Added 1,000,000 numbers within {time_end - time_start:0.4f} seconds")
    return Amount

if __name__ == "__main__":
    testCalSpeed()