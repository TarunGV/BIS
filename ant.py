import numpy as np
import random

class AntColonyTSP:
    def __init__(self, graph, n_ants, n_iterations, alpha, beta, evaporation_rate, pheromone_init, Q=1):
        self.graph = graph
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.Q = Q
        self.pheromone = np.ones_like(graph) * pheromone_init
        self.best_path = None
        self.best_path_length = float('inf')

    def _calculate_transition_probabilities(self, ant, visited):
        current_node = ant[-1]
        probabilities = []

        for j in range(len(self.graph)):
            if j not in visited:
                pheromone = self.pheromone[current_node][j] ** self.alpha
                distance = (1.0 / self.graph[current_node][j]) ** self.beta
                probabilities.append(pheromone * distance)
            else:
                probabilities.append(0)

        total_pheromone = sum(probabilities)
        if total_pheromone == 0:
            return [0 for _ in probabilities]

        probabilities = [p / total_pheromone for p in probabilities]
        return probabilities

    def _construct_path(self, start_node):
        visited = set([start_node])
        path = [start_node]
        total_distance = 0

        while len(path) < len(self.graph):
            current_node = path[-1]
            probabilities = self._calculate_transition_probabilities(path, visited)
            next_node = self._select_next_node(probabilities)
            visited.add(next_node)
            path.append(next_node)
            total_distance += self.graph[current_node][next_node]

        total_distance += self.graph[path[-1]][path[0]]
        path.append(path[0])
        return path, total_distance

    def _select_next_node(self, probabilities):
        return np.random.choice(len(probabilities), p=probabilities)

    def _update_pheromones(self, paths, path_lengths):
        self.pheromone *= (1 - self.evaporation_rate)

        for path, length in zip(paths, path_lengths):
            pheromone_deposit = self.Q / length
            for i in range(len(path) - 1):
                self.pheromone[path[i]][path[i + 1]] += pheromone_deposit
            self.pheromone[path[-1]][path[0]] += pheromone_deposit

    def run(self, start_node):
        for iteration in range(self.n_iterations):
            paths = []
            path_lengths = []
            for _ in range(self.n_ants):
                path, length = self._construct_path(start_node)
                paths.append(path)
                path_lengths.append(length)

                if length < self.best_path_length:
                    self.best_path_length = length
                    self.best_path = path

            self._update_pheromones(paths, path_lengths)

            print(f"Iteration {iteration + 1}: Best Path Length = {self.best_path_length}")

        return self.best_path, self.best_path_length


graph = np.array([
    [0, 2, 2, 5, 7],
    [2, 0, 4, 8, 2],
    [2, 4, 0, 1, 3],
    [5, 8, 1, 0, 6],
    [7, 2, 3, 6, 0]
])

n_ants = 10
n_iterations = 50
alpha = 1.0
beta = 2.0
evaporation_rate = 0.5
pheromone_init = 0.1

aco_tsp = AntColonyTSP(graph, n_ants, n_iterations, alpha, beta, evaporation_rate, pheromone_init)

best_path, best_path_length = aco_tsp.run(start_node=0)

print(f"Best Path: {best_path}")
print(f"Best Path Length: {best_path_length}")
     
Iteration 1: Best Path Length = 13
Iteration 2: Best Path Length = 13
Iteration 3: Best Path Length = 13
Iteration 4: Best Path Length = 13
Iteration 5: Best Path Length = 13
Iteration 6: Best Path Length = 13
Iteration 7: Best Path Length = 13
Iteration 8: Best Path Length = 13
Iteration 9: Best Path Length = 13
Iteration 10: Best Path Length = 13
Iteration 11: Best Path Length = 13
Iteration 12: Best Path Length = 13
Iteration 13: Best Path Length = 13
Iteration 14: Best Path Length = 13
Iteration 15: Best Path Length = 13
Iteration 16: Best Path Length = 13
Iteration 17: Best Path Length = 13
Iteration 18: Best Path Length = 13
Iteration 19: Best Path Length = 13
Iteration 20: Best Path Length = 13
Iteration 21: Best Path Length = 13
Iteration 22: Best Path Length = 13
Iteration 23: Best Path Length = 13
Iteration 24: Best Path Length = 13
Iteration 25: Best Path Length = 13
Iteration 26: Best Path Length = 13
Iteration 27: Best Path Length = 13
Iteration 28: Best Path Length = 13
Iteration 29: Best Path Length = 13
Iteration 30: Best Path Length = 13
Iteration 31: Best Path Length = 13
Iteration 32: Best Path Length = 13
Iteration 33: Best Path Length = 13
Iteration 34: Best Path Length = 13
Iteration 35: Best Path Length = 13
Iteration 36: Best Path Length = 13
Iteration 37: Best Path Length = 13
Iteration 38: Best Path Length = 13
Iteration 39: Best Path Length = 13
Iteration 40: Best Path Length = 13
Iteration 41: Best Path Length = 13
Iteration 42: Best Path Length = 13
Iteration 43: Best Path Length = 13
Iteration 44: Best Path Length = 13
Iteration 45: Best Path Length = 13
Iteration 46: Best Path Length = 13
Iteration 47: Best Path Length = 13
Iteration 48: Best Path Length = 13
Iteration 49: Best Path Length = 13
Iteration 50: Best Path Length = 13
Best Path: [0, 2, 3, 4, 1, 0]
Best Path Length: 13
