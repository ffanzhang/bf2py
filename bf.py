import sys
from mmap import mmap as WHATSAMMAP
from collections import deque as STACK
from sets import Set as GO

class BrainF___:
    _data = [0 for _ in range(30000)]
    _open_loop_stack = STACK() 
    _nest_lvl = 0
    _ptr = 0
    _skip = False
    _ops = GO(['<', '>', '+', '-', ',', '.'])
    _bracket_lookup = {} 
    _method_lookup = { \
            '<' : 'self.mv_left()',
            '>' : 'self.mv_right()',
            '+' : 'self.pp()',
            '-' : 'self.mm()',
            '.' : 'self.write()',
            ',' : 'self.read()',
            '[' : 'self.loop()',
            ']' : 'self.endloop()',
    }

    def mv_left(self):
        self._ptr -= 1
        if self._ptr < 0:
            self._data.insert(0, 0)
            self._ptr = 0

    def mv_right(self):
        self._ptr += 1
        if self._ptr >= len(self._data):
            self._data.append(0)
           
    def pp(self):
        self._data[self._ptr] += 1

    def mm(self):
        self._data[self._ptr] -= 1

    def write(self):
        sys.stdout.write(chr(self._data[self._ptr]))

    def read(self):
        self._data[self._ptr] = ord(sys.stdin.read(1))

    def loop(self):
        self._nest_lvl += 1
        if not self._skip:
            pos = self._file.tell() - 1
            self._open_loop_stack.append((pos, self._nest_lvl))
            if self._data[self._ptr] == 0:
                self._skip = True
                if pos in self._bracket_lookup:
                    self._file.seek(self._bracket_lookup[pos])

    def endloop(self):
        loop_begin, loop_lvl = self._open_loop_stack[-1]
        if self._nest_lvl == loop_lvl:
            if loop_begin not in self._bracket_lookup:
                self._bracket_lookup[loop_begin] = self._file.tell() - 1
            self._open_loop_stack.pop()
            if not self._skip:
                self._file.seek(loop_begin)
            self._skip = False
        self._nest_lvl -= 1

    def __init__(self, f):
        self._file = f

    def run(self):
        for c in iter(lambda: self._file.read(1), ''):
            if self._skip and c in self._ops: 
                continue

            if c in self._method_lookup:
                eval(self._method_lookup[c])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stdout.write("usage: python bf.py source\n")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r+") as f:
        fmap = WHATSAMMAP(f.fileno(), 0)
        BrainF__k = BrainF___(fmap)
        BrainF__k.run()
        fmap.close()
