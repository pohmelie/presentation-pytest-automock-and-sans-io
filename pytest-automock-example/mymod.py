import time

def get_data_from_network(x, y):
    time.sleep(1)
    return x + y

def logic(x):
    a, b = 0, 1
    while b < x:
        c = get_data_from_network(a, b)
        a, b = b, c
    return b
