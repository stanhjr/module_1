def dfs(graph: dict, start: tuple, end: tuple, path=None, route_list = [] ):
    """depth-first search function"""
    if path is None:
        path = []
    path = path + [start]
    if start == end:  # If we come to the exit, we return the solution
        route_list.append(path)
    for node in graph[start]:
        if node not in path:
            dfs(graph, node, end, path)
    return route_list

