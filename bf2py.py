import sys
import textwrap

defs = textwrap.dedent("""\
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
""")

handler_lookup = { \
        '<' : 'handle_left()\n',
        '>' : 'handle_right()\n',
        '+' : 'handle_pp()\n',
        '-' : 'handle_mm()\n',
        '[' : 'while data[ptr] != 0:\n',
        ']' : '\n',
        '.' : "sys.stdout.write(chr(data[ptr]))\n",
        ',' : "data[ptr] = ord(sys.stdin.read(1))\n",
}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stdout.write("usage: python bf2py.py source\n")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r+") as f:
        indentation_lvl = 1 
        tab = '    '
        with open(path + ".py", "w+") as w:
            w.write(defs)
            for line in f:
                for c in line:
                    if c in handler_lookup:
                        w.write(tab * indentation_lvl + handler_lookup[c])
                        if c == '[':
                            indentation_lvl += 1
                        elif c == ']':
                            indentation_lvl -= 1
