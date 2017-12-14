import collections
import time

import matplotlib.pyplot as plt
from numpy import random
from numpy.random import randint

from utils import (apply_crossover, apply_mutation, calculate_fitness,
                   check_fitness_percentage, find_two_fittest_individuals,
                   generate_population, parent_selection)

Item = collections.namedtuple('backpack', 'weight value')
Individual = collections.namedtuple('population', 'cromossome weight value')


def find_solution():
    population = generate_population(population_size, backpack_capacity)
    
    value = []
    weight = []
    iteraction = []
    highest = 0

    for i in range(max_generations):
        fitness = calculate_fitness(population, items, max_weight)
        parents = parent_selection(fitness)
        population = apply_crossover(parents, backpack_capacity, crossover_probability, mutation_probability)

        highest_new, _ = find_two_fittest_individuals(population)
        if  highest_new.value > highest:
            highest = highest_new.value
            value.append(highest_new.value)


        value.append(highest)
        iteraction.append(i)

        if i % 100 == 0:
            print i, highest

    plt.plot(iteraction, value)
    # plt.plot(iteraction, weight)
    plt.xlabel('Generation')
    plt.ylabel('Value')
    plt.show()
    

if __name__ == "__main__":
    max_generations = 1000
    population_size = 200

    crossover_probability = 0.8
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

    # random.seed(22)
    find_solution()


    # for item in items:
    #     max_backpack_value += item.value

    # print max_backpack_value
    # for p in population:
    #     print p.cromossome, p.weight, p.value

    # for i in range(max_generations):
        # find_solution()

    # for i in range(max_generations):
    #     evolved_population = find_solution(evolved_population)

    #     highest_value = 0
    #     highest_value_weight = 0

    #     for solution in evolved_population:
    #         if solution.value > highest_value:
    #             highest_value = solution.value
    #             highest_value_weight = solution.weight

        # if i % 100 == 0:
        #     print i, highest_value, highest_value_weight

    #     value.append(highest_value)
    #     weight.append(highest_value_weight)
    #     iteraction.append(i)

    # plt.plot(iteraction, value)
    # # plt.plot(iteraction, weight)
    # plt.xlabel('Generation')
    # plt.ylabel('Value')
    # plt.show()
