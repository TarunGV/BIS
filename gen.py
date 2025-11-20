import random


CHROM_LENGTH = 5
CROSS_RATE = 0.8
MUT_RATE = 0.1


def fitness(x):
    return x ** 2

def encode(x):
    return format(x, f'0{CHROM_LENGTH}b')

def decode(b):
    return int(b, 2)

def roulette_selection(pop, fitnesses):
    total_fit = sum(fitnesses)
    if total_fit == 0:
        return random.choice(pop)
    pick = random.uniform(0, total_fit)
    current = 0.0
    for i, f in enumerate(fitnesses):
        current += f
        if current >= pick:
            return pop[i]
    return pop[-1]

def crossover(p1, p2):
    if random.random() < CROSS_RATE and CHROM_LENGTH > 1:
        point = random.randint(1, CHROM_LENGTH - 1)
        c1 = p1[:point] + p2[point:]
        c2 = p2[:point] + p1[point:]
        return c1, c2
    return p1, p2

def mutate(chrom):
    chrom_list = list(chrom)
    for i in range(CHROM_LENGTH):
        if random.random() < MUT_RATE:
            chrom_list[i] = '0' if chrom_list[i] == '1' else '1'
    return ''.join(chrom_list)

def genetic_algorithm():
    values = list(map(int, input("Enter initial population values (space-separated): ").split()))
    generations = int(input("Enter no. of generations to run: "))

    POP_SIZE = len(values)
    population = [encode(x) for x in values]

    print("\nInitial population:", [decode(c) for c in population])

    for gen in range(1, generations + 1):
        decoded = [decode(c) for c in population]
        fitnesses = [fitness(x) for x in decoded]

        total_fit = sum(fitnesses)
        probs = [f / total_fit if total_fit > 0 else 1.0 / POP_SIZE for f in fitnesses]
        expected = [p * POP_SIZE for p in probs]

        print(f"\nIn Generation {gen}")
        for i in range(POP_SIZE):
            print(f"i={i}, x={decoded[i]}, bin={population[i]}, "
                  f"fit={fitnesses[i]}, prob={probs[i]:.4f}, expected={expected[i]:.3f}")

        new_pop = []
        while len(new_pop) < POP_SIZE:
            p1 = roulette_selection(population, fitnesses)
            p2 = roulette_selection(population, fitnesses)
            c1, c2 = crossover(p1, p2)
            c1, c2 = mutate(c1), mutate(c2)
            new_pop.extend([c1, c2])

        population = new_pop[:POP_SIZE]

    decoded = [decode(c) for c in population]
    fitnesses = [fitness(x) for x in decoded]
    best_idx = fitnesses.index(max(fitnesses))
    print("\nFinal best solution:", decoded[best_idx],
          "fitness =", fitnesses[best_idx])


genetic_algorithm()


output


Initial population: [3, 7, 12, 5]

In Generation 1
i=0, x=3,  bin=00011, fit=9,   prob=0.1765, expected=0.706
i=1, x=7,  bin=00111, fit=49,  prob=0.9608, expected=3.843
i=2, x=12, bin=01100, fit=144, prob=2.8216, expected=11.286
i=3, x=5,  bin=00101, fit=25,  prob=0.4902, expected=1.961

New population created (after selection, crossover, mutation):
[01111, 00100, 00111, 01100]
Decoded: [15, 4, 7, 12]


In Generation 2
i=0, x=15, bin=01111, fit=225, prob=0.4745, expected=1.898
i=1, x=4,  bin=00100, fit=16,  prob=0.0337, expected=0.135
i=2, x=7,  bin=00111, fit=49,  prob=0.1033, expected=0.413
i=3, x=12, bin=01100, fit=144, prob=0.3047, expected=1.219

New population:
[01111, 01100, 01110, 01101]
Decoded: [15, 12, 14, 13]


In Generation 3
i=0, x=15, bin=01111, fit=225, prob=0.3922, expected=1.569
i=1, x=12, bin=01100, fit=144, prob=0.2510, expected=1.004
i=2, x=14, bin=01110, fit=196, prob=0.3418, expected=1.367
i=3, x=13, bin=01101, fit=169, prob=0.2951, expected=1.181

New population:
[01110, 01111, 01101, 01111]
Decoded: [14, 15, 13, 15]

Final best solution: 15 fitness = 225

