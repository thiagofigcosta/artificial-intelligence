#!/usr/bin/env python
import astar 

def go_to_bucharest():
    """ensure that we take the shortest path, and not the path with less elements.
       the path with less elements is A -> B with a distance of 100
       the shortest path is A -> C -> D -> B with a distance of 60
    """
    nodes = {
            'Arad': [('Sibiu', 140), ('Timisoara', 118), ('Zerind', 75)],
            'Bucharest': [('Pitesti', 101), ('Fagaras', 211), ('Giurgiu', 90), ('Urziceni', 85)],
            'Craiova': [('Dobreta', 120), ('Rimnicu Vikea', 146), ('Pitesti', 138)],
            'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
            'Eforie': [('Hirsowa', 85)],
            'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
            'Giurgiu': [('Bucharest', 90)],
            'Hirsowa': [('Urziceni', 98), ('Eforie', 85)],
            'Iasi': [('Neamt', 87), ('Vaslui', 92)],
            'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
            'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
            'Neamt': [('Iasi', 87)],
            'Oradea': [('Zerind', 71), ('Sibiu', 151)],
            'Pitesti': [('Rimnicu Vikea', 97), ('Craiova', 138), ('Bucharest', 101)],
            'Rimnicu Vikea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
            'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vikea', 80)],
            'Timisoara': [('Arad', 118), ('Lugoj', 111)],
            'Urziceni': [('Bucharest', 85), ('Hirsowa', 98), ('Vaslui', 142)],
            'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
            'Zerind': [('Arad', 75), ('Oradea', 71)]
            }

    def neighbors(n):
        for n1, d in nodes[n]:
            yield n1

    def distance(n1, n2):
        for n, d in nodes[n1]:
            if n == n2:
                return d

    def cost(n, goal): #always return 1 if have no heuristic
        dist_to_buch={
            'Arad': 366,
            'Bucharest': 0,
            'Craiova': 160,
            'Dobreta': 242,
            'Eforie': 161,
            'Fagaras': 176,
            'Giurgiu': 77,
            'Hirsowa': 151,
            'Iasi': 226,
            'Lugoj': 244,
            'Mehadia': 241,
            'Neamt': 234,
            'Oradea': 380,
            'Pitesti': 10,
            'Rimnicu Vikea': 193,
            'Sibiu': 253,
            'Timisoara': 329,
            'Urziceni': 80,
            'Vaslui': 199,
            'Zerind': 374
        }
        return dist_to_buch[n]

    path = list(astar.find_path('Lugoj', 'Bucharest', neighbors_fnct=neighbors,
                heuristic_cost_estimate_fnct=cost, distance_between_fnct=distance))
    for x in range(len(path)-1):
        print (path[x]+' -> ', end="")
    print (path[len(path)-1])

go_to_bucharest()
