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
