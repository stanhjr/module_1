def search_path_maze(maze: list, start: tuple, end: tuple) -> list:
    """search exit from the maze
       index [0] - minimum number of moves to the exit
       index [1] - route to the exit"""

    def search_for_edges(x: int, y: int) -> list:
        """return list of indices of neighbors equal to zero"""

        list_edges = []

        if x < len(maze[x]) - 1 and y <= len(maze):
            if maze[x + 1][y] != 1:
                edges = (x + 1, y)
                list_edges.append(edges)

        if x <= len(maze[x]) and y < len(maze) - 1:
            if maze[x][y + 1] != 1:
                edges = (x, y + 1)
                list_edges.append(edges)

        if maze[x - 1][y] != 1 and x > 0:
            edges = (x - 1, y)
            list_edges.append(edges)

        if maze[x][y - 1] != 1 and y > 0:
            edges = (x, y - 1)
            list_edges.append(edges)

        return list_edges

    def dfs(graph: dict, start: tuple, end: tuple, path=None, route=[]):
        """depth-first search function"""
        if path is None:
            path = []
        path = path + [start]
        if start == end:  # If we come to the exit, we return the solution
            route.append(path)
        for node in graph[start]:
            if node not in path:
                dfs(graph, node, end, path)
        return route

    # graph adjacency list (type: dict)
    dict_vortex = {}
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] != 1:
                key = (x, y)
                dict_vortex[key] = search_for_edges(x, y)

    # list of exit paths
    route_list = dfs(dict_vortex, start, stop)



    min_answer = []

    for i in route_list:
        min_answer.append(len(i) - 1)
    if len(min_answer) == 0:
        return - 1
    answer = 'Minimum number of moves to the exit = ' + str(min(min_answer))

    return answer, route_list


# work check
maze = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 1, 0]
]

start = (0, 0)
stop = (2, 2)

an, route = search_path_maze(maze, start, stop)
print(search_path_maze(maze, start, stop))

print(an)
print(route)
