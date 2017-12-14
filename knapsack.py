import collections
import time

import matplotlib.pyplot as plt
from numpy import random
from numpy.random import randint

from utils import (apply_crossover, apply_mutation, calculate_fitness,
                   generate_population, parent_selection)


def find_solution(population):
    fitnessed_population = []
    selected_parents = []
    crossovered_population = []
    fitnessed_population = []

    fitnessed_population = calculate_fitness(population, population_size, backpack, backpack_capacity, max_backpack_weight)
    selected_parents = parent_selection(fitnessed_population, population_size)
    crossovered_population = apply_crossover(selected_parents, population_size, backpack_capacity, crossover_probability, mutation_probability)
    fitnessed_population = calculate_fitness(crossovered_population, population_size, backpack, backpack_capacity, max_backpack_weight)

    return fitnessed_population


if __name__ == "__main__":
    max_generations = 1000

    backpack_capacity = 20
    max_backpack_weight = 100
    max_backpack_value = 1000
    backpack = []
    population_size = 500

    crossover_probability = 1.0
    mutation_probability = 0.0

    Item = collections.namedtuple('backpack', 'weight value')
    Individual = collections.namedtuple(
        'population', 'cromossome weight value')

    for i in range(backpack_capacity):
        backpack.append(Item(weight=randint(1, max_backpack_weight), value=randint(0, 300)))

    for item in backpack:
        max_backpack_value += item.value

    random.seed(22)
    evolved_population = generate_population(population_size, backpack_capacity)

    value = []
    weight = []
    iteraction = []

    for i in range(max_generations):
        evolved_population = find_solution(evolved_population)

        highest_value = 0
        highest_value_weight = 0

        for solution in evolved_population:
            if solution.value > highest_value:
                highest_value = solution.value
                highest_value_weight = solution.weight

        if i % 100 == 0:
            print i, highest_value, highest_value_weight

        value.append(highest_value)
        weight.append(highest_value_weight)
        iteraction.append(i)

    plt.plot(iteraction, value)
    # plt.plot(iteraction, weight)
    plt.xlabel('Generation')
    plt.ylabel('Value')
    plt.show()
