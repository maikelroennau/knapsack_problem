import collections

import matplotlib.pyplot as plt
from numpy import random
from numpy.random import randint

from utils import (apply_crossover, apply_mutation, calculate_fitness,
                   generate_population, parent_selection)


def find_solution(population):
    fitnessed_population = calculate_fitness(population, population_size, backpack, backpack_capacity, max_backpack_weight)
    selected_parents = parent_selection(fitnessed_population, population_size)
    crossovered_population = apply_crossover(selected_parents, population_size, backpack_capacity, crossover_probability)
    mutated_population = apply_mutation(crossovered_population, population_size, backpack_capacity, mutation_probability)
    fitnessed_population = calculate_fitness(mutated_population, population_size, backpack, backpack_capacity, max_backpack_weight)

    return mutated_population


if __name__ == "__main__":
    max_generations = 3000

    backpack_capacity = 20
    max_backpack_weight = 100
    max_backpack_value = 0
    backpack = []
    population_size = 200

    crossover_probability = 0.85
    mutation_probability = 0.1

    Item = collections.namedtuple('backpack', 'weight value')
    Individual = collections.namedtuple(
        'population', 'cromossome weight value')

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
        
        if i % 100 == 0:
            print i

        evolved_population.sort(key=lambda x: x[2], reverse=True)
        
        xdata.append(i)
        ydata.append(evolved_population[0].value)
        line.set_xdata(xdata)
        line.set_ydata(ydata)
        plt.draw()

    plt.show()

