maze = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 1, 0]
]


def maze_upd(maze_in):
    """Создаем края для лабиринта"""
    list1 = [i * 0 + 1 for i in range(len(maze) + 2)]
    mazeupd = []
    mazeupd.append(list1)
    for i in range(len(maze)):
        mazeupd.append([1] + maze[i] + [1])
    mazeupd.append(list1)
    return mazeupd


maze = maze_upd(maze)

# Создаем пустую матрицу
mazepath = []
for i in range(len(maze)):
    mazepath.append([])
    for j in range(len(maze[i])):
        mazepath[-1].append(0)

# задаем точки старта
start = 1, 1
end = 3, 3
x, y = end
i, j = start
mazepath[i][j] = 1

k = 1
while k < len(mazepath) * len(mazepath[i]):
    for i in range(len(mazepath)):
        for j in range(len(mazepath[i])):
            if mazepath[i][j] == k:
                if i > 0 and mazepath[i - 1][j] == 0 and maze[i - 1][j] == 0:
                    mazepath[i - 1][j] = k + 1
                if j > 0 and mazepath[i][j - 1] == 0 and maze[i][j - 1] == 0:
                    mazepath[i][j - 1] = k + 1
                if i < len(mazepath) - 1 and mazepath[i + 1][j] == 0 and maze[i + 1][j] == 0:
                    mazepath[i + 1][j] = k + 1
                if j < len(mazepath[i]) - 1 and mazepath[i][j + 1] == 0 and maze[i][j + 1] == 0:
                    mazepath[i][j + 1] = k + 1
    k += 1
    answer = mazepath[x][y] - 1



print('Minimum number of moves to the exit = ', answer)
