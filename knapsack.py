import collections

import matplotlib.pyplot as plt
from numpy import random
from numpy.random import randint

from utils import (apply_crossover, apply_mutation, calculate_fitness,
                   generate_population, parent_selection)


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


def find_solution(population):
    # print 'Finding     ', population[0]
    fitnessed_population = calculate_fitness(population, population_size, backpack, backpack_capacity, max_backpack_weight, max_backpack_value)
    # print 'Fitnessed   ', fitnessed_population[0]
    selected_parents = parent_selection(fitnessed_population, population_size)
    # print 'Selected    ', selected_parents[0]
    # print 'Selected_2  ', selected_parents[-1]
    # print 'Selected_3  ', len(selected_parents)
    crossovered_population = apply_crossover(selected_parents, population_size, backpack_capacity, crossover_probability)
    # print 'Crossovered ', crossovered_population[0]
    mutated_population = apply_mutation(crossovered_population, population_size, backpack_capacity, mutation_probability)
    # print 'Mutated     ', mutated_population[0]

    return fitnessed_population


if __name__ == "__main__":
    max_generations = 10000

    backpack_capacity = 20
    max_backpack_weight = 100
    max_backpack_value = 0
    backpack = []
    population_size = 500

    crossover_probability = 0.85
    mutation_probability = 0.1

    Item = collections.namedtuple('backpack', 'weight value')
    Individual = collections.namedtuple(
        'population', 'cromossome weight value fitness')

    for i in range(backpack_capacity):
        backpack.append(Item(weight=randint(1, 15), value=randint(0, 100)))

    for item in backpack:
        max_backpack_value += item.value

    random.seed(22)
    evolved_population = generate_population(population_size, backpack_capacity)

    xdata = []
    ydata = []
    plt.show()

    axes = plt.gca()
    axes.set_xlim(0, max_generations)
    axes.set_ylim(0, +max_backpack_value)
    line, = axes.plot(xdata, ydata, 'r-')

    for i in range(max_generations):
        evolved_population = find_solution(evolved_population)
        print i

        highest_fitness = 0
        for individual in evolved_population:
            if individual.value > highest_fitness:
                highest_fitness = individual.value

        xdata.append(i)
        ydata.append(highest_fitness)
        line.set_xdata(xdata)
        line.set_ydata(ydata)
        plt.draw()

    plt.show()

