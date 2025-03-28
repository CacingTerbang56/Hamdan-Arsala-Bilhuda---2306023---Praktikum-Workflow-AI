# -*- coding: utf-8 -*-
"""A_Star.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mIbix0q_9Rs6g_USHQeqIhplYQNUYmd0
"""

from os import path
from queue import PriorityQueue

def a_star_tree_search(graph, heuristic, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    path = {}

    while not frontier.empty():
        _, current = frontier.get()
        if current == goal:
            print('goal node found')
            route = reconstruct_path(path, start, goal)
            print('route optimal', route)
            return True

        if current in graph:
            for neighbor, cost in graph[current].items():
                new_cost = heuristic[neighbor] + cost
                frontier.put((new_cost, neighbor))
                path[neighbor] = current

    print('goal node not found')
    return False

def a_star_graph_search(graph, heuristic, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    explored = set()
    path = {}
    while not frontier.empty():
        _, current = frontier.get()

        if current == goal:
            print('goal node found')
            route = reconstruct_path(path, start, goal)
            print('route optimal', route)
            return True
        explored.add(current)

        if current in graph:
            for neighbor, cost in graph[current].items():
                if neighbor not in explored:
                    total_cost = heuristic[neighbor] + cost
                    frontier.put((total_cost, neighbor))
                    path[neighbor] = current
    print('goal node not found')
    return False

def reconstruct_path(path, start, goal):
    route = [goal]
    current = goal
    while current != start:
        current = path[current]
        route.append(current)
    route.reverse()
    return route

heuristic = {
        'A': 4,
        'B': 3,
        'C': 3,
        'D': 1,
        'S': 6,
        'G': 0
    }

graph = {
    'S': {'A': 3, 'B': 2},
    'A': {'B': 1, 'D': 5},
    'B': {'C': 2, 'D': 3},
    'C': {'D': 3, 'G': 4},
    'D': {'G': 1},
}
start_node = 'S'
goal_node = 'G'
a_star_tree_search(graph, heuristic, start_node, goal_node)
a_star_graph_search(graph, heuristic, start_node, goal_node)