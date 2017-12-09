import numpy as np
import random
import collections

"""
GA()
    initialize population
    find fitness of population

    while (termination criteria is reached) do
        parent selection
        crossover with probability pc
        mutation with probability pm
        decode and fitness calculation
        survivor selection
        find best
    return best
"""


def find_solution(backpack, backpack_capacity, max_backpack_weight, population_size, max_generations):
    population = generate_population(population_size, backpack_capacity)
    population = calculate_fitness(population, population_size, backpack, backpack_capacity, max_backpack_weight)

    for p in population:
        print p.weight, p.value, p.fitness

def generate_population(population_size, backpack_capacity):
    population = []
    cromossomes = np.random.randint(2, size=(population_size, backpack_capacity))

    for i in range(population_size):
        population.append(Individual(cromossome=cromossomes[i], weight=-1, value=-1, fitness=-1))

    return population


def calculate_fitness(population, population_size, backpack, backpack_capacity, max_backpack_weight):
    weight = -1
    value = -1
    fitness = -1.

    for i in range(population_size):
        for j in range(backpack_capacity):
            if population[i].cromossome[j] == 1 and weight + backpack[j].weight <= max_backpack_weight:
                weight += backpack[j].weight
                value += backpack[j].value

        fitness = round(1-(float(weight) / float(value)), 4)

        if fitness < 0:
            fitness = 0

        population[i] = Individual(cromossome=population[i].cromossome, weight=weight, value=value, fitness=fitness)
        weight = -1
        value = -1
        fitness = -1

    return population

def apply_crossover():
    pass

def apply_mutation():
    pass

def survivals_selection(population):
    return ''

def show_best_solution():
    pass

def calculate_total_weight_and_value(individual, backpack):
    weight = 0
    value = 0

    for i, item in enumerate(individual):
        if item == 1:
            weight += backpack[i].weight
            value += backpack[i].value

    return weight, value


if __name__ == "__main__":
    population_size = 200
    backpack_capacity = 10
    max_backpack_weight = 70
    max_generations = 500

    backpack = []
    Item = collections.namedtuple('backpack', 'weight value')

    population = []
    Individual = collections.namedtuple('population', 'cromossome weight value fitness')


    for i in range(backpack_capacity):
        backpack.append(Item(weight=random.randint(1, 50), value=random.randint(0, 100)))

    find_solution(backpack, backpack_capacity, max_backpack_weight, population_size, max_generations)
