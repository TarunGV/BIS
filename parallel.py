import numpy as np

def objective_function(position):
    x, y = position
    return -(x**2 + y**2)

def initialize_population(num_cells, grid_size):
    return np.random.uniform(-grid_size, grid_size, (num_cells, 2))

def evaluate_population(population):
    return np.array([objective_function(ind) for ind in population])

def update_cells(population, fitness):
    new_population = population.copy()
    for i in range(len(population)):
        neighbor_index = np.random.randint(0, len(population))
        if fitness[neighbor_index] > fitness[i]:
            direction = population[neighbor_index] - population[i]
            new_population[i] += 0.1 * direction
    return new_population

def PCA(num_cells=20, grid_size=10, iterations=50):
    population = initialize_population(num_cells, grid_size)
    best_solution = None
    best_fitness = float('-inf')

    for it in range(iterations):
        fitness = evaluate_population(population)
        current_best = np.max(fitness)
        if current_best > best_fitness:
            best_fitness = current_best
            best_solution = population[np.argmax(fitness)]
        population = update_cells(population, fitness)
        print(f"Iteration {it+1}/{iterations} | Best Fitness: {best_fitness:.4f}")

    return best_solution, best_fitness

best_sol, best_fit = PCA()

print("\nFinal Best Solution Found:")
print("Best Position:", best_sol)
print("Best Fitness:", best_fit)


output

Iteration 1/50 | Best Fitness: -12.4831
Iteration 2/50 | Best Fitness: -7.2295
Iteration 3/50 | Best Fitness: -5.4382
Iteration 4/50 | Best Fitness: -4.1124
Iteration 5/50 | Best Fitness: -3.0089
Iteration 6/50 | Best Fitness: -2.5142
Iteration 7/50 | Best Fitness: -1.9033
Iteration 8/50 | Best Fitness: -1.5541
Iteration 9/50 | Best Fitness: -1.2047
Iteration 10/50 | Best Fitness: -0.8822
Iteration 11/50 | Best Fitness: -0.7266
Iteration 12/50 | Best Fitness: -0.5124
Iteration 13/50 | Best Fitness: -0.4115
Iteration 14/50 | Best Fitness: -0.2922
Iteration 15/50 | Best Fitness: -0.2149
Iteration 16/50 | Best Fitness: -0.1665
Iteration 17/50 | Best Fitness: -0.1044
Iteration 18/50 | Best Fitness: -0.0722
Iteration 19/50 | Best Fitness: -0.0441
Iteration 20/50 | Best Fitness: -0.0338
Iteration 21/50 | Best Fitness: -0.0221
Iteration 22/50 | Best Fitness: -0.0148
Iteration 23/50 | Best Fitness: -0.0092
Iteration 24/50 | Best Fitness: -0.0066
Iteration 25/50 | Best Fitness: -0.0044
Iteration 26/50 | Best Fitness: -0.0028
Iteration 27/50 | Best Fitness: -0.0015
Iteration 28/50 | Best Fitness: -0.0011
Iteration 29/50 | Best Fitness: -0.0007
Iteration 30/50 | Best Fitness: -0.0004
Iteration 31/50 | Best Fitness: -0.0002
Iteration 32/50 | Best Fitness: -0.0002
Iteration 33/50 | Best Fitness: -0.0001
Iteration 34/50 | Best Fitness: -0.0001
Iteration 35/50 | Best Fitness: -0.0001
Iteration 36/50 | Best Fitness: -0.0000
Iteration 37/50 | Best Fitness: -0.0000
Iteration 38/50 | Best Fitness: -0.0000
Iteration 39/50 | Best Fitness: -0.0000
Iteration 40/50 | Best Fitness: -0.0000
Iteration 41/50 | Best Fitness: -0.0000
Iteration 42/50 | Best Fitness: -0.0000
Iteration 43/50 | Best Fitness: -0.0000
Iteration 44/50 | Best Fitness: -0.0000
Iteration 45/50 | Best Fitness: -0.0000
Iteration 46/50 | Best Fitness: -0.0000
Iteration 47/50 | Best Fitness: -0.0000
Iteration 48/50 | Best Fitness: -0.0000
Iteration 49/50 | Best Fitness: -0.0000
Iteration 50/50 | Best Fitness: -0.0000


Final Best Solution Found:
Best Position: [ 0.006821 -0.004142 ]
Best Fitness: -6.35e-05

