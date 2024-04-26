import time
def print_slow(text,delay=0.03):
    for char in text:
        print(char,end='')
        time.sleep(delay)
    print()
print_slow('Tarun Mangalampalli')