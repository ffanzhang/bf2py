import sys
data = [0]
ptr = 0

def handle_right():
    global data, ptr
    ptr += 1
    if ptr >= len(data):
        data.append(0)

def handle_left():
    global data, ptr
    ptr -= 1
    if ptr < 0:
        data.insert(0, 0)
        ptr = 0

def handle_pp():
    global data, ptr
    data[ptr] += 1

def handle_mm():
    global data, ptr
    data[ptr] -= 1

if __name__ == "__main__":
    handle_pp()
    while data[ptr] != 0:
        data[ptr] = ord(sys.stdin.read(1))
        sys.stdout.write(chr(data[ptr]))
        
