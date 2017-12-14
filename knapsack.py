import collections
import time

import matplotlib.pyplot as plt
from numpy import random
from numpy.random import randint

from utils import (apply_crossover, apply_mutation, calculate_fitness,
                   find_two_fittest_individuals, generate_population,
                   parent_selection)

Item = collections.namedtuple('backpack', 'weight value')


def find_solution():
    population = generate_population(population_size, backpack_capacity)

    value = []
    iteraction = []
    best_solution = []

    for i in range(max_generations):
        fitness = calculate_fitness(population, items, max_weight)
        parents = parent_selection(fitness)
        crossovered = apply_crossover(parents, backpack_capacity, crossover_probability, mutation_probability)
        population = calculate_fitness(crossovered, items, max_weight)


        highest_new, _ = find_two_fittest_individuals(population)
        if len(best_solution) == 0:
            best_solution = highest_new
        elif highest_new.value > best_solution.value:
            best_solution = highest_new

        value.append(best_solution.value)
        iteraction.append(i)

        if i % 100 == 0:
            print i, best_solution.value

    plt.plot(iteraction, value)
    plt.xlabel('Generation')
    plt.ylabel('Value')
    plt.show()


if __name__ == "__main__":
    max_generations = 1000
    population_size = 200

    crossover_probability = 0.7
    mutation_probability = 0.1

    backpack_capacity = 20
    max_weight = 80

    max_item_weight = 15
    max_item_value = 100

    max_backpack_value = 0

    items = []
    population = []

    for i in range(backpack_capacity):
        items.append(
            Item(
                weight=randint(1, max_item_weight),
                value=randint(0, max_item_value)
            )
        )

    find_solution()
