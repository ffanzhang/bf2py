import sys

class BrainF___:
    _data = [0]
    _stack = []
    _nest_lvl_stack = []
    _ptr = 0
    _nest_lvl = 0
    _skip = False
    _method_lookup = { \
            '<' : 'self.mv_left()',
            '>' : 'self.mv_right()',
            '+' : 'self.pp()',
            '-' : 'self.mm()',
            '.' : 'self.write()',
            ',' : 'self.read()',
            '[' : 'self.whileloop()',
            ']' : 'self.endwhileloop()',
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

    def whileloop(self):
        self._nest_lvl += 1
        self._stack.append(self._file.tell() - 1)
        if not self._skip:
            self._nest_lvl_stack.append(self._nest_lvl)
            if self._data[self._ptr] == 0:
                self._skip = True

    def endwhileloop(self):
        if self._nest_lvl == self._nest_lvl_stack[-1]:
            self._nest_lvl_stack.pop(-1)
            if not self._skip:
                self._file.seek(self._stack[-1])
            self._skip = False
        self._stack.pop(-1)
        self._nest_lvl -= 1

    def __init__(self, f):
        self._file = f

    def run(self):
        for c in iter(lambda: self._file.read(1), ''):
            if self._skip and c in '<>+-,.': 
                continue

            if c in self._method_lookup:
                eval(self._method_lookup[c])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stdout.write("usage: python bf.py source\n")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r+") as f:
        BrainF__k = BrainF___(f)
        BrainF__k.run()
