import random
import math


def fitness(x):
    return x**2  


def levy_flight(beta=1.5):
    
    u = random.gauss(0, 1)  # Gaussian distribution for u
    v = random.gauss(0, 1)  # Gaussian distribution for v
    step = u / abs(v) ** (1 / beta)  # Levy flight step
    return step

# Cuckoo Search Algorithm
def cuckoo_search(nests=10, max_iter=100, pa=0.25):
    # Step 1: Initialize nests (solutions)
    nests_positions = [random.uniform(-10, 10) for _ in range(nests)]
    fitness_values = [fitness(x) for x in nests_positions]
    
    # Best solution initially
    best_nest = nests_positions[fitness_values.index(min(fitness_values))]
    best_fitness = min(fitness_values)
    
    # Iteration loop
    for t in range(max_iter):
        # Generate new solutions via Levy flight
        new_nests = [nest + levy_flight() * (nest - best_nest) for nest in nests_positions]
        
        # Evaluate fitness of new solutions
        new_fitness = [fitness(x) for x in new_nests]
        
        # Update nests with better solutions
        for i in range(nests):
            if new_fitness[i] < fitness_values[i]:
                nests_positions[i] = new_nests[i]
                fitness_values[i] = new_fitness[i]
        
       
        for i in range(nests):
            if random.random() < pa:
                nests_positions[i] = random.uniform(-10, 10)  # Generate a new random solution
                fitness_values[i] = fitness(nests_positions[i])
        
        # Update best solution
        current_best_nest = nests_positions[fitness_values.index(min(fitness_values))]
        current_best_fitness = min(fitness_values)
        
        if current_best_fitness < best_fitness:
            best_nest = current_best_nest
            best_fitness = current_best_fitness
        
        print(f"Iteration {t+1}, Best Fitness: {best_fitness}, Best Nest: {best_nest}")
    
    return best_nest, best_fitness


best_solution, best_value = cuckoo_search(nests=10, max_iter=100, pa=0.25)
print(f"Global minimum found at x = {best_solution}, f(x) = {best_value}")

output
Iteration 1, Best Fitness: 1.2921961942067006, Best Nest: -1.136748078602599
Iteration 2, Best Fitness: 0.5765134389217328, Best Nest: -0.7592848206843943
Iteration 3, Best Fitness: 0.5765134389217328, Best Nest: -0.7592848206843943
Iteration 4, Best Fitness: 0.02266899319505372, Best Nest: 0.15056225687420377
Iteration 5, Best Fitness: 0.0042965565622086685, Best Nest: 0.06554812401746268
Iteration 6, Best Fitness: 0.0042965565622086685, Best Nest: 0.06554812401746268
Iteration 7, Best Fitness: 0.0042965565622086685, Best Nest: 0.06554812401746268
Iteration 8, Best Fitness: 0.0042965565622086685, Best Nest: 0.06554812401746268
Iteration 9, Best Fitness: 0.002981228358757636, Best Nest: 0.05460062599236053
Iteration 10, Best Fitness: 9.187111896745005e-06, Best Nest: -0.0030310248921354976
Iteration 11, Best Fitness: 9.187111896745005e-06, Best Nest: -0.0030310248921354976
Iteration 12, Best Fitness: 9.187111896745005e-06, Best Nest: -0.0030310248921354976
Iteration 13, Best Fitness: 9.187111896745005e-06, Best Nest: -0.0030310248921354976
Iteration 14, Best Fitness: 9.187111896745005e-06, Best Nest: -0.0030310248921354976
Iteration 15, Best Fitness: 9.187111896745005e-06, Best Nest: -0.0030310248921354976
Iteration 16, Best Fitness: 9.187111896745005e-06, Best Nest: -0.0030310248921354976
Iteration 17, Best Fitness: 9.187111896745005e-06, Best Nest: -0.0030310248921354976
Iteration 18, Best Fitness: 9.187111896745005e-06, Best Nest: -0.0030310248921354976
Iteration 19, Best Fitness: 9.187111896745005e-06, Best Nest: -0.0030310248921354976
Iteration 20, Best Fitness: 4.773953830111175e-07, Best Nest: 0.0006909380457111314



