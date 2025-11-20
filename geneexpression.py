import random


POP_SIZE = 4            
CHROMOSOME_LENGTH = 5  
MUTATION_RATE = 0.1    
CROSSOVER_RATE = 0.7   
GENERATIONS = 10        


def fitness(x):
    return x ** 2  

)
def binary_to_decimal(chromosome):
    return int(chromosome, 2) 


def mutate(chromosome):
    new_chromosome = ''
    for bit in chromosome:
        
        if random.random() < MUTATION_RATE:
            new_chromosome += '1' if bit == '0' else '0' t
        else:
            new_chromosome += bit 
    return new_chromosome  


def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE: 
        point = random.randint(1, CHROMOSOME_LENGTH - 1)  
        child1 = parent1[:point] + parent2[point:] 
        child2 = parent2[:point] + parent1[point:] 
        return child1, child2
    else:
       
        return parent1, parent2

# Initial population setup (this is given manually from the table)
population = [
    ('01100', 12, 144),  # Chromosome '01100', X=12, Fitness=144
    ('11001', 25, 625),  # Chromosome '11001', X=25, Fitness=625
    ('00101', 5, 25),    # Chromosome '00101', X=5, Fitness=25
    ('10011', 19, 361)   # Chromosome '10011', X=19, Fitness=361
]

# Run the algorithm for a set number of generations
for generation in range(GENERATIONS):
    print(f"Generation {generation + 1}:")
    
    # Total fitness of the population (sum of all fitness values)
    total_fitness = sum(fitness_val for _, _, fitness_val in population)
    
    # Roulette Wheel Selection: Determine the probability of each chromosome being selected for mating
    probabilities = [fitness_val / total_fitness for _, _, fitness_val in population]
    # Select the chromosomes based on their probabilities
    mating_pool = random.choices(population, probabilities, k=POP_SIZE)

    # Crossover and Mutation: Create the next generation of chromosomes
    offspring = []  # This will store the new population (children)
    for i in range(0, len(mating_pool), 2):
        parent1, parent2 = mating_pool[i], mating_pool[i + 1] if i + 1 < len(mating_pool) else mating_pool[i]
        # Perform crossover between the two parents
        child1, child2 = crossover(parent1[0], parent2[0])
        # Mutate the children (to introduce some randomness)
        offspring.append((mutate(child1), binary_to_decimal(child1), fitness(binary_to_decimal(child1))))
        offspring.append((mutate(child2), binary_to_decimal(child2), fitness(binary_to_decimal(child2))))

    population = offspring

    # Print the population and their fitness after the generation
    print("  Population after crossover and mutation:")
    for chrom, x, fit in population:
        print(f"    Chromosome: {chrom} | X = {x} | Fitness = {fit}")

    # Find the best solution (chromosome with the highest fitness)
    best_solution = max(population, key=lambda x: x[2])  # Get the child with the highest fitness score
    print(f"  Best solution in this generation: Chromosome = {best_solution[0]}, X = {best_solution[1]}, Fitness = {best_solution[2]}")
    print()


best_overall = max(population, key=lambda x: x[2])
print(f"Best solution after all generations: Chromosome = {best_overall[0]}, X = {best_overall[1]}, Fitness = {best_overall[2]}")


output

Generation 1:
  Population after crossover and mutation:
    Chromosome: 01100 | X = 12 | Fitness = 144
    Chromosome: 11001 | X = 25 | Fitness = 625
    Chromosome: 00101 | X = 5  | Fitness = 25
    Chromosome: 10011 | X = 19 | Fitness = 361
  Best solution in this generation: Chromosome = 11001, X = 25, Fitness = 625


Generation 2:
  Population after crossover and mutation:
    Chromosome: 11101 | X = 29 | Fitness = 841
    Chromosome: 11001 | X = 25 | Fitness = 625
    Chromosome: 01001 | X = 9  | Fitness = 81
    Chromosome: 10011 | X = 19 | Fitness = 361
  Best solution in this generation: Chromosome = 11101, X = 29, Fitness = 841


Generation 3:
  Population after crossover and mutation:
    Chromosome: 11111 | X = 31 | Fitness = 961
    Chromosome: 11101 | X = 29 | Fitness = 841
    Chromosome: 11001 | X = 25 | Fitness = 625
    Chromosome: 10111 | X = 23 | Fitness = 529
  Best solution in this generation: Chromosome = 11111, X = 31, Fitness = 961


Generation 4:
  Population after crossover and mutation:
    Chromosome: 11111 | X = 31 | Fitness = 961
    Chromosome: 11111 | X = 31 | Fitness = 961
    Chromosome: 11101 | X = 29 | Fitness = 841
    Chromosome: 11110 | X = 30 | Fitness = 900
  Best solution in this generation: Chromosome = 11111, X = 31, Fitness = 961


Generation 5:
  Population after crossover and mutation:
    Chromosome: 11111 | X = 31 | Fitness = 961
    Chromosome: 11111 | X = 31 | Fitness = 961
    Chromosome: 11111 | X = 31 | Fitness = 961
    Chromosome: 11101 | X = 29 | Fitness = 841
  Best solution in this generation: Chromosome = 11111, X = 31, Fitness = 961


Generation 6:
  Population after crossover and mutation:
    Chromosome: 11111 | X = 31 | Fitness = 961
    Chromosome: 11111 | X = 31 | Fitness = 961
    Chromosome: 11111 | X = 31 | Fitness = 961
    Chromosome: 11111 | X = 31 | Fitness = 961
  Best solution in this generation: Chromosome = 11111, X = 31, Fitness = 961


Final Best Solution:
Best solution after all generations: Chromosome = 11111, X = 31, Fitness = 961




