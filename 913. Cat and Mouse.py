

graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]

def find_mouse_best_move(current, points):
    # Find the best move for the mouse
    for i in graph[current]:
        if points[i] == 0:
            return i
        
    