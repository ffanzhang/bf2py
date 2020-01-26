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
    handle_pp()
    handle_pp()
    handle_pp()
    handle_pp()
    handle_pp()
    handle_pp()
    handle_pp()
    while data[ptr] != 0:
        handle_right()
        handle_pp()
        handle_pp()
        handle_pp()
        handle_pp()
        while data[ptr] != 0:
            handle_right()
            handle_pp()
            handle_pp()
            handle_right()
            handle_pp()
            handle_pp()
            handle_pp()
            handle_right()
            handle_pp()
            handle_pp()
            handle_pp()
            handle_right()
            handle_pp()
            handle_left()
            handle_left()
            handle_left()
            handle_left()
            handle_mm()
            
        handle_right()
        handle_pp()
        handle_right()
        handle_pp()
        handle_right()
        handle_mm()
        handle_right()
        handle_right()
        handle_pp()
        while data[ptr] != 0:
            handle_left()
            
        handle_left()
        handle_mm()
        
    handle_right()
    handle_right()
    sys.stdout.write(chr(data[ptr]))
    handle_right()
    handle_mm()
    handle_mm()
    handle_mm()
    sys.stdout.write(chr(data[ptr]))
    handle_pp()
    handle_pp()
    handle_pp()
    handle_pp()
    handle_pp()
    handle_pp()
    handle_pp()
    sys.stdout.write(chr(data[ptr]))
    sys.stdout.write(chr(data[ptr]))
    handle_pp()
    handle_pp()
    handle_pp()
    sys.stdout.write(chr(data[ptr]))
    handle_right()
    handle_right()
    sys.stdout.write(chr(data[ptr]))
    handle_left()
    handle_mm()
    sys.stdout.write(chr(data[ptr]))
    handle_left()
    sys.stdout.write(chr(data[ptr]))
    handle_pp()
    handle_pp()
    handle_pp()
    sys.stdout.write(chr(data[ptr]))
    handle_mm()
    handle_mm()
    handle_mm()
    handle_mm()
    handle_mm()
    handle_mm()
    sys.stdout.write(chr(data[ptr]))
    handle_mm()
    handle_mm()
    handle_mm()
    handle_mm()
    handle_mm()
    handle_mm()
    handle_mm()
    handle_mm()
    sys.stdout.write(chr(data[ptr]))
    handle_right()
    handle_right()
    handle_pp()
    sys.stdout.write(chr(data[ptr]))
    handle_right()
    handle_pp()
    handle_pp()
    sys.stdout.write(chr(data[ptr]))
