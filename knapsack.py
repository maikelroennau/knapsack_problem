import numpy as np
from numpy import random
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


def find_solution(backpack, backpack_capacity, max_backpack_weight, max_backpack_value, population_size, max_generations):
    population = generate_population(population_size, backpack_capacity)
    population = calculate_fitness(population, population_size, backpack, backpack_capacity, max_backpack_value, max_backpack_weight)
    parent_selection(population, population_size, max_backpack_value)

    # for p in population:
        # print p

def generate_population(population_size, backpack_capacity):
    population = []
    cromossomes = random.randint(2, size=(population_size, backpack_capacity))

    for i in range(population_size):
        population.append(Individual(cromossome=cromossomes[i], weight=-1, value=-1, fitness=-1))

    return population


def calculate_fitness(population, population_size, backpack, backpack_capacity, max_backpack_value, max_backpack_weight):
    weight = 0
    value = 0
    fitness = 0

    for i in range(population_size):
        for j in range(backpack_capacity):
            if population[i].cromossome[j] == 1 and weight + backpack[j].weight <= max_backpack_weight:
                weight += backpack[j].weight
                value += backpack[j].value

        fitness = round(((float(value) * 100.0) / float( max_backpack_value)) / 100, 4)

        if fitness < 0:
            fitness = 0

        population[i] = Individual(cromossome=population[i].cromossome, weight=weight, value=value, fitness=fitness)
        weight = 0
        value = 0
        fitness = 0

    population.sort(key=lambda x: x[3], reverse=True) 

    return population

def parent_selection(population, population_size, max_backpack_value):
    parents = []
    fitness_sum = 0
    threshold = 0

    for individual in population:
        fitness_sum += individual.fitness

    threshold = random.randint(0, round(fitness_sum, 1)) / 100.0
    fitness_sum = round(fitness_sum / 100.0, 4)

    for individual in population:
        if individual.fitness >= threshold:
            parents.append(individual)

    return parents


def apply_crossover():
    pass

def apply_mutation():
    pass

def show_best_solution():
    pass


if __name__ == "__main__":
    max_generations = 500

    backpack_capacity = 20
    max_backpack_weight = 70
    max_backpack_value = 0
    backpack = []
    Item = collections.namedtuple('backpack', 'weight value')

    population_size = 200
    population = []
    Individual = collections.namedtuple('population', 'cromossome weight value fitness')


    for i in range(backpack_capacity):
        backpack.append(Item(weight=random.randint(1, 50), value=random.randint(0, 100)))


    for item in backpack:
        max_backpack_value += item.value

    print max_backpack_value

    find_solution(backpack, backpack_capacity, max_backpack_weight, max_backpack_value, population_size, max_generations)
