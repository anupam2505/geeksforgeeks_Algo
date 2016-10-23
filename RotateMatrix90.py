__Author__ = "Anupam Panwar"

__Date__ = 10 / 21 / 16

original = [[1, 2, 3,4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
            ]

rotated = zip(*original[::-1])
print rotated

