import collections
from collections import Counter
from random import shuffle

from numpy import concatenate
from numpy.random import randint

Individual = collections.namedtuple('population', 'cromossome weight value')


def generate_population(size, backpack_capacity):
    new_population = []

    for i in range(size):
        item = randint(0, backpack_capacity-1)

        new_population.append(
            Individual(
                cromossome=randint(2, size=(1, backpack_capacity))[0],
                weight=-1,
                value=-1
            )
        )


    return new_population


def calculate_fitness(population, items, max_weight):
    for i in range(len(population)):
        for j in range(len(items)):

            cromossome = population[i].cromossome
            weight, value = _calculate_weight_value(cromossome, items)

            while weight > max_weight:
                cromossome[randint(0, len(items)-1)] = 0
                weight, value = _calculate_weight_value(cromossome, items)

            population[i] = Individual(cromossome=cromossome, weight=weight, value=value)

    return population


def parent_selection(population):
    parents = []
    total_value = 0

    for individual in population:
        total_value += individual.value

    highest, second_highest = find_two_fittest_individuals(population)
    parents.append(highest)
    parents.append(second_highest)

    sum_value = 0
    while len(parents) < len(population):
        individual = randint(0, len(population)-1)
        sum_value += population[individual].value

        if sum_value >= total_value:
            parents.append(population[individual])

    return parents


def apply_crossover(population, backpack_capacity, crossover_probability, mutation_probability):
    crossovered_population = []

    while len(crossovered_population) < len(population):
        if randint(0, 100) <= crossover_probability * 100:
            parent_a = randint(0, len(population) - 1)
            parent_b = randint(0, len(population) - 1)

            cromossome_a = concatenate((population[parent_a].cromossome[:int(backpack_capacity / 2)],
                                        population[parent_b].cromossome[int(backpack_capacity / 2):]))
            cromossome_a = apply_mutation(cromossome_a, backpack_capacity, mutation_probability)

            cromossome_b = concatenate((population[parent_a].cromossome[int(backpack_capacity / 2):],
                                        population[parent_b].cromossome[:int(backpack_capacity / 2)]))
            cromossome_b = apply_mutation(cromossome_b, backpack_capacity, mutation_probability)


            crossovered_population.append(Individual(
                cromossome=cromossome_a,
                weight=-1,
                value=-1
            ))

            crossovered_population.append(Individual(
                cromossome=cromossome_b,
                weight=-1,
                value=-1
            ))

    return crossovered_population


def apply_mutation(cromossome, backpack_capacity, mutation_probability):
    if randint(0, 100) <= mutation_probability * 100:
        genes = randint(0, 2)

        for i in range(genes):
            gene = randint(0, backpack_capacity-1)
            if cromossome[gene] == 0:
                cromossome[gene] = 1
            else:
                cromossome[gene] = 0

    return cromossome


def _calculate_weight_value(cromossome, backpack):
    weight = 0
    value = 0

    for i, gene in enumerate(cromossome):
        if gene == 1:
            weight += backpack[i].weight
            value += backpack[i].value

    return weight, value


def find_two_fittest_individuals(population):
    highest = 0
    highest_index = 0
    second_highest = 0
    second_highest_index = 0

    for i in range(len(population)):
        if population[i].value > highest:
            highest = population[i].value
            highest_index = i

        if population[i].value > second_highest and population[i].value < highest:
            second_highest = population[i].value
            second_highest_index = i

    return population[highest_index], population[second_highest_index]
