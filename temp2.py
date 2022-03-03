import string
import random

width = 15
height = 15

upper = [x for x in string.ascii_uppercase]


class Grid:
    def __init__(self, words, size=15):
        self.words = words
        self.size = size
        self.mat = [random.choice(upper) for i in range(self.size) for j in range(self.size)]
        self.solved = ["" for i in range(self.size) for j in range(self.size)]

        random.shuffle(self.words)

    def put_word(self, word):
        n = len(word)
        mode = 0
        if mode == 0:
            pos = 4
            if pos % self.size > n - 1 and list(set(self.solved[pos:pos + n])) == [""]:
                self.mat[pos:pos + n] = word

    def print_mat(self):
        cnt = 0
        for i in range(self.size):
            for j in range(self.size):
                print(self.mat[cnt], end=" ")
                cnt += 1
            print("")


words = ["wear", "variable", "print", "minimum", "graduate", "room", "bulk", "advise", "completed", "memory",
         "hello",
         "what", "who", "basket", "tomorrow", "yester", "today", "teacher", "student", "india", "uniteds",
         "france"]
grid = Grid(["cat", "bat"], 5)
grid.put_word("hello")
grid.print_mat()
