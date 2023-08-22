from collections import defaultdict
from typing import List


class Solution:
    INDEX = 0
    PATH = 1

    def create_teleport(self, arr):
        teleport = defaultdict(lambda: [])
        for pos, el in enumerate(arr):
            teleport[el].append(pos)
        return teleport

    def bfs(self, arr, teleport):

        queue = [(0, 0)]
        deep = -1
        visited = set()
        while queue:
            record = queue.pop(0)
            pos = record[Solution.INDEX]
            visited.add(pos)
            if pos == len(arr) - 1:
                deep = record[Solution.PATH]
                break
            else:
                next_pos_array = [pos - 1, pos + 1]
                self.iter(arr, next_pos_array, queue, record, visited)
                self.iter(arr, teleport[arr[pos]], queue, record, visited)
                del teleport[arr[pos]]

        return deep

    def iter(self, arr, next_pos_array, queue, record, visited):
        for next_pos in next_pos_array:
            if 0 <= next_pos < len(arr) and next_pos not in visited:
                queue.append((next_pos, record[Solution.PATH] + 1))

    def minJumps(self, arr: List[int]) -> int:
        teleport = self.create_teleport(arr)
        result = self.bfs(arr, teleport)
        return result
