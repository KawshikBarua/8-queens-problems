import numpy as np
from statistics import mode

best_fitness = [0]
best_pop = [0]


def fitness(population, n):
    fit = []
    for i in range(len(population)):
        horizontalConflict = 0
        diagonalConflict = 0
        for j in range(0, int(n), 1):
            for k in range(j + 1, int(n), 1):
                if population[i][j] == population[i][k]:
                    horizontalConflict += 1
                elif abs(j - k) == abs(population[i][j] - population[i][k]):
                    diagonalConflict += 1
        totalConflicts = horizontalConflict + diagonalConflict
        fit.append(28 - totalConflicts)

    return fit


def select(population, fit):
    a = []
    for i in range(len(population)):
        a.append(i)
    size = 2
    p = []
    sum_fit = sum(fit)
    for i in range(len(fit)):
        p.append(fit[i]/sum_fit)
    replace = True
    return np.random.choice(a, size, replace, p)


def crossover(x, y):
    crossover_point = np.random.randint(0, len(x))
    child = np.zeros(len(x), dtype=int)
    for i in range(0, len(x), 1):
        if i >= crossover_point:
            child[i] = y[i]
        else:
            child[i] = x[i]

    return child


def mutate(child):
    c = mode(child)
    random_value = np.random.randint(0, 7)
    all_commons = []
    for i in range(0, len(child), 1):
        if child[i] == c:
            all_commons.append(i)
    idx = np.random.choice(all_commons)
    child[idx] = random_value
    return child


def GA(population, n, mutation_threshold):

    print("8 queens problem: ")
    global child
    global fit
    run = 100000
    timesRun = run
    non_attacking_pairs = 28
    new_population = [0]


    while timesRun > 0:
        fit = fitness(population, n)
        if check_if_fit(fit) == non_attacking_pairs:
            found = run - timesRun
            print("Population: ")
            print(*population)
            print("The solution was found after "+str(found)+" iterations.")
            return

        if timesRun == 100000:
            rand_selection = select(population, fit)
            child = crossover(population[rand_selection[0]], population[rand_selection[1]])

        if np.random.uniform(0, 1) < mutation_threshold:
            new_population[0] = (mutate(child))

        else:
            new_population[0] = child

        population = new_population
        best_fit(population, fit)
        timesRun -= 1

    print("Time exceeded answer was not found best fitness was "+str(*best_fitness))
    print("Population: ")
    print(*best_pop)


def check_if_fit(fit):
    found = 0
    for i in range(0, len(fit), 1):
        found = fit[i]
    return found


def best_fit(population, fit):
    global best_pop
    global best_fitness
    if fit[0] > best_fitness[0]:
        best_fitness[0] = fit[0]
        best_pop = population


n = 8
start_population = 10
mutation_threshold = 0.5
population = np.random.randint(0, n, (start_population, n))
GA(population, n, mutation_threshold)
