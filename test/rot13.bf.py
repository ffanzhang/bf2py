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
    handle_mm()
    data[ptr] = ord(sys.stdin.read(1))
    handle_pp()
    while data[ptr] != 0:
        handle_mm()
        while data[ptr] != 0:
            handle_right()
            handle_right()
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
                handle_pp()
                handle_pp()
                handle_pp()
                handle_pp()
                handle_left()
                handle_mm()
                
            handle_left()
            handle_pp()
            handle_left()
            handle_mm()
            while data[ptr] != 0:
                handle_right()
                handle_pp()
                handle_right()
                handle_pp()
                handle_right()
                handle_mm()
                while data[ptr] != 0:
                    handle_right()
                    handle_right()
                    handle_right()
                    
                handle_left()
                while data[ptr] != 0:
                    while data[ptr] != 0:
                        handle_right()
                        handle_pp()
                        handle_left()
                        handle_mm()
                        
                    handle_right()
                    handle_right()
                    handle_pp()
                    handle_right()
                    
                handle_left()
                handle_left()
                handle_left()
                handle_left()
                handle_left()
                handle_mm()
                
            
        handle_right()
        handle_right()
        handle_right()
        while data[ptr] != 0:
            handle_mm()
            
        handle_pp()
        handle_right()
        handle_mm()
        handle_mm()
        while data[ptr] != 0:
            handle_mm()
            while data[ptr] != 0:
                handle_left()
                handle_mm()
                handle_right()
                handle_pp()
                handle_pp()
                handle_pp()
                while data[ptr] != 0:
                    handle_mm()
                    
                
            
        handle_left()
        while data[ptr] != 0:
            handle_pp()
            handle_pp()
            handle_pp()
            handle_pp()
            handle_pp()
            handle_pp()
            handle_pp()
            handle_pp()
            handle_pp()
            handle_pp()
            handle_pp()
            handle_pp()
            handle_left()
            while data[ptr] != 0:
                handle_right()
                handle_mm()
                while data[ptr] != 0:
                    handle_right()
                    handle_pp()
                    handle_right()
                    handle_right()
                    
                handle_right()
                while data[ptr] != 0:
                    handle_pp()
                    while data[ptr] != 0:
                        handle_left()
                        handle_pp()
                        handle_right()
                        handle_mm()
                        
                    handle_right()
                    handle_pp()
                    handle_right()
                    handle_right()
                    
                handle_left()
                handle_left()
                handle_left()
                handle_left()
                handle_left()
                handle_mm()
                
            handle_right()
            handle_right()
            while data[ptr] != 0:
                handle_left()
                handle_pp()
                handle_right()
                handle_mm()
                
            handle_right()
            while data[ptr] != 0:
                handle_mm()
                while data[ptr] != 0:
                    handle_mm()
                    handle_left()
                    handle_left()
                    while data[ptr] != 0:
                        handle_mm()
                        
                    handle_right()
                    handle_right()
                    
                handle_left()
                handle_left()
                while data[ptr] != 0:
                    handle_left()
                    handle_left()
                    handle_mm()
                    handle_right()
                    handle_right()
                    handle_mm()
                    
                handle_right()
                handle_right()
                
            handle_left()
            handle_left()
            while data[ptr] != 0:
                handle_left()
                handle_left()
                handle_pp()
                handle_right()
                handle_right()
                handle_mm()
                
            
        handle_left()
        while data[ptr] != 0:
            handle_mm()
            
        handle_left()
        sys.stdout.write(chr(data[ptr]))
        while data[ptr] != 0:
            handle_mm()
            
        handle_left()
        handle_mm()
        data[ptr] = ord(sys.stdin.read(1))
        handle_pp()
        
