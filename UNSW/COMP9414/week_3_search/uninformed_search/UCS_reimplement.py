"""
Project Name: UNSW
Module Description: Reimplement UCS
Author: lixin
Date: 2024-07-13
Version: 1.0.0
Email: 395095201@qq.com, zangaixiaoxinxin@gmail.com

Description:
    None.

Usage:
    None.

Examples:
    If applicable, include a simple usage example.

Todo:
    - 

@file: daily-coding/UNSW/COMP9414/week_3_search/uninformed_search/UCS_reimplement.py
@software: Visual Studio Code
"""
import heapq


def ucs(graph, start, goal):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node not in visited:
            visited.add(node)
            path = path + [node]

            if node == goal:
                return cost, path
            
            for next_node, edge_cost in graph[node]:
                if next_node not in visited:
                    total_cost = cost + edge_cost
                    heapq.heappush(queue, (total_cost, next_node, path))

    return None


graph = {
    'A':[('B', 1), ('C', 4)],
    'B':[('C', 2), ('D', 5)],
    'C':[('D', 1)],
    'D':[],
}


start_node = 'A'
goal_node = 'D'
result = ucs(graph, start_node, goal_node)

if result:
    cost, path = result

    print(f"{start_node}->{goal_node}: {'->'.join(path)}, cost {cost}")
else:
    print(f"no path")