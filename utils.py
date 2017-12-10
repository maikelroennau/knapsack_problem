import collections

from numpy import concatenate
from numpy.random import randint

Item = collections.namedtuple('backpack', 'weight value')
Individual = collections.namedtuple('population', 'cromossome weight value fitness')


def generate_population(population_size, backpack_capacity):
    population = []
    cromossomes = randint(2, size=(population_size, backpack_capacity))

    for i in range(population_size):
        population.append(Individual(
            cromossome=cromossomes[i], weight=-1, value=-1, fitness=-1))

    return population


def calculate_fitness(population, population_size, backpack, backpack_capacity, max_backpack_weight):
    for i in range(population_size):
        cromossome = population[i].cromossome
        weight, value = calculate_weight_value(cromossome, backpack)

        while weight > max_backpack_weight:
            cromossome[randint(0, backpack_capacity - 1)] = 0
            weight, value = calculate_weight_value(cromossome, backpack)

        population[i] = Individual(
            cromossome=cromossome, weight=weight, value=value, fitness=-1)

    return population


def parent_selection(population, population_size):
    threshold = randint(0, population_size)
    parents = []

    for i in range(population_size):
        sum = 0
        while sum < threshold:
            sum += population[i].value

        parents.append(population[i])

    return parents


def apply_crossover(population, population_size, backpack_capacity, crossover_probability):
    for i in range(int(population_size * crossover_probability)):
        parent_a = randint(0, population_size - 1)
        parent_b = randint(0, population_size - 1)

        population[parent_a] = Individual(
            cromossome=concatenate((population[parent_a].cromossome[0:int(backpack_capacity / 2)],
                                    population[parent_b].cromossome[int(backpack_capacity / 2):])),
            weight=-1,
            value=-1,
            fitness=-1
        )

        population[parent_b] = Individual(
            cromossome=concatenate((population[parent_a].cromossome[0:int(backpack_capacity / 2)],
                                    population[parent_b].cromossome[int(backpack_capacity / 2):])),
            weight=-1,
            value=-1,
            fitness=-1
        )

    return population


def apply_mutation(population, population_size, backpack_capacity, mutation_probability):
    for i in range(int(population_size * mutation_probability)):
        individual = randint(0, population_size - 1)
        gene = randint(0, backpack_capacity - 1)

        cromossome = population[individual].cromossome

        if cromossome[gene] == 0:
            cromossome[gene] = 1
        else:
            cromossome[gene] = 0

        population[individual] = Individual(
            cromossome=cromossome,
            weight=-1,
            value=-1,
            fitness=-1
        )

    return population


def calculate_weight_value(cromossome, backpack):
    weight = 0
    value = 0

    for i, gene in enumerate(cromossome):
        if gene == 1:
            weight += backpack[i].weight
            value += backpack[i].value

    return weight, value


def calculate_total_value(population):
    value = 0
    for individual in population:
        value += individual.value

    return value
